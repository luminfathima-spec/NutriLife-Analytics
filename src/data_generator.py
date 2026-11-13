"""
Data Generation Script for Young Adults Food Habits & Lifestyle Pattern Survey
Target: 850 authentic responses across Undergraduates, Postgraduates, and Young Professionals.
Simulates realistic sociodemographic factors, dietary patterns, sleep metrics, and physiological indicators.
Includes realistic noise, casing inconsistencies, duplicate responses, and missing values
for thorough preprocessing demonstration.
"""

import numpy as np
import pandas as pd
import random

np.random.seed(42)
random.seed(42)

N = 850

# Demographic distributions
occupations = np.random.choice(
    ['Undergraduate Student', 'Postgraduate Student', 'Working Professional', 'Freelancer / Job Seeker'],
    size=N,
    p=[0.45, 0.25, 0.22, 0.08]
)

genders = np.random.choice(
    ['Male', 'Female', 'Non-binary / Other'],
    size=N,
    p=[0.51, 0.46, 0.03]
)

ages = []
for occ in occupations:
    if occ == 'Undergraduate Student':
        ages.append(np.random.randint(18, 22))
    elif occ == 'Postgraduate Student':
        ages.append(np.random.randint(21, 25))
    elif occ == 'Working Professional':
        ages.append(np.random.randint(22, 27))
    else:
        ages.append(np.random.randint(20, 26))
ages = np.array(ages)

living_options = ['Hostel / Dormitory', 'Shared Apartment', 'With Parents / Family', 'Living Independently']
living_arrangements = []
for occ in occupations:
    if occ in ['Undergraduate Student', 'Postgraduate Student']:
        living_arrangements.append(np.random.choice(living_options, p=[0.48, 0.27, 0.20, 0.05]))
    else:
        living_arrangements.append(np.random.choice(living_options, p=[0.10, 0.40, 0.35, 0.15]))

# Food & Lifestyle variables with realistic correlations
fast_food_freq = []
cooking_freq = []
skips_breakfast = []
monthly_budget = []
screen_time = []
sleep_hours = []
exercise_hours = []
stress_level = []
water_liters = []
fruit_veg_servings = []
caffeine_cups = []
sugar_cravings = []
bmi_values = []
energy_ratings = []
barriers = []

barrier_options = [
    'Lack of Time / Academic Load',
    'Budget Constraints',
    'Lack of Cooking Skills / Equipment',
    'Food Delivery Apps Accessibility',
    'Irregular Work / Study Hours',
    'None (Satisfied with Diet)'
]

for i in range(N):
    occ = occupations[i]
    living = living_arrangements[i]
    age = ages[i]
    
    # Stress calculation
    base_stress = 5.0
    if occ in ['Postgraduate Student', 'Working Professional']:
        base_stress += np.random.uniform(0.5, 2.0)
    if living in ['Hostel / Dormitory', 'Shared Apartment']:
        base_stress += np.random.uniform(0.2, 1.2)
    stress = np.clip(np.random.normal(base_stress, 1.8), 1, 10)
    stress_level.append(round(stress, 1))
    
    # Screen time (hours/day)
    base_screen = 6.5
    if stress > 6.5:
        base_screen += 1.5
    if occ in ['Undergraduate Student', 'Postgraduate Student']:
        base_screen += np.random.uniform(0.5, 2.5)
    screen = np.clip(np.random.normal(base_screen, 2.0), 3.0, 14.5)
    screen_time.append(round(screen, 1))
    
    # Sleep hours (strongly influenced negatively by screen time & stress)
    base_sleep = 8.0 - (screen * 0.18) - (stress * 0.22)
    sleep = np.clip(np.random.normal(base_sleep + np.random.uniform(-0.5, 0.5), 1.1), 3.5, 10.0)
    sleep_hours.append(round(sleep, 1))
    
    # Cooking frequency (days/week) & Fast food frequency
    if living == 'With Parents / Family':
        cook = np.random.choice([4, 5, 6, 7], p=[0.1, 0.2, 0.4, 0.3])
        ff = np.random.choice([0, 1, 2, 3], p=[0.35, 0.40, 0.20, 0.05])
    elif living in ['Hostel / Dormitory']:
        cook = np.random.choice([0, 1, 2], p=[0.75, 0.20, 0.05])
        ff = np.random.choice([2, 3, 4, 5, 6, 7], p=[0.15, 0.25, 0.30, 0.18, 0.08, 0.04])
    else:
        cook = np.random.choice([1, 2, 3, 4, 5], p=[0.20, 0.25, 0.30, 0.15, 0.10])
        ff = np.random.choice([1, 2, 3, 4, 5], p=[0.20, 0.30, 0.25, 0.15, 0.10])
        
    cooking_freq.append(int(cook))
    fast_food_freq.append(int(ff))
    
    # Breakfast habit (Yes = Skips Breakfast, No = Eats Breakfast Regularly)
    if sleep < 6.0 or screen > 8.0:
        bf = np.random.choice(['Yes', 'No', 'Occasionally'], p=[0.55, 0.18, 0.27])
    else:
        bf = np.random.choice(['Yes', 'No', 'Occasionally'], p=[0.18, 0.58, 0.24])
    skips_breakfast.append(bf)
    
    # Exercise hours per week
    base_ex = 4.0 - (stress * 0.25)
    if occ == 'Postgraduate Student':
        base_ex -= 0.8
    ex = max(0.0, np.random.normal(base_ex, 2.2))
    exercise_hours.append(round(min(ex, 14.0), 1))
    
    # Water intake (liters)
    water = np.clip(np.random.normal(2.2 + (0.15 * ex), 0.65), 0.8, 4.5)
    water_liters.append(round(water, 1))
    
    # Fruits & Vegetables (servings/day)
    if living == 'With Parents / Family':
        fv = np.random.choice([2, 3, 4, 5], p=[0.2, 0.4, 0.3, 0.1])
    else:
        fv = np.random.choice([0, 1, 2, 3], p=[0.3, 0.4, 0.25, 0.05])
    fruit_veg_servings.append(int(fv))
    
    # Caffeine intake (cups/day)
    caff_base = 1.0 + (stress * 0.25) + (1.0 if sleep < 6.0 else 0)
    caff = np.clip(np.random.normal(caff_base, 1.0), 0, 6)
    caffeine_cups.append(round(caff, 0))
    
    # Sugar craving (1-5)
    sugar = np.clip(int(np.round(2.0 + (stress * 0.2) + (1.2 if ff >= 4 else 0) + np.random.normal(0, 0.8))), 1, 5)
    sugar_cravings.append(sugar)
    
    # Monthly food expenditure (INR)
    if occ == 'Working Professional':
        budget = np.random.normal(8500, 2200)
    elif occ in ['Postgraduate Student']:
        budget = np.random.normal(5200, 1400)
    else:
        budget = np.random.normal(4200, 1200)
    monthly_budget.append(round(max(1500, budget), 0))
    
    # BMI calculation (correlated with fast food, exercise, sleep)
    base_bmi = 21.5 + (ff * 0.65) - (ex * 0.35) + ((8.0 - sleep) * 0.3)
    bmi = np.clip(np.random.normal(base_bmi, 3.2), 16.2, 36.5)
    bmi_values.append(round(bmi, 1))
    
    # Daily Energy Level Rating (1-10)
    energy = 8.5 - (stress * 0.35) + (sleep * 0.35) + (ex * 0.2) - (ff * 0.25)
    if bf == 'Yes':
        energy -= 1.5
    elif bf == 'Occasionally':
        energy -= 0.6
    energy = np.clip(np.random.normal(energy, 1.2), 1.0, 10.0)
    energy_ratings.append(round(energy, 1))
    
    # Barrier selection
    if occ in ['Undergraduate Student', 'Postgraduate Student']:
        barriers.append(np.random.choice(barrier_options, p=[0.42, 0.24, 0.16, 0.10, 0.05, 0.03]))
    else:
        barriers.append(np.random.choice(barrier_options, p=[0.35, 0.10, 0.12, 0.25, 0.12, 0.06]))

