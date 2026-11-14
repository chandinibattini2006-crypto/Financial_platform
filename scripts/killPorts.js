#!/usr/bin/env node

const { execSync } = require("child_process");

function unique(values) {
  return [...new Set(values)];
}

function parsePorts(args) {
  const parsed = args
    .map((p) => Number(p))
    .filter((p) => Number.isInteger(p) && p > 0 && p <= 65535);

  return parsed.length ? unique(parsed) : [3000, 3001];
}

function getPidsOnWindows(port) {
  try {
    const out = execSync(`netstat -ano -p tcp | findstr :${port}`, {
      stdio: ["ignore", "pipe", "ignore"],
      encoding: "utf8",
    });

    return unique(
      out
        .split(/\r?\n/)
        .map((line) => line.trim())
        .filter(Boolean)
        .filter((line) => line.includes("LISTENING"))
        .map((line) => line.split(/\s+/).pop())
        .filter((pid) => /^\d+$/.test(pid))
    );
  } catch {
    return [];
  }
}

function getPidsOnUnix(port) {
  const commands = [
    `lsof -ti tcp:${port}`,
    `ss -ltnp 'sport = :${port}' | awk -F'pid=' 'NF>1{print $2}' | awk -F',' '{print $1}'`,
  ];

  for (const command of commands) {
    try {
      const out = execSync(command, {
        stdio: ["ignore", "pipe", "ignore"],
        encoding: "utf8",
      });

      const pids = unique(
        out
          .split(/\r?\n/)
          .map((line) => line.trim())
          .filter((line) => /^\d+$/.test(line))
      );

      if (pids.length) return pids;
    } catch {
      // Try next command.
    }
  }

  return [];
}

function getPidsForPort(port) {
  return process.platform === "win32"
    ? getPidsOnWindows(port)
    : getPidsOnUnix(port);
}

function killPid(pid) {
  try {
    if (process.platform === "win32") {
      execSync(`taskkill /PID ${pid} /F`, { stdio: "ignore" });
    } else {
      execSync(`kill -9 ${pid}`, { stdio: "ignore" });
    }
    return true;
  } catch {
    return false;
  }
}

function main() {
  const ports = parsePorts(process.argv.slice(2));
  const allPids = unique(ports.flatMap((port) => getPidsForPort(port)));

  if (!allPids.length) {
    console.log(`[predev] No conflicting listeners found on ports: ${ports.join(", ")}`);
    return;
  }

  let killed = 0;
  for (const pid of allPids) {
    const ok = killPid(pid);
    if (ok) {
      killed += 1;
      console.log(`[predev] Stopped process PID ${pid}`);
    } else {
      console.warn(`[predev] Could not stop PID ${pid}`);
    }
  }

  console.log(`[predev] Cleanup complete. Processes stopped: ${killed}`);
}

main();
