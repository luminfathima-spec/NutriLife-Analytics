"""
Unit Tests for Data Preprocessing and Feature Engineering
"""

import pytest
import pandas as pd
import numpy as np
import os
import sys

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from preprocessing import clean_and_preprocess

@pytest.fixture
def sample_raw_data():
    return pd.DataFrame({
        'Respondent_ID': ['YA0001', 'YA0002', 'YA0002', 'YA0003'], # includes duplicate
        'Age': [19, 23, 23, 25],
        'Gender': ['male', ' FEMALE ', 'FEMALE', 'Male'], # mixed casing & spaces
        'Occupation_Status': ['Undergraduate Student', 'Postgraduate Student', 'Postgraduate Student', 'Working Professional'],
        'Living_Arrangement': [' Hostel ', 'Shared Apartment', 'Shared Apartment', 'With Parents / Family'],
        'Monthly_Food_Budget_INR': [4500.0, np.nan, np.nan, 8000.0], # missing value
        'Cooking_Frequency_Per_Week': [0, 3, 3, 6],
        'Fast_Food_Frequency_Per_Week': [5, 2, 2, 1],
        'Skips_Breakfast': ['yes', 'No', 'No', 'occasionally'],
        'Daily_Water_Intake_Liters': [1.8, 2.5, 2.5, np.nan], # missing value
        'Fruit_Veg_Servings_Per_Day': [1, 3, 3, 4],
        'Caffeine_Cups_Per_Day': [2.0, np.nan, np.nan, 1.0], # missing value
        'Sugar_Craving_Level': [4, 2, 2, 1],
        'Sleep_Hours_Per_Night': [5.5, 7.5, 7.5, 8.0],
        'Screen_Time_Hours_Per_Day': [9.0, 5.0, 5.0, 4.0],
        'Exercise_Hours_Per_Week': [np.nan, 4.0, 4.0, 6.0], # missing value
        'Perceived_Stress_Level': [8.0, 4.0, 4.0, 3.0],
        'Daily_Energy_Rating': [4.5, 8.0, 8.0, 8.5],
        'BMI': [27.5, 22.1, 22.1, 23.4],
        'Primary_Barrier_To_Healthy_Eating': ['Lack of Time', 'Budget Constraints', 'Budget Constraints', 'None']
    })

def test_deduplication(sample_raw_data):
    cleaned_df, report = clean_and_preprocess(sample_raw_data)
    assert report['duplicates_removed'] == 1
    assert len(cleaned_df) == 3

def test_casing_and_whitespace_cleaning(sample_raw_data):
    cleaned_df, report = clean_and_preprocess(sample_raw_data)
    # Check normalized gender
    assert set(cleaned_df['Gender'].unique()).issubset({'Male', 'Female', 'Non-binary / Other'})
    # Check trimmed whitespace
    assert cleaned_df.loc[cleaned_df['Respondent_ID'] == 'YA0001', 'Living_Arrangement'].values[0] == 'Hostel'
    assert cleaned_df.loc[cleaned_df['Respondent_ID'] == 'YA0001', 'Skips_Breakfast'].values[0] == 'Yes'

def test_missing_value_imputation(sample_raw_data):
    cleaned_df, report = clean_and_preprocess(sample_raw_data)
    # No NaN values should remain
    assert cleaned_df.isnull().sum().sum() == 0
    assert cleaned_df['Monthly_Food_Budget_INR'].notnull().all()
    assert cleaned_df['Exercise_Hours_Per_Week'].notnull().all()

def test_feature_engineering_columns(sample_raw_data):
    cleaned_df, report = clean_and_preprocess(sample_raw_data)
    expected_features = [
        'BMI_Category', 'Sleep_Category', 'Fast_Food_Tier',
        'Screen_Time_Tier', 'Age_Group', 'Lifestyle_Health_Score', 'Health_Risk_Level'
    ]
    for feat in expected_features:
        assert feat in cleaned_df.columns

def test_health_score_range(sample_raw_data):
    cleaned_df, report = clean_and_preprocess(sample_raw_data)
    scores = cleaned_df['Lifestyle_Health_Score']
    assert (scores >= 0).all() and (scores <= 100).all()
    # High stress + high fast food + low sleep should score significantly lower
    low_profile_score = cleaned_df.loc[cleaned_df['Respondent_ID'] == 'YA0001', 'Lifestyle_Health_Score'].values[0]
    high_profile_score = cleaned_df.loc[cleaned_df['Respondent_ID'] == 'YA0003', 'Lifestyle_Health_Score'].values[0]
    assert low_profile_score < high_profile_score

