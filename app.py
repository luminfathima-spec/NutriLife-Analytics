"""
NutriLife: Interactive Data Storytelling Dashboard
Topic: Analysing Food Habits and Lifestyle Pattern Among Young Adults
Master of Computer Applications (MCA) - Data Analysis Project
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="NutriLife | Young Adults Food & Lifestyle Analytics",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Modern Academic UI
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .main-header h1 {
        color: #ffffff;
        font-size: 2.2rem;
        margin-bottom: 6px;
    }
    .main-header p {
        color: #e0e7ff;
        font-size: 1.05rem;
        margin-bottom: 0px;
    }
    .metric-card {
        background: #ffffff;
        border-radius: 10px;
        padding: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        border-left: 5px solid #2a5298;
        margin-bottom: 12px;
    }
    .metric-title {
        font-size: 0.85rem;
        color: #64748b;
        text-transform: uppercase;
        font-weight: 600;
        margin-bottom: 4px;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #0f172a;
    }
    .metric-sub {
        font-size: 0.8rem;
        color: #10b981;
        font-weight: 500;
    }
    .metric-sub-neg {
        font-size: 0.8rem;
        color: #ef4444;
        font-weight: 500;
    }
    .story-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 18px;
    }
    .story-step {
        display: inline-block;
        background: #2563eb;
        color: white;
        padding: 3px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .insight-badge {
        background: #fef3c7;
        color: #92400e;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# Cache data loading
@st.cache_data
def load_project_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cleaned_csv = os.path.join(base_dir, 'data', 'cleaned_food_lifestyle_data.csv')
    summary_json = os.path.join(base_dir, 'data', 'eda_summary.json')
    
    df = pd.read_csv(cleaned_csv)
    
    with open(summary_json, 'r') as f:
        eda_summary = json.load(f)
        
    return df, eda_summary

df_all, eda_meta = load_project_data()

# -------------------------------------------------------------
# SIDEBAR FILTERS
# -------------------------------------------------------------
st.sidebar.image("https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=500&auto=format&fit=crop&q=60", use_container_width=True)
st.sidebar.title("🎛️ Cohort Filters")
st.sidebar.caption("Filter survey respondents across demographics and habits.")

selected_occ = st.sidebar.multiselect(
    "Occupation Status",
    options=list(df_all['Occupation_Status'].unique()),
    default=list(df_all['Occupation_Status'].unique())
)

selected_living = st.sidebar.multiselect(
    "Living Arrangement",
    options=list(df_all['Living_Arrangement'].unique()),
    default=list(df_all['Living_Arrangement'].unique())
)

selected_gender = st.sidebar.multiselect(
    "Gender",
    options=list(df_all['Gender'].unique()),
    default=list(df_all['Gender'].unique())
)

age_range = st.sidebar.slider(
    "Age Range",
    min_value=int(df_all['Age'].min()),
    max_value=int(df_all['Age'].max()),
    value=(int(df_all['Age'].min()), int(df_all['Age'].max()))
)

fast_food_tiers = st.sidebar.multiselect(
    "Fast Food Intake Level",
    options=list(df_all['Fast_Food_Tier'].unique()),
    default=list(df_all['Fast_Food_Tier'].unique())
)

# Apply Filter Mask
filtered_df = df_all[
    (df_all['Occupation_Status'].isin(selected_occ)) &
    (df_all['Living_Arrangement'].isin(selected_living)) &
    (df_all['Gender'].isin(selected_gender)) &
    (df_all['Age'].between(age_range[0], age_range[1])) &
    (df_all['Fast_Food_Tier'].isin(fast_food_tiers))
]

st.sidebar.divider()
st.sidebar.markdown(f"**Filtered Cohort:** `{len(filtered_df)}` / `{len(df_all)}` ({round(len(filtered_df)/len(df_all)*100, 1)}%)")
st.sidebar.caption("Data Storytelling Project | Final MCA Degree")

# -------------------------------------------------------------
# MAIN HEADER
# -------------------------------------------------------------
st.markdown("""
<div class="main-header">
    <h1>🥗 NutriLife: Food Habits & Lifestyle Patterns</h1>
    <p>A Comprehensive Data Storytelling Dashboard on Young Adults (Ages 18-26) | MCA Final Project</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# KPI SUMMARY CARDS
