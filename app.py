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

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)