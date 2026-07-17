from flask import Flask, render_template, request
from Interest import Interest  # Capital 'I' matches your filename Interest.py!

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def render():
    results = None
    if request.method == 'POST':
        # Using fallback '0' prevents the engine from crashing if a field is left empty
        monthly_deposit = float(request.form.get('monthly_deposit') or '0')
        annual_rate = float(request.form.get('annual_rate') or '0')
        years = float(request.form.get('years') or '0')
        inc = float(request.form.get('inc') or '0')
        
        calc = Interest()
        results = calc.sip(
            monthly_deposit=monthly_deposit, 
            annual_rate=annual_rate, 
            years=years,
            annual_increment_percent=inc
        )
        
    return render_template('new.html', results=results)

# ─── ADD THIS NEW ROUTE FOR YOUR LOAN CALCULATOR ───
@app.route('/loan', methods=['GET', 'POST'])
def loan_calculator():
    loan_results = None
    if request.method == 'POST':
        principal = float(request.form.get('principal') or '0')
        rate = float(request.form.get('rate') or '0')
        years = float(request.form.get('years') or '0')
        
        calc = Interest()
        # Using compound interest as an example for the loan calculation maturity value
        maturity_value = calc.compound_interest(P=principal, r=rate, t=years, n=12)
        
        loan_results = {
            "principal": principal,
            "rate": rate,
            "years": years,
            "maturity_value": round(maturity_value, 2),
            "interest_charged": round(maturity_value - principal, 2)
        }
        
    return render_template('loan.html', results=loan_results)
@app.route('/home', methods=['GET', 'POST'])
def simple_interest():
    si_results = None
    ci_results = None
    
    if request.method == 'POST':
        # Identify which button fired the calculation engine
        calc_type = request.form.get('calc_type')
        
        principal = float(request.form.get('principal') or '0')
        rate = float(request.form.get('rate') or '0')
        years = float(request.form.get('years') or '0')
        
        cal = Interest()
        
        if calc_type == 'simple':
            answer = cal.simple_interest(P=principal, r=rate, t=years)
            si_results = {
                "principal": principal,
                "rate": rate,
                "total": round(answer, 2),
                "interest": round(answer - principal, 2)
            }
        elif calc_type == 'compound':
            # Uses monthly compounding frequency (n=12) by default
            answer = cal.compound_interest(P=principal, r=rate, t=years, n=12)
            ci_results = {
                "principal": principal,
                "rate": rate,
                "total": round(answer, 2),
                "interest": round(answer - principal, 2)
            }
            
    # Send both pointers back down. One will contain data, the other stays None.
    return render_template('home.html', si_results=si_results, ci_results=ci_results)
@app.route('/calc',methods=['GET','POST'])
def calculator():
    result=None
    if request.method == 'POST':
        
        sign = (request.form.get('sign') or '+')
        num1 = float(request.form.get('num1') or '0')
        num2 = float(request.form.get('num2') or '0')
        
        cal = Interest()
        if sign=='+':
            result=num1+num2
        elif sign=='-':
            result=num1-num2
        elif sign=="*":
            result=num1*num2
        elif sign=="/":
            if num2!=0:
                result=num1/num2
            else:
                result="denominator cant be zero"
        else:
            result=num1**num2
            


            
    # Send both pointers back down. One will contain data, the other stays None.
    return render_template('calc.html', results=result)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)