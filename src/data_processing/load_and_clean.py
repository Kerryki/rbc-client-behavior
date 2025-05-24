import numpy as np
import pandas as pd
import os

# Get current file location
base_dir = os.path.dirname(__file__)

# Load CSV
raw=pd.read_csv(os.path.join(base_dir, '..', '..', 'data', 'raw', 'clients.csv'))


#removing duplicates
raw.drop_duplicates(subset='client_id',inplace=True) 

#ensure all columns are in the correct data type
raw['age']=pd.to_numeric(raw['age'], errors='coerce') #convert to numeric
raw['postal_code']=pd.to_numeric(raw['postal_code'], errors='coerce') #convert to string
raw['account_open_date']=pd.to_datetime(raw['account_open_date'], errors='coerce') #convert to datetime
raw['avg_monthly_balance']=pd.to_numeric(raw['avg_monthly_balance'], errors='coerce') #convert to numeric
raw['avg_monthly_transactions']=pd.to_numeric(raw['avg_monthly_transactions'], errors='coerce') #convert to numeric
raw['total_transaction_volume']=pd.to_numeric(raw['total_transaction_volume'], errors='coerce') #convert to numeric
raw['credit_card_usage_percent']=pd.to_numeric(raw['credit_card_usage_percent'], errors='coerce') #convert to numeric
raw['num_overdrafts_last_6_months']=pd.to_numeric(raw['num_overdrafts_last_6_months'], errors='coerce') #convert to numeric
raw['missed_payments_last_12_months']=pd.to_numeric(raw['missed_payments_last_12_months'], errors='coerce') #convert to numeric
raw['mortgage_balance']=pd.to_numeric(raw['mortgage_balance'], errors='coerce') #convert to numeric
raw['auto_loan_balance']=pd.to_numeric(raw['auto_loan_balance'], errors='coerce') #convert to numeric

# Standardize all text columns: strip whitespace and make lowercase
for col in raw.select_dtypes(include='object').columns:
    raw[col] = raw[col].str.strip().str.title()


#fill all empty values with 0
raw.fillna(value=0, inplace=True) #fillna with 0


raw.to_csv(os.path.join(base_dir, '..', '..', 'data', 'processed', 'clients.csv'), index=False)

#explore columns
stats=(raw.describe(include='all')).reset_index()
stats.to_csv(os.path.join(base_dir, '..', '..', 'data', 'processed', 'clients_stats.csv'), index=False)