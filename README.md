# IBM_AI_CERTIFICATION_Final_Project
# Coffee Sales Analysis

**Author:** Kezia Shiny Pothumudi  
**Project:** IBM AI Developer Final Project  

---

## **Project Overview**
This project analyzes coffee sales data to uncover trends and patterns in sales over time, by coffee type, by hour of day, and between weekdays and weekends. The goal is to provide actionable insights for business decision-making, such as inventory planning, staffing, and promotions.

---

## **Dataset**
The dataset contains coffee sales records including the following columns:

- `Date` – Date of the sale  
- `Time_of_Day` – Morning, Afternoon, or Night  
- `hour_of_day` – Hour of the sale (numeric)  
- `Weekday` – Day of the week  
- `coffee_name` – Type of coffee sold  
- `money` – Sale amount  

---

## **Analysis Steps**
1. **Data Cleaning & Preparation**
   - Convert date columns to datetime objects.  
   - Strip whitespace from column names and categorical variables.  
   - Create new columns:
     - `IsWeekend` – True if sale occurred on Saturday/Sunday  
     - `HourCategory` – Morning, Afternoon, Night based on `hour_of_day`  

2. **Exploratory Data Analysis (EDA)**
   - Daily sales trends  
   - Sales by coffee type  
   - Sales by hour of day  
   - Sales by weekday and weekend  
   - Sales by time of day  

3. **Hypothesis Testing**
   - **t-test:** Compare weekend vs. weekday sales  
   - **ANOVA:** Compare sales across different times of day  

4. **Visualization**
   - Bar plots for all trends  
   - Highlighted plots for highest sales periods  

---

## **Key Insights**
- Weekend sales show [higher/lower/similar] trends compared to weekdays.  
- The most popular coffee type is **[insert top coffee type]**.  
- Peak sales occur during **[insert peak hour/time of day]**.  
- These insights can guide business decisions for promotions, inventory, and staffing.

---

## **Files in This Repository**
- `IBM.py` – Jupyter notebook with code, analysis, and visualizations.  
- `coffee_sales_report.pdf` – PDF report generated from the notebook.  
- `Coffe_sales.csv` – Dataset (or sample dataset if original is confidential).  

---

## **How to Run**
1. Clone the repository:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/IBM_AI_Final_Project.git
