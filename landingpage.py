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

# 3. Your exact HTML code
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZNA - AI Resume Builder</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        /* Base Styles & Reset */
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
        body { background-color: #ffffff; color: #333333; overflow-x: hidden; }

        /* Navigation - Logo Only */
        .navbar { padding: 24px 5%; display: flex; justify-content: flex-start; align-items: center; }
        .logo-container { height: 75px; display: flex; align-items: center; }

        /* Hero Layout */
        .hero-section { display: flex; padding: 20px 5% 80px 5%; gap: 60px; align-items: flex-start; }

        /* Left Column (Content) */
        .left-content { flex: 1; max-width: 600px; position: relative; z-index: 10; }
        h1 { font-size: 56px; font-weight: 800; color: #222222; line-height: 1.1; margin-bottom: 20px; letter-spacing: -1px; }
        .subtitle { font-size: 18px; color: #555555; line-height: 1.6; margin-bottom: 40px; }

        .features { display: flex; flex-direction: column; gap: 24px; margin-bottom: 40px; }
        .feature-item { display: flex; gap: 16px; align-items: flex-start; }
        .feature-icon { font-size: 20px; color: #0b3d6e; margin-top: 4px; }
        .feature-item h3 { font-size: 16px; font-weight: 700; margin-bottom: 4px; color: #111111; }
        .feature-item p { font-size: 15px; color: #666666; line-height: 1.5; }

        /* Call to Action Button */
        .cta-button {
            display: inline-block; background-color: #ffb800; color: #000000; font-weight: 700;
            font-size: 18px; padding: 16px 32px; border-radius: 50px; text-decoration: none;
            transition: transform 0.2s ease, box-shadow 0.2s ease; box-shadow: 0 4px 6px rgba(255, 184, 0, 0.2);
        }
        .cta-button:hover { transform: translateY(-2px); box-shadow: 0 6px 12px rgba(255, 184, 0, 0.3); }

        /* Right Column (Visuals) */
        .right-content { flex: 1; position: relative; min-height: 750px; display: flex; justify-content: flex-end; }

        /* Dark Blue Background Shape */
        .blue-bg {
            position: absolute; top: 0; right: -10%; width: 90%; height: 100%;
            background-color: #0b3d6e; border-top-left-radius: 20px; z-index: 0;
        }

        /* Main Resume Mockup */
        .resume-mockup {
            position: relative; z-index: 1; background-color: #ffffff; width: 80%; max-width: 500px;
            height: 680px; border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            padding: 40px; margin-top: 20px; margin-right: 60px; border: 1px solid #eaeaea;
        }
        .resume-mockup h2 { color: #0b3d6e; margin-bottom: 8px; }
        .resume-mockup .contact-info { font-size: 10px; color: #888; margin-bottom: 20px; border-bottom: 1px solid #eee; padding-bottom: 10px; }
        .resume-mockup .summary { font-size: 10px; color: #555; margin-bottom: 20px; line-height: 1.5; }
        .resume-mockup h4 { font-size: 12px; color: #333; margin-bottom: 10px; }
        .resume-mockup .job-title { font-size: 11px; font-weight: bold; margin-bottom: 5px; }
        .resume-mockup ul { padding-left: 15px; font-size: 10px; color: #666; margin-bottom: 15px; }
        .resume-mockup ul li { margin-bottom: 4px; }

        /* Floating Feature Cards */
        .floating-card {
            position: absolute; background: #ffffff; border-radius: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            padding: 20px; z-index: 2; border: 1px solid #f0f0f0; transition: transform 0.3s ease;
        }
        .floating-card:hover { transform: translateY(-5px); }
        .card-1 { top: 40px; right: -20px; width: 280px; }
        .card-2 { top: 240px; right: -20px; width: 280px; }

        .card-header { display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #0b3d6e; margin-bottom: 15px; }
        .card-1-content { display: flex; justify-content: space-between; align-items: center; }
        .progress-bars { flex: 1; }
        .bar { height: 4px; background: #eee; margin-bottom: 8px; border-radius: 2px; width: 80%; }
        .bar.filled { background: #ffb800; width: 60%; }

        .score-circle {
            width: 60px; height: 60px; border-radius: 50%; border: 4px solid #0b3d6e; display: flex;
            flex-direction: column; align-items: center; justify-content: center; font-weight: bold; color: #0b3d6e;
        }
        .score-circle span { font-size: 8px; font-weight: normal; }

        .ai-textbox { border: 1px solid #e0e0e0; border-radius: 6px; padding: 10px; font-size: 10px; color: #555; position: relative; }
        .ai-textbox::after {
            content: "Save bullet"; position: absolute; bottom: -10px; right: 10px; background: #0b3d6e;
            color: white; font-size: 8px; padding: 4px 8px; border-radius: 10px;
        }

        /* --- Cover Letter Stack Component --- */
        .cl-stack-container { position: absolute; bottom: 40px; right: -30px; width: 260px; height: 320px; z-index: 4; transition: transform 0.3s ease; }
        .cl-stack-container:hover { transform: translateY(-5px); }
        .cl-card { position: absolute; width: 240px; height: 300px; background: #ffffff; border-radius: 6px; box-shadow: 0 15px 35px rgba(0,0,0,0.2); border: 1px solid #d1d5db; }
        .cl-card-bg1 { transform: rotate(-10deg) translate(-25px, 15px); z-index: 1; background: #f8fafc; }
        .cl-card-bg2 { transform: rotate(-5deg) translate(-10px, 5px); z-index: 2; background: #f1f5f9; }
        .cl-card-front {
            z-index: 3; transform: rotate(0deg); display: flex; flex-direction: column; align-items: center;
            justify-content: center; padding: 24px; text-align: center; outline: 2px solid #94a3b8; outline-offset: -10px;
        }
        .cl-card-front::before, .cl-card-front::after { content: ''; position: absolute; width: 12px; height: 12px; border: 2px solid #94a3b8; }
        .cl-card-front::before { top: 6px; left: 6px; border-right: none; border-bottom: none; }
        .cl-card-front::after { bottom: 6px; right: 6px; border-left: none; border-top: none; }
        .cl-title { color: #1e293b; font-size: 22px; font-weight: 800; line-height: 1.1; margin-bottom: 12px; letter-spacing: -0.5px; margin-top: 15px; }
        .cl-subtitle { color: #475569; font-size: 13px; line-height: 1.4; font-weight: 500; }

        /* Responsive Design */
        @media (max-width: 1024px) {
            .hero-section { flex-direction: column; }
            .right-content { width: 100%; justify-content: center; margin-top: 40px; }
            .blue-bg { width: 100vw; right: -5%; border-radius: 0; }
            .resume-mockup { margin-right: 0; }
            .card-1, .card-2, .cl-stack-container { right: 5%; }
        }
    </style>
</head>
<body>

    <nav class="navbar">
        <div class="logo-container">
            <svg width="240" height="80" viewBox="0 0 350 110" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#4a90e2;stop-opacity:1" />
                        <stop offset="100%" style="stop-color:#0b3d6e;stop-opacity:1" />
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
                <text x="40" y="105" font-family="'Inter', sans-serif" font-weight="700" font-size="18" fill="#0b3d6e" letter-spacing="1">INNOVATE YOUR CAREER</text>
            </svg>
        </div>
    </nav>

    <main class="hero-section">
        <div class="left-content">
            <h1>The Best Free AI Resume Builder</h1>
            <p class="subtitle">Our Resume Builder creates ATS-friendly resumes in minutes. Build a new resume or improve an existing one with unlimited downloads, instant job matching, and smart AI suggestions.</p>
            <div class="features">
                <div class="feature-item"><i class="fas fa-chart-line feature-icon"></i><div class="feature-text"><h3>Optimize for ATS</h3><p>Format your resume so it's easy for recruiters to find in searches.</p></div></div>
                <div class="feature-item"><i class="fas fa-bullseye feature-icon"></i><div class="feature-text"><h3>Job matching</h3><p>Instantly edit any resume to match a job description using AI.</p></div></div>
                <div class="feature-item"><i class="fas fa-infinity feature-icon"></i><div class="feature-text"><h3>Create without limits</h3><p>Build, update, edit, and export as many resumes as you need — free.</p></div></div>
                <div class="feature-item"><i class="fab fa-linkedin feature-icon" style="color: #0077b5;"></i><div class="feature-text"><h3>Direct apply through LinkedIn</h3><p>Seamlessly submit your tailored resume directly to LinkedIn job postings.</p></div></div>
                <div class="feature-item"><i class="fas fa-file-signature feature-icon"></i><div class="feature-text"><h3>Automatic generation of cover letter</h3><p>Generate a matching cover letter instantly tailored to the job description.</p></div></div>
            </div>
            <a href="https://airesumebuilder-g3x89b2t4vqnsdxvisf26a.streamlit.app/" class="cta-button" target="_blank">Start building free</a>
        </div>
        <div class="right-content">
            <div class="blue-bg"></div>
            <div class="resume-mockup">
                <h2>Tina Miller</h2>
                <div class="contact-info">Florida • 123-545-7890 • tinamiller@email.com • linkedin.com/in/tinamiller</div>
                <div class="summary">7+ years of social marketing experience, driving customer growth, B2B, and content marketing campaigns. Increased brand awareness by 40%, customer acquisition by 25%, customer lifetime value by 15% in 6 months.</div>
                <h4>WORK EXPERIENCE</h4>
                <div class="job-title">Senior Marketing Manager • WeWork</div>
                <ul><li>Increased lead generation by 30% in 3 months through the development of cross-channel campaigns targeting key customer segments.</li><li>Increased company's online presence by 25%, driving a 40% ROI and generating $2M in revenue through successful digital campaigns.</li></ul>
                <div class="job-title" style="margin-top: 15px;">Marketing Manager • NVIDIA</div>
                <ul><li>Managed a comprehensive cross functional marketing campaign overseeing a team of 10 professionals...</li></ul>
            </div>
            <div class="floating-card card-1">
                <div class="card-header"><i class="fas fa-file-contract"></i> Resume Analysis and Matching</div>
                <div class="card-1-content">
                    <div class="progress-bars">
                        <div style="font-size: 9px; margin-bottom: 2px;">Resume Structure</div><div class="bar filled"></div>
                        <div style="font-size: 9px; margin-bottom: 2px;">Measurable Results</div><div class="bar filled" style="width: 40%; background: #ef5350;"></div>
                    </div>
                    <div class="score-circle">80%<span>Good Match</span></div>
                </div>
            </div>
            <div class="floating-card card-2">
                <div class="card-header"><i class="fas fa-magic"></i> Enhance with AI</div>
                <div class="ai-textbox">Increased website traffic by XX% through a targeted content marketing campaign over Y months, enhancing brand visibility and engagement.</div>
            </div>
            <div class="cl-stack-container">
                <div class="cl-card cl-card-bg1"></div><div class="cl-card cl-card-bg2"></div>
                <div class="cl-card cl-card-front">
                    <svg width="120" height="40" viewBox="0 0 350 110" xmlns="http://www.w3.org/2000/svg">
                        <path d="M40 20 L110 20 L40 85 L110 85" fill="none" stroke="#0b3d6e" stroke-width="20" stroke-linejoin="bevel"/>
                        <path d="M125 85 L125 20 L185 85 L185 20" fill="none" stroke="#0b3d6e" stroke-width="20" stroke-linejoin="bevel"/>
                        <path d="M200 85 L235 20 L270 85" stroke="#0b3d6e" stroke-width="20" fill="none"/>
                        <path d="M215 65 Q250 55 285 35" stroke="#0b3d6e" stroke-width="12" fill="none" stroke-linecap="round"/>
                        <path d="M275 35 L285 35 L285 45" stroke="#0b3d6e" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <div class="cl-title">AI-Powered Cover Letters</div>
                    <div class="cl-subtitle">Generate tailored cover letters instantly</div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
"""

# 4. Use components.html instead of markdown to render safely!
components.html(html_content, height=1000, scrolling=True)
