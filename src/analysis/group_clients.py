import os
import pandas as pd

# Get current file location
base_dir = os.path.dirname(__file__)

# Build absolute path to CSV file
csv_path = os.path.join(base_dir, '..', '..', 'data', 'raw', 'clients.csv')

# Load CSV
df = pd.read_csv(csv_path)

#classifying into different age groups
bins = [17, 24, 34, 44, 54, 120]
labels = ['18-24', '25-34', '35-44', '45-54', '55+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

df.to_csv(os.path.join(base_dir, '..', '..', 'data', 'processed', 'clients_with_age_groups.csv'), index=False)

#grouping now the age groups into different provinces and account types
a=df.groupby(['age_group', 'province','account_type'], observed=False).size().reset_index(name='counts')
a.to_csv(os.path.join(base_dir, '..', '..', 'data', 'processed', 'grouped_clients.csv'), index=False)

