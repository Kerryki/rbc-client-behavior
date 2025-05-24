import numpy as np
import pandas as pd
import os


# Get current file location
base_dir = os.path.dirname(__file__)

# Build absolute path to CSV file
csv_path = os.path.join(base_dir, '..', '..', 'data', 'processed', 'grouped_clients.csv')

# Load CSV
df = pd.read_csv(csv_path)
raw=pd.read_csv(os.path.join(base_dir, '..', '..', 'data', 'processed', 'clients_with_age_groups.csv'))

# Create age groups
a=df.groupby('age_group')['counts'].sum().reset_index() #takes what you had in counts on that column and then adds vertically
a.to_csv(os.path.join(base_dir, '..', '..', 'data', 'processed', 'age_group_counts.csv'), index=False)


#average account balance per group
b=raw.groupby('age_group')['avg_monthly_balance'].mean().reset_index()
b.to_csv(os.path.join(base_dir, '..', '..', 'data', 'processed', 'age_group_avg_balance.csv'), index=False)

#median account balance per group
c=raw.groupby('age_group')['avg_monthly_balance'].median().reset_index()
c.to_csv(os.path.join(base_dir, '..', '..', 'data', 'processed', 'age_group_median_balance.csv'), index=False)

#kpis of loans in each group
d=raw.groupby('age_group').agg({'auto_loan_balance':['sum','mean','median']}).reset_index()
d.to_csv(os.path.join(base_dir, '..', '..', 'data', 'processed', 'age_group_loans_kpis.csv'), index=False)

#account opening range dates
raw['account_open_date'] = pd.to_datetime(raw['account_open_date']) #convert to datetime
raw['account_opening_year'] = raw['account_open_date'].dt.year #extract year
e=raw.groupby(['age_group','account_opening_year']).size().reset_index(name='new_client_counts')
e.to_csv(os.path.join(base_dir, '..', '..', 'data', 'processed', 'new_clients_by_opening_date.csv'), index=False)