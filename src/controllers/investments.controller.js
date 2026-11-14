// src/controllers/investments.controller.js
const axios = require("axios");
const Loan = require("../models/loan.model");
const Transaction = require("../models/transaction.model");

// Cache for stock prices to avoid rate limiting (cache for 30 minutes)
const stockCache = new Map();
const CACHE_DURATION = 30 * 60 * 1000; // 30 minutes in milliseconds

//const investmentData = require("../../scripts/investment.data");

// Fallback prices in USD (approximate current values)
const FALLBACK_PRICES = {
  AAPL: { price: 225, change: 1.2 },
  NFLX: { price: 680, change: -0.5 },
  META: { price: 485, change: 2.1 },
  AMZN: { price: 185, change: 0.8 }
};

const USD_TO_INR = 84.5;

const getAuthenticatedUserId = (req) =>
  req.user?.id || req.user?._id || req.user?.userId || null;

const buildFallbackStock = (stock) => {
  const fallback = FALLBACK_PRICES[stock.symbol] || { price: 100, change: 0 };
  const convert = (val) => (val != null ? val * USD_TO_INR : null);

  return {
    name: stock.name,
    symbol: stock.symbol,
    current_price: convert(fallback.price),
    change_pct: `${fallback.change}%`,
    high: convert(fallback.price * 1.02),
    low: convert(fallback.price * 0.98),
    open: convert(fallback.price),
    previous_close: convert(fallback.price),
    volume: null,
    timestamp: Math.floor(Date.now() / 1000),
    isFallback: true,
  };
};

exports.getStockApiKey = (req, res) => {
  return res.json({ apiKey: process.env.FINNHUB_API_KEY || "" });
};

exports.getRealTimeStock = async (req, res) => {
  try {
    const symbol = req.query.symbol; // e.g. ?symbol=AAPL

    if (!symbol) {
      return res.status(400).json({ error: "Stock symbol is required" });
    }

    const API_KEY = process.env.FINNHUB_API_KEY;
    if (!API_KEY) {
      const fallbackStock = buildFallbackStock({ name: symbol, symbol });
      return res.json({
        symbol,
        current_price: fallbackStock.current_price,
        high: fallbackStock.high,
        low: fallbackStock.low,
        open: fallbackStock.open,
        previous_close: fallbackStock.previous_close,
        volume: fallbackStock.volume,
        timestamp: fallbackStock.timestamp,
        isFallback: true,
      });
    }

    const url = `https://finnhub.io/api/v1/quote?symbol=${symbol}&token=${API_KEY}`;
    const response = await axios.get(url);
    const data = response.data || {};

    const convert = (val) => (val != null ? val * USD_TO_INR : null);

    return res.json({
      symbol,
      current_price: convert(data.c),
      high: convert(data.h),
      low: convert(data.l),
      open: convert(data.o),
      previous_close: convert(data.pc),
      volume: data.v ?? null,
      timestamp: data.t ?? null,
    });
  } catch (err) {
    console.error("Error fetching real-time stock:", err.message || err);
    return res
      .status(500)
      .json({ error: "Error fetching real-time stock data" });
  }
};

