import random
from faker import Faker
import csv
fake=Faker()

with open('data/raw/clients.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
    'client_id',
    'first_name',
    'last_name',
    'age',
    'gender',
    'email',
    'phone_number',
    'address',
    'city',
    'province',
    'postal_code',
    'employment_status',
    'income_bracket',
    'account_type',
    'account_open_date',
    'avg_monthly_balance',
    'avg_monthly_transactions',
    'total_transaction_volume',
    'loan_products',
    'credit_card_usage_percent',
    'num_overdrafts_last_6_months',
    'missed_payments_last_12_months',
    'online_banking_usage',
    'products_owned',
    'has_investment_account',
    'has_mortgage',
    'mortgage_balance',
    'has_auto_loan',
    'auto_loan_balance'
])

    for x in range(10000):
        client_id = x
        first_name=fake.first_name()
        last_name=fake.last_name()
        age=random.randint(18, 80)
        gender=random.choice(['Male', 'Female', 'Other'])
        email=fake.email()
        phone_number= fake.phone_number()
        address=fake.street_address()
        city=fake.city()
        province=fake.state()  
        postal_code=fake.postalcode()
        employment_status=random.choice(['Employed', 'Unemployed', 'Student', 'Retired'])
        income_bracket=random.choice(['<$30k', '$30k–$60k', '$60k–$100k', '>$100k'])
        account_type=random.choice(['Chequing', 'Savings', 'Joint', 'Business'])
        account_open_date=fake.date_between(start_date='-10y', end_date='today')
        avg_monthly_balance=random.randint(500, 10000)
        avg_monthly_transactions=random.randint(5, 100)     
        total_transaction_volume=random.randint(1000, 100000)
        loan_products=random.choice(['Yes', 'No'])
        credit_card_usage_percent=random.randint(0, 100)    
        num_overdrafts_last_6_months=random.randint(0, 5)        
        missed_payments_last_12_months=random.randint(0, 3)      
        online_banking_usage=random.choice(['Daily', 'Weekly', 'Rarely', 'Never'])
        products_owned=random.sample(['Credit Card', 'Mortgage', 'TFSA', 'RRSP'], k=random.randint(1,4))  
        has_investment_account=random.choice(['Yes', 'No'])   
        has_mortgage=random.choice(['Yes', 'No'])  
        mortgage_balance=random.randint(10000, 500000) if has_mortgage== 'Yes' else 0
        has_auto_loan=random.choice(['Yes', 'No'])  
        auto_loan_balance = random.randint(5000, 100000) if has_auto_loan == 'Yes' else 0
        writer.writerow([client_id,first_name,last_name,age,gender,email,phone_number,address,city,province,postal_code,employment_status,income_bracket,account_type,account_open_date,avg_monthly_balance,avg_monthly_transactions,total_transaction_volume,loan_products,credit_card_usage_percent,num_overdrafts_last_6_months,missed_payments_last_12_months,online_banking_usage,";".join(products_owned),has_investment_account,has_mortgage,mortgage_balance,has_auto_loan,auto_loan_balance])




