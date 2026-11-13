# Black Box Test Plan: Young Adults Food Habits & Lifestyle Analytics Dashboard

**Course / Degree:** Master of Computer Applications (MCA)  
**Subject:** Data Analysis & Software Quality Assurance  
**Project Topic:** Analysing Food Habits and Lifestyle Pattern Among Young Adults  
**System Under Test (SUT):** NutriLife Data Storytelling & Analytics Application  

---

## 1. Executive Summary & Purpose

The purpose of this Black Box Test Plan is to validate the functional, behavioral, boundary, and interface specifications of the **NutriLife** Data Analytics and Storytelling System from an end-user / evaluator perspective without access to internal source logic.

This testing verifies that:
1. The survey data cleaning pipeline correctly ingests, filters, and standardizes all records.
2. The interactive Streamlit dashboard accurately responds to multidimensional user filter actions.
3. The What-If Lifestyle Health Risk Simulator behaves reliably across extreme edge boundaries and valid input ranges.
4. Exploratory data charts and statistical test outputs match expected statistical distributions.
5. Search and CSV export functionality generates conformant, uncorrupted data deliverables.

---

## 2. Test Scope & Focus Areas

| Module / Area | Focus & Validation Criteria |
| :--- | :--- |
| **Data Ingestion & Integrity** | Deduplication, range validation, categorical consistency, missing value handling. |
| **Dynamic Dashboard Filtering** | Multi-select filters (Occupation, Living arrangement, Gender, Fast Food tier) and Age slider. |
| **KPI Metrics Accuracy** | Real-time calculation of cohort size, average sleep, screen time, fast-food days, and risk percentages. |
| **Interactive Visualizations** | Plotly charts rendering, tooltips, legends, and responsive scaling. |
| **Lifestyle Risk Calculator** | Input boundary conditions, composite score calculations (0-100), risk status tiering, BMI projection. |
| **Data Explorer & Search** | Keyword filtering across Respondent ID and Occupation; CSV download integrity. |
| **Cross-Browser & Usability** | Visual layout hierarchy, accessibility, and presentation clarity. |

---

## 3. Black Box Testing Methodologies Applied

### A. Equivalence Partitioning (EP)
Input domains are divided into valid and invalid equivalence classes:
- **Age Input:** 
  - Valid: [18 to 26] (Target Young Adults Cohort)
  - Invalid: [< 18] (Minors) or [> 26] (Older Adult cohorts)
- **Sleep Hours:**
  - Critical Deficit: `< 6.0 hrs`
  - Borderline: `6.0 - 6.9 hrs`
  - Recommended / Optimal: `7.0 - 8.5 hrs`
  - Extended: `> 8.5 hrs`
- **Fast Food Intake:**
  - Minimal: `0 - 1 days/week`
  - Moderate: `2 - 3 days/week`
  - High: `4 - 5 days/week`
  - Critical: `6 - 7 days/week`
- **Lifestyle Health Risk Score:**
  - Low Risk: `70.0 - 100.0`
  - Moderate Risk: `50.0 - 69.9`
  - High Risk: `0.0 - 49.9`

### B. Boundary Value Analysis (BVA)
Testing edge conditions and thresholds:
- Fast Food Days: `0` (min), `1`, `6`, `7` (max)
- Sleep Hours: `3.0` (min floor), `5.9` (boundary), `6.0`, `7.0`, `8.5`, `8.6`, `11.0` (max ceiling)
- Daily Screen Time: `1.0` (min), `7.0` (threshold), `15.0` (max)
- Daily Water Intake: `0.5L` (lower limit), `2.5L` (target), `5.0L` (upper limit)
- Stress Level: `1.0` (min), `5.0` (baseline), `10.0` (max)

### C. Decision Table Testing
Testing combinatorial conditions in the What-If Health Simulator:
- Case 1: High Screen (>8h) + Poor Sleep (<6h) + Heavy Fast Food (>=4) + High Stress (>=7) -> Expected: **High Risk (Score < 50)**.
- Case 2: Optimal Sleep (7.5h) + Low Screen (<5h) + High Cooking (5 days) + Daily Exercise (>=4h) -> Expected: **Low Risk (Score >= 70)**.

### D. Error Guessing & Robustness
- Selecting conflicting filter combinations (e.g., filter with no matching records) to verify graceful handling without crashes.
- Submitting empty or special-character search queries in the Data Explorer.

---

## 4. Test Environment

- **Operating System:** Microsoft Windows 11
- **Runtime Environment:** Python 3.13.3
- **Primary Frameworks:** Streamlit 1.67.0, Plotly 7.1.0, Pandas 3.1.1, SciPy 1.17.1
- **Execution Tool:** Automated Python Black Box Test Runner (`black_box_testing/run_black_box_tests.py`)

