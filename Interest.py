import math
class Interest():
    def __init__(self):
        pass

    def simple_interest(self, P, r, t):
        """Simple interest for any time in years (including fractional years)."""
        return P * (1 + (r / 100) * t)

    def compound_interest(self, P, r, t, n=1):
        """Compound interest for any time in years.

        P = principal
        r = annual interest rate in percent
        t = time in years (can be 1.5, 2.25, etc.)
        n = compounding periods per year (1 annual, 12 monthly, 4 quarterly)
        """
        rate = r / 100
        return P * (1 + rate / n) ** (n * t)

    def continuous_compound_interest(self, P, r, t):
        """Continuous compound interest for fractional years."""
        import math
        rate = r / 100
        return P * math.exp(rate * t)

    def sip(self, monthly_deposit, annual_rate, years, annual_increment_percent=0.0, compounds_per_year=12):
        """Calculate SIP value with optional annual deposit increment.

        monthly_deposit: initial monthly deposit amount
        annual_rate: annual interest rate in percent
        years: total investment period in years (can be fractional)
        annual_increment_percent: yearly increase in monthly deposit, in percent
        compounds_per_year: compounding frequency, default 12 for monthly compounding
        """
        annual_rate = annual_rate / 100
        monthly_rate = annual_rate / compounds_per_year
        total_amount = 0.0
        total_invested = 0.0
        months = int(round(years * 12))
        current_monthly = monthly_deposit

        for month in range(1, months + 1):
            if month > 1 and (month - 1) % 12 == 0:
                current_monthly *= 1 + annual_increment_percent / 100

            total_invested += current_monthly
            total_amount = (total_amount + current_monthly) * (1 + monthly_rate)

        gain = total_amount - total_invested
        return {
            "total_amount": round(total_amount, 2),
            "total_invested": round(total_invested, 2),
            "gain": round(gain, 2),
        }


if __name__ == '__main__':
    it = Interest()
    print(it.simple_interest(100, 10, 1.5))
    print(it.compound_interest(100, 10, 1.5, n=1))
    print(it.continuous_compound_interest(100, 10, 1.5))
    print(it.sip(monthly_deposit=1000, annual_rate=12, years=1, annual_increment_percent=5))
