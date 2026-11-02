# 📊 HR Analytics & Talent Development Dashboard

An end-to-end People Analytics project built to transform raw workforce data into actionable HR insights. This project covers the entire data pipeline: **Data Cleaning & Engineering (Python)**, **Data Relational Warehousing (PostgreSQL)**, and **Interactive Reporting (Power BI)**.

---

## 🎯 Business Goals & Objectives
This dashboard is engineered to help HR Executives and Leadership Teams make **data-driven human capital decisions** by evaluating organization health across three critical pillars:

1. **Workforce Capability:** Understanding employee allocation, diversity splits, marital status, and employment types across 48 unique operational locations.
2. **Talent Attrition Risk:** Pinpointing monthly resignation trends and turnover rates to mitigate voluntary turnover and optimize employee retention.
3. **Talent & Development Growth:** Evaluating workforce scaling through the correlation of internal career progression (`promotion_count`) and continuous training hours.

---

## 🛠️ Tech Stack & Architecture Pipeline
```text
[Raw Excel Dataset] ──> [Python / Pandas] ──> [PostgreSQL Warehouse] ──> [Power BI Desktop]
                        (ETL & Cleansing)       (Data Storage & Queries)     (DAX Reporting)
```

* **Data Processing & ETL:** Python 3 (Pandas, SQLAlchemy, Openpyxl)
* **Database Warehouse:** PostgreSQL
* **Business Intelligence Tool:** Power BI Desktop

---

## 📝 Step-by-Step Implementation Pipeline

### Phase 1: Data Cleansing & Preparation (Python Scripting)
The raw dataset contained nested missing parameters and unstandardized column formats. An automated Python preprocessing pipeline (`etl_script.py`) was engineered to execute the following audits:
* **Imputation Strategy:** Handled missing data by setting unreleased termination variables to `'Still Employed'`, filling empty education records with `'Unknown'`, and calculating baseline feature medians to fill missing values for `job_satisfaction` and `work_life_balance`.
* **Data Standardization:** Standardized schema structures by lowere-casing features, replacing blank spaces with underscores (`_`), and stripping accidental ghost-spaces from text data fields.
* **Warehouse Migration:** Automatically pushed the fully cleaned structured DataFrame into a local PostgreSQL database using an active SQLAlchemy engine.

### Phase 2: Relational Warehousing & Insights (SQL Analytics)
Once migrated into PostgreSQL (`hr_db`), custom database scripts were verified to build strategic staging queries for downstream reporting:
* **Seniority Classification:** Used `CASE WHEN` conditional mapping to categorize employees into career loyalty groups (`New Hire`, `Junior`, `Mid`, `Senior`) based on tenure.
* **Aggregated Performance Metrics:** Conducted multi-dimensional aggregations to analyze average and maximum salaries split by gender and department.

### Phase 3: Dashboard Visualization & DAX Development (Power BI)
A production-ready UI/UX interface was drafted in Power BI matching modern corporate design templates:
* **Interactive Navigation:** Implemented a clean, web-app style vertical **Page Navigator** panel equipped with dynamic state properties (`Default`, `Hover`, `Selected`) for a seamless layout experience.
* **Geographical Mapping:** Activated localized Bing Map features, transforming standard country text strings into geo-coded spatial variables to visualize headcount concentrations across Indonesian regions.
* **Key DAX Metrics:** Developed accurate calculations to avoid zero-division execution errors:
  ```dax
  Turnover Rate = 
  ROUND(
      (COUNT(CASE WHEN employee_status = 'Resigned' THEN 1 END)::NUMERIC / COUNT(employee_id)) * 100, 
      2
  )
  ```
  ```dax
  Avg Training Hours per Employee = 
  DIVIDE(
      SUM('hr'[training_hours_last_year]), 
      DISTINCTCOUNT('hr'[employee_id]), 
      0
  )
  ```

---

## 💡 Key Metric Insights From Dashboard
* **Workforce Population:** Manages a workforce of **5,000 Total Registered Employees** with a current operational capacity of **4,000 Active Staff**.
* **Organizational Attrition:** Tracks an overall corporate **Turnover/Turn over Rate of 11.66%**, enabling HR to cross-filter month-over-month resignation surges against specific departments.
* **Employee Well-being Score:** Highlights a stable corporate **Work Life-Balance index of 3.00/5**, signaling positive indicators for employee retention initiatives.

---

## 🚀 How To Clone and Run This Repository

1. **Clone the Portfolio Repository:**
   ```bash
   git clone https://github.com[Your-Username]/hr-analytics-dashboard.git
   cd hr-analytics-dashboard
   ```

2. **Execute Python ETL Pipeline:**
   Ensure PostgreSQL is running locally, then update your database credentials inside `etl_script.py` and run:
   ```bash
   pip install pandas sqlalchemy psycopg2 openpyxl
   python etl_script.py
   ```

3. **Explore Dashboard Visuals:**
   Open the `.pbix` template file directly inside **Power BI Desktop** to check the interactive slicers and data model linkages.