# Create DataFrame
df = pd.DataFrame({
    'Respondent_ID': [f'YA{i+1:04d}' for i in range(N)],
    'Age': ages,
    'Gender': genders,
    'Occupation_Status': occupations,
    'Living_Arrangement': living_arrangements,
    'Monthly_Food_Budget_INR': monthly_budget,
    'Cooking_Frequency_Per_Week': cooking_freq,
    'Fast_Food_Frequency_Per_Week': fast_food_freq,
    'Skips_Breakfast': skips_breakfast,
    'Daily_Water_Intake_Liters': water_liters,
    'Fruit_Veg_Servings_Per_Day': fruit_veg_servings,
    'Caffeine_Cups_Per_Day': caffeine_cups,
    'Sugar_Craving_Level': sugar_cravings,
    'Sleep_Hours_Per_Night': sleep_hours,
    'Screen_Time_Hours_Per_Day': screen_time,
    'Exercise_Hours_Per_Week': exercise_hours,
    'Perceived_Stress_Level': stress_level,
    'Daily_Energy_Rating': energy_ratings,
    'BMI': bmi_values,
    'Primary_Barrier_To_Healthy_Eating': barriers
})

# Introduce real-world anomalies for testing & demonstration of Preprocessing:
# 1. Casing / Whitespace variations
casing_gender = ['Male', 'male', 'MALE', 'Female', 'female', 'FEMALE']
for idx in np.random.choice(N, size=40, replace=False):
    g_curr = df.at[idx, 'Gender']
    if g_curr == 'Male':
        df.at[idx, 'Gender'] = random.choice(['male', 'MALE', ' Male '])
    elif g_curr == 'Female':
        df.at[idx, 'Gender'] = random.choice(['female', 'FEMALE', ' Female '])

for idx in np.random.choice(N, size=30, replace=False):
    df.at[idx, 'Living_Arrangement'] = ' ' + df.at[idx, 'Living_Arrangement'] + ' '

# 2. Missing values (~2-4%)
for col, count in [('Monthly_Food_Budget_INR', 22), 
                   ('Exercise_Hours_Per_Week', 18), 
                   ('Caffeine_Cups_Per_Day', 15), 
                   ('Daily_Water_Intake_Liters', 12)]:
    null_indices = np.random.choice(N, size=count, replace=False)
    df.loc[null_indices, col] = np.nan

# 3. Duplicate survey entries (simulate multiple student submissions)
dup_rows = df.iloc[np.random.choice(N, size=14, replace=False)].copy()
df = pd.concat([df, dup_rows], ignore_index=True)

# Save raw dataset
output_path = "C:/Users/lumin/.gemini/antigravity/scratch/food_lifestyle_data_story_project/data/raw_survey_data.csv"
df.to_csv(output_path, index=False)
print(f"Successfully generated raw survey dataset with {len(df)} records at {output_path}")
