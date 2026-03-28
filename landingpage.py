import streamlit as st
import streamlit.components.v1 as components

# 1. Setup the page
st.set_page_config(page_title="ZNA - AI Resume Builder", layout="wide", initial_sidebar_state="collapsed")

# 2. Hide Streamlit's default UI borders
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Your entire HTML code securely wrapped in a Python string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZNA - AI Resume Architect</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        /* Base Styles & Reset */
        :root {
            /* Light Theme (Default) Variables */
            --bg-color: #ffffff;
            --text-color: #333333;
            --h1-color: #222222;
            --navbar-bg-color: #ffffff;
            --feature-card-bg: #ffffff;
            
            --accent-dark-blue: #0b3d6e; 
            --accent-yellow: #ffb800;
            --accent-orange: #ff7e5f; /* FAQ plus icon color */
            --light-border: #eaeaea;
            --dark-border: #eee;
            --light-shadow: rgba(0,0,0,0.08);
            --dark-shadow: rgba(0,0,0,0.1);
            --logo-grad-stop-1: #4a90e2;
            --logo-grad-stop-2: #0b3d6e;
            
            /* Testimonial Avatars */
            --avatar-1: #4a90e2;
            --avatar-2: #9b59b6;
            --avatar-3: #2ecc71;
        }

        /* Dark Theme Variables */
        body.night-mode {
            --bg-color: #121212;
            --text-color: #eaeaea;
            --h1-color: #ffffff;
            --navbar-bg-color: #1a1a1a;
            --feature-card-bg: #1e1e1e;
            --light-border: #333333;
            --dark-border: #444444;
            --light-shadow: rgba(255,255,255,0.05);
            --dark-shadow: rgba(255,255,255,0.08);
            --cta-bg: #e6a600;
            --logo-grad-stop-1: #90caf9;
            --logo-grad-stop-2: #3b82f6;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
            transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            overflow-x: hidden;
        }

        /* Semantic Navigation */
        .navbar {
            position: sticky;
            top: 0;
            z-index: 100;
            background-color: var(--navbar-bg-color);
            padding: 24px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--light-border);
        }

        .logo-container {
            height: 75px;
            display: flex;
            align-items: center;
        }

        .nav-links {
            display: flex;
            gap: 32px;
            align-items: center;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-color);
            font-weight: 500;
            font-size: 16px;
        }

        .nav-links a:hover {
            color: var(--accent-dark-blue);
        }

        .theme-toggle {
            cursor: pointer;
            font-size: 20px;
            color: var(--text-color);
        }

        /* ORANGE/PINK GRADIENT CTA BUTTON */
        .cta-button {
            display: inline-block;
            background: linear-gradient(90deg, #ff7e5f 0%, #feb47b 100%);
            color: #ffffff !important;
            font-weight: 700;
            font-size: 16px;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            box-shadow: 0 4px 10px rgba(255, 126, 95, 0.3);
        }

        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(255, 126, 95, 0.4);
        }

        /* Main Hero Section */
        section { padding: 80px 5%; }
        
        .hero-section {
            display: flex;
            padding-top: 20px;
            padding-left: 5%;
            padding-right: 5%;
            gap: 60px;
            align-items: flex-start;
        }

        .left-content { flex: 1; max-width: 600px; position: relative; z-index: 10; }
        h1 { font-size: 56px; font-weight: 800; color: var(--h1-color); line-height: 1.1; margin-bottom: 20px; letter-spacing: -1px; }
        .subtitle { font-size: 18px; color: #555555; line-height: 1.6; margin-bottom: 40px; }
        body.night-mode .subtitle { color: #aaaaaa; }

        .features { display: flex; flex-direction: column; gap: 24px; margin-bottom: 40px; }
        .feature-item { display: flex; gap: 16px; align-items: flex-start; }
        .feature-icon { font-size: 20px; color: var(--accent-dark-blue); margin-top: 4px; }
        .feature-item h3 { font-size: 16px; font-weight: 700; margin-bottom: 4px; color: var(--h1-color); }
        .feature-item p { font-size: 15px; color: #666666; line-height: 1.5; }
        body.night-mode .feature-item p { color: #aaaaaa; }

        .right-content { flex: 1; position: relative; min-height: 750px; display: flex; justify-content: flex-end; }
        .blue-bg { position: absolute; top: 0; right: -10%; width: 90%; height: 100%; background-color: var(--accent-dark-blue); border-top-left-radius: 20px; z-index: 0; }

        .resume-mockup { position: relative; z-index: 1; background-color: #ffffff; width: 80%; max-width: 500px; height: 680px; border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); padding: 40px; margin-top: 20px; margin-right: 60px; border: 1px solid var(--light-border); }
        body.night-mode .resume-mockup { background-color: #1a1a1a; border-color: #333; box-shadow: 0 20px 40px rgba(255,255,255,0.05); }
        .resume-mockup h2 { color: var(--accent-dark-blue); margin-bottom: 8px; }
        .resume-mockup .contact-info { font-size: 10px; color: #888; margin-bottom: 20px; border-bottom: 1px solid var(--dark-border); padding-bottom: 10px; }
        .resume-mockup .summary { font-size: 10px; color: #555; margin-bottom: 20px; line-height: 1.5; }
        body.night-mode .resume-mockup .summary { color: #aaaaaa; }
        .resume-mockup h4 { font-size: 12px; color: #333; margin-bottom: 10px; }
        body.night-mode .resume-mockup h4 { color: #eaeaea; }
        .resume-mockup .job-title { font-size: 11px; font-weight: bold; margin-bottom: 5px; }
        body.night-mode .resume-mockup .job-title { color: #fff; }
        .resume-mockup ul { padding-left: 15px; font-size: 10px; color: #666; margin-bottom: 15px; }
        body.night-mode .resume-mockup ul { color: #aaaaaa; }
        .resume-mockup ul li { margin-bottom: 4px; }

        .floating-card { position: absolute; background: #ffffff; border-radius: 10px; box-shadow: 0 10px 30px var(--light-shadow); padding: 20px; z-index: 2; border: 1px solid var(--light-border); transition: transform 0.3s ease; }
        body.night-mode .floating-card { background: #1a1a1a; border-color: #333; }
        .floating-card:hover { transform: translateY(-5px); }
        .card-1 { top: 40px; right: -20px; width: 280px; }
        .card-2 { top: 240px; right: -20px; width: 280px; }
        .card-header { display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: var(--accent-dark-blue); margin-bottom: 15px; }
        .card-1-content { display: flex; justify-content: space-between; align-items: center; }
        .progress-bars { flex: 1; }
        .bar { height: 4px; background: #eee; margin-bottom: 8px; border-radius: 2px; width: 80%; }
        body.night-mode .bar { background: #333; }
        .bar.filled { background: var(--accent-yellow); width: 60%; }
        .score-circle { width: 60px; height: 60px; border-radius: 50%; border: 4px solid var(--accent-dark-blue); display: flex; flex-direction: column; align-items: center; justify-content: center; font-weight: bold; color: var(--accent-dark-blue); }
        .score-circle span { font-size: 8px; font-weight: normal; }
        .ai-textbox { border: 1px solid var(--dark-border); border-radius: 6px; padding: 10px; font-size: 10px; color: #555; position: relative; }
        body.night-mode .ai-textbox { color: #aaaaaa; }
        .ai-textbox::after { content: "Save bullet"; position: absolute; bottom: -10px; right: 10px; background: var(--accent-dark-blue); color: white; font-size: 8px; padding: 4px 8px; border-radius: 10px; }

        .cl-stack-container { position: absolute; bottom: 40px; right: -30px; width: 260px; height: 320px; z-index: 4; transition: transform 0.3s ease; }
        .cl-stack-container:hover { transform: translateY(-5px); }
        .cl-card { position: absolute; width: 240px; height: 300px; background: #ffffff; border-radius: 6px; box-shadow: 0 15px 35px var(--dark-shadow); border: 1px solid #d1d5db; }
        body.night-mode .cl-card { background: #1a1a1a; border-color: #333; }
        .cl-card-bg1 { transform: rotate(-10deg) translate(-25px, 15px); z-index: 1; background: #f8fafc; }
        body.night-mode .cl-card-bg1 { background: #121212; }
        .cl-card-bg2 { transform: rotate(-5deg) translate(-10px, 5px); z-index: 2; background: #f1f5f9; }
        body.night-mode .cl-card-bg2 { background: #1a1a1a; }
        .cl-card-front { z-index: 3; transform: rotate(0deg); display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 24px; text-align: center; outline: 2px solid #94a3b8; outline-offset: -10px; }
        .cl-card-front::before, .cl-card-front::after { content: ''; position: absolute; width: 12px; height: 12px; border: 2px solid #94a3b8; }
        .cl-card-front::before { top: 6px; left: 6px; border-right: none; border-bottom: none; }
        .cl-card-front::after { bottom: 6px; right: 6px; border-left: none; border-top: none; }
        .cl-title { color: #1e293b; font-size: 22px; font-weight: 800; line-height: 1.1; margin-bottom: 12px; letter-spacing: -0.5px; margin-top: 15px; }
        body.night-mode .cl-title { color: #fff; }
        .cl-subtitle { color: #475569; font-size: 13px; line-height: 1.4; font-weight: 500; }
        body.night-mode .cl-subtitle { color: #aaa; }

        /* Feature Grid */
        .grid-section { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 40px; }
        .grid-header { max-width: 600px; margin-bottom: 40px; }
        .grid-header p { color: #555; line-height: 1.6; }
        body.night-mode .grid-header p { color: #aaa; }
        .tool-card { background-color: var(--feature-card-bg); border-radius: 12px; padding: 24px; border: 1px solid var(--light-border); box-shadow: 0 10px 30px var(--light-shadow); position: relative; }
        body.night-mode .tool-card { border-color: #333; box-shadow: 0 10px 30px rgba(255,255,255,0.05); }
        .tool-card h3 { font-size: 18px; font-weight: 700; color: var(--h1-color); margin-bottom: 12px; }
        .tool-card p { font-size: 15px; color: #666666; line-height: 1.5; margin-bottom: 24px; }
        body.night-mode .tool-card p { color: #aaaaaa; }
        .tool-card .tool-icon { font-size: 32px; color: var(--accent-dark-blue); margin-bottom: 16px; background: var(--light-border); padding: 12px; border-radius: 50%; display: inline-block; }
        body.night-mode .tool-card .tool-icon { background: #333; }
        .tool-link { text-decoration: none; color: var(--accent-dark-blue); font-weight: 600; display: inline-flex; align-items: center; gap: 8px; margin-top: 10px;}
        body.night-mode .tool-link { color: #90caf9; }
        .score-badge { font-size: 48px; font-weight: 800; color: var(--accent-dark-blue); margin-bottom: 8px; }
        body.night-mode .score-badge { color: #90caf9; }
        .tool-card.span-col { grid-column: span 1; grid-row: span 2; display: flex; flex-direction: column; justify-content: space-between; }

        /* --- HOW IT WORKS SECTION --- */
        .numbered-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }
        .step-card { background-color: var(--feature-card-bg); border-radius: 12px; padding: 32px; border: 1px solid var(--light-border); box-shadow: 0 10px 30px var(--light-shadow); }
        body.night-mode .step-card { border-color: #333; }
        .step-card .step-number { font-size: 24px; font-weight: 800; color: #fff; background-color: var(--accent-dark-blue); width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; }
        .step-card h3 { font-size: 18px; font-weight: 700; color: var(--h1-color); margin-bottom: 12px; }
        .step-card p { font-size: 15px; color: #666666; line-height: 1.5; }
        body.night-mode .step-card p { color: #aaaaaa; }

        /* --- FAQ SECTION --- */
        .faq-section {
            max-width: 800px;
            margin: 0 auto;
        }
        .faq-item {
            border-bottom: 1px solid var(--light-border);
        }
        .faq-question {
            width: 100%;
            background: none;
            border: none;
            text-align: left;
            padding: 24px 0;
            font-size: 18px;
            font-weight: 600;
            color: var(--h1-color);
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: color 0.3s ease;
        }
        .faq-question:hover { color: var(--accent-orange); }
        .faq-question i {
            color: var(--accent-orange);
            font-size: 20px;
            transition: transform 0.3s ease;
        }
        .faq-answer {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease;
        }
        .faq-answer p {
            padding-bottom: 24px;
            color: #555;
            line-height: 1.6;
            font-size: 16px;
        }
        body.night-mode .faq-answer p { color: #aaa; }
        
        .faq-item.active .faq-answer {
            max-height: 300px;
        }
        .faq-item.active .faq-question i {
            transform: rotate(45deg);
        }

        /* Reviews */
        .reviews-section { background-color: #f8fafc; border-top: 1px solid var(--light-border); border-bottom: 1px solid var(--light-border); }
        body.night-mode .reviews-section { background-color: #1a1a1a; border-color: #333; }
        .review-header { text-align: center; margin-bottom: 60px; }
        .review-header p { font-size: 14px; font-weight: 700; color: var(--accent-dark-blue); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
        .testimonial-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
        .testimonial-card { background-color: var(--feature-card-bg); border-radius: 12px; padding: 32px; border: 1px solid var(--light-border); box-shadow: 0 10px 30px var(--light-shadow); display: flex; flex-direction: column; justify-content: space-between; }
        body.night-mode .testimonial-card { border-color: #333; }
        .stars { color: var(--accent-yellow); margin-bottom: 16px; }
        .testimonial-card p { font-size: 15px; color: #555; line-height: 1.6; margin-bottom: 24px; }
        body.night-mode .testimonial-card p { color: #aaa; }
        .user-info { display: flex; gap: 12px; align-items: center; }
        .user-avatar { width: 48px; height: 48px; border-radius: 50%; color: #fff; font-weight: 700; font-size: 18px; display: flex; align-items: center; justify-content: center; }
        .user-details h4 { font-size: 14px; color: var(--h1-color); font-weight: 700; }
        .user-details p { font-size: 12px; color: #666; margin: 0; }
        body.night-mode .user-details p { color: #aaa; }

        /* Footer */
        footer { padding: 40px 5%; text-align: center; border-top: 1px solid var(--light-border); font-size: 14px; color: #888; }
        body.night-mode footer { border-color: #333; color: #aaa; }

        @media (max-width: 1024px) {
            .navbar { padding: 16px 5%; }
            .nav-links { display: none; }
            .hero-section, .numbered-grid, .testimonial-grid, .grid-section { flex-direction: column; grid-template-columns: 1fr; gap: 30px; }
            .right-content { width: 100%; justify-content: center; margin-top: 40px; }
            .blue-bg { width: 100vw; right: -5%; border-radius: 0; }
            .resume-mockup { margin-right: 0; }
            .card-1, .card-2, .cl-stack-container { right: 5%; }
            .cta-button { font-size: 14px; padding: 10px 20px; }
            h1 { font-size: 36px; }
            .subtitle { font-size: 16px; }
            .tool-card.span-col { grid-row: auto; }
            .faq-question { font-size: 16px; }
        }
    </style>
</head>
<body>

    <nav class="navbar">
        <div class="logo-container">
            <svg width="240" height="80" viewBox="0 0 350 110" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:var(--logo-grad-stop-1);stop-opacity:1" />
                        <stop offset="100%" style="stop-color:var(--logo-grad-stop-2);stop-opacity:1" />
                    </linearGradient>
                    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
                        <feGaussianBlur in="SourceAlpha" stdDeviation="2" />
                        <feOffset dx="2" dy="2" result="offsetblur" />
                        <feComponentTransfer><feFuncA type="linear" slope="0.3" /></feComponentTransfer>
                        <feMerge><feMergeNode /><feMergeNode in="SourceGraphic" /></feMerge>
                    </filter>
                </defs>
                <path d="M40 20 L110 20 L40 85 L110 85" fill="none" stroke="url(#logoGrad)" stroke-width="15" stroke-linejoin="bevel" filter="url(#shadow)"/>
                <path d="M125 85 L125 20 L185 85 L185 20" fill="none" stroke="url(#logoGrad)" stroke-width="15" stroke-linejoin="bevel" filter="url(#shadow)"/>
                <g filter="url(#shadow)">
                    <path d="M200 85 L235 20" stroke="url(#logoGrad)" stroke-width="15" fill="none"/>
                    <path d="M235 20 L270 85" stroke="url(#logoGrad)" stroke-width="15" fill="none"/>
                    <path d="M215 65 Q250 55 285 35" stroke="url(#logoGrad)" stroke-width="8" fill="none" stroke-linecap="round"/>
                    <path d="M275 35 L285 35 L285 45" stroke="url(#logoGrad)" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                </g>
                <text x="40" y="105" font-family="'Inter', sans-serif" font-weight="700" font-size="18" fill="var(--accent-dark-blue)" letter-spacing="1">INNOVATE YOUR CAREER</text>
            </svg>
        </div>
        <div class="nav-links">
            <a href="#features">Features</a>
            <a href="#howitworks">How it works</a>
            <a href="#faq">FAQ</a>
            <a href="#reviews">Reviews</a>
            <i class="fas fa-moon theme-toggle" id="theme-toggle"></i>
            <a href="https://airesumebuilder-g3x89b2t4vqnsdxvisf26a.streamlit.app/" class="cta-button" target="_blank">Start building free</a>
        </div>
    </nav>

    <main class="hero-section">
        <div class="left-content">
            <h1>The Best Free AI Resume Builder</h1>
            <p class="subtitle">Our Resume Builder creates ATS-friendly, professional resumes in minutes. Extract data instantly, tailor for any job, and build your career directly through our powerful workspace.</p>
            <div class="cta-section">
                <a href="https://airesumebuilder-g3x89b2t4vqnsdxvisf26a.streamlit.app/" class="cta-button" target="_blank" style="padding: 16px 32px; font-size: 18px; border-radius: 50px;">Start building free</a>
            </div>
        </div>

        <div class="right-content">
            <div class="blue-bg"></div>
            <div class="resume-mockup">
                <h2>Tina Miller</h2>
                <div class="contact-info">Florida • 123-545-7890 • tinamiller@email.com • linkedin.com/in/tinamiller</div>
                <div class="summary">7+ years of social marketing experience, driving customer growth, B2B, and content marketing campaigns. Increased brand awareness by 40%, customer acquisition by 25%, customer lifetime value by 15% in 6 months.</div>
                <h4>WORK EXPERIENCE</h4>
                <div class="job-title">Senior Marketing Manager • WeWork</div>
                <ul>
                    <li>Increased lead generation by 30% in 3 months through the development of cross-channel campaigns targeting key customer segments.</li>
                    <li>Increased company's online presence by 25%, driving a 40% ROI and generating $2M in revenue through successful digital campaigns.</li>
                </ul>
                <div class="job-title" style="margin-top: 15px;">Marketing Manager • NVIDIA</div>
                <ul><li>Managed a comprehensive cross functional marketing campaign overseeing a team of 10 professionals...</li></ul>
            </div>

            <div class="floating-card card-1">
                <div class="card-header"><i class="fas fa-file-contract"></i> Resume Analysis and Matching</div>
                <div class="card-1-content">
                    <div class="progress-bars">
                        <div style="font-size: 9px; margin-bottom: 2px;">Resume Structure</div>
                        <div class="bar filled"></div>
                        <div style="font-size: 9px; margin-bottom: 2px;">Measurable Results</div>
                        <div class="bar filled" style="width: 40%; background: #ef5350;"></div>
                    </div>
                    <div class="score-circle">80%<span>Good Match</span></div>
                </div>
            </div>

            <div class="floating-card card-2">
                <div class="card-header"><i class="fas fa-magic"></i> Enhance with AI</div>
                <div class="ai-textbox">Increased website traffic by XX% through a targeted content marketing campaign over Y months, enhancing brand visibility and engagement.</div>
            </div>
            
            <div class="cl-stack-container">
                <div class="cl-card cl-card-bg1"></div>
                <div class="cl-card cl-card-bg2"></div>
                <div class="cl-card cl-card-front">
                    <svg width="120" height="40" viewBox="0 0 350 110" xmlns="http://www.w3.org/2000/svg">
                        <path d="M40 20 L110 20 L40 85 L110 85" fill="none" stroke="#0b3d6e" stroke-width="20" stroke-linejoin="bevel"/>
                        <path d="M125 85 L125 20 L185 85 L185 20" fill="none" stroke="#0b3d6e" stroke-width="20" stroke-linejoin="bevel"/>
                        <path d="M200 85 L235 20 L270 85" stroke="#0b3d6e" stroke-width="20" fill="none"/>
                        <path d="M215 65 Q250 55 285 35" stroke="#0b3d6e" stroke-width="12" fill="none" stroke-linecap="round"/>
                        <path d="M275 35 L285 35 L285 45" stroke="#0b3d6e" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <div class="cl-title">AI Cover Letters</div>
                    <div class="cl-subtitle">Generate tailored cover letters instantly</div>
                </div>
            </div>
        </div>
    </main>

    <section id="features">
        <div class="grid-header">
            <h1>Built for the modern job seeker</h1>
            <p>Five powerful tools in one workspace. No account needed — just your Gemini API key.</p>
        </div>
        <div class="grid-section">
            <div class="tool-card span-col">
                <i class="fas fa-bullseye tool-icon"></i>
                <h3>ATS Optimisation Engine</h3>
                <p>Semantic NLP analysis compares your resume against any job description and returns a match score, matched keywords, missing gaps, and one-click tailoring.</p>
                <div class="score-badge">94%</div>
                <p style="font-size: 11px;">Average ATS score after tailoring</p>
                <a href="https://airesumebuilder-g3x89b2t4vqnsdxvisf26a.streamlit.app/" class="tool-link" target="_blank">Learn more →</a>
            </div>
            
            <div class="tool-card">
                <i class="fab fa-linkedin tool-icon" style="color:#0077b5;"></i>
                <h3>Auto-Parse LinkedIn</h3>
                <p>Paste your LinkedIn profile or old resume. Gemini extracts and structures everything automatically.</p>
                <a href="https://airesumebuilder-g3x89b2t4vqnsdxvisf26a.streamlit.app/" class="tool-link" target="_blank">Try it →</a>
            </div>

            <div class="tool-card">
                <i class="fas fa-file-signature tool-icon"></i>
                <h3>AI Cover Letters</h3>
                <p>One-click personalised cover letters tailored to each company and role. Professional, concise, and compelling.</p>
                <a href="https://airesumebuilder-g3x89b2t4vqnsdxvisf26a.streamlit.app/" class="tool-link" target="_blank">See example →</a>
            </div>

            <div class="tool-card">
                <i class="fas fa-file-download tool-icon"></i>
                <h3>Clean PDF Export</h3>
                <p>Download your resume in clean PDF. Your contact details are automatically rendered as clickable hyperlinks.</p>
                <a href="https://airesumebuilder-g3x89b2t4vqnsdxvisf26a.streamlit.app/" class="tool-link" target="_blank">Export now →</a>
            </div>

            <div class="tool-card">
                <i class="fas fa-door-open tool-icon"></i>
                <h3>LinkedIn Job Portal</h3>
                <p>Set your target job title and we surface live LinkedIn listings instantly. Direct apply in one tap.</p>
                <a href="https://airesumebuilder-g3x89b2t4vqnsdxvisf26a.streamlit.app/" class="tool-link" target="_blank">Open portal →</a>
            </div>
        </div>
    </section>
    
    <section id="howitworks">
        <div class="grid-header">
            <h1>How ZNA Works</h1>
            <p>From data paste to direct apply, our platform guides you through a seamless career optimization journey.</p>
        </div>
        <div class="numbered-grid">
            <div class="step-card">
                <div class="step-number">1</div>
                <h3>Paste your data</h3>
                <p>Copy your LinkedIn profile, paste your old resume, or fill in the structured form. Our AI extracts every detail automatically.</p>
            </div>
            <div class="step-card">
                <div class="step-number">2</div>
                <h3>Generate with AI</h3>
                <p>Gemini rewrites your experience with strong action verbs, quantified achievements, and Intricate ATS-optimised keywords for your target role.</p>
            </div>
            <div class="step-card">
                <div class="step-number">3</div>
                <h3>Score, tailor & apply</h3>
                <p>Run the ATS scanner against any job description, tailor with one click, generate a cover letter, and apply directly via LinkedIn.</p>
            </div>
        </div>
    </section>

    <section id="faq">
        <div class="grid-header" style="text-align: center; margin: 0 auto 60px auto;">
            <h1>Frequently Asked Questions</h1>
            <p>Everything you need to know about building the perfect resume.</p>
        </div>
        
        <div class="faq-section">
            <div class="faq-item">
                <button class="faq-question">Do I need to download an app to use the resume builder on mobile? <i class="fas fa-plus"></i></button>
                <div class="faq-answer"><p>No, you do not need to download an app. Our AI resume builder is fully responsive and works perfectly directly in your mobile or desktop web browser.</p></div>
            </div>
            
            <div class="faq-item">
                <button class="faq-question">What makes our tool the best resume builder? <i class="fas fa-plus"></i></button>
                <div class="faq-answer"><p>We use Google's advanced Gemini 2.5 Flash AI to not just format your text, but semantically rewrite your experience with strong action verbs and quantified achievements to pass ATS filters.</p></div>
            </div>

            <div class="faq-item">
                <button class="faq-question">What is the main purpose of a resume builder? <i class="fas fa-plus"></i></button>
                <div class="faq-answer"><p>To save you hours of formatting and writing. Our tool organizes your raw data into a professional, readable format that catches recruiters' eyes immediately.</p></div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Does the mobile resume builder have the same features as desktop? <i class="fas fa-plus"></i></button>
                <div class="faq-answer"><p>Yes! You get the exact same powerful AI generation, Cover Letter Engine, and PDF export features whether you are on your phone, tablet, or desktop.</p></div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Can resume builders help with ATS optimization? <i class="fas fa-plus"></i></button>
                <div class="faq-answer"><p>Absolutely. Our tool features a dedicated ATS Match Engine. Simply paste a job description, and the AI will analyze your resume against it, providing a match score and missing keywords.</p></div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Is my information secure and compliant with data privacy laws? <i class="fas fa-plus"></i></button>
                <div class="faq-answer"><p>Yes, your data is processed securely through your personal Google Gemini API key. We do not store your resume data or personal information permanently on our servers.</p></div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Should I download my new resume as a PDF or text file? <i class="fas fa-plus"></i></button>
                <div class="faq-answer"><p>Always download as a PDF for job applications to preserve your formatting. Our tool exports perfectly formatted PDFs where your Email, Phone, and LinkedIn are fully clickable links.</p></div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Is this a free resume builder? <i class="fas fa-plus"></i></button>
                <div class="faq-answer"><p>Yes! ZNA AI Resume Architect is completely free to use. Just plug in your Gemini API key and build, edit, and export without limits or watermarks.</p></div>
            </div>
        </div>
    </section>

    <section id="reviews" class="reviews-section">
        <div class="review-header">
            <p>Real results, real people</p>
            <h1>Loved by Job Seekers</h1>
        </div>
        <div class="testimonial-grid">
            <div class="testimonial-card">
                <div>
                    <div class="stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                    <p>"Got my ATS score from 58% to 92% in minutes. The tailoring feature is incredible — it knows exactly which keywords are missing."</p>
                </div>
                <div class="user-info">
                    <div class="user-avatar" style="background-color: var(--avatar-1);">AR</div>
                    <div class="user-details"><h4>Arjun Rao</h4><p>Software Engineer → Google</p></div>
                </div>
            </div>
            <div class="testimonial-card">
                <div>
                    <div class="stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                    <p>"The cover letter generator saved me hours. Each letter feels genuinely personalised — not templated. Landed 3 interviews in one week."</p>
                </div>
                <div class="user-info">
                    <div class="user-avatar" style="background-color: var(--avatar-2);">SP</div>
                    <div class="user-details"><h4>Sanya Patel</h4><p>Marketing Manager → Meta</p></div>
                </div>
            </div>
            <div class="testimonial-card">
                <div>
                    <div class="stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                    <p>"I pasted my LinkedIn and had a polished PDF resume in under 2 minutes. The dark mode is 🔥 and the LinkedIn job portal is a game changer."</p>
                </div>
                <div class="user-info">
                    <div class="user-avatar" style="background-color: var(--avatar-3);">ZK</div>
                    <div class="user-details"><h4>Zaid Karim</h4><p>CS Student → SWE Intern, Amazon</p></div>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <p>&copy; 2026 ZNA Innovate Your Career. All rights reserved.</p>
    </footer>

    <script>
        // Theme Toggling Logic
        const toggleButton = document.getElementById('theme-toggle');
        const body = document.body;
        const logoGradStop1 = document.querySelector('#logoGrad stop[offset="0%"]');
        const logoGradStop2 = document.querySelector('#logoGrad stop[offset="100%"]');

        function updateGradient(theme) {
            if (theme === 'night') {
                logoGradStop1.style.stopColor = '#90caf9';
                logoGradStop2.style.stopColor = '#3b82f6';
            } else {
                logoGradStop1.style.stopColor = '#4a90e2';
                logoGradStop2.style.stopColor = '#0b3d6e';
            }
        }

        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'night-mode') {
            body.classList.add('night-mode');
            toggleButton.classList.remove('fa-moon');
            toggleButton.classList.add('fa-sun');
            updateGradient('night');
        } else {
            updateGradient('day');
        }

        toggleButton.addEventListener('click', () => {
            body.classList.toggle('night-mode');
            if (body.classList.contains('night-mode')) {
                toggleButton.classList.remove('fa-moon');
                toggleButton.classList.add('fa-sun');
                localStorage.setItem('theme', 'night-mode');
                updateGradient('night');
            } else {
                toggleButton.classList.remove('fa-sun');
                toggleButton.classList.add('fa-moon');
                localStorage.setItem('theme', 'light-mode');
                updateGradient('day');
            }
        });

        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // FAQ Accordion Logic
        const faqItems = document.querySelectorAll('.faq-item');
        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question');
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');
                // Close all others
                faqItems.forEach(otherItem => otherItem.classList.remove('active'));
                // Toggle current
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        });
    </script>
</body>
</html>
"""

# 4. Render HTML securely. Increased height to 5000 to fit the new FAQ section!
components.html(html_content, height=5000, scrolling=True)
