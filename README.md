---

# ⚙️ How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/AnantKamat12/SIP_Calculator.git
cd SIP_Calculator
```

## 2. Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Flask Application

```bash
python app.py
```

If everything starts successfully, Flask will display output similar to:

```text
* Running on http://127.0.0.1:5000/
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

# 🌐 Available Routes

| Route | Description |
|-------|-------------|
| `/` | SIP Growth Calculator |
| `/home` | Simple & Compound Interest Calculators |
| `/loan` | Loan Maturity Calculator |
| `/about` | About the Project |

---

# 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, Bootstrap 5
- **Templating Engine:** Jinja2
- **Language:** Python 3

---

# 📦 Requirements

- Python 3.9 or later
- Flask

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 📸 Screenshots

You can add screenshots of the SIP Calculator, Interest Calculator, and Loan Calculator here to showcase the application's UI.

---

# 📄 License

This project was created for learning and educational purposes to understand Flask routing, backend integration, mathematical computation, and responsive frontend development.