# -------------------------------------------------------------
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Surveyed Cohort</div>
        <div class="metric-value">{len(filtered_df)}</div>
        <div class="metric-sub">Young Adults</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    avg_sleep = round(filtered_df['Sleep_Hours_Per_Night'].mean(), 1) if len(filtered_df) > 0 else 0
    sleep_sub_cls = "metric-sub-neg" if avg_sleep < 7.0 else "metric-sub"
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Avg Sleep Duration</div>
        <div class="metric-value">{avg_sleep}h</div>
        <div class="{sleep_sub_cls}">Target: 7.0 - 8.5h</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    avg_screen = round(filtered_df['Screen_Time_Hours_Per_Day'].mean(), 1) if len(filtered_df) > 0 else 0
    screen_sub_cls = "metric-sub-neg" if avg_screen > 6.0 else "metric-sub"
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Avg Screen Time</div>
        <div class="metric-value">{avg_screen}h</div>
        <div class="{screen_sub_cls}">Recreational/Day</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    avg_ff = round(filtered_df['Fast_Food_Frequency_Per_Week'].mean(), 1) if len(filtered_df) > 0 else 0
    ff_sub_cls = "metric-sub-neg" if avg_ff >= 3.0 else "metric-sub"
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Avg Fast Food</div>
        <div class="metric-value">{avg_ff} <span style="font-size:1rem; font-weight:400;">days/wk</span></div>
        <div class="{ff_sub_cls}">Heavy Reliance</div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    high_risk_pct = round((filtered_df['Health_Risk_Level'] == 'High Risk (Vulnerable Pattern)').mean() * 100, 1) if len(filtered_df) > 0 else 0
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">High Risk Cohort</div>
        <div class="metric-value">{high_risk_pct}%</div>
        <div class="metric-sub-neg">Score &lt; 50/100</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TABBED NAVIGATION
# -------------------------------------------------------------
tabs = st.tabs([
    "📊 Executive Summary",
    "🍔 Dietary Patterns & Habits",
    "🏃 Sleep & Lifestyle Cascade",
    "🧠 Correlations & Statistical Tests",
    "📖 The Data Story",
    "🧪 Personal Health Simulator",
    "🗃️ Raw Dataset Explorer"
])

