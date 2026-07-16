# WealthCalc - Flask & Bootstrap Financial Calculator Suite

This is an experimental, minimum viable web application built to explore full-stack development using **Flask** for backend logic and **Bootstrap 5** for a responsive, modern frontend user interface. 

The goal of this project was to connect interactive HTML forms with mathematical Python algorithms in the backend, learning how data flows between the user interface and server routines using GET and POST methods.

---

## 🚀 Key Features

The application serves as a comprehensive interest and wealth growth calculator suite, split across distinct interactive views:

1. **Simple & Compound Interest Studio (`/home`)**
   * **Simple Interest Calculator:** Computes basic growth metrics over a fixed tenure using standard interest calculations.
   * **Compound Interest Calculator:** Computes growth using recurring monthly compound interest periods.
   * *Both calculators are nested side-by-side using Bootstrap grids and track calculations independently utilizing distinct state flags.*

2. **SIP Growth Calculator (`/`)**
   * Calculates Systematic Investment Plan (SIP) returns with a compounding growth engine.
   * Supports an advanced **Yearly Increment (%)** features to simulate annual step-up amounts in your monthly contributions.

3. **Loan Maturity Calculator (`/loan`)**
   * Computes overall asset maturity frameworks and monitors cumulative interest charges generated over the loan's lifecycle.

4. **Informational Route (`/about`)**
   * A clean text layout introducing the project parameters and providing a direct link back to the source repository.

---

## 📁 Project Architecture & File Flow

The application follows the strict, structured directory environment required by Flask:

```text
zproject/
│
├── app.py                 # Core routing traffic director & form data extraction
├── Interest.py           # Pure Python math engine housing the calculation classes
├── requirements.txt       # Project dependencies (Flask)
├── templates/             # Jinja2 template files
│   ├── base.html          # Master structural shell layout (Navbar, CSS/JS links)
│   ├── home.html          # Simple & Compound interest dashboard view
│   ├── new.html           # SIP calculator interface
│   ├── loan.html          # Loan breakdown display
│   └── about.html         # Project details page
└── static/                # Local static folders for asset styling overrides
    ├── css/style.css (not used) only bootstrap css was used
    └── js/main.js  (not used)  only bootstrap jss was used
