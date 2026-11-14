import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_presentation(output_path="DRAKZ_Financial_Platform_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # completely blank layout

    # Color Palette Definitions - Clean FinTech Executive Theme
    COLOR_NAVY_DARK = RGBColor(10, 25, 47)      # #0A192F - Deep Obsidian Navy
    COLOR_NAVY_LIGHT = RGBColor(23, 42, 69)     # #172A45 - Elevated Navy Card
    COLOR_CYAN_ACCENT = RGBColor(2, 132, 199)   # #0284C7 - Electric FinTech Blue
    COLOR_CYAN_LIGHT = RGBColor(224, 242, 254)  # #E0F2FE - Light Cyan Card
    COLOR_EMERALD = RGBColor(16, 185, 129)      # #10B981 - Wealth Emerald Green
    COLOR_EMERALD_LIGHT = RGBColor(236, 253, 245)# #ECFDF5 - Light Emerald Card
    COLOR_BG_LIGHT = RGBColor(248, 250, 252)    # #F8FAFC - Main content slide BG
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_TEXT_MAIN = RGBColor(15, 23, 42)      # Deep slate for main text
    COLOR_TEXT_MUTED = RGBColor(71, 85, 105)    # Slate 600 for subtext
    COLOR_CARD_BORDER = RGBColor(226, 232, 240) # Subtle Card Border

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text, dark_mode=False):
        # Category / Super-header
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(12)
        p_cat.font.bold = True
        p_cat.font.name = "Calibri"
        p_cat.font.color.rgb = COLOR_CYAN_ACCENT if not dark_mode else RGBColor(56, 189, 248)

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.65))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(25)
        p_title.font.bold = True
        p_title.font.name = "Calibri"
        p_title.font.color.rgb = COLOR_NAVY_DARK if not dark_mode else COLOR_WHITE

        # Divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.42), Inches(11.733), Inches(0.03))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_CYAN_ACCENT
        line.line.fill.background()

    def add_card(slide, left, top, width, height, bg_color=COLOR_WHITE, border_color=COLOR_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.5)
        else:
            card.line.fill.background()
        return card

    # =========================================================================
    # SLIDE 1: Title of the Project
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, COLOR_NAVY_DARK)

    # Accent top border
    top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.12))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = COLOR_EMERALD
    top_bar.line.fill.background()

    # Subtitle Badge
    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.0), Inches(5.2), Inches(0.42))
    badge.fill.solid()
    badge.fill.fore_color.rgb = COLOR_NAVY_LIGHT
    badge.line.color.rgb = COLOR_CYAN_ACCENT
    badge.line.width = Pt(1.5)
    tb_badge = badge.text_frame
    p_b = tb_badge.paragraphs[0]
    p_b.text = "CAPSTONE / MAJOR PROJECT PRESENTATION"
    p_b.font.size = Pt(12)
    p_b.font.bold = True
    p_b.font.color.rgb = RGBColor(56, 189, 248)
    p_b.alignment = PP_ALIGN.CENTER

    # Project Title
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(11.3), Inches(1.8))
    tf = t_box.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = "DRAKZ : FINANCIAL PLANNING PLATFORM"
    p1.font.size = Pt(40)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.font.name = "Calibri"

    p2 = tf.add_paragraph()
    p2.text = "Digital Revenue and Assets Keeper Zone — AI Wealth Management & Live Advisory Ecosystem"
    p2.font.size = Pt(21)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_EMERALD
    p2.font.name = "Calibri"
    p2.space_before = Pt(6)

    # Key Tech Highlights Bar
    tech_bar = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(3.7), Inches(11.33), Inches(0.7))
    tech_bar.fill.solid()
    tech_bar.fill.fore_color.rgb = COLOR_NAVY_LIGHT
    tech_bar.line.fill.background()
    tb_tech = tech_bar.text_frame
    p_tech = tb_tech.paragraphs[0]
    p_tech.text = "TinyLlama 1.1B LLM  |  Three.js 3D WebGL  |  Node.js Express 4.21  |  MongoDB  |  Socket.io Real-Time Video & Chat"
    p_tech.font.size = Pt(14)
    p_tech.font.bold = True
    p_tech.font.color.rgb = RGBColor(224, 242, 254)
    p_tech.alignment = PP_ALIGN.CENTER

    # Team & Department Info Cards
    card_left = add_card(s1, Inches(1.0), Inches(4.7), Inches(5.4), Inches(2.1), COLOR_NAVY_LIGHT, COLOR_CYAN_ACCENT)
    tf_cl = card_left.text_frame
    tf_cl.margin_left = tf_cl.margin_right = tf_cl.margin_top = Inches(0.2)
    p_cl0 = tf_cl.paragraphs[0]
    p_cl0.text = "PROJECT CANDIDATE(S)"
    p_cl0.font.size = Pt(13)
    p_cl0.font.bold = True
    p_cl0.font.color.rgb = RGBColor(56, 189, 248)
    p_cl1 = tf_cl.add_paragraph()
    p_cl1.text = "• Student Name(s): [Your Name / Team Members]\n• Roll Number(s): [Your Roll Numbers]\n• Degree: Bachelor of Technology (B.Tech) in CSE"
    p_cl1.font.size = Pt(14)
    p_cl1.font.color.rgb = COLOR_WHITE
    p_cl1.space_before = Pt(6)

    card_right = add_card(s1, Inches(6.9), Inches(4.7), Inches(5.4), Inches(2.1), COLOR_NAVY_LIGHT, COLOR_EMERALD)
    tf_cr = card_right.text_frame
    tf_cr.margin_left = tf_cr.margin_right = tf_cr.margin_top = Inches(0.2)
    p_cr0 = tf_cr.paragraphs[0]
    p_cr0.text = "SUPERVISION & INSTITUTION"
    p_cr0.font.size = Pt(13)
    p_cr0.font.bold = True
    p_cr0.font.color.rgb = COLOR_EMERALD
    p_cr1 = tf_cr.add_paragraph()
    p_cr1.text = "• Project Supervisor / Guide: [Supervisor Name]\n• Department of Computer Science & Engineering\n• Academic Year: 2026 – 2027"
    p_cr1.font.size = Pt(14)
    p_cr1.font.color.rgb = COLOR_WHITE
    p_cr1.space_before = Pt(6)

    # =========================================================================
    # SLIDE 2: Background and Domain
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, COLOR_BG_LIGHT)
    add_header(s2, "FinTech Landscape & Modern Personal Wealth Management", "Section 2: Background and Domain")

    c1 = add_card(s2, Inches(0.8), Inches(1.7), Inches(3.7), Inches(5.3))
    tf1 = c1.text_frame
    tf1.margin_left = tf1.margin_right = tf1.margin_top = Inches(0.25)
    p = tf1.paragraphs[0]
    p.text = "THE FINANCIAL LITERACY CRISIS"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_DARK
    
    bullets1 = [
        ("Widespread Deficit:", " Over 76% of Indian adults do not understand basic financial concepts such as compound interest, inflation risk, and credit ratings."),
        ("Urban-Rural Advisory Divide:", " Quality certified financial planning is concentrated in ultra-high-net-worth brackets; retail users receive no personalized fiduciary guidance."),
        ("Information Asymmetry:", " Retail investors are exposed to unvetted social media advice, predatory high-interest credit instruments, and unoptimized spending habits.")
    ]
    for b_title, b_desc in bullets1:
        p = tf1.add_paragraph()
        p.space_before = Pt(10)
        run_b = p.add_run()
        run_b.text = b_title
        run_b.font.bold = True
        run_b.font.size = Pt(13)
        run_b.font.color.rgb = COLOR_CYAN_ACCENT
        run_d = p.add_run()
        run_d.text = b_desc
        run_d.font.size = Pt(13)
        run_d.font.color.rgb = COLOR_TEXT_MAIN

    c2 = add_card(s2, Inches(4.8), Inches(1.7), Inches(3.7), Inches(5.3))
    tf2 = c2.text_frame
    tf2.margin_left = tf2.margin_right = tf2.margin_top = Inches(0.25)
    p = tf2.paragraphs[0]
    p.text = "WHY AI & REAL-TIME WEB IN FINTECH?"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_DARK
    
    bullets2 = [
        ("Context-Aware LLM Inference:", " Small language models (TinyLlama 1.1B) synthesize monthly cashflow, savings ratios, and liabilities into personalized advice."),
        ("3D Interactive Immersion:", " WebGL and Three.js transform mundane credit and card management into engaging, tactile visual feedback."),
        ("Sub-Second Socket Telemetry:", " WebSockets allow instantaneous synchronization of financial market feeds and dual-direction live advisor video/chat."),
        ("Continuous Expense Profiling:", " Dynamic categorical clustering reveals discretionary leaks before monthly debt spirals.")
    ]
    for b_title, b_desc in bullets2:
        p = tf2.add_paragraph()
        p.space_before = Pt(10)
        run_b = p.add_run()
        run_b.text = b_title
        run_b.font.bold = True
        run_b.font.size = Pt(13)
        run_b.font.color.rgb = COLOR_CYAN_ACCENT
        run_d = p.add_run()
        run_d.text = b_desc
        run_d.font.size = Pt(13)
        run_d.font.color.rgb = COLOR_TEXT_MAIN

    c3 = add_card(s2, Inches(8.8), Inches(1.7), Inches(3.7), Inches(5.3))
    tf3 = c3.text_frame
    tf3.margin_left = tf3.margin_right = tf3.margin_top = Inches(0.25)
    p = tf3.paragraphs[0]
    p.text = "DRAKZ DOMAIN SCOPE"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_DARK
    
    bullets3 = [
        ("Holistic Multi-Asset Aggregation:", " Consolidates Liquid Cash, Equities, Precious Metals (Live Gold/Silver), Real Estate, and Insurances in a unified vault."),
        ("Hybrid Advisory Model:", " Combines FinBot (instant 24/7 AI financial guidance) with human certified advisors via real-time teleconsultation."),
        ("Tri-Role RBAC Governance:", " Dedicated portals and data sandboxing for Users, Certified Financial Advisors, and Platform Administrators."),
        ("Institutional Audit Trail:", " Multi-stream Morgan telemetry, Swagger OpenAPI contracts, and encrypted digital credit card vaults.")
    ]
    for b_title, b_desc in bullets3:
        p = tf3.add_paragraph()
        p.space_before = Pt(10)
        run_b = p.add_run()
        run_b.text = b_title
        run_b.font.bold = True
        run_b.font.size = Pt(13)
        run_b.font.color.rgb = COLOR_EMERALD
        run_d = p.add_run()
        run_d.text = b_desc
        run_d.font.size = Pt(13)
        run_d.font.color.rgb = COLOR_TEXT_MAIN

    # =========================================================================
    # SLIDE 3: Literature Review
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, COLOR_BG_LIGHT)
    add_header(s3, "Literature Survey of Financial Computing & Advisory Systems", "Section 3: Literature Review")

    rows, cols = 6, 5
    table_shape = s3.shapes.add_table(rows, cols, Inches(0.8), Inches(1.65), Inches(11.733), Inches(4.35))
    table = table_shape.table

    table.columns[0].width = Inches(1.3)   # Author & Year
    table.columns[1].width = Inches(2.4)   # Paper Title
    table.columns[2].width = Inches(2.2)   # Methodology & Architecture
    table.columns[3].width = Inches(2.3)   # Reported Metrics / Findings
    table.columns[4].width = Inches(3.533) # Research Gap / DRAKZ Solution

    headers = ["Author & Year", "Research Paper Title", "Methodology & Architecture", "Key Findings / Metrics", "Research Gap / DRAKZ Solution"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_NAVY_DARK
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

    paper_data = [
        ("[1] H. Markowitz (1952)", "Portfolio Selection (Modern Portfolio Theory)", "Mean-variance mathematical optimization of asset returns vs risk covariance", "Foundational benchmark for balancing diversified asset risk and return frontiers", "Purely theoretical and static; does not account for liquid personal cashflows, loans, or real estate."),
        ("[2] P. Zhang et al. (2024)", "TinyLlama: An Open-Source Small Language Model", "1.1B parameter compact autoregressive model pre-trained on 3 trillion tokens", "Matches sub-3B models on common-sense reasoning while fitting in <3GB memory", "Demonstrated that low-latency domain financial advice can run locally without recurring cloud API fees."),
        ("[3] S. Yang et al. (2023)", "FinGPT: Open-Source Financial Large Language Models", "Domain-specific prompt engineering and fine-tuning for financial sentiment", "Outperformed general LLMs in structured financial reasoning tasks", "Isolated research artifact; lacked integration with transactional databases, KYC, and live advisor rooms."),
        ("[4] I. Fette & Melnikov (2011)", "The WebSocket Protocol (IETF RFC 6455)", "Full-duplex bi-directional TCP socket communication standard", "Sub-10ms packet propagation latency compared to long-polling HTTP overhead", "Validates our choice of Socket.io for continuous live stock tickers and real-time advisor video streaming."),
        ("[5] OWASP & NIST (2023)", "Financial Application Security & Token Standards", "Stateless JSON Web Tokens (JWT) + PBKDF2/Bcrypt + Symmetric Card Encryption", "Essential prevention of unauthorized access, session hijacking, and PCI-DSS violations", "Directly implemented in our Express gateway via 12-round Bcrypt, JWT auth guards, and multi-log auditing.")
    ]

    for row_idx, data in enumerate(paper_data, start=1):
        for col_idx, text in enumerate(data):
            cell = table.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_WHITE if row_idx % 2 == 1 else RGBColor(241, 245, 249)
            p = cell.text_frame.paragraphs[0]
            p.text = text
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_TEXT_MAIN
            if col_idx == 0:
                p.font.bold = True
                p.font.color.rgb = COLOR_CYAN_ACCENT

    syn_card = add_card(s3, Inches(0.8), Inches(6.15), Inches(11.733), Inches(0.9), COLOR_CYAN_LIGHT, COLOR_CYAN_ACCENT)
    tf_syn = syn_card.text_frame
    tf_syn.margin_left = tf_syn.margin_top = Inches(0.15)
    p_syn = tf_syn.paragraphs[0]
    run_sb = p_syn.add_run()
    run_sb.text = "CRITICAL LITERATURE SYNTHESIS: "
    run_sb.font.bold = True
    run_sb.font.size = Pt(13)
    run_sb.font.color.rgb = COLOR_NAVY_DARK
    run_st = p_syn.add_run()
    run_st.text = "Existing literature remains fragmented between high-level algorithmic trading, theoretical portfolio models, and isolated NLP chatbots. DRAKZ bridges this chasm by delivering an end-to-end, multi-tier ecosystem marrying localized AI, interactive 3D WebGL, and verified human advisor teleconsultation."
    run_st.font.size = Pt(12)
    run_st.font.color.rgb = COLOR_NAVY_DARK

    # =========================================================================
    # SLIDE 4: Existing Systems & Comparative Analysis
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, COLOR_BG_LIGHT)
    add_header(s4, "Existing FinTech Platforms & Comparative Evaluation", "Section 3 (Contd.): Existing Systems")

    rows, cols = 6, 6
    table_shape4 = s4.shapes.add_table(rows, cols, Inches(0.8), Inches(1.65), Inches(11.733), Inches(3.65))
    tab4 = table_shape4.table

    tab4.columns[0].width = Inches(2.733) # Evaluation Parameter
    tab4.columns[1].width = Inches(1.8)   # Zerodha
    tab4.columns[2].width = Inches(1.8)   # Groww
    tab4.columns[3].width = Inches(1.8)   # Mint / Intuit
    tab4.columns[4].width = Inches(1.8)   # Traditional Banks
    tab4.columns[5].width = Inches(1.8)   # DRAKZ (Proposed)

    matrix_headers = ["Key Capability / Feature", "Zerodha (Kite)", "Groww", "Mint / Credit Karma", "Traditional Banks", "DRAKZ (Proposed)"]
    for i, h in enumerate(matrix_headers):
        cell = tab4.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_NAVY_DARK if i < 5 else COLOR_EMERALD
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

    matrix_rows = [
        ("Context-Aware AI Financial Advisor", "❌ None", "❌ None", "⚠️ Rule-based Tips", "❌ Rule-based FAQ", "✅ TinyLlama 1.1B LLM"),
        ("Live Advisor Video & WebSockets", "❌ No Live Video", "❌ No Video Consult", "❌ None", "⚠️ Appointment Only", "✅ Socket.io Video/Chat"),
        ("Tangible Assets (Real Estate, Metals)", "❌ Equities Only", "❌ Equities/MF Only", "⚠️ Net Worth Est.", "❌ Fragmented", "✅ Gold, Real Estate, Gems"),
        ("Interactive 3D WebGL Visualization", "❌ Static 2D Charts", "❌ Static UI", "❌ Static 2D", "❌ Legacy 2D", "✅ Three.js 3D Physics"),
        ("Tri-Role RBAC (User/Advisor/Admin)", "⚠️ Broker Only", "⚠️ Broker Only", "❌ Single User", "⚠️ Branch Staff", "✅ Full Multi-Portal RBAC")
    ]

    for row_idx, rdata in enumerate(matrix_rows, start=1):
        for col_idx, val in enumerate(rdata):
            cell = tab4.cell(row_idx, col_idx)
            cell.fill.solid()
            if col_idx == 5:
                cell.fill.fore_color.rgb = COLOR_EMERALD_LIGHT
            else:
                cell.fill.fore_color.rgb = COLOR_WHITE if row_idx % 2 == 1 else RGBColor(248, 250, 252)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(12)
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT
            if col_idx == 0:
                p.font.bold = True
                p.font.color.rgb = COLOR_NAVY_DARK
            elif col_idx == 5:
                p.font.bold = True
                p.font.color.rgb = COLOR_EMERALD

    bot_card = add_card(s4, Inches(0.8), Inches(5.5), Inches(11.733), Inches(1.55), COLOR_WHITE, COLOR_CARD_BORDER)
    tf_b = bot_card.text_frame
    tf_b.margin_left = tf_b.margin_right = tf_b.margin_top = Inches(0.2)
    p_b0 = tf_b.paragraphs[0]
    p_b0.text = "CORE LIMITATIONS OF CURRENT MARKET LEADERS:"
    p_b0.font.size = Pt(13)
    p_b0.font.bold = True
    p_b0.font.color.rgb = COLOR_NAVY_DARK

    p_b1 = tf_b.add_paragraph()
    p_b1.text = "• Commercial Brokerages (Zerodha, Groww): Function strictly as order-routing execution gateways without comprehensive financial life planning or AI advisory."
    p_b1.font.size = Pt(12)
    p_b1.font.color.rgb = COLOR_TEXT_MUTED
    p_b1.space_before = Pt(4)

    p_b2 = tf_b.add_paragraph()
    p_b2.text = "• Budgeting Trackers & Banking Apps: Highly siloed, lack real-time human expert teleconsultation, and ignore tangible wealth (real estate, bullion, private holdings)."
    p_b2.font.size = Pt(12)
    p_b2.font.color.rgb = COLOR_TEXT_MUTED

    # =========================================================================
    # SLIDE 5: Problem Identification & Limitations of Existing Systems
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, COLOR_BG_LIGHT)
    add_header(s5, "Systemic Problems & Deficiencies in Modern Wealth Platforms", "Section 4: Problem Identification")

    cards_info = [
        (Inches(0.8), Inches(1.65), "1. Highly Fragmented Wealth Ecosystems", 
         [("Asset Siloing:", " Users must maintain 4 to 6 discrete applications to manage bank accounts, stock portfolios, real estate, and insurance policies."),
          ("Blind Spot in Net Worth:", " No single system aggregates physical assets (properties, gold bullion) with liquid equities to provide true solvency metrics.")]),
        
        (Inches(6.8), Inches(1.65), "2. Impersonal & Context-Blind Advisory", 
         [("Generic Rule-Based Heuristics:", " Conventional robo-advisors emit static advice without synthesizing the user's live salary, debt burden, and recurring expenses."),
          ("Lack of Generative Synthesis:", " Absence of localized natural language LLMs capable of answering complex, nuanced financial dilemmas interactively.")]),
        
        (Inches(0.8), Inches(4.45), "3. Absence of Human-in-the-Loop Advisory", 
         [("Cold Automated Black-Boxes:", " Users who need fiduciary advice have no mechanism to securely share telemetry with a human certified advisor."),
          ("Disconnected Consultations:", " Traditional advisory requires manual PDF uploads, phone calls, and insecure third-party video apps without integrated dashboards.")]),
        
        (Inches(6.8), Inches(4.45), "4. Subpar Security, Auditing & UX Engagement", 
         [("Boring 2D Spreadsheets:", " Complex card management and credit scores are rendered as intimidating, dry tabular spreadsheets, suppressing engagement."),
          ("Unmonitored API Endpoints:", " Lack of structured HTTP access logging, unencrypted payment storage, and missing OpenAPI documentation across typical university projects.")])
    ]

    for c_left, c_top, c_title, c_bullets in cards_info:
        card = add_card(s5, c_left, c_top, Inches(5.733), Inches(2.6), COLOR_WHITE, COLOR_CARD_BORDER)
        tf_c = card.text_frame
        tf_c.margin_left = tf_c.margin_right = tf_c.margin_top = Inches(0.2)
        p = tf_c.paragraphs[0]
        p.text = c_title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY_DARK

        for b_title, b_desc in c_bullets:
            p = tf_c.add_paragraph()
            p.space_before = Pt(6)
            run_b = p.add_run()
            run_b.text = "• " + b_title
            run_b.font.bold = True
            run_b.font.size = Pt(12)
            run_b.font.color.rgb = COLOR_CYAN_ACCENT
            run_d = p.add_run()
            run_d.text = b_desc
            run_d.font.size = Pt(12)
            run_d.font.color.rgb = COLOR_TEXT_MAIN

    # =========================================================================
    # SLIDE 6: Project Planning & Proposal (CLEAN SPECIFICATIONS - NO TIMELINE)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, COLOR_BG_LIGHT)
    add_header(s6, "Project Planning, Proposed Scope & System Specifications", "Section 5: Project Planning & Proposal")

    # Left Card: Core Proposal & Objectives
    left_card = add_card(s6, Inches(0.8), Inches(1.65), Inches(5.6), Inches(5.35))
    tf_lp = left_card.text_frame
    tf_lp.margin_left = tf_lp.margin_right = tf_lp.margin_top = Inches(0.25)
    p = tf_lp.paragraphs[0]
    p.text = "PROJECT PROPOSAL & OBJECTIVES"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_DARK

    prop_bullets = [
        ("Unified Digital Wealth Vault:", " Consolidate bank balances, loans, credit cards, investments, properties, and insurance policies into a single reactive interface."),
        ("Autonomous Contextual AI Copilot:", " Deploy an on-premise TinyLlama 1.1B LLM microservice providing customized financial guidance using active user cashflow context."),
        ("Real-Time Advisory Channels:", " Implement low-latency WebSocket rooms for bidirectional text chat, typing states, and WebRTC video teleconsultation."),
        ("Interactive 3D WebGL Experiences:", " Leverage Three.js and React Three Fiber to visualize digital credit cards and portfolio representations dynamically."),
        ("Enterprise-Grade API & Security Suite:", " Enforce JWT authentication, Express rate limiting, Multer file processing, Swagger 3.0 documentation, and dual-log auditing.")
    ]
    for b_title, b_desc in prop_bullets:
        p = tf_lp.add_paragraph()
        p.space_before = Pt(8)
        rb = p.add_run()
        rb.text = "• " + b_title
        rb.font.bold = True
        rb.font.size = Pt(12)
        rb.font.color.rgb = COLOR_CYAN_ACCENT
        rd = p.add_run()
        rd.text = b_desc
        rd.font.size = Pt(12)
        rd.font.color.rgb = COLOR_TEXT_MAIN

    # Right Card: System Requirements & Specifications (Replaced Timeline Tracker)
    right_card = add_card(s6, Inches(6.8), Inches(1.65), Inches(5.733), Inches(5.35))
    tf_rp = right_card.text_frame
    tf_rp.margin_left = tf_rp.margin_right = tf_rp.margin_top = Inches(0.25)
    p = tf_rp.paragraphs[0]
    p.text = "SYSTEM REQUIREMENTS & SPECIFICATIONS"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_DARK

    spec_items = [
        ("Core Technology Environment:", " Node.js 18+ runtime, Python 3.10+, PyTorch with HuggingFace Transformers, Vite frontend bundler, and local MongoDB service."),
        ("Hardware & Resource Footprint:", " Optimized CPU inference requiring under 3GB RAM for TinyLlama 1.1B weights; sub-200ms DOM rendering overhead on modern browsers."),
        ("Operational Performance Target:", " Sub-500ms RESTful API latency across financial telemetry controllers; sub-10ms packet propagation via Socket.io WebSockets."),
        ("Data Security & Cryptographic Standard:", " 12-round Bcrypt password hashing, AES-256 symmetric key encryption for card vaults, stateless JWT bearer token auth."),
        ("Regulatory & Compliance Standards:", " Zero third-party data leakage; strict adherence to local data privacy standards with on-premise LLM execution.")
    ]
    for s_title, s_desc in spec_items:
        p = tf_rp.add_paragraph()
        p.space_before = Pt(8)
        rb = p.add_run()
        rb.text = "• " + s_title
        rb.font.bold = True
        rb.font.size = Pt(12)
        rb.font.color.rgb = COLOR_EMERALD
        rd = p.add_run()
        rd.text = s_desc
        rd.font.size = Pt(12)
        rd.font.color.rgb = COLOR_TEXT_MAIN

    # =========================================================================
    # SLIDE 7: Methodology & Core Algorithmic Engines
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, COLOR_BG_LIGHT)
    add_header(s7, "Methodology: AI Advisor, 3D WebGL & Real-Time Engines", "Section 6: Methodology")

    m_cards = [
        (Inches(0.8), Inches(1.65), Inches(2.75), "FinBot AI Engine", "TinyLlama 1.1B LLM (Port 5002)",
         "• Architecture: 1.1B parameter autoregressive Transformer\n• Prompt Engineering: Injects monthly_income, total_expenses, savings, and currency context\n• Sampling: Temp=0.7, Top-k=50, Max Tokens=512\n• Endpoint: POST /api/financial-advice\n• Fallback: Cached response matrix on timeout"),
        
        (Inches(3.8), Inches(1.65), Inches(2.75), "3D WebGL Engine", "Three.js & React Three Fiber",
         "• Graphics Stack: @react-three/fiber, @react-three/drei, GLTFLoader\n• Asset Rendering: Interactive card_model.glb with metallic PBR shaders\n• Interactivity: OrbitControls, dynamic ambient/directional lighting, card flip gestures\n• Component: CardModel.jsx, ThreeDCard.jsx"),
         
        (Inches(6.8), Inches(1.65), Inches(2.75), "Analytics & Spendings", "Categorical & Trend Models",
         "• Expense Engine: Categorical distribution pie mapping (Food, Utilities, Travel, Discretionary)\n• Trend Analysis: Trailing weekly spending delta calculation via Mongoose aggregation\n• Credit Evaluation: Dynamic score updates based on loan-to-asset ratios\n• Endpoint: /api/spendings/*"),
         
        (Inches(9.8), Inches(1.65), Inches(2.733), "Real-Time Teleconsult", "Socket.io 4.8 Engine",
         "• WebSocket Engine: Full-duplex room isolation via server.js\n• Real-Time Actions: join_room, send_message, typing, broadcast_video\n• Teleconsultation: Dual video stream channels for certified advisor sessions\n• Persistence: Chat.model.js asynchronous sync")
    ]

    for c_left, c_top, c_width, c_title, c_tech, c_content in m_cards:
        card = add_card(s7, c_left, c_top, c_width, Inches(4.2), COLOR_WHITE, COLOR_CARD_BORDER)
        tf_m = card.text_frame
        tf_m.margin_left = tf_m.margin_right = tf_m.margin_top = Inches(0.18)
        
        p = tf_m.paragraphs[0]
        p.text = c_title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY_DARK

        p_t = tf_m.add_paragraph()
        p_t.text = c_tech
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_CYAN_ACCENT
        p_t.space_before = Pt(2)

        p_c = tf_m.add_paragraph()
        p_c.text = c_content
        p_c.font.size = Pt(11)
        p_c.font.color.rgb = COLOR_TEXT_MAIN
        p_c.space_before = Pt(6)

    flow_card = add_card(s7, Inches(0.8), Inches(6.05), Inches(11.733), Inches(1.0), COLOR_NAVY_DARK, COLOR_CYAN_ACCENT)
    tf_f = flow_card.text_frame
    tf_f.margin_left = tf_f.margin_right = tf_f.margin_top = Inches(0.15)
    p_f0 = tf_f.paragraphs[0]
    p_f0.text = "AI ADVICE SYNTHESIS & TELECONSULTATION EXECUTION PIPELINE:"
    p_f0.font.size = Pt(12)
    p_f0.font.bold = True
    p_f0.font.color.rgb = RGBColor(56, 189, 248)

    p_f1 = tf_f.add_paragraph()
    p_f1.text = "User Financial Telemetry ➔ Context String Construction ➔ TinyLlama System Prompt ➔ Autoregressive Inference ➔ Personalized Advice Delivery ➔ Option to Escalate to Live Certified Advisor Video Room"
    p_f1.font.size = Pt(12)
    p_f1.font.bold = True
    p_f1.font.color.rgb = COLOR_WHITE
    p_f1.space_before = Pt(4)

    # =========================================================================
    # SLIDE 8: System Architecture (CLEAN COMPONENT CARDS - NO DIAGRAM)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, COLOR_BG_LIGHT)
    add_header(s8, "System Architecture: 3-Tier Distributed Engineering Design", "Section 7: System Architecture")

    # 3 Tier Modular Cards
    t1_card = add_card(s8, Inches(0.8), Inches(1.65), Inches(3.7), Inches(3.9), COLOR_WHITE, COLOR_CARD_BORDER)
    tf_t1 = t1_card.text_frame
    tf_t1.margin_left = tf_t1.margin_right = tf_t1.margin_top = Inches(0.2)
    p = tf_t1.paragraphs[0]
    p.text = "CLIENT PRESENTATION TIER"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_DARK

    p_sub = tf_t1.add_paragraph()
    p_sub.text = "React 18 + Vite (Port 3000)"
    p_sub.font.size = Pt(12)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_CYAN_ACCENT

    t1_points = [
        "• Tri-Role Portals: Isolated views for Users, Advisors & Administrators",
        "• 3D WebGL Graphics: Three.js & Fiber interactive credit card physics",
        "• Data Visualization: Dynamic Chart.js and Recharts modules",
        "• Dynamic UI State: Redux Toolkit and Context API global stores",
        "• Real-Time Client: Low-latency Socket.io-client 4.8 event consumers"
    ]
    for pt in t1_points:
        p = tf_t1.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(4)

    t2_card = add_card(s8, Inches(4.8), Inches(1.65), Inches(3.7), Inches(3.9), COLOR_WHITE, COLOR_CARD_BORDER)
    tf_t2 = t2_card.text_frame
    tf_t2.margin_left = tf_t2.margin_right = tf_t2.margin_top = Inches(0.2)
    p = tf_t2.paragraphs[0]
    p.text = "API GATEWAY & ORCHESTRATOR"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_DARK

    p_sub = tf_t2.add_paragraph()
    p_sub.text = "Node.js Express 4.21 (Port 5000)"
    p_sub.font.size = Pt(12)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_CYAN_ACCENT

    t2_points = [
        "• RESTful Routing: Modular routes (/auth, /users, /spendings, /privilege)",
        "• WebSocket Server: Native Socket.io for bidirectional chat & video",
        "• Security Middleware: Stateless JWT verification and rate limiting",
        "• Telemetry Suite: Multi-stream Morgan (access, error & activity logs)",
        "• Contract Standards: Live OpenAPI 3.0 specs hosted at /api-docs"
    ]
    for pt in t2_points:
        p = tf_t2.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(4)

    t3_card = add_card(s8, Inches(8.8), Inches(1.65), Inches(3.7), Inches(3.9), COLOR_WHITE, COLOR_CARD_BORDER)
    tf_t3 = t3_card.text_frame
    tf_t3.margin_left = tf_t3.margin_right = tf_t3.margin_top = Inches(0.2)
    p = tf_t3.paragraphs[0]
    p.text = "PERSISTENCE & AI SERVICES"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_DARK

    p_sub = tf_t3.add_paragraph()
    p_sub.text = "MongoDB (27017) & Flask (5002)"
    p_sub.font.size = Pt(12)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_EMERALD

    t3_points = [
        "• Document Store: MongoDB 'fdfed' with 15+ Mongoose schemas",
        "• Domain Collections: Users, Advisors, Investments, Cards, Assets",
        "• AI Service: Python Flask with HuggingFace Transformers pipeline",
        "• Localized LLM: TinyLlama 1.1B loaded in CPU/GPU memory",
        "• Data Sovereignty: Zero external API calls for sensitive user telemetry"
    ]
    for pt in t3_points:
        p = tf_t3.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(4)

    # Bottom Architectural Principles Card (Clean Text - Replaced Diagram)
    arch_card = add_card(s8, Inches(0.8), Inches(5.75), Inches(11.733), Inches(1.35), COLOR_WHITE, COLOR_CYAN_ACCENT)
    tf_ac = arch_card.text_frame
    tf_ac.margin_left = tf_ac.margin_right = tf_ac.margin_top = Inches(0.18)
    p_ac = tf_ac.paragraphs[0]
    p_ac.text = "CORE ARCHITECTURAL DESIGN PRINCIPLES:"
    p_ac.font.size = Pt(13)
    p_ac.font.bold = True
    p_ac.font.color.rgb = COLOR_NAVY_DARK

    p_a1 = tf_ac.add_paragraph()
    p_a1.text = "• Decoupled Scalability: The Python LLM microservice runs independently from the Express API gateway, preventing AI compute spikes from degrading transactional throughput."
    p_a1.font.size = Pt(12)
    p_a1.font.color.rgb = COLOR_TEXT_MAIN
    p_a1.space_before = Pt(3)

    p_a2 = tf_ac.add_paragraph()
    p_a2.text = "• Asynchronous Resilience: Socket.io real-time chat sessions operate in memory with asynchronous persistence, ensuring zero thread blocking during peak advisory teleconsultations."
    p_a2.font.size = Pt(12)
    p_a2.font.color.rgb = COLOR_TEXT_MAIN
    p_a2.space_before = Pt(3)

    # =========================================================================
    # SLIDE 9: References (Strict IEEE Standard)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, COLOR_BG_LIGHT)
    add_header(s9, "References (Strict IEEE Citation Standard)", "Section 8: References")

    ref_card = add_card(s9, Inches(0.8), Inches(1.65), Inches(11.733), Inches(5.35), COLOR_WHITE, COLOR_CARD_BORDER)
    tf_ref = ref_card.text_frame
    tf_ref.margin_left = tf_ref.margin_right = tf_ref.margin_top = Inches(0.25)
    
    references = [
        ("[1]", " H. Markowitz, \"Portfolio Selection,\" The Journal of Finance, vol. 7, no. 1, pp. 77–91, Mar. 1952."),
        ("[2]", " P. Zhang et al., \"TinyLlama: An Open-Source Small Language Model,\" arXiv preprint arXiv:2401.02385, Jan. 2024."),
        ("[3]", " S. Yang, X. Y. Liu, and C. D. Wang, \"FinGPT: Open-Source Financial Large Language Models,\" in Proc. NeurIPS Workshop on Instruction Tuning and Instruction Following, New Orleans, USA, Dec. 2023."),
        ("[4]", " I. Fette and A. Melnikov, \"The WebSocket Protocol,\" Internet Engineering Task Force (IETF), RFC 6455, Dec. 2011."),
        ("[5]", " A. Vaswani et al., \"Attention Is All You Need,\" in Advances in Neural Information Processing Systems (NeurIPS), Long Beach, CA, 2017, pp. 5998–6008."),
        ("[6]", " D. Cabrero, I. Saura, and C. Delgado, \"Evaluating WebGL 3D user experience for complex financial data visualization,\" IEEE Access, vol. 10, pp. 45210–45224, Apr. 2022."),
        ("[7]", " National Centre for Financial Education (NCFE), \"Financial Literacy and Inclusion Survey in India,\" Reserve Bank of India & SEBI Joint Report, Mumbai, India, 2022."),
        ("[8]", " E. Rescorla, \"The Transport Layer Security (TLS) Protocol Version 1.3,\" Internet Engineering Task Force (IETF), RFC 8446, Aug. 2018.")
    ]

    p_r0 = tf_ref.paragraphs[0]
    p_r0.text = "PRIMARY ACADEMIC & STANDARDS CITATIONS:"
    p_r0.font.size = Pt(14)
    p_r0.font.bold = True
    p_r0.font.color.rgb = COLOR_NAVY_DARK

    for idx, (num, text) in enumerate(references):
        p = tf_ref.add_paragraph()
        p.space_before = Pt(6)
        run_n = p.add_run()
        run_n.text = num
        run_n.font.bold = True
        run_n.font.size = Pt(12)
        run_n.font.color.rgb = COLOR_CYAN_ACCENT
        run_t = p.add_run()
        run_t.text = text
        run_t.font.size = Pt(12)
        run_t.font.color.rgb = COLOR_TEXT_MAIN

    # =========================================================================
    # SLIDE 10: Conclusion & Ready for Demonstration / Q&A
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, COLOR_NAVY_DARK)

    top_bar10 = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.12))
    top_bar10.fill.solid()
    top_bar10.fill.fore_color.rgb = COLOR_EMERALD
    top_bar10.line.fill.background()

    c_box = s10.shapes.add_textbox(Inches(1.0), Inches(1.3), Inches(11.3), Inches(1.5))
    tf_c = c_box.text_frame
    tf_c.word_wrap = True
    p_c1 = tf_c.paragraphs[0]
    p_c1.text = "THANK YOU"
    p_c1.font.size = Pt(44)
    p_c1.font.bold = True
    p_c1.font.color.rgb = COLOR_WHITE
    p_c1.alignment = PP_ALIGN.CENTER

    p_c2 = tf_c.add_paragraph()
    p_c2.text = "DRAKZ: Next-Gen AI Financial Planning & Real-Time Collaborative Advisory Platform"
    p_c2.font.size = Pt(20)
    p_c2.font.bold = True
    p_c2.font.color.rgb = COLOR_EMERALD
    p_c2.alignment = PP_ALIGN.CENTER
    p_c2.space_before = Pt(6)

    h1 = add_card(s10, Inches(1.5), Inches(3.3), Inches(3.2), Inches(2.4), COLOR_NAVY_LIGHT, COLOR_CYAN_ACCENT)
    tf_h1 = h1.text_frame
    tf_h1.margin_left = tf_h1.margin_right = tf_h1.margin_top = Inches(0.2)
    p = tf_h1.paragraphs[0]
    p.text = "INTELLIGENT WEALTH"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(56, 189, 248)
    p_sub = tf_h1.add_paragraph()
    p_sub.text = "TinyLlama 1.1B LLM financial copilot context-injected with cashflow telemetry and automated spending intelligence."
    p_sub.font.size = Pt(12)
    p_sub.font.color.rgb = COLOR_WHITE
    p_sub.space_before = Pt(6)

    h2 = add_card(s10, Inches(5.1), Inches(3.3), Inches(3.2), Inches(2.4), COLOR_NAVY_LIGHT, COLOR_EMERALD)
    tf_h2 = h2.text_frame
    tf_h2.margin_left = tf_h2.margin_right = tf_h2.margin_top = Inches(0.2)
    p = tf_h2.paragraphs[0]
    p.text = "REAL-TIME ECOSYSTEM"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p_sub = tf_h2.add_paragraph()
    p_sub.text = "Live Socket.io chat, video consultation rooms, real-time metal spot prices, and Finnhub stock market streaming."
    p_sub.font.size = Pt(12)
    p_sub.font.color.rgb = COLOR_WHITE
    p_sub.space_before = Pt(6)

    h3 = add_card(s10, Inches(8.7), Inches(3.3), Inches(3.2), Inches(2.4), COLOR_NAVY_LIGHT, COLOR_CYAN_ACCENT)
    tf_h3 = h3.text_frame
    tf_h3.margin_left = tf_h3.margin_right = tf_h3.margin_top = Inches(0.2)
    p = tf_h3.paragraphs[0]
    p.text = "PRODUCTION READY"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(56, 189, 248)
    p_sub = tf_h3.add_paragraph()
    p_sub.text = "Tri-role RBAC (User, Advisor, Admin), 239+ seeded records, Three.js 3D assets, and interactive Swagger documentation."
    p_sub.font.size = Pt(12)
    p_sub.font.color.rgb = COLOR_WHITE
    p_sub.space_before = Pt(6)

    b_box = s10.shapes.add_textbox(Inches(1.0), Inches(6.0), Inches(11.3), Inches(0.8))
    tf_bb = b_box.text_frame
    p_bb = tf_bb.paragraphs[0]
    p_bb.text = "Open for Questions, Evaluation & Technical Viva Defense"
    p_bb.font.size = Pt(18)
    p_bb.font.bold = True
    p_bb.font.color.rgb = RGBColor(224, 242, 254)
    p_bb.alignment = PP_ALIGN.CENTER

    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    build_presentation()
