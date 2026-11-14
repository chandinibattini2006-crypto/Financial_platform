import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def build_financial_from_template():
    template_path = r"c:\Users\kommi\Desktop\sushuruth\Sushuruth_Review1_PPT.pptx"
    primary_output = r"c:\Users\kommi\Desktop\DRAKZ_Financial_Platform_Template_PPT.pptx"
    alt_output = r"c:\Users\kommi\Desktop\FINANCIAL_PROJECT\DRAKZ_Financial_Platform_Template_PPT.pptx"

    if not os.path.exists(template_path):
        print(f"Error: Template not found at {template_path}")
        return

    prs = Presentation(template_path)
    
    # Colors matching the exact Review 1 template
    COLOR_PRIMARY_BLUE = RGBColor(0, 102, 204)  # #0066CC - Header highlight color
    COLOR_DARK_TEXT = RGBColor(30, 41, 59)      # #1E293B - Crisp readable text
    COLOR_TITLE = RGBColor(15, 23, 42)          # #0F172A - Main slide title
    
    # =============================================================
    # SLIDE 1: Title & Project Details
    # =============================================================
    s1 = prs.slides[0]
    
    # Update main title in shape 0
    if len(s1.shapes) > 0 and s1.shapes[0].has_text_frame:
        tf0 = s1.shapes[0].text_frame
        tf0.paragraphs[0].text = "DRAKZ — Financial Planning Platform"
        tf0.paragraphs[0].font.size = Pt(36)
        tf0.paragraphs[0].font.bold = True
        tf0.paragraphs[0].font.color.rgb = COLOR_PRIMARY_BLUE

    # Update Department in shape 4
    if len(s1.shapes) > 4 and s1.shapes[4].has_text_frame:
        tf4 = s1.shapes[4].text_frame
        tf4.paragraphs[0].text = "Department of Computer Science & Engineering"
        tf4.paragraphs[0].font.size = Pt(20)
        tf4.paragraphs[0].font.bold = True

    # Update Academic Year / Review in shape 5
    if len(s1.shapes) > 5 and s1.shapes[5].has_text_frame:
        tf5 = s1.shapes[5].text_frame
        tf5.paragraphs[0].text = "Major Project: Review Presentation (Academic Year 2026-27)"
        tf5.paragraphs[0].font.size = Pt(18)
        tf5.paragraphs[0].font.bold = True

    # Helper function to populate Title & Content slides cleanly
    def populate_slide(slide, title_text, sections):
        # Set Title
        if slide.shapes.title:
            slide.shapes.title.text = title_text
            p_t = slide.shapes.title.text_frame.paragraphs[0]
            p_t.font.size = Pt(28)
            p_t.font.bold = True
            p_t.font.color.rgb = COLOR_TITLE

        # Find Content Placeholder (shape 1)
        content_shape = None
        for sh in slide.shapes:
            if sh != slide.shapes.title and sh.has_text_frame:
                content_shape = sh
                break

        if not content_shape:
            return

        tf = content_shape.text_frame
        tf.clear() # Clear existing paragraphs

        is_first = True
        for header, bullets in sections:
            # Section Header Paragraph
            if is_first:
                p_head = tf.paragraphs[0]
                is_first = False
            else:
                p_head = tf.add_paragraph()
                p_head.space_before = Pt(12)

            p_head.level = 0
            r_h = p_head.add_run()
            r_h.text = header
            r_h.font.size = Pt(20)
            r_h.font.bold = True
            r_h.font.color.rgb = COLOR_PRIMARY_BLUE

            # Bullets under this section
            for bullet in bullets:
                p_b = tf.add_paragraph()
                p_b.level = 0
                p_b.space_before = Pt(3)
                r_b = p_b.add_run()
                r_b.text = bullet
                r_b.font.size = Pt(17)
                r_b.font.color.rgb = COLOR_DARK_TEXT

    # =============================================================
    # SLIDE 2: Background and Domain
    # =============================================================
    s2_sections = [
        ("Financial Literacy & Advisory Crisis", [
            "\u2022 Over 76% of Indian adults do not understand basic financial tenets (compound interest, inflation, credit rating)",
            "\u2022 Fiduciary wealth advisory is traditionally gatekept for ultra-high-net-worth individuals, ignoring retail users",
            "\u2022 Heavy reliance on unvetted social media financial tips leads to unoptimized savings and debt traps"
        ]),
        ("The Role of AI & Modern Web in FinTech", [
            "\u2022 Context-Aware LLMs (TinyLlama 1.1B) synthesize user income, recurring expenses, and savings into custom advice",
            "\u2022 Interactive 3D WebGL (Three.js) transforms dry banking spreadsheets into tactile, engaging credit asset physics",
            "\u2022 Low-Latency WebSockets enable instantaneous stock market reflection and real-time advisor teleconsultation"
        ]),
        ("Domain Scope of DRAKZ Platform", [
            "\u2022 Holistic Asset Vault: Liquid Bank Balances, Equities, Precious Metals (Live Gold/Silver), Real Estate, and Loans",
            "\u2022 Hybrid Advisory Model: 24/7 FinBot AI copilot with seamless handoff to verified certified financial advisors",
            "\u2022 Tri-Role RBAC Governance: Dedicated portals and data sandboxing for Users, Advisors, and Administrators"
        ])
    ]
    populate_slide(prs.slides[1], "Background and Domain", s2_sections)

    # =============================================================
    # SLIDE 3: Literature Review & Existing Systems
    # =============================================================
    s3_sections = [
        ("Survey of Foundational Research Papers", [
            "\u2022 H. Markowitz (1952): Portfolio Selection \u2014 Mathematical mean-variance optimization of asset risk vs returns",
            "\u2022 P. Zhang et al. (2024): TinyLlama \u2014 1.1B compact autoregressive model for efficient, on-premise edge LLM inference",
            "\u2022 S. Yang et al. (2023): FinGPT \u2014 Open-source domain prompt engineering for personalized financial reasoning",
            "\u2022 I. Fette & Melnikov (2011): RFC 6455 WebSocket Protocol \u2014 Full-duplex bi-directional TCP communication standard",
            "\u2022 OWASP & NIST (2023): Financial Application Security \u2014 Stateless JWT authentication, 12-round Bcrypt, and AES encryption"
        ]),
        ("Critical Literature Insights & Synthesis", [
            "\u2022 Existing literature focuses overwhelmingly on high-frequency algorithmic trading or standalone NLP chatbots",
            "\u2022 Prior models lack multi-asset consolidation across tangible properties, gold bullion, and live equities",
            "\u2022 Absence of unified platforms that integrate on-premise generative AI with verified human advisor video rooms"
        ])
    ]
    populate_slide(prs.slides[2], "Literature Review", s3_sections)

    # =============================================================
    # SLIDE 4: Existing Systems & Comparative Analysis
    # =============================================================
    s4_sections = [
        ("Analysis of Current Commercial FinTech Systems", [
            "\u2022 Commercial Brokerages (Zerodha, Groww): Order execution engines without financial planning or AI guidance",
            "\u2022 Budgeting Trackers (Mint, Walnut): Read-only expense tracking without tangible asset vaults or advisor rooms",
            "\u2022 Traditional Banking Portals: Rigid, siloed accounts with legacy 2D interfaces and zero real-time collaboration"
        ]),
        ("Common Limitations in Existing Systems", [
            "\u2022 Siloed Ecosystems: Users must juggle 4\u20136 separate apps for spendings, stocks, bank loans, and insurance",
            "\u2022 Impersonal Heuristics: Generic robo-advisors offer static rule tips without user cashflow context",
            "\u2022 Advisory Disconnect: No frictionless digital bridge to consult a verified fiduciary advisor with live telemetry",
            "\u2022 Weak Auditability: Unmonitored endpoints lack structured HTTP access logging and standardized OpenAPI specs"
        ])
    ]
    populate_slide(prs.slides[3], "Existing Systems & Comparative Analysis", s4_sections)

    # =============================================================
    # SLIDE 5: Problem Identification & Limitations of Existing Systems
    # =============================================================
    s5_sections = [
        ("Key Problems Identified in Current Wealth Platforms", [
            "\u2022 Asset Fragmentation: Inability to track liquid equities and tangible assets (real estate, gold) in one dashboard",
            "\u2022 Context-Blind Advice: Static calculators ignore monthly income, discretionary burn rates, and revolving debt",
            "\u2022 The Advisory Chasm: High-net-worth advisory is expensive and disconnected from user real-time financial data",
            "\u2022 Engagement Apathy: Intimidating tabular spreadsheets cause high abandonment rates among retail users"
        ]),
        ("Engineering Gaps Addressed by DRAKZ", [
            "\u2022 Unified multi-asset wealth vault uniting liquid funds, live metal spot prices, and property valuations",
            "\u2022 Localized TinyLlama 1.1B LLM microservice providing sub-second personalized advice with zero external data leaks",
            "\u2022 Real-time Socket.io teleconsultation rooms enabling dual-direction chat and WebRTC video with certified advisors"
        ])
    ]
    populate_slide(prs.slides[4], "Problem Identification & Limitations of Existing Systems", s5_sections)

    # =============================================================
    # SLIDE 6: Project Planning & Proposal (CLEAN - NO TIMELINE)
    # =============================================================
    s6_sections = [
        ("Project Proposal & Core Objectives", [
            "\u2022 Build DRAKZ: A unified 3-tier financial ecosystem combining multi-asset tracking with AI copilot and advisory",
            "\u2022 Deploy an on-premise TinyLlama 1.1B microservice providing customized advice via prompt context injection",
            "\u2022 Implement Tri-Role Portals: User Dashboard (18 views), Advisor Portal (6 views), and Admin Cockpit (8 views)",
            "\u2022 Provide interactive 3D WebGL asset visualization using Three.js and React Three Fiber with realistic physics"
        ]),
        ("System Specifications & Core Requirements (No Timeline)", [
            "\u2022 Core Environment: React 18, Vite, Node.js Express 4.21, Python 3.10 Flask, MongoDB 7.8, and Socket.io 4.8",
            "\u2022 Performance Benchmark: Sub-500ms RESTful API latency; TinyLlama 1.1B runs locally consuming under 3GB RAM",
            "\u2022 Enterprise Security: 12-round Bcrypt password hashing, symmetric AES-256 card encryption, and stateless JWT tokens",
            "\u2022 Data Sovereignty & Audit: Localized LLM prevents external financial data leakage; multi-stream Morgan telemetry"
        ])
    ]
    populate_slide(prs.slides[5], "Project Planning & Proposal", s6_sections)

    # =============================================================
    # SLIDE 7: Methodology — Core AI & Financial Engines
    # =============================================================
    s7_sections = [
        ("Multi-Engine Technical Methodology", [
            "\u2022 FinBot AI Engine (TinyLlama 1.1B on Port 5002): Autoregressive Transformer with dynamic cashflow prompt injection",
            "\u2022 3D WebGL Graphics Engine: Three.js and React Three Fiber rendering interactive card_model.glb with metallic PBR shaders",
            "\u2022 Spendings Analytics Engine: Categorical expense distribution pie mapping and trailing weekly trend interpolation",
            "\u2022 Real-Time Teleconsultation Hub: Socket.io 4.8 full-duplex room isolation for live chat and WebRTC video streaming"
        ]),
        ("Context-Injected Advice & Advisory Execution Pipeline", [
            "\u2022 User Financial Telemetry \u2192 Context String Formulation \u2192 TinyLlama Prompt \u2192 Personalized Financial Guidance",
            "\u2022 Seamless Escalation: Direct one-click handoff from automated AI advice into a live certified advisor video room",
            "\u2022 Resilient Gateway Architecture: Axios interceptors in Express gateway ensure fallback response matrix on AI timeout"
        ])
    ]
    populate_slide(prs.slides[6], "Methodology — Core Financial & AI Engines", s7_sections)

    # =============================================================
    # SLIDE 8: System Architecture & Component Specifications (NO DIAGRAM)
    # =============================================================
    s8_sections = [
        ("3-Tier Distributed Microservices Blueprint", [
            "\u2022 Client Presentation Tier: React 18, Vite, Tailwind CSS, Three.js 3D WebGL, Recharts, Socket.io-client (Port 3000)",
            "\u2022 API Gateway & Orchestrator: Node.js Express 4.21, JWT Auth, Bcrypt, Multer file upload, Socket.io (Port 5000)",
            "\u2022 AI Computing Tier: Python Flask, HuggingFace Transformers, TinyLlama 1.1B Chat Pipeline (Port 5002)",
            "\u2022 Database Persistence Tier: MongoDB 7.8 on Port 27017 with 15+ Mongoose schemas (239+ seeded records in 'fdfed')"
        ]),
        ("Core Architectural Design Principles", [
            "\u2022 Decoupled Scalability: The Python LLM microservice runs independently, preventing AI compute spikes from slowing API routes",
            "\u2022 Asynchronous Resilience: Socket.io chat & video signaling operate in memory with asynchronous MongoDB persistence",
            "\u2022 Enterprise Observability: Multi-stream Morgan logging (access.log, error.log, user-activity.log) and Swagger UI at /api-docs"
        ])
    ]
    populate_slide(prs.slides[7], "System Architecture & Component Specifications", s8_sections)

    # =============================================================
    # SLIDE 9: References (Strict IEEE Standard)
    # =============================================================
    s9 = prs.slides[8]
    if s9.shapes.title:
        s9.shapes.title.text = "References"
        s9.shapes.title.text_frame.paragraphs[0].font.size = Pt(28)
        s9.shapes.title.text_frame.paragraphs[0].font.bold = True
        s9.shapes.title.text_frame.paragraphs[0].font.color.rgb = COLOR_TITLE

    content_shape9 = None
    for sh in s9.shapes:
        if sh != s9.shapes.title and sh.has_text_frame:
            content_shape9 = sh
            break

    if content_shape9:
        tf9 = content_shape9.text_frame
        tf9.clear()

        p_rh = tf9.paragraphs[0]
        r_rh = p_rh.add_run()
        r_rh.text = "IEEE Standard Citations:"
        r_rh.font.size = Pt(20)
        r_rh.font.bold = True
        r_rh.font.color.rgb = COLOR_PRIMARY_BLUE

        ieee_refs = [
            "[1] H. Markowitz, \"Portfolio Selection,\" The Journal of Finance, vol. 7, no. 1, pp. 77\u201391, Mar. 1952.",
            "[2] P. Zhang et al., \"TinyLlama: An Open-Source Small Language Model,\" arXiv preprint arXiv:2401.02385, Jan. 2024.",
            "[3] S. Yang, X. Y. Liu, and C. D. Wang, \"FinGPT: Open-Source Financial Large Language Models,\" in Proc. NeurIPS Workshop, 2023.",
            "[4] I. Fette and A. Melnikov, \"The WebSocket Protocol,\" Internet Engineering Task Force (IETF), RFC 6455, Dec. 2011.",
            "[5] A. Vaswani et al., \"Attention Is All You Need,\" in Advances in Neural Information Processing Systems (NeurIPS), 2017, pp. 5998\u20136008.",
            "[6] D. Cabrero, I. Saura, and C. Delgado, \"Evaluating WebGL 3D user experience for financial data visualization,\" IEEE Access, vol. 10, 2022.",
            "[7] National Centre for Financial Education (NCFE), \"Financial Literacy and Inclusion Survey in India,\" RBI & SEBI Report, 2022.",
            "[8] E. Rescorla, \"The Transport Layer Security (TLS) Protocol Version 1.3,\" Internet Engineering Task Force (IETF), RFC 8446, 2018."
        ]

        for ref in ieee_refs:
            p_ref = tf9.add_paragraph()
            p_ref.space_before = Pt(3)
            r_ref = p_ref.add_run()
            r_ref.text = ref
            r_ref.font.size = Pt(14)
            r_ref.font.color.rgb = COLOR_DARK_TEXT

    # =============================================================
    # SLIDE 10: Thank You! & Project Readiness
    # =============================================================
    s10 = prs.slides[9]
    if s10.shapes.title:
        s10.shapes.title.text = "Thank You!"
        s10.shapes.title.text_frame.paragraphs[0].font.size = Pt(32)
        s10.shapes.title.text_frame.paragraphs[0].font.bold = True
        s10.shapes.title.text_frame.paragraphs[0].font.color.rgb = COLOR_TITLE

    content_shape10 = None
    for sh in s10.shapes:
        if sh != s10.shapes.title and sh.has_text_frame:
            content_shape10 = sh
            break

    if content_shape10:
        tf10 = content_shape10.text_frame
        tf10.clear()

        p1 = tf10.paragraphs[0]
        r1 = p1.add_run()
        r1.text = "DRAKZ — Financial Planning Platform"
        r1.font.size = Pt(22)
        r1.font.bold = True
        r1.font.color.rgb = COLOR_PRIMARY_BLUE

        bullets10 = [
            "\u2022 Major Project Review Milestone Accomplished & Fully Operational",
            "\u2022 3-Tier Distributed Architecture (React 18 + Express API Gateway + Flask LLM + MongoDB)",
            "\u2022 Localized TinyLlama 1.1B Contextual AI Financial Copilot Running on Port 5002",
            "\u2022 Real-time Certified Advisor Video Teleconsultation & Socket.io WebSockets",
            "\u2022 Interactive Three.js 3D WebGL Credit Assets & Dynamic Spendings Analytics",
            "\u2022 239+ Seeded Real-World Records & Interactive Swagger OpenAPI Documentation (/api-docs)",
            "\u2022 System Tested & Fully Prepared for Live Evaluation Demonstration"
        ]
        for b in bullets10:
            p = tf10.add_paragraph()
            p.space_before = Pt(5)
            r = p.add_run()
            r.text = b
            r.font.size = Pt(17)
            r.font.color.rgb = COLOR_DARK_TEXT

        p_q = tf10.add_paragraph()
        p_q.space_before = Pt(16)
        r_q = p_q.add_run()
        r_q.text = "Questions & Feedback Welcome from the Review Panel"
        r_q.font.size = Pt(20)
        r_q.font.bold = True
        r_q.font.color.rgb = COLOR_PRIMARY_BLUE

        p_quote = tf10.add_paragraph()
        p_quote.space_before = Pt(6)
        r_quote = p_quote.add_run()
        r_quote.text = "\"Democratizing intelligent wealth management through privacy-first AI and real-time collaboration.\""
        r_quote.font.size = Pt(15)
        r_quote.font.italic = True
        r_quote.font.color.rgb = RGBColor(100, 116, 139)

    prs.save(primary_output)
    print(f"Successfully generated presentation using Sushruth Review 1 template at: {primary_output}")
    try:
        prs.save(alt_output)
        print(f"Also saved in project directory: {alt_output}")
    except Exception as e:
        print(f"Note: Could not save alt_output ({e}). Primary output is saved.")

if __name__ == "__main__":
    build_financial_from_template()
