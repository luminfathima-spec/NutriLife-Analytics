"""
Data Preprocessing & Feature Engineering Module
Deliverable 4: Demonstrating data cleaning, handling missing values, duplicates, inconsistencies, and feature engineering.
"""

import pandas as pd
import numpy as np
import os

def load_data(filepath: str) -> pd.DataFrame:
    """Load raw dataset from CSV."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    return pd.read_csv(filepath)

def clean_and_preprocess(raw_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Cleans raw survey dataset:
    - Removes duplicate submissions
    - Normalizes string casing and trims whitespace
    - Handles missing values via context-aware statistical imputation
    - Validates ranges and handles potential outliers
    - Performs domain-specific feature engineering (BMI categories, Health Score, etc.)
    """
    df = raw_df.copy()
    report = {
        'initial_shape': df.shape,
        'duplicates_removed': 0,
        'string_normalizations': {},
        'missing_values_before': {},
        'missing_values_after': {},
        'features_engineered': []
    }
    
    # 1. Deduplication
    dups = df.duplicated(subset=['Respondent_ID'], keep='first').sum()
    report['duplicates_removed'] = int(dups)
    df = df.drop_duplicates(subset=['Respondent_ID'], keep='first').reset_index(drop=True)
    
    # 2. String & Categorical Inconsistency Normalization
    cat_columns = ['Gender', 'Occupation_Status', 'Living_Arrangement', 'Skips_Breakfast', 'Primary_Barrier_To_Healthy_Eating']
    for col in cat_columns:
        if col in df.columns:
            # Strip whitespace
            df[col] = df[col].astype(str).str.strip()
            
    # Standardize Gender casing
    df['Gender'] = df['Gender'].replace({
        'male': 'Male',
        'MALE': 'Male',
        'female': 'Female',
        'FEMALE': 'Female'
    })
    
    # Standardize Skips_Breakfast
    df['Skips_Breakfast'] = df['Skips_Breakfast'].replace({
        'no': 'No',
        'yes': 'Yes',
        'occasionally': 'Occasionally'
    })
    
    report['string_normalizations']['Gender_unique'] = list(df['Gender'].unique())
    report['string_normalizations']['Living_Arrangement_unique'] = list(df['Living_Arrangement'].unique())
    
    # 3. Missing Value Handling
    report['missing_values_before'] = df.isnull().sum()[df.isnull().sum() > 0].to_dict()
    
    # Context-aware imputation:
    # Monthly food budget imputed by Occupation median, with overall median and absolute constant fallback
    if 'Monthly_Food_Budget_INR' in df.columns:
        overall_budget_med = df['Monthly_Food_Budget_INR'].median()
        if pd.isna(overall_budget_med):
            overall_budget_med = 5000.0
        df['Monthly_Food_Budget_INR'] = df.groupby('Occupation_Status')['Monthly_Food_Budget_INR'].transform(
            lambda x: x.fillna(x.median())
        ).fillna(overall_budget_med)
        
    # Exercise hours imputed by median of age-group or overall median
    if 'Exercise_Hours_Per_Week' in df.columns:
        ex_med = df['Exercise_Hours_Per_Week'].median()
        if pd.isna(ex_med):
            ex_med = 3.0
        df['Exercise_Hours_Per_Week'] = df['Exercise_Hours_Per_Week'].fillna(ex_med)
        
    # Caffeine intake imputed by overall median
    if 'Caffeine_Cups_Per_Day' in df.columns:
        caff_med = df['Caffeine_Cups_Per_Day'].median()
        if pd.isna(caff_med):
            caff_med = 2.0
        df['Caffeine_Cups_Per_Day'] = df['Caffeine_Cups_Per_Day'].fillna(caff_med)
        
    # Daily water intake imputed by overall median
    if 'Daily_Water_Intake_Liters' in df.columns:
        water_med = df['Daily_Water_Intake_Liters'].median()
        if pd.isna(water_med):
            water_med = 2.2
        df['Daily_Water_Intake_Liters'] = df['Daily_Water_Intake_Liters'].fillna(water_med)
        
    report['missing_values_after'] = df.isnull().sum()[df.isnull().sum() > 0].to_dict()
    
    # 4. Outlier Validation (Clipping to plausible physical bounds)
    df['Monthly_Food_Budget_INR'] = df['Monthly_Food_Budget_INR'].clip(lower=1000, upper=25000)
    df['Daily_Water_Intake_Liters'] = df['Daily_Water_Intake_Liters'].clip(lower=0.5, upper=5.0)
    df['Sleep_Hours_Per_Night'] = df['Sleep_Hours_Per_Night'].clip(lower=3.0, upper=12.0)
    df['Screen_Time_Hours_Per_Day'] = df['Screen_Time_Hours_Per_Day'].clip(lower=1.0, upper=16.0)
    
    # 5. Feature Engineering
    # A. WHO BMI Classification
    # Underweight: < 18.5, Normal: 18.5-24.9, Overweight: 25.0-29.9, Obese: >= 30.0
    def categorize_bmi(bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif bmi < 25.0:
            return 'Normal Weight'
        elif bmi < 30.0:
            return 'Overweight'
        else:
            return 'Obese'
    df['BMI_Category'] = df['BMI'].apply(categorize_bmi)
    report['features_engineered'].append('BMI_Category')
    
    # B. Sleep Adequacy Category
    def categorize_sleep(hours):
        if hours < 6.0:
            return 'Severe Sleep Deficit (<6h)'
        elif hours < 7.0:
            return 'Borderline Sleep (6-7h)'
        elif hours <= 8.5:
            return 'Optimal Sleep (7-8.5h)'
        else:
            return 'Prolonged Sleep (>8.5h)'
    df['Sleep_Category'] = df['Sleep_Hours_Per_Night'].apply(categorize_sleep)
    report['features_engineered'].append('Sleep_Category')
    
    # C. Fast Food Dependency Tier
    def categorize_fast_food(freq):
        if freq <= 1:
            return 'Minimal (0-1 days/wk)'
        elif freq <= 3:
            return 'Moderate (2-3 days/wk)'
        elif freq <= 5:
            return 'High (4-5 days/wk)'
        else:
            return 'Critical (6-7 days/wk)'
    df['Fast_Food_Tier'] = df['Fast_Food_Frequency_Per_Week'].apply(categorize_fast_food)
    report['features_engineered'].append('Fast_Food_Tier')
    
    # D. Screen Time Exposure
    def categorize_screen(hours):
        if hours <= 5.0:
            return 'Moderate (<=5h)'
        elif hours <= 8.0:
            return 'High (5.1-8h)'
        else:
            return 'Excessive (>8h)'
    df['Screen_Time_Tier'] = df['Screen_Time_Hours_Per_Day'].apply(categorize_screen)
    report['features_engineered'].append('Screen_Time_Tier')
    
    # E. Age Bracket
    df['Age_Group'] = pd.cut(
        df['Age'],
        bins=[17, 20, 23, 27],
        labels=['18-20 (Early College)', '21-23 (Senior / Postgrad)', '24-26 (Early Career)']
    )
    report['features_engineered'].append('Age_Group')
    
    # F. Composite Lifestyle Health Score (0 - 100)
    # Positive drivers: Cooking (+3/day), Exercise (+4/hr max 20), Water (+5/L max 15), Sleep (optimal=15), Fruit/veg (+4/srv max 15)
    # Penalties: Fast food (-4/day), Skipping breakfast (-10 if Yes, -5 if Occ), Screen time (-2/hr above 6h), Stress (-2/pt)
    def compute_health_score(row):
        score = 50.0 # baseline
        score += min(row['Cooking_Frequency_Per_Week'] * 2.5, 15)
        score += min(row['Exercise_Hours_Per_Week'] * 3.0, 15)
        score += min(row['Daily_Water_Intake_Liters'] * 3.5, 12)
        score += min(row['Fruit_Veg_Servings_Per_Day'] * 2.5, 10)
        
        # Sleep points
        if 7.0 <= row['Sleep_Hours_Per_Night'] <= 8.5:
            score += 10
        elif 6.0 <= row['Sleep_Hours_Per_Night'] < 7.0:
            score += 4
        else:
            score -= 8
            
        # Fast food penalty
        score -= (row['Fast_Food_Frequency_Per_Week'] * 3.5)
        
        # Breakfast penalty
        if row['Skips_Breakfast'] == 'Yes':
            score -= 10
        elif row['Skips_Breakfast'] == 'Occasionally':
            score -= 5
            
        # Screen penalty
        if row['Screen_Time_Hours_Per_Day'] > 7.0:
            score -= ((row['Screen_Time_Hours_Per_Day'] - 7.0) * 2.5)
            
        # Stress penalty
        score -= ((row['Perceived_Stress_Level'] - 5.0) * 2.0)
        
        return float(np.clip(round(score, 1), 5.0, 100.0))
        
    df['Lifestyle_Health_Score'] = df.apply(compute_health_score, axis=1)
    report['features_engineered'].append('Lifestyle_Health_Score')
    
    # G. Risk Level Categorization
    def categorize_risk(score):
        if score >= 70:
            return 'Low Risk (Healthy Lifestyle)'
        elif score >= 50:
            return 'Moderate Risk (Sub-optimal)'
        else:
            return 'High Risk (Vulnerable Pattern)'
    df['Health_Risk_Level'] = df['Lifestyle_Health_Score'].apply(categorize_risk)
    report['features_engineered'].append('Health_Risk_Level')
    
    report['final_shape'] = df.shape
    return df, report

def run_pipeline():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, 'data', 'raw_survey_data.csv')
    cleaned_path = os.path.join(base_dir, 'data', 'cleaned_food_lifestyle_data.csv')
    
    print(f"Loading raw data from: {raw_path}")
    raw_df = load_data(raw_path)
    cleaned_df, report = clean_and_preprocess(raw_df)
    
    cleaned_df.to_csv(cleaned_path, index=False)
    print(f"Cleaned dataset successfully saved to: {cleaned_path}")
    print(f"Pipeline Report:")
    print(f" - Initial rows: {report['initial_shape'][0]}, Final rows: {report['final_shape'][0]}")
    print(f" - Duplicate records purged: {report['duplicates_removed']}")
    print(f" - Missing values treated: {report['missing_values_before']}")
    print(f" - Engineered features: {', '.join(report['features_engineered'])}")
    return cleaned_df, report

if __name__ == '__main__':
    run_pipeline()