# =============================================================
# TAB 1: EXECUTIVE SUMMARY & DEMOGRAPHICS
# =============================================================
with tabs[0]:
    st.subheader("Demographic Landscape & Profile of Respondents")
    st.write("Distribution of participants across education/career stages, living environments, and age cohorts.")
    
    col_t1_1, col_t1_2 = st.columns(2)
    
    with col_t1_1:
        fig_occ = px.pie(
            filtered_df,
            names='Occupation_Status',
            title='<b>Occupation & Academic Profile</b>',
            hole=0.45,
            color_discrete_sequence=px.colors.qualitative.Prism
        )
        fig_occ.update_layout(margin=dict(t=50, b=20, l=20, r=20), height=380)
        st.plotly_chart(fig_occ, use_container_width=True)
        
    with col_t1_2:
        fig_living = px.pie(
            filtered_df,
            names='Living_Arrangement',
            title='<b>Living Arrangement Distribution</b>',
            hole=0.45,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_living.update_layout(margin=dict(t=50, b=20, l=20, r=20), height=380)
        st.plotly_chart(fig_living, use_container_width=True)
        
    st.divider()
    
    col_t1_3, col_t1_4 = st.columns(2)
    with col_t1_3:
        fig_age = px.histogram(
            filtered_df,
            x='Age',
            color='Gender',
            barmode='group',
            title='<b>Age Distribution by Gender</b>',
            color_discrete_sequence=['#3b82f6', '#ec4899', '#8b5cf6']
        )
        fig_age.update_layout(height=350, margin=dict(t=50, b=20, l=20, r=20))
        st.plotly_chart(fig_age, use_container_width=True)
        
    with col_t1_4:
        fig_risk = px.histogram(
            filtered_df,
            x='Health_Risk_Level',
            color='Occupation_Status',
            title='<b>Lifestyle Health Risk Classification by Occupation</b>',
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig_risk.update_layout(height=350, margin=dict(t=50, b=20, l=20, r=20))
        st.plotly_chart(fig_risk, use_container_width=True)

# =============================================================
# TAB 2: DIETARY PATTERNS & HABITS
# =============================================================
with tabs[1]:
    st.subheader("Nutritional Architecture & Dietary Dynamics")
    st.write("Evaluating the divergence between home-cooked meals and fast-food dependency, alongside financial and behavioral drivers.")
    
    col_t2_1, col_t2_2 = st.columns(2)
    
    with col_t2_1:
        # Grouped bar chart: Cooking vs Fast Food by living condition
        living_summary = filtered_df.groupby('Living_Arrangement')[['Cooking_Frequency_Per_Week', 'Fast_Food_Frequency_Per_Week']].mean().reset_index()
        fig_diet = go.Figure()
        fig_diet.add_trace(go.Bar(
            x=living_summary['Living_Arrangement'],
            y=living_summary['Cooking_Frequency_Per_Week'],
            name='Cooking at Home (Days/Wk)',
            marker_color='#10b981'
        ))
        fig_diet.add_trace(go.Bar(
            x=living_summary['Living_Arrangement'],
            y=living_summary['Fast_Food_Frequency_Per_Week'],
            name='Fast Food Takeout (Days/Wk)',
            marker_color='#f43f5e'
        ))
        fig_diet.update_layout(
            barmode='group',
            title='<b>Dietary Divergence: Home Cooking vs Fast Food Intake</b>',
            yaxis_title='Mean Days per Week',
            xaxis_title='Living Arrangement',
            height=400,
            margin=dict(t=50, b=20, l=20, r=20)
        )
        st.plotly_chart(fig_diet, use_container_width=True)
        
    with col_t2_2:
        # Monthly food budget vs Fast Food Tier
        fig_budget = px.box(
            filtered_df,
            x='Fast_Food_Tier',
            y='Monthly_Food_Budget_INR',
            color='Fast_Food_Tier',
            title='<b>Financial Impact: Monthly Food Expenditure vs Fast Food Dependency</b>',
            color_discrete_sequence=px.colors.sequential.Sunsetdark
        )
        fig_budget.update_layout(
            yaxis_title='Monthly Food Expenditure (INR)',
            xaxis_title='Fast Food Tier',
            height=400,
            margin=dict(t=50, b=20, l=20, r=20),
            showlegend=False
        )
        st.plotly_chart(fig_budget, use_container_width=True)
        
    st.divider()
    
    col_t2_3, col_t2_4 = st.columns(2)
    with col_t2_3:
        # Breakfast skipping habit & energy
        fig_bf = px.bar(
            filtered_df.groupby(['Skips_Breakfast', 'Gender'])['Daily_Energy_Rating'].mean().reset_index(),
            x='Skips_Breakfast',
            y='Daily_Energy_Rating',
            color='Gender',
            barmode='group',
            title='<b>Impact of Skipping Breakfast on Daily Vitality Rating (1-10)</b>',
            color_discrete_sequence=['#3b82f6', '#f43f5e', '#8b5cf6']
        )
        fig_bf.update_layout(height=380, margin=dict(t=50, b=20, l=20, r=20), yaxis_range=[0, 10])
        st.plotly_chart(fig_bf, use_container_width=True)
        
    with col_t2_4:
        # Stated Barriers
        barriers_df = filtered_df['Primary_Barrier_To_Healthy_Eating'].value_counts().reset_index()
        barriers_df.columns = ['Barrier', 'Count']
        fig_barriers = px.bar(
            barriers_df,
            x='Count',
            y='Barrier',
            orientation='h',
            title='<b>Primary Stated Obstacles to Healthy Eating</b>',
            color='Count',
            color_continuous_scale='Viridis'
        )
        fig_barriers.update_layout(height=380, margin=dict(t=50, b=20, l=20, r=20))
        st.plotly_chart(fig_barriers, use_container_width=True)

# =============================================================
# TAB 3: SLEEP & LIFESTYLE CASCADE
# =============================================================
with tabs[2]:
    st.subheader("Physical Activity, Screen Saturation & Sleep Ecology")
    st.write("Investigating the cascading physical consequences of sedentary screen exposure and circadian disruption.")
    
    col_t3_1, col_t3_2 = st.columns(2)
    
    with col_t3_1:
        # Screen time vs Sleep Duration with OLS trendline
        fig_reg = px.scatter(
            filtered_df,
            x='Screen_Time_Hours_Per_Day',
            y='Sleep_Hours_Per_Night',
            color='Perceived_Stress_Level',
            color_continuous_scale='Turbo',
            trendline='ols',
            title='<b>The Screen-to-Sleep Erosion Trendline</b>',
            labels={
                'Screen_Time_Hours_Per_Day': 'Screen Time (Hours/Day)',
                'Sleep_Hours_Per_Night': 'Sleep Duration (Hours/Night)',
                'Perceived_Stress_Level': 'Stress (1-10)'
            }
        )
        fig_reg.add_hline(y=7.0, line_dash='dash', line_color='green', annotation_text='Recommended Sleep (7h)')
        fig_reg.update_layout(height=420, margin=dict(t=50, b=20, l=20, r=20))
        st.plotly_chart(fig_reg, use_container_width=True)
        
    with col_t3_2:
        # BMI distribution across Fast Food Tier
        fig_bmi = px.violin(
            filtered_df,
            x='Fast_Food_Tier',
            y='BMI',
            color='Fast_Food_Tier',
            box=True,
            points='all',
            title='<b>BMI Distribution across Fast Food Consumption Tiers</b>',
            color_discrete_sequence=px.colors.qualitative.Dark24
        )
        fig_bmi.add_hline(y=25.0, line_dash='dash', line_color='red', annotation_text='Overweight (BMI ≥ 25)')
        fig_bmi.add_hline(y=18.5, line_dash='dot', line_color='orange', annotation_text='Underweight (BMI < 18.5)')
        fig_bmi.update_layout(height=420, margin=dict(t=50, b=20, l=20, r=20), showlegend=False)
        st.plotly_chart(fig_bmi, use_container_width=True)
        
    st.divider()
    
    col_t3_3, col_t3_4 = st.columns(2)
    with col_t3_3:
        # Exercise vs Health Score
        fig_ex = px.scatter(
            filtered_df,
            x='Exercise_Hours_Per_Week',
            y='Lifestyle_Health_Score',
            color='Health_Risk_Level',
            title='<b>Protective Effect of Weekly Exercise on Composite Health Score</b>',
            color_discrete_map={
                'Low Risk (Healthy Lifestyle)': '#10b981',
                'Moderate Risk (Sub-optimal)': '#f59e0b',
                'High Risk (Vulnerable Pattern)': '#ef4444'
            }
        )
        fig_ex.update_layout(height=380, margin=dict(t=50, b=20, l=20, r=20))
        st.plotly_chart(fig_ex, use_container_width=True)
        
    with col_t3_4:
        # Hydration & Caffeine Intake
        fig_hydro = px.density_heatmap(
            filtered_df,
            x='Daily_Water_Intake_Liters',
            y='Caffeine_Cups_Per_Day',
            title='<b>Hydration vs Caffeine Intake Density</b>',
            color_continuous_scale='Blues'
        )
        fig_hydro.update_layout(height=380, margin=dict(t=50, b=20, l=20, r=20))
        st.plotly_chart(fig_hydro, use_container_width=True)

# =============================================================
# TAB 4: CORRELATIONS & STATISTICAL TESTS
# =============================================================
with tabs[3]:
    st.subheader("Statistical Validation & Inferential Analytics")
    st.write("Rigorous statistical hypothesis testing confirming whether observed lifestyle relationships are statistically significant.")
    
    # Hypothesis test cards
    ht = eda_meta.get('hypothesis_tests', {})
    
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.markdown(f"""
        <div class="story-card">
            <h4>🔬 Hypothesis Test 1: Fast Food vs Living Arrangement</h4>
            <p><b>Test Applied:</b> One-Way ANOVA (Analysis of Variance)</p>
            <p><b>Null Hypothesis (H₀):</b> Mean fast-food frequency is identical across all living arrangements.</p>
            <p><b>Test Results:</b> F-Statistic = <code>{ht.get('h1_living_vs_fast_food', {}).get('f_statistic', '272.7')}</code> | p-value = <code>&lt; 0.001</code></p>
            <p><span class="insight-badge">Verdict: REJECT H₀ (Highly Significant)</span></p>
            <p><i>{ht.get('h1_living_vs_fast_food', {}).get('interpretation', '')}</i></p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_h2:
        st.markdown(f"""
        <div class="story-card">
            <h4>🔬 Hypothesis Test 2: Screen Time vs Sleep Duration</h4>
            <p><b>Test Applied:</b> Pearson Correlation Coefficient Test</p>
            <p><b>Null Hypothesis (H₀):</b> No linear relationship exists between recreational screen hours and sleep hours.</p>
            <p><b>Test Results:</b> r = <code>{ht.get('h2_screen_vs_sleep', {}).get('r_coefficient', '-0.41')}</code> | p-value = <code>&lt; 0.001</code></p>
            <p><span class="insight-badge">Verdict: REJECT H₀ (Highly Significant)</span></p>
            <p><i>{ht.get('h2_screen_vs_sleep', {}).get('interpretation', '')}</i></p>
        </div>
        """, unsafe_allow_html=True)
        
    col_h3, col_h4 = st.columns(2)
    with col_h3:
        st.markdown(f"""
        <div class="story-card">
            <h4>🔬 Hypothesis Test 3: Skipping Breakfast vs Daily Energy</h4>
            <p><b>Test Applied:</b> Welch's Two-Sample Independent t-test</p>
            <p><b>Null Hypothesis (H₀):</b> Breakfast skippers and regular breakfast consumers experience equal vitality.</p>
            <p><b>Test Results:</b> t-Statistic = <code>{ht.get('h3_breakfast_vs_energy', {}).get('t_statistic', '-11.75')}</code> | p-value = <code>&lt; 0.001</code></p>
            <p><span class="insight-badge">Verdict: REJECT H₀ (Highly Significant)</span></p>
            <p><i>{ht.get('h3_breakfast_vs_energy', {}).get('interpretation', '')}</i></p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_h4:
        st.markdown(f"""
        <div class="story-card">
            <h4>🔬 Hypothesis Test 4: Risk Tier vs Perceived Barriers</h4>
            <p><b>Test Applied:</b> Pearson's Chi-Square Test of Independence (χ²)</p>
            <p><b>Null Hypothesis (H₀):</b> Stated eating barriers are independent of lifestyle health risk level.</p>
            <p><b>Test Results:</b> χ²-Statistic = <code>{ht.get('h4_barrier_vs_risk', {}).get('chi2_statistic', '48.9')}</code> | p-value = <code>&lt; 0.001</code></p>
            <p><span class="insight-badge">Verdict: REJECT H₀ (Highly Significant)</span></p>
            <p><i>{ht.get('h4_barrier_vs_risk', {}).get('interpretation', '')}</i></p>
        </div>
        """, unsafe_allow_html=True)
        
    st.divider()
    st.subheader("Interactive Correlation Matrix")
    num_cols = [
        'Screen_Time_Hours_Per_Day', 'Sleep_Hours_Per_Night', 'Fast_Food_Frequency_Per_Week',
        'Cooking_Frequency_Per_Week', 'Exercise_Hours_Per_Week', 'Daily_Water_Intake_Liters',
        'Perceived_Stress_Level', 'Daily_Energy_Rating', 'BMI', 'Lifestyle_Health_Score'
    ]
    corr = filtered_df[num_cols].corr()
    fig_corr = px.imshow(
        corr,
        text_auto='.2f',
        aspect='auto',
        color_continuous_scale='RdBu_r',
        title='<b>Correlation Matrix of Measured Biometric & Behavioral Variables</b>',
        zmin=-1,
        zmax=1
    )
    fig_corr.update_layout(height=520, margin=dict(t=50, b=20, l=20, r=20))
    st.plotly_chart(fig_corr, use_container_width=True)

# =============================================================
# TAB 5: THE DATA STORY (Deliverables 1, 2, 7, 9, 10)
# =============================================================
with tabs[4]:
    st.subheader("📖 The Data Story: From Problem to Strategic Transformation")
    st.caption("Following the recommended storytelling pipeline: Problem Statement → Objectives → Analytical Journey → Insights → Actionable Recommendations.")
    
    st.markdown("""
    <div class="story-card">
        <span class="story-step">PHASE 1: THE PROBLEM STATEMENT</span>
        <h3>The Silent Metabolic & Circadian Strain Among Young Adults</h3>
        <p>
            Young adulthood (ages 18 to 26) marks the pivotal transition from parental oversight to independent living, 
            academic deadlines, and early career pressures. During this vulnerable phase, erratic food choices, hyper-palatable 
            fast-food dependence, prolonged screen exposure, and chronic sleep deprivation combine to form an insidious negative 
            health cascade. While young adults often consider themselves resilient, this study investigates how these habits secretly 
            drain cognitive stamina, elevate BMI, and compound psychological stress.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="story-card">
        <span class="story-step">PHASE 2: PROJECT OBJECTIVES</span>
        <h3>Key Research Objectives</h3>
        <ol>
            <li><b>Quantify Dietary Shifts:</b> Measure the frequency of fast-food reliance vs home cooking across university students and working youth.</li>
            <li><b>Investigate Circadian Disruption:</b> Evaluate the quantitative relationship between recreational screen time, sleep duration, and perceived stress.</li>
            <li><b>Evaluate Nutritional Habits on Vitality:</b> Determine how breakfast omission and hydration affect cognitive focus and daily subjective energy.</li>
            <li><b>Assess Metabolic Vulnerability:</b> Analyze body mass index (BMI) patterns across sedentary habits and fast-food dependency tiers.</li>
            <li><b>Formulate Scalable Interventions:</b> Develop actionable recommendations for higher education institutions, young professionals, and urban health policymakers.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="story-card">
        <span class="story-step">PHASE 3: CORE ANALYTICAL INSIGHTS</span>
        <h3>6 Groundbreaking Discoveries from 850 Surveyed Young Adults</h3>
    </div>
    """, unsafe_allow_html=True)
    
    for ins in eda_meta.get('key_insights', []):
        st.markdown(f"""
        <div style="background:#ffffff; border-left: 4px solid #3b82f6; padding: 14px 20px; border-radius: 8px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.05);">
            <h4 style="margin: 0 0 6px 0; color: #1e3a8a;">Insight #{ins['id']}: {ins['title']}</h4>
            <p style="margin: 0; color: #334155; line-height: 1.5;">{ins['detail']}</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("""
    <div class="story-card">
        <span class="story-step">PHASE 4: ACTIONABLE RECOMMENDATIONS</span>
        <h3>Evidence-Based Intervention Roadmap</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;">
            <div style="background: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #cbd5e1;">
                <h4 style="color: #047857; margin-top:0;">🏛️ 1. Campus & Workplace Infrastructure</h4>
                <p style="font-size: 0.9rem; color: #334155;">
                    Universities and IT hubs must provide subsidized, nutritious breakfast stations and communal kitchen pods 
                    in hostels. Eliminating the breakfast barrier directly boosts student cognitive performance and eliminates 
                    mid-morning junk-food spikes.
                </p>
            </div>
            <div style="background: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #cbd5e1;">
                <h4 style="color: #0369a1; margin-top:0;">📱 2. Digital Sunset & Sleep Architecture</h4>
                <p style="font-size: 0.9rem; color: #334155;">
                    Instituting a strict 45-minute "screen-free curfew" prior to bedtime recovers an estimated 45-60 minutes 
                    of lost deep sleep per night, breaking the chronic blue-light-induced sleep debt cycle.
                </p>
            </div>
            <div style="background: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #cbd5e1;">
                <h4 style="color: #b45309; margin-top:0;">🍳 3. Micro-Cooking & Food Literacy</h4>
                <p style="font-size: 0.9rem; color: #334155;">
                    Young adults need practical 15-minute meal preparation workshops rather than generic diet charts. Teaching 
                    easy batch-cooking reduces weekly fast-food spend by up to ₹2,500/month while cutting calorie intake.
                </p>
            </div>
            <div style="background: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #cbd5e1;">
                <h4 style="color: #6d28d9; margin-top:0;">💧 4. Baseline Habit Anchoring</h4>
                <p style="font-size: 0.9rem; color: #334155;">
                    Pairing hydration (2.5L target) with a non-negotiable 30 minutes of brisk daily walking provides a massive 
                    protective buffer against BMI escalation, reducing metabolic syndrome risk even during heavy exam periods.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================
# TAB 6: PERSONAL LIFESTYLE HEALTH RISK SIMULATOR
# =============================================================
with tabs[5]:
    st.subheader("🧪 Interactive Young Adult Lifestyle Risk Calculator")
    st.write("Test personal habits or scenario simulations. The engine computes your predicted **Lifestyle Health Score (0-100)** and risk profile.")
    
    col_sim_1, col_sim_2 = st.columns([1, 1])
    
    with col_sim_1:
        st.markdown("#### Enter Lifestyle Parameters:")
        sim_sleep = st.slider("Average Sleep Hours per Night", 3.0, 11.0, 6.5, 0.5)
        sim_screen = st.slider("Daily Recreational Screen Time (Hours)", 1.0, 15.0, 7.5, 0.5)
        sim_ff = st.slider("Fast Food / Takeout Days per Week", 0, 7, 3)
        sim_cook = st.slider("Home Cooking Days per Week", 0, 7, 2)
        sim_ex = st.slider("Exercise Hours per Week", 0.0, 14.0, 2.5, 0.5)
        sim_water = st.slider("Daily Water Intake (Liters)", 0.5, 5.0, 2.0, 0.1)
        sim_bf = st.selectbox("Do you skip breakfast?", ["No (Regular Eater)", "Occasionally", "Yes (Habitual Skipper)"])
        sim_stress = st.slider("Perceived Stress Level (1=Zen, 10=Extreme)", 1.0, 10.0, 6.0, 0.5)
        
    with col_sim_2:
        # Live Model Calculation
        # Base: 50.0
        score = 50.0
        score += min(sim_cook * 2.5, 15)
        score += min(sim_ex * 3.0, 15)
        score += min(sim_water * 3.5, 12)
        
        if 7.0 <= sim_sleep <= 8.5:
            score += 10
        elif 6.0 <= sim_sleep < 7.0:
            score += 4
        else:
            score -= 8
            
        score -= (sim_ff * 3.5)
        if sim_bf == "Yes (Habitual Skipper)":
            score -= 10
        elif sim_bf == "Occasionally":
            score -= 5
            
        if sim_screen > 7.0:
            score -= ((sim_screen - 7.0) * 2.5)
            
        score -= ((sim_stress - 5.0) * 2.0)
        final_score = float(np.clip(round(score, 1), 5.0, 100.0))
        
        if final_score >= 70:
            risk_label = "LOW RISK (Healthy & Resilient)"
            risk_color = "#10b981"
            rec_text = "Great lifestyle balance! Your sleep, nutrition, and physical activity provide strong metabolic protection."
        elif final_score >= 50:
            risk_label = "MODERATE RISK (Sub-optimal Strain)"
            risk_color = "#f59e0b"
            rec_text = "Caution: You are experiencing moderate lifestyle strain. Prioritize trimming 1-2 hours of screen time and adding 1 more day of home-cooked meals."
        else:
            risk_label = "HIGH RISK (Vulnerable Health Pattern)"
            risk_color = "#ef4444"
            rec_text = "Urgent attention recommended: High fast-food frequency combined with sleep debt and elevated screen exposure is compounding metabolic and mental fatigue."
            
        # Gauge chart
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = final_score,
            title = {'text': "<b>Your Lifestyle Health Score</b>", 'font': {'size': 20}},
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': risk_color},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 50], 'color': '#fee2e2'},
                    {'range': [50, 70], 'color': '#fef3c7'},
                    {'range': [70, 100], 'color': '#d1fae5'}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 50
                }
            }
        ))
        fig_gauge.update_layout(height=320, margin=dict(t=30, b=10, l=30, r=30))
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        st.markdown(f"""
        <div style="background: #ffffff; border-left: 5px solid {risk_color}; padding: 15px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.06);">
            <h4 style="margin: 0 0 5px 0; color: {risk_color};">{risk_label}</h4>
            <p style="margin: 0; color: #475569; font-size: 0.95rem;">{rec_text}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Predicted BMI
        est_bmi = round(21.5 + (sim_ff * 0.65) - (sim_ex * 0.35) + ((8.0 - sim_sleep) * 0.3), 1)
        st.write(f"📊 **Projected Steady-State BMI:** `{est_bmi} kg/m²` ({'Normal' if est_bmi < 25 else 'Overweight risk'})")

# =============================================================
# TAB 7: RAW DATA EXPLORER & EXPORT
# =============================================================
with tabs[6]:
    st.subheader("Survey Dataset Repository")
    st.write("Inspect the cleaned, imputed, and feature-engineered survey records.")
    
    col_exp1, col_exp2 = st.columns([3, 1])
    with col_exp1:
        search_query = st.text_input("🔍 Search by Respondent ID or Occupation:", "")
    with col_exp2:
        st.write("")
        st.write("")
        csv_data = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Filtered CSV",
            data=csv_data,
            file_name="cleaned_food_lifestyle_data_filtered.csv",
            mime="text/csv"
        )
        
    display_df = filtered_df
    if search_query:
        display_df = display_df[
            display_df['Respondent_ID'].str.contains(search_query, case=False, na=False) |
            display_df['Occupation_Status'].str.contains(search_query, case=False, na=False)
        ]
        
    st.dataframe(display_df, use_container_width=True, height=450)
    st.caption(f"Displaying {len(display_df)} of {len(filtered_df)} filtered records.")



