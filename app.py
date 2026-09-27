from flask import Flask, render_template, request
from CarPayment import CarPayments, get_location_and_tax, get_apr_from_credit_score

app = Flask(__name__)

@app.route("/")
def home():
    """Displays the loan calculator input form"""  
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    """Reads the submitted form data, verifies it, calculates the loan details
    (using a live ZIP code API and static tax data), and returns the results page.
    Returns a styled error page instead if any input is invalid"""
    
    zip_code = request.form["zip_code"]
    county_tax_rate = float(request.form["county_tax_rate"])
    credit_score = int(request.form["credit_score"])
    loan_type = request.form["loan_type"]
    
    car_price = float(request.form["car_price"])
    down_payment = float(request.form["down_payment"])
    trade_in_value = float(request.form["trade_in_value"])
    dealer_markup = float(request.form["dealer_markup"])
    term_years = int(request.form["term_years"])
    dealership_fee = float(request.form["dealership_fee"])
    title_fee = float(request.form["title_fee"])
    
    # --- validation ---
    if credit_score < 300 or credit_score > 850:
        return render_template("error.html", error_message="Credit score must be between 300 and 850.")
    
    if car_price <= 0:
        return render_template("error.html", error_message="Car price must be greater than 0.")
    
    if down_payment < 0:
        return render_template("error.html", error_message="Down payment cannot be negative.")
    
    if term_years <= 0:
        return render_template("error.html", error_message="Loan term must be at least 1 year.")
    
    if county_tax_rate < 0 or county_tax_rate > 1:
        return render_template("error.html", error_message="County tax rate must be a decimal between 0 and 1 (e.g. 0.01 for 1%).")
    
    state, city, state_rate = get_location_and_tax(zip_code)

    if state is None:
        return render_template("error.html", error_message="Invalid ZIP code. Please enter a real US ZIP code.")

    apr = get_apr_from_credit_score(credit_score, loan_type)
    
    my_car = CarPayments(
        car_price=car_price,
        down_payment=down_payment,
        trade_in_value=trade_in_value,
        dealer_markup=dealer_markup,
        apr=apr,
        term_years=term_years,
        state_tax_rate=state_rate,
        county_tax_rate=county_tax_rate,
        dealership_fee=dealership_fee,
        title_fee=title_fee
    )
    
    return render_template(
        "results.html",
        city=city,
        state=state,
        apr=apr,
        loan_amount=f"{my_car.loan_amount():.2f}",
        monthly_payment=f"{my_car.monthly_payment():.2f}",
        total_interest=f"{my_car.total_interest_paid():.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5001)