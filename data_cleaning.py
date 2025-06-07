import pandas as pd

# Load the dirty data
df = pd.read_csv('dirty_data.csv')

# Drop rows with missing Name or Email
df = df.dropna(subset=['Name', 'Email'])

# Fill missing Age with the average age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Fix the 'Joined' column to datetime format
df['Joined'] = pd.to_datetime(df['Joined'], errors='coerce')

# Drop rows where 'Joined' couldn't be parsed
df = df.dropna(subset=['Joined'])

# Save the cleaned data
df.to_csv('cleaned_data.csv', index=False)

print("Data cleaned and saved as cleaned_data.csv")