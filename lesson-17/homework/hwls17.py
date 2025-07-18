import pandas as pd
import numpy as np

# ----------------------------
# Homework 1
# ----------------------------
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Rename column names using function
df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# 2. Print the first 3 rows
first_3_rows = df.head(3)

# 3. Find mean age
mean_age = df['age'].mean()

# 4. Select and print only the 'first_name' and 'city' columns
name_city = df[['first_name', 'city']]

# 5. Add a new column 'Salary' with random salary values
np.random.seed(0)
df['salary'] = np.random.randint(50000, 100000, size=len(df))

# 6. Display summary statistics of the DataFrame
summary_stats = df.describe(include='all')

# ----------------------------
# Homework 2
# ----------------------------
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(sales_data)

max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()

# ----------------------------
# Homework 3
# ----------------------------
expenses_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(expenses_data)

# Make Category column as index
expenses.set_index('Category', inplace=True)

# Calculate max, min, and average expense for each category
max_expense_per_category = expenses.max(axis=1)
min_expense_per_category = expenses.min(axis=1)
avg_expense_per_category = expenses.mean(axis=1)

# Display results
import ace_tools as tools; tools.display_dataframe_to_user(name="Homework 1 - DataFrame with Salary and Summary", dataframe=df)
tools.display_dataframe_to_user(name="Homework 2 - Sales and Expenses", dataframe=sales_and_expenses)
tools.display_dataframe_to_user(name="Homework 3 - Monthly Expenses", dataframe=expenses)

print("Homework 1 Results:")
print("First 3 rows:\n", first_3_rows)
print("Mean age:", mean_age)
print("Name and City columns:\n", name_city)
print("Summary statistics:\n", summary_stats)

print("\nHomework 2 Results:")
print("Max Sales:", max_sales, " Max Expenses:", max_expenses)
print("Min Sales:", min_sales, " Min Expenses:", min_expenses)
print("Average Sales:", avg_sales, " Average Expenses:", avg_expenses)

print("\nHomework 3 Results:")
print("Max expense per category:\n", max_expense_per_category)
print("Min expense per category:\n", min_expense_per_category)
print("Average expense per category:\n", avg_expense_per_category)
