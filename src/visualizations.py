"""
Publication-Quality Visualization Generator
Deliverable 6: Minimum 5-7 meaningful charts using Matplotlib and Seaborn, saved to figures/.
"""

import os
import matplotlib
matplotlib.use('Agg') # Headless rendering
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set aesthetic styling
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

def generate_all_visualizations(df: pd.DataFrame, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    generated_files = []
    
    # -------------------------------------------------------------
    # Chart 1: Dietary Patterns across Living Arrangements
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 6))
    melted_diet = df.groupby('Living_Arrangement')[['Cooking_Frequency_Per_Week', 'Fast_Food_Frequency_Per_Week']].mean().reset_index()
    melted_diet = pd.melt(melted_diet, id_vars=['Living_Arrangement'], 
                          value_vars=['Cooking_Frequency_Per_Week', 'Fast_Food_Frequency_Per_Week'],
                          var_name='Dietary_Habit', value_name='Average_Days_Per_Week')
    melted_diet['Dietary_Habit'] = melted_diet['Dietary_Habit'].replace({
        'Cooking_Frequency_Per_Week': 'Home Cooking (Days/Wk)',
        'Fast_Food_Frequency_Per_Week': 'Fast Food Consumption (Days/Wk)'
    })
    
    palette = {'Home Cooking (Days/Wk)': '#2a9d8f', 'Fast Food Consumption (Days/Wk)': '#e76f51'}
    sns.barplot(data=melted_diet, x='Living_Arrangement', y='Average_Days_Per_Week', hue='Dietary_Habit', palette=palette, ax=ax)
    ax.set_title("1. Dietary Divergence: Cooking vs Fast Food by Living Arrangement", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Living Arrangement", fontsize=12, labelpad=10)
    ax.set_ylabel("Average Days per Week", fontsize=12, labelpad=10)
    ax.legend(title="", frameon=True)
    plt.xticks(rotation=15, ha='right')
    plt.tight_layout()
    p1 = os.path.join(output_dir, "01_dietary_patterns_by_living_arrangement.png")
    plt.savefig(p1, dpi=300)
    plt.close()
    generated_files.append(p1)

    # -------------------------------------------------------------
    # Chart 2: Fast Food vs Stress Levels & Cravings
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 6))
    df['Stress_Bracket'] = pd.cut(df['Perceived_Stress_Level'], bins=[0, 3.5, 6.5, 10], labels=['Low Stress (1-3)', 'Moderate Stress (4-6)', 'High Stress (7-10)'])
    sns.boxplot(data=df, x='Stress_Bracket', y='Fast_Food_Frequency_Per_Week', hue='Sugar_Craving_Level', palette='YlOrRd', ax=ax)
    ax.set_title("2. Stress-Induced Emotional Eating: Fast Food & Sugar Cravings", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Perceived Stress Level", fontsize=12, labelpad=10)
    ax.set_ylabel("Fast Food Frequency (Days/Week)", fontsize=12, labelpad=10)
    ax.legend(title="Sugar Craving (1=Low, 5=Severe)", frameon=True, loc='upper left')
    plt.tight_layout()
    p2 = os.path.join(output_dir, "02_fast_food_vs_stress_and_cravings.png")
    plt.savefig(p2, dpi=300)
    plt.close()
    generated_files.append(p2)

    # -------------------------------------------------------------
    # Chart 3: Screen Time vs Sleep Duration
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.regplot(data=df, x='Screen_Time_Hours_Per_Day', y='Sleep_Hours_Per_Night',
                scatter_kws={'alpha': 0.4, 'color': '#3a86ff'},
                line_kws={'color': '#d90429', 'linewidth': 2.5}, ax=ax)
    ax.axhline(7.0, color='green', linestyle='--', linewidth=1.5, label='Recommended Minimum Sleep (7h)')
    ax.set_title("3. The Blue-Light Effect: Daily Screen Time vs Sleep Duration", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Recreational Screen Time (Hours/Day)", fontsize=12, labelpad=10)
    ax.set_ylabel("Sleep Duration (Hours/Night)", fontsize=12, labelpad=10)
    ax.legend(frameon=True, loc='upper right')
    plt.tight_layout()
    p3 = os.path.join(output_dir, "03_screen_time_vs_sleep_duration.png")
    plt.savefig(p3, dpi=300)
    plt.close()
    generated_files.append(p3)

    # -------------------------------------------------------------
    # Chart 4: BMI Distribution by Exercise & Fast Food Tier
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(data=df, x='Fast_Food_Tier', y='BMI', hue='Fast_Food_Tier', palette='Blues', legend=False, inner='quartile', ax=ax)
    ax.axhline(25.0, color='#e63946', linestyle='--', label='Overweight Threshold (BMI >= 25)')
    ax.axhline(18.5, color='#f4a261', linestyle=':', label='Underweight Threshold (BMI < 18.5)')
    ax.set_title("4. Impact of Fast Food Dependency on Body Mass Index (BMI)", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Fast Food Dependency Level", fontsize=12, labelpad=10)
    ax.set_ylabel("BMI (kg/m²)", fontsize=12, labelpad=10)
    ax.legend(frameon=True, loc='upper left')
    plt.tight_layout()
    p4 = os.path.join(output_dir, "04_bmi_distribution_by_fast_food_tier.png")
    plt.savefig(p4, dpi=300)
    plt.close()
    generated_files.append(p4)

    # -------------------------------------------------------------
    # Chart 5: Correlation Heatmap of Lifestyle Metrics
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(11, 8))
    cols_corr = [
        'Screen_Time_Hours_Per_Day', 'Sleep_Hours_Per_Night', 'Fast_Food_Frequency_Per_Week',
        'Cooking_Frequency_Per_Week', 'Exercise_Hours_Per_Week', 'Daily_Water_Intake_Liters',
        'Perceived_Stress_Level', 'Daily_Energy_Rating', 'BMI', 'Lifestyle_Health_Score'
    ]
    corr = df[cols_corr].corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1,
                linewidths=0.5, cbar_kws={"shrink": .8}, ax=ax)
    ax.set_title("5. Comprehensive Correlation Matrix: Food, Lifestyle & Health Indicators", fontsize=14, fontweight='bold', pad=15)
    plt.xticks(rotation=30, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    p5 = os.path.join(output_dir, "05_correlation_heatmap_lifestyle_metrics.png")
    plt.savefig(p5, dpi=300)
    plt.close()
    generated_files.append(p5)

    # -------------------------------------------------------------
    # Chart 6: Energy Vitality vs Breakfast Habit across Age Groups
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 6))
    palette_bf = {'Yes': '#2a9d8f', 'Occasionally': '#e9c46a', 'No': '#e76f51'}
    sns.barplot(data=df, x='Age_Group', y='Daily_Energy_Rating', hue='Skips_Breakfast', palette=palette_bf, errorbar=('ci', 95), capsize=0.1, ax=ax)
    ax.set_title("6. Breakfast Habit vs Daily Energy Vitality Across Age Cohorts", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Age Cohort", fontsize=12, labelpad=10)
    ax.set_ylabel("Mean Daily Energy Rating (1-10)", fontsize=12, labelpad=10)
    ax.set_ylim(0, 10)
    ax.legend(title="Skips Breakfast", frameon=True)
    plt.tight_layout()
    p6 = os.path.join(output_dir, "06_energy_vitality_vs_breakfast_habit.png")
    plt.savefig(p6, dpi=300)
    plt.close()
    generated_files.append(p6)

    # -------------------------------------------------------------
    # Chart 7: Primary Barriers to Healthy Eating
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 6))
    barrier_counts = df['Primary_Barrier_To_Healthy_Eating'].value_counts()
    sns.barplot(x=barrier_counts.values, y=barrier_counts.index, hue=barrier_counts.index, palette='mako', legend=False, ax=ax)
    ax.set_title("7. Primary Barriers to Healthy Eating Among Young Adults", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Number of Respondents", fontsize=12, labelpad=10)
    ax.set_ylabel("Stated Barrier", fontsize=12, labelpad=10)
    for i, v in enumerate(barrier_counts.values):
        ax.text(v + 5, i, f"{v} ({round(v/len(df)*100, 1)}%)", va='center', fontweight='bold', color='#333333')
    plt.tight_layout()
    p7 = os.path.join(output_dir, "07_primary_barriers_to_healthy_eating.png")
    plt.savefig(p7, dpi=300)
    plt.close()
    generated_files.append(p7)

    print(f"Generated {len(generated_files)} publication-ready charts in: {output_dir}")
    return generated_files

def run_visualizations():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cleaned_path = os.path.join(base_dir, 'data', 'cleaned_food_lifestyle_data.csv')
    output_dir = os.path.join(base_dir, 'figures')
    
    df = pd.read_csv(cleaned_path)
    generate_all_visualizations(df, output_dir)

if __name__ == '__main__':
    run_visualizations()
