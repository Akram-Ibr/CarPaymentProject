import json

def get_tax_rates(state):
    """Looks up and returns the state tax rate for the given state inputed by the user from the tax_rates.json"""
    
    with open("tax_rates.json") as f:
        tax_data = json.load(f)
    return tax_data[state]

import requests

def get_state_city_from_zip(zip_code):
    """It pulls in an API and inputs a zipcode from the user to determine the state and city the zipcode is located in"""
    
    response = requests.get(f"https://api.zippopotam.us/us/{zip_code}")
    
    if response.status_code != 200:
        return None, None
    
    data = response.json()
    place_info = data["places"][0]
    state = place_info["state"]
    city = place_info["place name"]
    
    return state, city



def get_location_and_tax(zip_code):
    """The function pulls in a previous function containing a API based off the users input zipcode and returns the state tax rate"""
    
    state, city = get_state_city_from_zip(zip_code)
    
    if state is None:
        return None, None, None
    
    state_rate = get_tax_rates(state)
    return state, city, state_rate


def get_apr_from_credit_score(score, loan_type="new"):
    """The function determines an APR for the user based off the users credit score and loan type, new or old"""
    
    if score >= 781:
        return 4.55 if loan_type == "new" else 6.30
    elif score >= 661:
        return 6.23 if loan_type == "new" else 8.77
    elif score >= 601:
        return 9.67 if loan_type == "new" else 14.03
    else:
        return 13.44 if loan_type == "new" else 19.42



class CarPayments:
    
    """Represents a financial car loan where anyone can make inputs and recieve an estimated monthly car payment """
    
    
    def __init__(self, car_price, down_payment, trade_in_value, dealer_markup,
                 apr, term_years, state_tax_rate, county_tax_rate,
                 dealership_fee, title_fee):
        """Python automatically runs this function creating an object for the user by using self and user inputs"""
        
        self.car_price = car_price
        self.down_payment = down_payment
        self.trade_in_value = trade_in_value
        self.dealer_markup = dealer_markup
        self.apr = apr
        self.term_months = self.years_to_months(term_years)
        self.state_tax_rate = state_tax_rate
        self.county_tax_rate = county_tax_rate
        self.dealership_fee = dealership_fee
        self.title_fee = title_fee
    
    def years_to_months(self, years):
        """Receives the years and converts into months"""
        
        return years * 12

    def taxed_amount(self):
        """The function takes in the car adds the remaining for the msrp then substracts it by the trade in value and returns it"""
        
        return (self.car_price + self.dealer_markup) - self.trade_in_value

    def total_tax(self):
        """The function takes in thereturns the total taxes used in the transaction"""  
        
        taxable = self.taxed_amount()
        return taxable * (self.state_tax_rate + self.county_tax_rate)

    def loan_amount(self):
        """The function returns the total msrp of the car substracted by the downpayment the user inputs then returns that value"""
        
        pre_tax = self.taxed_amount() - self.down_payment
        return pre_tax + self.total_tax() + self.dealership_fee + self.title_fee
    
    def monthly_payment(self):
        """The function divides the apr by 12 for monthly rate then by 100 to decimal value and calculates the monthly payment by using an equation and returns the monthly payment """
    
        principal = self.loan_amount()
        monthly_rate = self.apr / 12 / 100
        
        if monthly_rate == 0:
            return principal / self.term_months
        
        return principal * monthly_rate / (1 - (1 + monthly_rate) ** -self.term_months)
    
    def total_interest_paid(self):
        """The function takes the monthly payments multiplied by term months to recieve total paid cost of the car then substracts it by the price it was brought to determien the total tax paid""" 
        
        total_paid = self.monthly_payment() * self.term_months
        return total_paid - self.loan_amount()
    
    def amortization(self):
        """Returns a monthly payment schedule"""
        schedule = []
        balance = self.loan_amount()
        monthly_rate = self.apr / 12 / 100
        payment = self.monthly_payment()
        
        for month in range(1, self.term_months + 1):
            
            interest_payment = balance * monthly_rate
            principal_payment = payment - interest_payment
            balance -= principal_payment
        
            schedule.append({"month": month, "payment": round(payment, 2), "principal": round(principal_payment, 2), "interest": round(interest_payment, 2), "balance": round(max(balance, 0), 2)})
        return schedule
    

def get_valid_number(prompt, number_type=float, min_value=None, max_value=None):
    """This function is used to require to errors to occur for a user in case of invalid character inputs"""
    
    while True:
        try:
            value = number_type(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Please enter a value of at least {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Please enter a value of at most {max_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    """The User is required to input their values to determine their monthly car payment"""
    
    
    zip_code = input("Enter your ZIP code: ")
    state, city, state_rate = get_location_and_tax(zip_code)
    print(f"Detected location: {city}, {state}")
    print(f"State tax rate: {state_rate}")
    
    county_tax_rate = get_valid_number("Enter your county tax rate (e.g. 0.01 for 1%): ")
    
    credit_score = get_valid_number("Enter your credit score: ", int, 300, 850)
    
    loan_type = input("Is this a new or used car? (new/used): ").lower()
    apr = get_apr_from_credit_score(credit_score, loan_type)
    print(f"Estimated APR based on your credit: {apr}%")
    
    car_price = get_valid_number("Enter the car price: ")
    down_payment = get_valid_number("Enter your down payment: ")
    trade_in_value = get_valid_number("Enter your trade-in value (0 if none): ")
    dealer_markup = get_valid_number("Enter the dealership markup: ")
    term_years = get_valid_number("Enter the loan term in years: ", int)
    dealership_fee = get_valid_number("Enter the dealership fee: ")
    title_fee = get_valid_number("Enter the title fee: ")
    
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
    
    print(f"\n--- Your Loan Summary ---")
    print(f"Loan amount: ${my_car.loan_amount():.2f}")
    print(f"Monthly payment: ${my_car.monthly_payment():.2f}")
    print(f"Total interest paid: ${my_car.total_interest_paid():.2f}")    
  
    
    
    
    
    