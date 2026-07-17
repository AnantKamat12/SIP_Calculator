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
   * Supports an advanced **Yearly Increment (%)** feature to simulate annual step-up amounts in your monthly contributions.

3. **Loan Maturity Calculator (`/loan`)**
   * Computes overall asset maturity frameworks and monitors cumulative interest charges generated over the loan's lifecycle.

4. **Informational Route (`/about`)**
   * A clean text layout introducing the project parameters and providing a direct link back to the source repository.
5. **CALCULATOR Route (`/calc`)**
   * A simple calculater page

---

## 📁 Project Architecture & File Flow

The application follows the structured directory layout required by Flask:

```text
zproject/
│
├── app.py                 # Core routing traffic director & form data extraction
├── Interest.py            # Pure Python math engine housing the calculation classes
├── requirements.txt       # Project dependencies (Flask)
├── templates/             # Jinja2 template files
│   ├── base.html          # Master structural shell layout (Navbar, CSS/JS links)
│   ├── home.html          # Simple & Compound Interest dashboard view
│   ├── new.html           # SIP Calculator interface
│   ├── loan.html          # Loan breakdown display
│   └── about.html         # Project details page
└── static/                # Local static folders
    ├── css/style.css      # Not used (Bootstrap handles styling)
    └── js/main.js         # Not used (Bootstrap JS only)
```

---

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/AnantKamat12/SIP_Calculator.git
cd SIP_Calculator
```

### 2. Create a Virtual Environment (Optional but Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Server

```bash
python app.py
```

The application will start on:

```
http://127.0.0.1:5000/
```

Open the above URL in your browser.

---

## 🌐 Application Routes

| Route | Purpose |
|--------|---------|
| `/` | SIP Growth Calculator |
| `/home` | Simple & Compound Interest Calculators |
| `/loan` | Loan Maturity Calculator |
| `/about` | About Page |

---

## 🛠️ Technology Stack

- Python
- Flask
- HTML5
- Bootstrap 5
- Jinja2 Templates

---

## 📦 Dependencies

- Python 3.x
- Flask

Install using:

```bash
pip install -r requirements.txt
```

---

## 📄 License

This project was developed for educational purposes to explore Flask routing, backend programming, mathematical computation, and responsive web development using Bootstrap.
