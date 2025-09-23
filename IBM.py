#import libraries
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

#visualization
sns.set(style="whitegrid")

#file path
file_path = r"C:\Users\hi\Desktop\Coffe_sales.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Preview the first 5 rows
print("first 5 rows:\n",df.head())

#shape of dataset
print("dataset shape:", df.shape)

# Check column names and data types
print("Info:\n",df.info())

#check missing values
print("missing values per column:\n", df.isnull().sum())

#check duplicate rows
print("number of duplicate rows: ", df.duplicated().sum())

#convert 'Date' column to datetime
df['date'] = pd.to_datetime(df['Date'])

#exploratory data analysis (EDA)

#Daily total sales
daily_sales = df.groupby('date')['money'].sum().reset_index()
plt.figure(figsize=(12,5))
sns.lineplot(x='date', y='money', data=daily_sales)
plt.title('Daily Coffee Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Money Spent')
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()

#sales by coffee type
coffee_sales = df.groupby('coffee_name')['money'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
sns.barplot(x=coffee_sales.index, y=coffee_sales.values)
plt.title('Total Sales by Coffee Type')
plt.xlabel('Coffee Type')
plt.ylabel('Total Money Spent')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#sales by hour of day
hourly_sales = df.groupby('hour_of_day')['money'].sum().reset_index()
plt.figure(figsize=(10,5))
sns.barplot(x='hour_of_day', y='money', data=hourly_sales)
plt.title('Total Sales by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Total Money Spent')
plt.tight_layout()
plt.show()

# Strip column names just in case
df.columns = df.columns.str.strip()

# Strip hidden spaces or weird characters in Weekday
df['Weekday'] = df['Weekday'].str.strip().replace(r'\s+', '', regex=True)

# Check unique values to see what’s inside
print(df['Weekday'].unique())


#sales in a week
week_order = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

week_sales = df.groupby('Weekday')['money'].sum().reset_index()
week_sales['Weekday'] = pd.Categorical(week_sales['Weekday'], categories=week_order, ordered=True)
week_sales = week_sales.sort_values('Weekday')

plt.figure(figsize=(10,5))
sns.barplot(x='Weekday', y='money', data=week_sales)
plt.title('Total Sales in a Week')
plt.xlabel('Weekday')
plt.ylabel('Total Money Spent')
plt.tight_layout()
plt.show()
print(week_sales)


# remove any extra spaces from column names
df.columns = df.columns.str.strip()
#sales by time of day
timeofday_sales = df.groupby('Time_of_Day')['money'].sum().reset_index()
plt.figure(figsize=(6,4))
sns.barplot(x='Time_of_Day', y='money', data=timeofday_sales)
plt.title('Total Sales by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Total Money Spent')
plt.tight_layout()
plt.show()
print(timeofday_sales)
print(df.describe())

#create a new column for weekend
df['IsWeekend'] = df['Weekday'].isin(['Sat', 'Sun'])

#Categorize hours into time-of-day
def categorize_hour(hour):
    if 6<=hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    else:
        return 'Night'
df['HourCategory'] = df['hour_of_day'].apply(categorize_hour)

print(df[['hour_of_day', 'HourCategory', 'Weekday', 'IsWeekend']].head(10))

#------------------------------

#Hypothesis testing

#-------------------------------

#1. Sales on weekends
weekend_sales = df[df['IsWeekend']]['money']

#2. Sales on weekdays
weekday_sales = df[~df['IsWeekend']]['money']

#t-test (compares the mean between 2 groups)
from scipy.stats import ttest_ind
t_stat, p_value = ttest_ind(weekend_sales, weekday_sales)
print("t-statistic:", t_stat)
print("p-value:", p_value)

#Compare the means
print("Average weekend sale:", weekend_sales.mean())
print("Average weekday sale:", weekday_sales.mean())

#interpret results
if p_value < 0.05:
    print("Reject null hypothesis: Weekend sales are significantly different from weekday sales")
else:
    print("Fail to reject null hypothesis: No significant difference")

#sales for each time category
morning_sales = df[df['Time_of_Day'] == 'Morning']['money']
afternoon_sales = df[df['Time_of_Day'] == 'Afternoon']['money']
night_sales = df[df['Time_of_Day'] == 'Night']['money']

#ANOVA(Analysis of Variance)
f_stat, p_value = stats.f_oneway(morning_sales, afternoon_sales, night_sales)

print("F-statistic:", f_stat)
print("p-value:", p_value)

#group means
print("Average Morning sale:", morning_sales.mean())
print("Average Afternoon sale:", afternoon_sales.mean())
print("Average Night sale:", night_sales.mean())



# Calculate average sales by time of day
avg_sales = df.groupby('Time_of_Day')['money'].mean().reset_index()

plt.figure(figsize=(8,5))

# Highlight the bar with highest sales
colors = ['lightblue' if x != avg_sales['money'].max() else 'orange' for x in avg_sales['money']]

sns.barplot(x='Time_of_Day', y='money', data=avg_sales, palette=colors)

# Add labels on top of bars
for index, row in avg_sales.iterrows():
    plt.text(index, row.money + 0.5, f"${row.money:.2f}", ha='center', fontsize=12)

plt.title('Average Coffee Sales by Time of Day', fontsize=14)
plt.xlabel('Time of Day', fontsize=12)
plt.ylabel('Average Money Spent ($)', fontsize=12)
plt.ylim(0, max(avg_sales['money']) * 1.1)  # Adds some space on top for labels
plt.tight_layout()
plt.show()

