# 📊 Workforce Insights BI: End-to-End HR Analytics & Talent Pipeline

An end-to-end People Analytics project built to transform raw, unstandardized workforce data into actionable HR insights. This project covers the entire data pipeline: **Data Cleaning & Engineering (Python)**, **Data Relational Warehousing (PostgreSQL)**, and **Interactive Multi-Page Reporting (Power BI)**.

---

## 🎯 Business Goals & Objectives
This dashboard is engineered to help HR Executives and Leadership Teams make **data-driven human capital decisions** by evaluating organizational health across three critical pillars:

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
* **Data Standardization:** Standardized schema structures by lower-casing features, replacing blank spaces with underscores (`_`), and stripping accidental ghost-spaces from text data fields.
* **Warehouse Migration:** Automatically pushed the fully cleaned structured DataFrame into a local PostgreSQL database using an active SQLAlchemy engine.

### Phase 2: Relational Warehousing & Insights (SQL Analytics)
Once migrated into PostgreSQL (`hr_db`), custom database scripts were verified to build strategic staging queries for downstream reporting:
* **Seniority Classification:** Used `CASE WHEN` conditional mapping to categorize employees into career loyalty groups (`New Hire`, `Junior`, `Mid`, `Senior`) based on tenure.
* **Aggregated Performance Metrics:** Conducted multi-dimensional aggregations to analyze average and maximum salaries split by gender and department.

### Phase 3: Dashboard Visualization & DAX Development (Power BI)
A production-ready UI/UX interface was drafted in Power BI matching modern corporate design templates:
* **Interactive Navigation:** Implemented a clean, web-app style vertical **Page Navigator** panel equipped with dynamic state properties (`Default`, `Hover`, `Selected`) for a seamless layout experience.
* **Geographical Mapping:** Activated geo-coded spatial variables using localized map visuals to visualize headcount concentrations across regions.
* **Key DAX Metrics:** Developed accurate calculations to avoid zero-division execution errors:
  ```dax
  Turnover Rate = 
  DIVIDE(
      CALCULATE(DISTINCTCOUNT(hr[employee_id]), hr[employee_status] = "Resigned"),
      DISTINCTCOUNT(hr[employee_id]),
      0
  )
  ```
  ```dax
  Avg Training Hours per Employee = 
  DIVIDE(
      SUM(hr[training_hours_last_year]), 
      DISTINCTCOUNT(hr[employee_id]), 
      0
  )
  ```

---

## 📊 Interactive Dashboard Previews & Features

### 1. Workforce Executive Summary (Page 1 - Overview)
*Strategic macro insights tracking overall workforce demographics, job levels, diversity, and operational capacity across operational regions. It captures the baseline of 5,000 total registered employees, 4,000 active staff, and a global 11.66% turnover rate.*

#### Default Macro View
![Workforce Overview Dashboard - Default](dashboard_page1_default.png)

#### Dynamic Slicing & Scenario Analysis
*Demonstrates cross-filtering power. Slicing by Marital Status: Divorced + Gender: Male + Region: Jabodetabek + Performance: Exceeds Expectations instantly narrows the data down to 13 specific employees, revealing a localized turnover spike of 15.38%.*
![Workforce Overview Dashboard - Filtered](dashboard_page1_filtered.png)

---

### 2. Attrition & Employee Turnover Analysis (Page 2)
*Deep-dive evaluation of month-over-month resignation trends, organizational turnover velocity, and matrix-based heatmaps to isolate retention risk zones by department and specific roles.*

#### Default Analytics View
![Attrition Analytics Dashboard - Default](dashboard_page2_default.png)

#### Hierarchy Cross-Filtering Control
*HR can dynamically explore department hierarchies and specific role selections inside the slicer panels to instantly see targeted termination reasons and line graphs.*
![Attrition Analytics Dashboard - Slicer](dashboard_page2_filtered.png)

---

### 3. Talent Development & Performance Tracking (Page 3)
*Correlating continuous training investments against employee internal promotion counts and organizational performance distributions to track competency development.*

#### Default Talent Insights View
![Talent Development Dashboard - Default](dashboard_page3_default.png)

#### Full-Time Workforce Competency Scenario
*Filtering specifically by Full-time employees dynamically recalibrates total training hours and filters the granular dataset table log in real-time.*
![Talent Development Dashboard - Filtered](dashboard_page3_filtered.png)

---

### 4. Tabular Data Log Audit (Page 4 - Operational View)
*A detailed granular matrix view engineered for HR operations, allowing row-by-row internal cross-checking, hire date validation, and clean historical log auditing.*
![Table Data Dashboard](dashboard_page4.png)

---

## 🚀 How To Clone and Run This Repository

1. **Clone the Portfolio Repository:**
   ```bash
   git clone https://github.com/muhammadrizkiadzani/workforce-insights-bi.git
   cd workforce-insights-bi
   ```

2. **Execute Python ETL Pipeline:**
   Ensure PostgreSQL is running locally, then update your database credentials inside `etl_script.py` and run:
   ```bash
   pip install pandas sqlalchemy psycopg2 openpyxl
   python etl_script.py
   ```

3. **Explore Dashboard Visuals:**
   Open the file inside the `/dashboard` directory directly using **Power BI Desktop** to explore the interactive elements and relational model structures.
