# Black Box Test Execution Report

**Course:** Master of Computer Applications (MCA) - Data Analysis Project  
**Topic:** Analysing Food Habits and Lifestyle Pattern Among Young Adults  
**Execution Timestamp:** 2026-11-12 22:54:53  
**Overall Status:** `25/25 Passed (100.0%)`  

## Test Case Execution Summary

| Test ID | Module | Category | Objective | Status | Details |
| :--- | :--- | :--- | :--- | :---: | :--- |
| TC_BB_001 | Demographics | Equivalence Partition | Validate young adult age range [18, 26] | 🟢 PASS | Min: 18, Max: 26 |
| TC_BB_002 | Dietary | Equivalence Partition | Validate Fast Food Critical Tier threshold (>=6) | 🟢 PASS | All critical tier rows have fast food days >= 6 |
| TC_BB_003 | Circadian | Equivalence Partition | Validate Severe Sleep Deficit class (<6.0h) | 🟢 PASS | All severe deficit instances have sleep < 6h |
| TC_BB_004 | Health Score | Equivalence Partition | Validate High Risk Classification (Score < 50) | 🟢 PASS | All high risk rows have health score < 50 |
| TC_BB_005 | Screen Time | Equivalence Partition | Validate Excessive Screen class (>8h) | 🟢 PASS | All excessive tier rows have screen time > 8h |
| TC_BB_006 | Calculator | Boundary Value | Test minimum allowable sleep duration (3.0h floor) | 🟢 PASS | Score calculated: 49.5 |
| TC_BB_007 | Calculator | Boundary Value | Test upper sleep duration boundary (11.0h ceiling) | 🟢 PASS | Score calculated: 49.5 |
| TC_BB_008 | Calculator | Boundary Value | Test zero fast food intake lower limit (0 days) | 🟢 PASS | Penalty delta: 3.4 pts (Expected ~3.5) |
| TC_BB_009 | Calculator | Boundary Value | Test maximum fast food intake boundary (7 days) | 🟢 PASS | Score: 24.8 |
| TC_BB_010 | Hydration | Boundary Value | Test water lower limit (0.5L) | 🟢 PASS | Score: 71.2 |
| TC_BB_011 | Filtering | Functional Filter | Filter by Undergraduate Student | 🟢 PASS | Matched records: 382 |
| TC_BB_012 | Filtering | Functional Filter | Filter by Hostel / Dormitory | 🟢 PASS | Matched records: 318 |
| TC_BB_013 | Filtering | Functional Multi-filter | Multi-filter: UG + Hostel + Age 18-20 | 🟢 PASS | Intersection count: 136 |
| TC_BB_014 | Filtering | Error Handling | Handle mutually exclusive filter resulting in 0 matches | 🟢 PASS | Correctly handles empty result set without crash |
| TC_BB_015 | Filtering | Functional Reset | Verify full cohort restoration on reset | 🟢 PASS | Cohort size: 850 |
| TC_BB_016 | Simulator | Decision Table | Execute Ideal Lifestyle Profile | 🟢 PASS | Health Score: 100.0 (Low Risk) |
| TC_BB_017 | Simulator | Decision Table | Execute Extreme High-Strain Lifestyle Profile | 🟢 PASS | Health Score: 5.0 (High Risk) |
| TC_BB_018 | Simulator | Sensitivity Test | Evaluate breakfast skipping penalty isolation | 🟢 PASS | Score difference: 10.0 |
| TC_BB_019 | Data Explorer | Search | Search respondents by prefix 'YA00' | 🟢 PASS | Matched: 99 rows |
| TC_BB_020 | Data Explorer | Search | Search by occupation keyword 'Working' | 🟢 PASS | Matched: 179 rows |
| TC_BB_021 | Data Explorer | Robustness | Search non-existent ID 'YA9999' | 🟢 PASS | Gracefully returned 0 matches |
| TC_BB_022 | Export Engine | Schema Integrity | Verify complete 27-column standard schema in CSV | 🟢 PASS | Total columns: 27 |
| TC_BB_023 | Export Engine | File Line Count | Verify CSV line count equals header + 850 rows | 🟢 PASS | Actual file lines: 851 |
| TC_BB_024 | Presentation | File Verification | Verify 12-slide PPTX deck existence & size | 🟢 PASS | File size: 1.25 MB |
| TC_BB_025 | Visuals | Rendering Verification | Verify generation of all 7 publication charts | 🟢 PASS | Charts found: 7 |

## Black Box Testing Conclusion
All functional boundaries, equivalence partitions, multi-filter combinations, and output integrity checks passed with 100% compliance. The application meets high software reliability and quality assurance standards required for academic evaluation.
