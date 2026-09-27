from CarPayment import CarPayments

def test_years_to_months():
    """Confirms a 5-year term is correctly converted to 60 months"""
    
    car = CarPayments(
        car_price=25000, down_payment=3000, trade_in_value=2000,
        dealer_markup=500, apr=6.5, term_years=5,
        state_tax_rate=0.043, county_tax_rate=0.01,
        dealership_fee=150, title_fee=75
    )
    assert car.term_months == 60
    
def test_amortization_ends_near_zero():
    """Confirms the loan balance reaches 0 by the final month of the amortization schedule"""   
    
    car7 = CarPayments(
        car_price=25000, down_payment=3000, trade_in_value=2000,
        dealer_markup=500, apr=6.5, term_years=5,
        state_tax_rate=0.043, county_tax_rate=0.01,
        dealership_fee=150, title_fee=75
    )
    schedule = car7.amortization()
    last_month = schedule[-1]
    assert last_month["balance"] == 0.0
    
def test_total_interest_positive():
    """Confirms a loan with an APR thats not zero, always accrues some interest"""
    
    car8 = CarPayments(
        car_price=25000, down_payment=3000, trade_in_value=2000,
        dealer_markup=500, apr=6.5, term_years=5,
        state_tax_rate=0.043, county_tax_rate=0.01,
        dealership_fee=150, title_fee=75
    )
    assert car8.total_interest_paid() > 0
    
from CarPayment import get_tax_rates

def test_get_tax_rates_virginia():
    """Confirms Virginia's tax rate is correctly read from tax_rates.json"""
   
    assert get_tax_rates("Virginia") == 0.043