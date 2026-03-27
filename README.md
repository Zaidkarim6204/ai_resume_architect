# 🎨 ZNA - AI Resume Builder (Frontend Portal)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Wrapper-FF4B4B)
![UI/UX](https://img.shields.io/badge/UI%2FUX-Custom_Design-success)

This repository contains the custom-built, high-conversion landing page for the **ZNA AI Resume Architect** platform. It serves as the visual entry point for users before seamlessly routing them to the Python/LLM backend engine.

Developed as part of a Final Year Computer Science Engineering Project.

---

## ✨ Design & Architectural Features

* **🖌️ Custom SVG Branding:** Features a meticulously coded, mathematically plotted SVG logo ("ZNA") with dynamic linear gradients and drop-shadow rendering.
* **📱 Fully Responsive UI:** Built with fluid CSS flexbox layouts and media queries to ensure perfect rendering across desktop, tablet, and mobile devices.
* **🪟 Advanced CSS Aesthetics:** Utilizes modern UI/UX principles, including floating overlapping cards, 3D stack effects, custom hover physics, and glassmorphism elements.
* **🔗 Seamless Backend Routing:** The primary Call-to-Action (CTA) button routes user traffic directly to the live Streamlit AI backend processing server.
* **🚀 Python Wrapper Integration:** Cleverly bypasses Streamlit's default UI constraints using a custom `components.v1.html` injection, allowing raw, edge-to-edge HTML deployment on Streamlit Community Cloud.

---

## 🛠️ Tech Stack

* **Markup:** HTML5
* **Styling:** CSS3 (Custom animations, gradients, and flexbox)
* **Typography & Icons:** Google Fonts ('Inter') & FontAwesome
* **Deployment Engine:** Streamlit Wrapper (`landing_page.py`)

---

## 🚀 How to Run Locally

Because this HTML page is designed to be hosted on Streamlit Cloud, it uses a Python wrapper script.

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR-USERNAME/zna-frontend.git](https://github.com/YOUR-USERNAME/zna-frontend.git)
cd zna-frontend
2. Install Streamlit

Bash
pip install streamlit
3. Launch the Portal

Bash
streamlit run landing_page.py
Note: This will render the edge-to-edge HTML layout inside a local browser tab.
