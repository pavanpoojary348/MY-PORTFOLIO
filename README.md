# 🌐 Pavan Poojary &mdash; Developer Portfolio

<div align="center">

[![Live Portfolio](https://img.shields.io/badge/Live_Portfolio-pavanpoojary.vercel.app-00f0ff?style=for-the-badge&logo=vercel&logoColor=black)](https://pavanpoojary.vercel.app)
[![GitHub](https://img.shields.io/badge/GitHub-pavanpoojary348-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pavanpoojary348)
[![LeetCode](https://img.shields.io/badge/LeetCode-pavanlpoojary-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/pavanlpoojary/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-pavanlpoojary-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pavanlpoojary/)

**A responsive, cyberpunk-inspired personal portfolio web application built with Python (Flask) and modern Vanilla JavaScript / CSS, featuring an interactive canvas particle background, `Ctrl+K` Command Palette, categorized project showcase, and deployed globally on Vercel Serverless Edge.**

[Explore Live Website 🚀](https://pavanpoojary.vercel.app)

</div>

---

## 👨‍💻 About Me

Hi! I'm **Pavan Poojary**, an **Information Science & Engineering (B.Tech)** student at **NMAM Institute of Technology (NMAMIT)** (Expected 2028).

I specialize in building full-stack web applications, machine learning tools, and algorithmic problem-solving in Python and C++. Passionate about clean code, high performance, and interactive user experiences.

---

## ⚡ Highlights & Key Features

- **Cyberpunk Dark Glassmorphism**: Custom neon theme with cyan (`#00f0ff`) and purple glow accents, styled scrollbars, and dynamic particle canvas background.
- **Interactive Command Palette (`Ctrl + K`)**: Quick fuzzy search across all site routes, external developer profiles (GitHub, LinkedIn, LeetCode), and 1-click email copy.
- **Categorized Project Showcase**: Instant client-side filtering across AI/ML & Multi-Agent systems, Web Applications, and Data/ETL pipelines with terminal-style headers and live links.
- **Coding & DSA Profiles**: Integrated GitHub repositories and live LeetCode problem-solving showcase (`@pavanlpoojary`) with core DSA focus badges.
- **Verified Credentials & Resume Preview**: Verified certificates from IBM, Coursera, and Credly, with an in-browser PDF reader modal and direct download.
- **Working Contact Form**: Integrated EmailJS with Flask-Mail backend fallback, live character counter (`0 / 500`), and real-time status feedback.
- **Sub-Second Global Performance**: Deployed serverless on Vercel's global edge network with static asset CDN caching for instantaneous page loads.

---

## 🛠️ Tech Stack

| Category | Technologies |
| :--- | :--- |
| **Backend** | Python 3, Flask, Werkzeug, Flask-Mail |
| **Frontend** | Semantic HTML5, Modern Vanilla CSS, JavaScript (ES6+), Canvas API |
| **Design & UI** | Cyberpunk Glassmorphism, Font Awesome 6, Google Fonts (Outfit, Fira Code) |
| **Deployment** | Vercel Serverless Edge (`@vercel/python`) |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```text
MY-PORTFOLIO/
├── api/
│   └── index.py            # Vercel serverless WSGI entrypoint
├── public/                 # Edge CDN static assets (favicon, images, PDF)
│   └── static/
├── static/                 # Styles, scripts, and media assets
│   ├── style.css
│   ├── script.js
│   ├── Pavan.jpg
│   └── Pavan_Poojary_Resume.pdf
├── templates/              # Jinja2 HTML templates
│   ├── index.html          # Home page
│   ├── about.html          # About Pavan
│   ├── projects.html       # Projects with category filter
│   ├── skills.html         # Skills & DSA Matrix
│   ├── certificates.html   # Certificates & In-Browser Resume Modal
│   ├── contact.html        # Contact form with live counter
│   └── 404.html            # Cyberpunk 404 error page
├── app.py                  # Main Flask application with WSGI routing middleware
├── requirements.txt        # Python dependencies
└── vercel.json             # Vercel serverless rewrite & routing rules
```

---

## 🚀 Local Development Setup

### 1. Clone the repository
```bash
git clone https://github.com/pavanpoojary348/MY-PORTFOLIO.git
cd MY-PORTFOLIO
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows (PowerShell):
venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the development server
```bash
python app.py
```
Open **[http://localhost:5000](http://localhost:5000)** in your browser.

---

## 📬 Contact & Connect

- 🌐 **Live Website**: [https://pavanpoojary.vercel.app](https://pavanpoojary.vercel.app)
- 🐙 **GitHub**: [github.com/pavanpoojary348](https://github.com/pavanpoojary348)
- 💻 **LeetCode**: [leetcode.com/u/pavanlpoojary](https://leetcode.com/u/pavanlpoojary/)
- 💼 **LinkedIn**: [linkedin.com/in/pavanlpoojary](https://www.linkedin.com/in/pavanlpoojary/)
- 📧 **Email**: [poojaryp379@gmail.com](mailto:poojaryp379@gmail.com)

---

<div align="center">
  <sub>&copy; 2026 Pavan Poojary &bull; Built with dedication and clean code.</sub>
</div>