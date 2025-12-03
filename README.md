# Predicting Hospital Readmission Rates Using CMS and Clinical Data

## Introduction
This project analyzes and predicts hospital readmission risk using two data sources:
1. Nationwide hospital quality metrics from CMS APIs.
2. A patient-level diabetes readmission dataset from Kaggle.

The goal is to (1) understand which hospital characteristics and clinical features are associated with higher readmission, and (2) build a baseline machine learning model to predict whether a patient will be readmitted within 30 days.

## Data sources

| # | Name                                | Source URL                                                              | Type | Main fields 
| 1 | CMS Hospital Readmissions Reduction Program (HRRP) | https://data.cms.gov/provider-data/dataset/9n3s-kdb3/                   | API  | Facility Name, Facility ID, State, Measure Name, Excess Readmission Ratio, Predicted/Expected Readmission Rate |
| 2 | CMS Hospital General Information    | https://data.cms.gov/provider-data/dataset/xubh-q36u/                   | API  | Facility ID, Hospital Type, Hospital Ownership, Hospital overall rating, State, County, quality group counts    |
| 3 | Diabetes 130-US hospitals for years 1999–2008 (readmission dataset) | https://www.kaggle.com/datasets/brandao/diabetes-readmission-dataset    | File | Age, time_in_hospital, n_lab_procedures, n_procedures, n_medications, encounters, diagnoses, lab test flags, readmitted |

## Analysis

- **CMS analysis**
  - Loaded HRRP and Hospital General Information datasets via API.
  - Merged on facility ID to combine readmission performance with ownership, type, and overall star ratings.
  - Created scatterplots and regression lines to study the relationship between hospital overall rating and excess readmission ratio.
  - Aggregated excess readmission ratios by hospital ownership and type to compare performance across systems.

- **Predictive modeling (Kaggle data)**
  - Cleaned and encoded categorical variables (diagnosis groups, medical specialty, lab test flags, medications, age).
  - Defined a binary target: whether the patient was readmitted within 30 days.
  - Trained Logistic Regression and Random Forest classifiers.
  - Evaluated models using accuracy and confusion matrices.
  - Computed feature importances from the Random Forest model to identify key predictors.

## Summary of the results

- There is a weak negative correlation between hospital overall rating and excess readmission ratio: higher-rated hospitals tend to have slightly lower readmission ratios, but the relationship is not strong.
- Hospital ownership shows clearer differences: proprietary (for-profit) hospitals generally have higher excess readmission ratios compared to non-profit and government hospitals.
- Nearly all hospitals in the HRRP dataset are acute care hospitals, so hospital type does not explain much variation.
- The Random Forest model achieved about 60% accuracy on the Kaggle readmission dataset. It predicts non-readmissions better than true readmissions, reflecting the difficulty and class imbalance of the problem.
- Important predictors of readmission include:
  - Number of lab procedures
  - Number of medications
  - Length of stay (time_in_hospital)
  - Diagnosis categories and medical specialty  
  These features capture patient complexity and illness severity.

## How to run

### 1. Clone the repository

```bash
git clone https://github.com/wblimjr8/dsci510_fall2025_final_project.git
cd dsci510_fall2025_final_project