import math

def calculate_monthly_payment(loan_amount, interest_rate, loan_term_years):
    monthly_interest_rate = interest_rate / 12 / 100
    num_payments = loan_term_years * 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -num_payments))
    return monthly_payment

def calculate_loan_costs(monthly_payment, loan_term_years):
    total_loan_cost = monthly_payment * 12 * loan_term_years
    return total_loan_cost

def generate_amortization_schedule(loan_amount, interest_rate, loan_term_years):
    monthly_interest_rate = interest_rate / 12 / 100
    num_payments = loan_term_years * 12

    balance = loan_amount
    schedule = []

    for month in range(1, num_payments + 1):
        interest_payment = balance * monthly_interest_rate
        principal_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term_years) - interest_payment
        balance -= principal_payment

        schedule.append({
            'Month': month,
            'Balance': round(balance, 2),
            'Principal': round(principal_payment, 2),
            'Interest': round(interest_payment, 2),
        })

    return schedule

# Example usage:
loan_amount = 220000  # Example loan amount in dollars
interest_rate = 7 # Example annual interest rate
loan_term_years = 30  # Example loan term in years

monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term_years)
total_loan_cost = calculate_loan_costs(monthly_payment, loan_term_years)
amortization_schedule = generate_amortization_schedule(loan_amount, interest_rate, loan_term_years)

# Print results
print(f"Monthly Payment: ${round(monthly_payment, 2)}")
print(f"Total Loan Cost: ${round(total_loan_cost, 2)}")
print("\nAmortization Schedule:")
for entry in amortization_schedule:
    print(entry)
