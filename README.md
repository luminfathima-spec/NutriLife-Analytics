# NutriLife: Analysing Food Habits and Lifestyle Patterns Among Young Adults
### Master of Computer Applications (MCA) Final Project - Data Analysis & Storytelling

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red.svg)](https://streamlit.io/)
[![Unit Tests](https://img.shields.io/badge/Unit%20Tests-12%2F12%20Passed-brightgreen.svg)]()
[![Black Box Tests](https://img.shields.io/badge/Black%20Box%20Tests-25%2F25%20Passed-brightgreen.svg)]()

---

## 📌 Project Overview
This project fulfills all requirements specified in the Data Analysis & Storytelling curriculum for the topic:
**"Analysing Food Habits and Lifestyle Pattern Among Young Adults"**.

It investigates the interconnected relationships between:
- Dietary habits (home cooking vs. fast food dependency)
- Circadian disruption (recreational screen time vs. sleep deprivation)
- Nutritional anchoring (breakfast skipping vs. daytime vitality)
- Physiological outcomes (BMI, stress levels, and composite health risk score)

---

## 📁 Repository Directory Structure

```
food_lifestyle_data_story_project/
├── data/
│   ├── raw_survey_data.csv                 # Raw multi-institution survey data (N=850 + duplicates/nulls)
│   ├── cleaned_food_lifestyle_data.csv     # Cleaned, imputed, feature-engineered dataset
│   └── eda_summary.json                    # Summary descriptive statistics and hypothesis test results
├── src/
│   ├── data_generator.py                   # Data generator script for realistic survey cohort
│   ├── preprocessing.py                    # Data cleaning, deduplication, imputation, feature engineering
│   ├── eda.py                              # Statistical evaluation & hypothesis tests (ANOVA, t-test, Chi-square)
│   └── visualizations.py                   # Publication-ready Matplotlib/Seaborn visualization pipeline
├── figures/                                # 7 Saved publication charts (300 DPI)
│   ├── 01_dietary_patterns_by_living_arrangement.png
│   ├── 02_fast_food_vs_stress_and_cravings.png
│   ├── 03_screen_time_vs_sleep_duration.png
│   ├── 04_bmi_distribution_by_fast_food_tier.png
│   ├── 05_correlation_heatmap_lifestyle_metrics.png
│   ├── 06_energy_vitality_vs_breakfast_habit.png
│   └── 07_primary_barriers_to_healthy_eating.png
├── app.py                                  # Full-featured interactive Streamlit Dashboard
├── presentation/
│   ├── generate_presentation.py            # Automated PowerPoint generator (python-pptx)
│   └── Food_Habits_Lifestyle_Young_Adults_Presentation.pptx # 12-slide PowerPoint presentation
├── tests/
│   ├── test_preprocessing.py               # Unit tests for preprocessing & imputation
│   ├── test_eda.py                         # Unit tests for statistical hypothesis tests
│   └── test_dashboard_logic.py             # Unit tests for dashboard filters & simulation formulas
├── black_box_testing/
│   ├── black_box_test_plan.md              # SQA Black Box Test Specification document
│   ├── test_cases_matrix.csv               # 25 Tabular black box test cases
│   ├── run_black_box_tests.py              # Automated black box test execution script
│   └── black_box_test_report.md            # Generated execution report (100% pass)
├── Final_Project_Report.md                 # Complete MCA Academic Project Documentation
└── README.md                               # Project execution instructions
```

---

## 🚀 How to Run the Project

### 1. Launch the Interactive Streamlit Dashboard
To run the live interactive dashboard:
```powershell
streamlit run app.py
```
This opens the dashboard in your default browser (typically at `http://localhost:8501`), featuring:
- Live KPI Metrics and Demographic breakdown
- Dietary Dynamics & Fast Food Analysis
- Sleep & Screen Time Linear Regression
- Statistical Hypothesis Testing Cards
- The Scrollytelling Data Story Narrative
- What-If Personal Lifestyle Risk Simulator & Gauge
- Data Explorer with CSV Export

### 2. Run the Automated Unit Tests
To run the full unit test suite:
```powershell
pytest tests -v
```
*(All 12 unit tests pass).*

### 3. Run the Automated Black Box Testing Suite
To execute the comprehensive black box test harness:
```powershell
python black_box_testing/run_black_box_tests.py
```
*(All 25 test cases across Equivalence Partitioning, Boundary Value Analysis, Multi-filters, and File Integrity pass with 100% compliance).*

### 4. Regenerate Figures and Presentation (Optional)
```powershell
# Rebuild the dataset and execute data pipelines
python src/preprocessing.py
python src/eda.py
python src/visualizations.py
python presentation/generate_presentation.py
```

---

## 📊 Summary of 12 Academic Deliverables

| Deliverable | Location in Repository |
| :--- | :--- |
| **1. Project Title & Problem Statement** | `Final_Project_Report.md` (Sec 2) & Presentation Slide 2 |
| **2. Project Objectives** | `Final_Project_Report.md` (Sec 3) & Presentation Slide 3 |
| **3. Real-World Dataset** | `data/raw_survey_data.csv` (850 youth survey responses) |
| **4. Data Preprocessing** | `src/preprocessing.py` (Deduplication, imputation, feature engineering) |
| **5. Exploratory Data Analysis (EDA)** | `src/eda.py` (ANOVA, Pearson $r$, Welch's $t$, Chi-square) |
| **6. Data Visualizations** | `figures/` (7 publication charts) & Streamlit Plotly charts |
| **7. Key Insights** | `Final_Project_Report.md` (Sec 8) & Presentation Slide 8 |
| **8. Interactive Dashboard** | `app.py` (Streamlit 7-tab application) |
| **9. Data Story** | `Final_Project_Report.md` (Sec 9) & Tab 5 in Dashboard |
| **10. Recommendations** | `Final_Project_Report.md` (Sec 10) & Presentation Slide 10 |
| **11. Final Project Report** | `Final_Project_Report.md` (Comprehensive academic report) |
| **12. Final Presentation** | `presentation/Food_Habits_Lifestyle_Young_Adults_Presentation.pptx` |

