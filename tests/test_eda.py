"""
Unit Tests for Exploratory Data Analysis & Statistical Testing
"""

import pytest
import pandas as pd
import numpy as np
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from eda import perform_eda

@pytest.fixture
def cleaned_dataset():
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'cleaned_food_lifestyle_data.csv'))
    assert os.path.exists(csv_path), "Cleaned dataset must exist for EDA test"
    return pd.read_csv(csv_path)

def test_descriptive_stats_presence(cleaned_dataset):
    results = perform_eda(cleaned_dataset)
    assert 'descriptive_statistics' in results
    stats = results['descriptive_statistics']
    assert 'BMI' in stats
    assert 'Sleep_Hours_Per_Night' in stats
    assert 'Fast_Food_Frequency_Per_Week' in stats
    assert stats['BMI']['mean'] > 15 and stats['BMI']['mean'] < 40

def test_prevalence_metrics(cleaned_dataset):
    results = perform_eda(cleaned_dataset)
    prev = results['prevalence']
    assert prev['total_respondents'] == 850
    assert 0 <= prev['skips_breakfast_pct'] <= 100
    assert 0 <= prev['sleep_deficit_pct'] <= 100

def test_hypothesis_testing_rigor(cleaned_dataset):
    results = perform_eda(cleaned_dataset)
    ht = results['hypothesis_tests']
    assert 'h1_living_vs_fast_food' in ht
    assert 'h2_screen_vs_sleep' in ht
    assert 'h3_breakfast_vs_energy' in ht
    assert 'h4_barrier_vs_risk' in ht
    
    # Statistical significance checks
    assert ht['h1_living_vs_fast_food']['p_value'] < 0.05
    assert ht['h2_screen_vs_sleep']['r_coefficient'] < 0 # Negative correlation
    assert ht['h3_breakfast_vs_energy']['group_1_mean_energy'] > ht['h3_breakfast_vs_energy']['group_2_mean_energy']

def test_key_insights_count(cleaned_dataset):
    results = perform_eda(cleaned_dataset)
    insights = results['key_insights']
    assert len(insights) >= 5, "Must provide minimum 5 key insights as per project requirements"

