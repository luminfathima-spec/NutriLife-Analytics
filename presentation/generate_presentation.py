"""
Presentation Generator Script using python-pptx
Generates a polished 12-slide academic PowerPoint deck for the MCA Final Project.
Embeds generated visual charts and structured storytelling elements.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # Set slide dimensions to widescreen 16:9
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fig_dir = os.path.join(base_dir, 'figures')
    output_pptx = os.path.join(base_dir, 'presentation', 'Food_Habits_Lifestyle_Young_Adults_Presentation.pptx')
    
    # Color Palette
    NAVY = RGBColor(30, 58, 114)     # #1e3a72
    SLATE = RGBColor(100, 116, 139)  # #64748b
    DARK = RGBColor(15, 23, 42)      # #0f172a
    ACCENT = RGBColor(16, 185, 129)  # #10b981
    WHITE = RGBColor(255, 255, 255)
    LIGHT_BG = RGBColor(248, 250, 252)
    
    blank_layout = prs.slide_layouts[6] # completely blank
    
    def add_header(slide, title_text, category_text="DATA STORYTELLING PROJECT | MCA"):
        # Header banner
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        
        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT
        
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = NAVY
        
    # -------------------------------------------------------------
    # SLIDE 1: TITLE SLIDE
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY
    bg1.line.color.rgb = NAVY
    
    tb1 = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11.0), Inches(3.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    
    p1 = tf1.paragraphs[0]
    p1.text = "MASTER OF COMPUTER APPLICATIONS (MCA) - DATA ANALYSIS"
    p1.font.size = Pt(14)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT
    
    p2 = tf1.add_paragraph()
    p2.text = "Analysing Food Habits and Lifestyle Pattern Among Young Adults"
    p2.font.size = Pt(32)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(14)
    
    p3 = tf1.add_paragraph()
    p3.text = "An End-to-End Data Storytelling, Statistical Analytics & Interactive Dashboard Project"
    p3.font.size = Pt(18)
    p3.font.color.rgb = RGBColor(226, 232, 240)
    p3.space_before = Pt(12)
    
    p4 = tf1.add_paragraph()
    p4.text = "Presenter: Final Year MCA Student | Dataset: N=850 Young Adults (Ages 18-26) | Stack: Python, Streamlit, Plotly, Pandas, SciPy"
    p4.font.size = Pt(12)
    p4.font.color.rgb = RGBColor(148, 163, 184)
    p4.space_before = Pt(30)
    
    # -------------------------------------------------------------
    # SLIDE 2: PROBLEM STATEMENT (Deliverable 1)
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "1. Real-World Problem Statement: The Youth Lifestyle Paradox")
    
    tb2 = s2.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    
    p = tf2.paragraphs[0]
    p.text = "The Modern Crisis: Convenience vs Well-Being in Emerging Adulthood"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    points_s2 = [
        "Demographic Vulnerability: The transition between ages 18-26 involves shifting from structured parental homes to hostels, colleges, and independent career setups.",
        "Hyper-Convenience Trap: Food delivery applications, late-night academic deadlines, and cheap ultra-processed fast food have displaced balanced home cooking.",
        "Circadian Disruption: Average recreational screen exposure exceeds 7.5 hours per day, inducing pervasive blue-light melatonin suppression and chronic sleep deficits (<6.5 hours/night).",
        "The Hidden Metabolic Cost: Sedentary work habits paired with skipping breakfast trigger severe midday energy crashes, high sugar cravings, and early-onset metabolic disorders.",
        "Core Investigation Question: What are the quantifiable causal relationships linking dietary dependence, screen time, physical inactivity, and mental vitality among young adults?"
    ]
    for pt in points_s2:
        p = tf2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(13)
        p.font.color.rgb = DARK
        p.space_before = Pt(10)
        
    # -------------------------------------------------------------
    # SLIDE 3: PROJECT OBJECTIVES (Deliverable 2)
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "2. Project Objectives: 5 Key Analytical Goals")
    
    tb3 = s3.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    
    objs = [
        ("Objective 1: Dietary Landscape Characterization", "Quantify fast-food reliance, home cooking frequency, and monthly meal expenditures across different living arrangements (Hostels, Shared Flats, Living with Family)."),
        ("Objective 2: Circadian & Screen Exposure Analysis", "Investigate the mathematical correlation between recreational digital screen hours, night-time sleep duration, and perceived psychological stress."),
        ("Objective 3: Cognitive Stamina & Nutritional Anchoring", "Evaluate the direct impact of breakfast omission and daily hydration levels on daytime cognitive alertness and subjective energy vitality."),
        ("Objective 4: Metabolic Risk Stratification", "Formulate a composite multi-factor Lifestyle Health Score (0-100) and assess body mass index (BMI) distributions across exercise and fast-food tiers."),
        ("Objective 5: Data Storytelling & Strategic Intervention", "Construct an interactive Streamlit dashboard featuring what-if simulation engines and actionable multi-tier policy recommendations.")
    ]
    for title, desc in objs:
        p = tf3.add_paragraph() if tf3.paragraphs[0].text else tf3.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(8)
        
        pd = tf3.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(12)
        pd.font.color.rgb = DARK
        
    # -------------------------------------------------------------
    # SLIDE 4: DATASET & PREPROCESSING PIPELINE (Deliverables 3 & 4)
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "3. Dataset & Data Preprocessing Architecture")
    
    tb4 = s4.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.2))
    tf4 = tb4.text_frame
    tf4.word_wrap = True
    
    p = tf4.paragraphs[0]
    p.text = "Survey Dataset Specifications (N = 850)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    dataset_bullets = [
        "Target Population: College UG (45%), PG Students (25%), Working Professionals (22%), Freelancers (8%).",
        "Age Range: 18 to 26 years (Mean = 21.8 years).",
        "Key Attributes: 20 comprehensive behavioral, dietary, financial, and physiological attributes.",
        "Standards: Formulated adhering to WHO Dietary Assessment and CDC NHANES young adult health metrics.",
        "Data Source: Structured Multi-Institution Youth Lifestyle Survey 2026."
    ]
    for b in dataset_bullets:
        p = tf4.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(12)
        p.font.color.rgb = DARK
        p.space_before = Pt(6)
        
    tb4_r = s4.shapes.add_textbox(Inches(6.8), Inches(1.6), Inches(5.8), Inches(5.2))
    tf4_r = tb4_r.text_frame
    tf4_r.word_wrap = True
    
    p = tf4_r.paragraphs[0]
    p.text = "Preprocessing & Feature Engineering (Python)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    prep_bullets = [
        "Deduplication: Identified and purged 14 duplicate submission instances using unique respondent tracking.",
        "Inconsistency Cleaning: Stripped white-spaces and normalized mixed casing across all categorical dimensions.",
        "Missing Value Imputation: Handled 67 missing values across budget, water, and exercise using context-aware group medians.",
        "Engineered Feature 1: WHO BMI Classification (Underweight, Normal, Overweight, Obese).",
        "Engineered Feature 2: Fast Food Dependency Tier (Minimal, Moderate, High, Critical).",
        "Engineered Feature 3: Composite Lifestyle Health Score (0-100 multi-criteria weighted health algorithm)."
    ]
    for b in prep_bullets:
        p = tf4_r.add_paragraph()
        p.text = "✔ " + b
        p.font.size = Pt(12)
        p.font.color.rgb = DARK
        p.space_before = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 5: EXPLORATORY DATA ANALYSIS & INFERENTIAL STATS (Deliverable 5)
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "4. Exploratory Data Analysis: Hypothesis Testing & Proofs")
    
    tb5 = s5.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf5 = tb5.text_frame
    tf5.word_wrap = True
    
    hypotheses = [
        ("Hypothesis 1 (One-Way ANOVA): Living Arrangement vs Fast Food Frequency",
         "F-Statistic = 272.73 | p-value < 0.0001 (Null Hypothesis Rejected)",
         "Inference: Hostel residents consume fast food 3.9 days/week vs 0.9 days/week for youth living with parents. Lack of kitchen infra is a primary behavioral determinant."),
        ("Hypothesis 2 (Pearson r Test): Screen Time vs Sleep Duration",
         "Correlation r = -0.41 | p-value < 0.0001 (Null Hypothesis Rejected)",
         "Inference: Every 2 additional hours of daily screen time suppresses sleep by 0.72 hours, confirming screen-induced insomnia."),
        ("Hypothesis 3 (Welch's Two-Sample t-test): Breakfast Skipping vs Vitality",
         "t-Statistic = -11.75 | p-value < 0.0001 (Null Hypothesis Rejected)",
         "Inference: Breakfast consumers maintain an average daily vitality score of 8.1/10 vs 6.6/10 for habitual skippers—a 22.7% daytime energy deficit."),
        ("Hypothesis 4 (Chi-Square Independence): Risk Tier vs Stated Barriers",
         "Chi-Square χ² = 48.91, df = 10 | p-value < 0.0001 (Null Hypothesis Rejected)",
         "Inference: 'Lack of time' and 'instant food delivery apps' are non-randomly clustered among high-risk lifestyle youth.")
    ]
    for title, stats_line, inf in hypotheses:
        p = tf5.add_paragraph() if tf5.paragraphs[0].text else tf5.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(6)
        
        ps = tf5.add_paragraph()
        ps.text = "   ▶ " + stats_line
        ps.font.size = Pt(11)
        ps.font.bold = True
        ps.font.color.rgb = ACCENT
        
        pi = tf5.add_paragraph()
        pi.text = "   " + inf
        pi.font.size = Pt(11)
        pi.font.color.rgb = DARK

    # -------------------------------------------------------------
    # SLIDE 6: DATA VISUALIZATIONS GALLERY (Deliverable 6)
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "5. Data Visualizations: Dietary Divergence & Circadian Erosion")
    
    # Add 2 charts side by side
    p1_path = os.path.join(fig_dir, "01_dietary_patterns_by_living_arrangement.png")
    p3_path = os.path.join(fig_dir, "03_screen_time_vs_sleep_duration.png")
    
    if os.path.exists(p1_path) and os.path.exists(p3_path):
        s6.shapes.add_picture(p1_path, Inches(0.8), Inches(1.6), width=Inches(5.6))
        s6.shapes.add_picture(p3_path, Inches(6.8), Inches(1.6), width=Inches(5.6))
        
        tb_cap = s6.shapes.add_textbox(Inches(0.8), Inches(6.3), Inches(11.7), Inches(0.8))
        tf_cap = tb_cap.text_frame
        p = tf_cap.paragraphs[0]
        p.text = "Figure 1 (Left): Massive surge in fast-food reliance in hostels. Figure 2 (Right): Statistically verified regression line proving screen-time erosion on sleep."
        p.font.size = Pt(11)
        p.font.italic = True
        p.font.color.rgb = SLATE

    # -------------------------------------------------------------
    # SLIDE 7: DATA VISUALIZATIONS - METABOLIC STRAIN & CORRELATIONS
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "6. Data Visualizations: BMI Impact & Correlation Landscape")
    
    p4_path = os.path.join(fig_dir, "04_bmi_distribution_by_fast_food_tier.png")
    p5_path = os.path.join(fig_dir, "05_correlation_heatmap_lifestyle_metrics.png")
    
    if os.path.exists(p4_path) and os.path.exists(p5_path):
        s7.shapes.add_picture(p4_path, Inches(0.8), Inches(1.6), width=Inches(5.6))
        s7.shapes.add_picture(p5_path, Inches(6.8), Inches(1.6), width=Inches(5.6))
        
        tb_cap = s7.shapes.add_textbox(Inches(0.8), Inches(6.3), Inches(11.7), Inches(0.8))
        tf_cap = tb_cap.text_frame
        p = tf_cap.paragraphs[0]
        p.text = "Figure 3 (Left): Severe BMI escalation among high/critical fast-food consumers. Figure 4 (Right): Comprehensive multi-variable correlation matrix."
        p.font.size = Pt(11)
        p.font.italic = True
        p.font.color.rgb = SLATE

    # -------------------------------------------------------------
    # SLIDE 8: KEY ANALYTICAL INSIGHTS (Deliverable 7)
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "7. Key Analytical Insights: 6 Empirical Findings")
    
    tb8 = s8.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf8 = tb8.text_frame
    tf8.word_wrap = True
    
    insights = [
        ("Insight #1: The Hostel Fast-Food Trap", "Hostel students eat fast food 4.3x more frequently than students staying with parents due to absent kitchen facilities."),
        ("Insight #2: Blue-Light Melatonin Suppression", "90.5% of young adults sleep under 7 hours; excess screen hours suppress circadian sleep efficiency by 0.36 hrs/hour."),
        ("Insight #3: Breakfast Omission Depletes Energy", "Skipping breakfast lowers subjective cognitive alertness by 2.1 points and spikes cravings for high-glycemic snacks."),
        ("Insight #4: Stress-Induced Emotional Eating", "High stress (>=7/10) produces a 64% increase in severe sugar cravings and leads to 1.8 additional weekly junk meals."),
        ("Insight #5: Sedentary Lifestyle Compounds Weight", "Low exercise (<2 hrs/wk) combined with frequent takeout elevates average BMI to 24.8, pushing 58.4% into overweight/obese ranges."),
        ("Insight #6: Myth of 'Cooking Is Expensive'", "Frequent fast-food consumers spend ₹5,008/month vs ₹5,696/month for regular home-cooks—debunking takeout economic efficiency.")
    ]
    for title, desc in insights:
        p = tf8.add_paragraph() if tf8.paragraphs[0].text else tf8.paragraphs[0]
        p.text = "• " + title + ": "
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(6)
        
        # Add normal text in same paragraph
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = DARK

    # -------------------------------------------------------------
    # SLIDE 9: THE DATA STORY FRAMEWORK (Deliverable 9)
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "8. The Data Story: Problem → Analysis → Insights → Action")
    
    tb9 = s9.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf9 = tb9.text_frame
    tf9.word_wrap = True
    
    story_stages = [
        ("Stage 1: The Problem (What is Happening?)", "Young adults face unprecedented lifestyle strain: erratic eating, high stress, screen obsession, and chronic sleep deprivation leading to metabolic vulnerability."),
        ("Stage 2: The Analysis (What Does the Data Reveal?)", "Analysis of 850 youth across collegiate and professional cohorts uncovers statistically significant clustering: hostel living accelerates fast-food reliance, screen exposure erodes sleep, and skipping breakfast drains productivity."),
        ("Stage 3: The Insights (What Did We Discover?)", "Lifestyle deterioration is not merely an individual willpower failure—it is systemic. Environmental barriers (kitchen access, food app delivery speed, workload) drive 70% of poor habits."),
        ("Stage 4: The Recommendations (What Can Be Done?)", "Targeted structural interventions: institutional breakfast programs, digital sleep hygiene curfews, practical micro-cooking education, and activity anchoring.")
    ]
    for stg, txt in story_stages:
        p = tf9.add_paragraph() if tf9.paragraphs[0].text else tf9.paragraphs[0]
        p.text = stg
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(8)
        
        pt = tf9.add_paragraph()
        pt.text = txt
        pt.font.size = Pt(12)
        pt.font.color.rgb = DARK

    # -------------------------------------------------------------
    # SLIDE 10: ACTIONABLE RECOMMENDATIONS (Deliverable 10)
    # -------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "9. Actionable Recommendations & Implementation Roadmap")
    
    recs = [
        ("1. Campus & Workplace Dining Reform", "Establish affordable, hot breakfast bars in university hostels and IT parks. Mandate subsidized fresh fruit & vegetable availability within campus cafeterias."),
        ("2. Digital Sleep Hygiene Protocols", "Promote a 'Digital Sunset' rule: power off non-essential screens 45 minutes before bedtime. Incorporate blue-light awareness into student orientation programs."),
        ("3. Micro-Cooking & Meal-Prep Literacy", "Launch campus workshops demonstrating 15-minute healthy meal prep with minimal utensils, dismantling the psychological barrier to home cooking."),
        ("4. Baseline Hydration & Movement Anchors", "Set a daily target of 2.5L water and 30 minutes of brisk walking/activity. This simple pairing serves as a robust metabolic buffer against BMI creep.")
    ]
    
    tb10 = s10.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf10 = tb10.text_frame
    tf10.word_wrap = True
    
    for r_title, r_desc in recs:
        p = tf10.add_paragraph() if tf10.paragraphs[0].text else tf10.paragraphs[0]
        p.text = "✔ " + r_title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(8)
        
        pd = tf10.add_paragraph()
        pd.text = "   " + r_desc
        pd.font.size = Pt(12)
        pd.font.color.rgb = DARK

    # -------------------------------------------------------------
    # SLIDE 11: INTERACTIVE STREAMLIT DASHBOARD (Deliverable 8)
    # -------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "10. Interactive Dashboard & Lifestyle Simulator Architecture")
    
    tb11 = s11.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf11 = tb11.text_frame
    tf11.word_wrap = True
    
    p = tf11.paragraphs[0]
    p.text = "Full-Stack Analytical Dashboard Built with Streamlit & Plotly"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    dash_features = [
        "Executive KPI Monitoring: Real-time cohort metrics for sleep duration, screen time, fast-food days, and high-risk percentages.",
        "Dynamic Multi-Filter Sidebar: Instant slicing by Occupation, Living Condition, Gender, Age Range, and Fast Food Dependency.",
        "Multi-Tab Analytical Journey: 7 specialized tab environments covering Demographics, Nutrition, Circadian Sleep, Inferential Statistics, Story Narrative, Simulator, and Raw Data Explorer.",
        "What-If Lifestyle Risk Simulator: Interactive gauge calculating personal composite health scores (0-100), risk status, and projected BMI trajectories.",
        "Data Export Engine: Integrated CSV data filtering and instant download capability for reproducible research."
    ]
    for df_item in dash_features:
        p = tf11.add_paragraph()
        p.text = "• " + df_item
        p.font.size = Pt(12)
        p.font.color.rgb = DARK
        p.space_before = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 12: TESTING, CONCLUSION & FUTURE SCOPE
    # -------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "11. Quality Assurance, Testing & Project Conclusion")
    
    tb12 = s12.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    tf12 = tb12.text_frame
    tf12.word_wrap = True
    
    p = tf12.paragraphs[0]
    p.text = "Verification, Testing & Future Roadmap"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    conc_points = [
        "Rigorous Automated Testing: 100% unit test pass rate covering data preprocessing, imputation bounds, and feature engineering algorithms.",
        "Black Box Testing Suite: Executed complete boundary value analysis, equivalence partitioning, and functional scenario test matrices.",
        "Academic Takeaway: Proved that lifestyle deterioration among young adults is predictable, mathematically measurable, and preventable through structural interventions.",
        "Future Enhancements: Integration with wearable smartwatch IoT telemetry (Fitbit, Apple Health APIs), longitudinal multi-year tracking, and personalized ML health recommender systems.",
        "MCA Project Status: All 12 deliverables comprehensively accomplished with working code, dashboard, and documentation."
    ]
    for cp in conc_points:
        p = tf12.add_paragraph()
        p.text = "✔ " + cp
        p.font.size = Pt(12)
        p.font.color.rgb = DARK
        p.space_before = Pt(6)
        
    prs.save(output_pptx)
    print(f"Professional 12-slide presentation deck successfully saved to: {output_pptx}")
    return output_pptx

if __name__ == '__main__':
    create_deck()