exports.getUserStocks = async (req, res) => {
  try {
    const API_KEY = process.env.FINNHUB_API_KEY;

    // Only names & symbols are fixed – prices are fetched live
    const baseStocks = [
      { name: "Apple", symbol: "AAPL" },
      { name: "Netflix", symbol: "NFLX" },
      { name: "Meta", symbol: "META" },
      { name: "Amazon", symbol: "AMZN" },
    ];

    // Fetch stocks sequentially to avoid rate limiting
    const results = [];

    for (const stock of baseStocks) {
      try {
        // Check cache first
        const cacheKey = stock.symbol;
        const cachedData = stockCache.get(cacheKey);

        if (cachedData && (Date.now() - cachedData.timestamp < CACHE_DURATION)) {
          console.log(`✓ Using cached data for ${stock.symbol} (age: ${Math.round((Date.now() - cachedData.timestamp) / 1000)}s)`);
          results.push(cachedData.data);
          continue;
        }

        // If market API key is not configured, gracefully return fallback values.
        if (!API_KEY) {
          const fallbackResult = buildFallbackStock(stock);
          results.push(fallbackResult);
          continue;
        }

        // Fetch from API with delay to avoid rate limiting
        console.log(`Fetching fresh data for ${stock.symbol}...`);
        await new Promise(resolve => setTimeout(resolve, 1000)); // 1 second delay between requests

        const url = `https://finnhub.io/api/v1/quote?symbol=${stock.symbol}&token=${API_KEY}`;
        const { data } = await axios.get(url, { timeout: 10000 });

        const curr = data?.c;
        const prev = data?.pc;
        let changePct = null;

        if (curr != null && prev != null && prev !== 0) {
          changePct = (((curr - prev) / prev) * 100).toFixed(2) + "%";
        }

        // Helper to convert USD -> INR
        const convert = (val) => (val != null ? val * USD_TO_INR : null);

        const result = {
          name: stock.name,
          symbol: stock.symbol,
          current_price: convert(curr),
          change_pct: changePct,
          high: convert(data?.h),
          low: convert(data?.l),
          open: convert(data?.o),
          previous_close: convert(prev),
          volume: data?.v ?? null,
          timestamp: data?.t ?? null,
        };

        // Cache the result
        stockCache.set(cacheKey, {
          data: result,
          timestamp: Date.now()
        });

        console.log(`✓ Cached fresh data for ${stock.symbol}`);
        results.push(result);
      } catch (err) {
        const errorDetails = err.response?.status
          ? `HTTP ${err.response.status}`
          : err.code
            ? `${err.code}`
            : err.message || 'Unknown error';

        console.error(
          `Error fetching stock ${stock.symbol}: ${errorDetails}`
        );

        // Try to use cached data even if expired
        const cachedData = stockCache.get(stock.symbol);
        if (cachedData) {
          console.log(`⚠ Using stale cache for ${stock.symbol} due to error`);
          results.push(cachedData.data);
        } else {
          console.log(`⚠ Using fallback price for ${stock.symbol}`);
          results.push(buildFallbackStock(stock));
        }
      }
    }

    return res.json(results);
  } catch (err) {
    console.error("Error fetching user stocks:", err);
    return res.status(500).json({ error: "Server error" });
  }
};


exports.getUserLoans = async (req, res) => {
  try {
    // Filter loans by the logged-in user's ID
    const userId = getAuthenticatedUserId(req);
    if (!userId) {
      return res.status(401).json({ error: "User not authenticated" });
    }

    const loans = await Loan.find({
      $or: [{ user_id: userId }, { userId: userId }],
    }).lean();
    return res.json(loans || []);
  } catch (err) {
    console.error("Error fetching user loans:", err);
    return res.status(500).json({ error: "Server error" });
  }
};


/*
|--------------------------------------------------------------------------
| 4. Get Investment History (Total Investment graph)
|   1M  -> group by DAY (last 30 days)
|   6M  -> group by MONTH (last 6 months)
|   1Y  -> group by MONTH (last 12 months)
|--------------------------------------------------------------------------
*/

/* exports.getInvestmentHistory = async (req, res) => {
  try {
    const mongoose = require("mongoose");

    if (!req.user?.id) {
      return res.status(401).json({ error: "User not authenticated" });
    }

    const userId = new mongoose.Types.ObjectId(req.user.id);
    const range = req.query.range || "6M";
    const now = new Date();

    let fromDate, groupStage, sortStage;

    if (range === "1M") {
      fromDate = new Date();
      fromDate.setDate(fromDate.getDate() - 30);

      groupStage = {
        _id: {
          year: { $year: "$date" },
          month: { $month: "$date" },
          day: { $dayOfMonth: "$date" },
        },
        total: { $sum: "$amount" },
      };

      sortStage = {
        "_id.year": 1,
        "_id.month": 1,
        "_id.day": 1,
      };

    } else if (range === "6M") {
      fromDate = new Date(now.getFullYear(), now.getMonth() - 5, 1);

      groupStage = {
        _id: {
          year: { $year: "$date" },
          month: { $month: "$date" },
        },
        total: { $sum: "$amount" },
      };

      sortStage = {
        "_id.year": 1,
        "_id.month": 1,
      };

    } else {
      fromDate = new Date(now.getFullYear() - 1, now.getMonth(), 1);

      groupStage = {
        _id: {
          year: { $year: "$date" },
          month: { $month: "$date" },
        },
        total: { $sum: "$amount" },
      };

      sortStage = {
        "_id.year": 1,
        "_id.month": 1,
      };
    }

    const data = await Transaction.aggregate([
      {
        $match: {
          userId,
          type: "Investment",
          date: { $gte: fromDate },
        },
      },
      { $group: groupStage },
      { $sort: sortStage },
    ]);

    if (!data.length) return res.json([]);

    const months = [
      "Jan","Feb","Mar","Apr","May","Jun",
      "Jul","Aug","Sep","Oct","Nov","Dec"
    ]; */
/* 
    const chartData = data.map((item) => {
      if (range === "1M") {
        return {
          name: String(item._id.day),
          value: item.total,
        };
      }

      return {
        name: months[item._id.month - 1],
        value: item.total,
      };
    });

    res.json(chartData); */
