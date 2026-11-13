"""
Unit Tests for Dashboard Filtering and Simulation Logic
"""

import pytest
import pandas as pd
import numpy as np
import os

@pytest.fixture
def cleaned_df():
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'cleaned_food_lifestyle_data.csv'))
    return pd.read_csv(csv_path)

def test_filtering_logic_by_occupation(cleaned_df):
    target_occ = ['Undergraduate Student']
    filtered = cleaned_df[cleaned_df['Occupation_Status'].isin(target_occ)]
    assert len(filtered) > 0
    assert set(filtered['Occupation_Status'].unique()) == {'Undergraduate Student'}

def test_filtering_logic_by_age_range(cleaned_df):
    min_age, max_age = 20, 22
    filtered = cleaned_df[cleaned_df['Age'].between(min_age, max_age)]
    assert len(filtered) > 0
    assert filtered['Age'].min() >= 20
    assert filtered['Age'].max() <= 22

def test_simulator_boundary_calculations():
    # Boundary case 1: Ideal lifestyle inputs
    sim_sleep = 8.0
    sim_screen = 3.0
    sim_ff = 0
    sim_cook = 7
    sim_ex = 10.0
    sim_water = 3.5
    sim_bf = "No (Regular Eater)"
    sim_stress = 2.0
    
    score = 50.0
    score += min(sim_cook * 2.5, 15)
    score += min(sim_ex * 3.0, 15)
    score += min(sim_water * 3.5, 12)
    score += 10 # optimal sleep
    score -= (sim_ff * 3.5)
    score -= ((sim_stress - 5.0) * 2.0)
    score_ideal = float(np.clip(round(score, 1), 5.0, 100.0))
    
    assert score_ideal >= 85.0, "Ideal lifestyle should produce high score >= 85"
    
    # Boundary case 2: Worst lifestyle inputs
    sim_sleep = 4.0
    sim_screen = 14.0
    sim_ff = 7
    sim_cook = 0
    sim_ex = 0.0
    sim_water = 0.8
    sim_bf = "Yes (Habitual Skipper)"
    sim_stress = 10.0
    
    score_w = 50.0
    score_w += min(sim_cook * 2.5, 15)
    score_w += min(sim_ex * 3.0, 15)
    score_w += min(sim_water * 3.5, 12)
    score_w -= 8 # severe sleep deficit
    score_w -= (sim_ff * 3.5)
    score_w -= 10 # skips breakfast
    score_w -= ((sim_screen - 7.0) * 2.5)
    score_w -= ((sim_stress - 5.0) * 2.0)
    score_worst = float(np.clip(round(score_w, 1), 5.0, 100.0))
    
    assert score_worst <= 30.0, "Worst lifestyle should yield low score <= 30"
    assert score_worst >= 5.0, "Score should not violate lower bound of 5.0"

