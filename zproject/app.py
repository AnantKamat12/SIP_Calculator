from flask import Flask, render_template, request
from Interest import Interest  # Imports your math class

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def render():
    results = None
    if request.method == 'POST':
        # 1. Capture the inputs from the HTML form
        monthly_deposit = float(request.form.get('monthly_deposit'))
        annual_rate = float(request.form.get('annual_rate'))
        years = float(request.form.get('years'))
        inc=float(request.form.get('inc')) 
        
        # 2. Run the math from your Interest class
        calc = Interest()
        results = calc.sip(
            monthly_deposit=monthly_deposit, 
            annual_rate=annual_rate, 
            years=years,
            annual_increment_percent=inc
        )
        
    # 3. Send the results data back to the webpage layout
    return render_template('new.html', results=results)
@app.route('/loan', methods=['GET', 'POST'])
def loanrender():
    simple_result = None
    compound_result = None

    if request.method == 'POST':
        principal = float(request.form.get('loan', 0))
        annual_rate = float(request.form.get('annual_rate', 0))
        years = float(request.form.get('years', 0))
        interest_type = request.form.get('interest_type', 'simple')

        calc = Interest()

        if interest_type == 'compound':
            compounds_per_year = int(request.form.get('compounds_per_year', 1))
            total_amount = calc.compound_interest(principal, annual_rate, years, n=compounds_per_year)
            compound_result = {
                'principal': principal,
                'annual_rate': annual_rate,
                'years': years,
                'compounds_per_year': compounds_per_year,
                'total_amount': round(total_amount, 2),
                'interest_earned': round(total_amount - principal, 2),
            }
        else:
            total_amount = calc.simple_interest(principal, annual_rate, years)
            simple_result = {
                'principal': principal,
                'annual_rate': annual_rate,
                'years': years,
                'total_amount': round(total_amount, 2),
                'interest_earned': round(total_amount - principal, 2),
            }

    return render_template('loan.html', simple_result=simple_result, compound_result=compound_result)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)