/* let chartData = [];

if (range === "1M") {
const map = new Map();

data.forEach(d => {
map.set(d._id.day, d.total);
});

// fill last 30 days
for (let i = 29; i >= 0; i--) {
const d = new Date(now);
d.setDate(now.getDate() - i);

const day = d.getDate();

chartData.push({
  name: String(day),
  value: map.get(day) || 0,
});
}

} else {
const months = [
"Jan","Feb","Mar","Apr","May","Jun",
"Jul","Aug","Sep","Oct","Nov","Dec"
];

const map = new Map();
data.forEach(d => {
map.set(`${d._id.year}-${d._id.month}`, d.total);
});

const monthsCount = range === "6M" ? 6 : 12;

for (let i = monthsCount - 1; i >= 0; i--) {
const d = new Date(now);
d.setMonth(now.getMonth() - i);

const key = `${d.getFullYear()}-${d.getMonth() + 1}`;

chartData.push({
  name: months[d.getMonth()],
  value: map.get(key) || 0,
});
}
}

res.json(chartData);


} catch (err) {
console.error("Investment history error:", err);
res.status(500).json({ error: "Server error" });
}
};
*/

exports.getInvestmentHistory = async (req, res) => {
  try {
    const mongoose = require("mongoose");

    const authenticatedUserId = getAuthenticatedUserId(req);
    if (!authenticatedUserId) {
      return res.status(401).json({ error: "User not authenticated" });
    }

    if (!mongoose.Types.ObjectId.isValid(authenticatedUserId)) {
      return res.status(400).json({ error: "Invalid user id" });
    }

    const userId = new mongoose.Types.ObjectId(authenticatedUserId);
    const range = req.query.range || "6M";
    const now = new Date();

    let fromDate, groupStage, sortStage;

    /* ---------------- RANGE SETUP ---------------- */

    if (range === "1M") {
      fromDate = new Date();
      fromDate.setDate(fromDate.getDate() - 29); // 30 days including today

      groupStage = {
        _id: {
          year: { $year: "$date" },
          month: { $month: "$date" },
          day: { $dayOfMonth: "$date" },
        },
        total: { $sum: "$amount" },
      };

      sortStage = {
        "_id.year": 1,
        "_id.month": 1,
        "_id.day": 1,
      };

    } else if (range === "6M") {
      fromDate = new Date(now.getFullYear(), now.getMonth() - 5, 1);

      groupStage = {
        _id: {
          year: { $year: "$date" },
          month: { $month: "$date" },
        },
        total: { $sum: "$amount" },
      };

      sortStage = {
        "_id.year": 1,
        "_id.month": 1,
      };

    } else { // 1Y
      fromDate = new Date(now.getFullYear() - 1, now.getMonth(), 1);

      groupStage = {
        _id: {
          year: { $year: "$date" },
          month: { $month: "$date" },
        },
        total: { $sum: "$amount" },
      };

      sortStage = {
        "_id.year": 1,
        "_id.month": 1,
      };
    }

    /* ---------------- AGGREGATION ---------------- */

    const data = await Transaction.aggregate([
      {
        $match: {
          userId,
          type: { $regex: /^Investment$/i },
          date: { $gte: fromDate },
        },
      },
      { $group: groupStage },
      { $sort: sortStage },
    ]);

    /* ---------------- BUILD CHART ---------------- */

    let chartData = [];

    if (range === "1M") {
      const map = new Map();

      data.forEach(d => {
        const key =
          `${d._id.year}-${String(d._id.month).padStart(2, "0")}-${String(d._id.day).padStart(2, "0")}`;

        map.set(key, d.total);
      });

      for (let i = 29; i >= 0; i--) {
        const d = new Date();
        d.setDate(now.getDate() - i);

        const key =
          `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;

        const monthNamesShort = [
          "Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ];

        chartData.push({
          name: `${d.getDate()} ${monthNamesShort[d.getMonth()]}`,
          value: map.get(key) || 0,
        });

      }

    } else {
      const months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
      ];

      const map = new Map();
      data.forEach(d => {
        map.set(`${d._id.year}-${d._id.month}`, d.total);
      });

      const monthsCount = range === "6M" ? 6 : 12;

      for (let i = monthsCount - 1; i >= 0; i--) {
        const d = new Date(now);
        d.setMonth(now.getMonth() - i);

        const key = `${d.getFullYear()}-${d.getMonth() + 1}`;

        chartData.push({
          name: months[d.getMonth()],
          value: map.get(key) || 0,
        });
      }
    }

    res.json(chartData);

  } catch (err) {
    console.error("Investment history error:", err);
    res.status(500).json({ error: "Server error" });
  }
};
