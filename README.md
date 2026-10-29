#  Maven Music, Customer Churn Analysis Dashboard

## Project Overview

Maven Music is an advanced analytics platform dedicated to investigating factors contributing to customer attrition in a music streaming service. This project integrates exploratory data analysis (EDA) techniques, feature engineering, and statistical visualization to identify behavioral patterns associated with user churn.

## Objectives

The initiative is grounded on the following academic and professional objectives:

- **Churn factor identification** : Determine behavioral and structural variables correlated with customer attrition
- **Comparative analysis** : Evaluate churn rates across subscription tiers and engagement levels
- **Feature engineering** : Construct derived variables capturing complex user dynamics
- **Strategic insights** : Develop quantified recommendations for retention interventions

## Key Features

###  Dashboard Pages

1. **Home** - Project overview and key synthetic metrics
2. **Data Overview** - Descriptive analysis and data quality assessment
3. **Exploratory Analysis** - Univariate and bivariate distributional visualizations
4. **Churn Analysis** - Segmented churn analysis by tier and engagement level
5. **Feature Engineering** - Documentation of created variables and preparation steps
6. **Insights & Recommendations** - Summary of findings and action plan

###  Technologies Used

- **Streamlit** : Interactive visualization framework
- **Pandas** : Data manipulation and transformation
- **NumPy** : Vectorized numerical computing
- **Matplotlib & Seaborn** : Statistical visualization
- **Python 3.8+** : Primary programming language

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or download the project**
   ```bash
   git clone <repository_url>
   cd maven-music-churn-analysis
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Activation (Windows)
   venv\Scripts\activate
   
   # Activation (macOS/Linux)
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Maven Music logo**
   - Name your image `maven_logo.png`
   - Place it in the project root directory

## Usage

### Launch the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

### Navigation

Use the sidebar to navigate between different analysis pages. Each page offers a distinct perspective on the churn phenomenon.

## Data Structure

### Dataset Variables

| Variable | Type | Description |
|----------|------|-------------|
| customer_id | Integer | Unique customer identifier |
| subscription_tier | Categorical | Subscription tier (Free, Premium, Student) |
| subscription_duration_days | Integer | Duration in days since registration |
| total_listens | Integer | Total number of tracks listened |
| playlist_count | Integer | Number of playlists created |
| days_since_activity | Integer | Days elapsed since last activity |
| churn | Binary | Churn status (0 = Retained, 1 = Churned) |

### Derived Variables

- **engagement_level** : Trinomial categorization based on listening frequency
- **churn_rate** : Proportion of users who churned by segment

## Key Findings

### Main Discoveries

1. **Engagement impact** : Low-engagement users exhibit significantly higher churn rates
2. **Tier variation** : Attrition patterns differ substantially across subscription tiers
3. **Critical window** : Prolonged inactivity (>30 days) is strongly associated with churn
4. **Curation effect** : Playlist creation correlates negatively with attrition

### Strategic Recommendations

| Priority | Action | Target Segment | Expected Impact |
|----------|--------|-----------------|-----------------|
| High | Re-engagement campaigns | Inactive users (>30 days) | Reduce churn by 15-20% |
| High | Premium tier incentives | Free-to-Premium conversion | Increase ARPU |
| Medium | Personalized recommendations | Low engagement users | +25% engagement |
| Medium | Playlist creation tutorials | New users | Improved 90-day retention |
| Low | Community features | Active users | Strengthen community bonds |

## Project Phases

- ✅ **Data Collection** - Historical aggregation of subscription data
- ✅ **Data Cleaning** - Quality assurance and standardization
- ◈ **Exploratory Analysis** - Pattern identification and visualizations
- ◈ **Feature Engineering** - Creation of derived variables
- ⊗ **Model Preparation** - Structuring for ML pipeline (upcoming)

## Code Architecture

```
maven-music-churn-analysis/
├── app.py                 # Main Streamlit application
├── maven_logo.png         # Maven Music logo
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── data/                  # Data directory (dynamically generated)
    └── sample_data.csv    # Sample data
```

## Future Extensions

1. **Predictive Modeling** : Development of classification models (Logistic Regression, Random Forest, XGBoost)
2. **Propensity Scoring** : Customer-level churn propensity score calculation
3. **Cohort Analysis** : Longitudinal tracking by registration cohort
4. **A/B Testing** : Evaluation of retention intervention strategies
5. **Automation** : ETL pipeline for daily/weekly data updates

## Recommended System Configuration

- **Processor** : Dual-core minimum
- **RAM** : 4 GB minimum (8 GB recommended)
- **Disk Space** : 500 MB minimum
- **Browser** : Chrome, Firefox, Safari (recent version)

## Troubleshooting

### Application fails to launch
```bash
# Verify Streamlit is properly installed
pip install --upgrade streamlit

# Relaunch the application
streamlit run app.py
```

### Logo error
- Ensure `maven_logo.png` is in the root directory
- Verify the filename matches exactly (case-sensitive)

### Slow performance
- Reduce dataset size in `load_sample_data()`
- Increase Python memory allocation
- Close other resource-intensive applications

## License

This project is provided for educational and professional purposes. All rights reserved to Maven Music.



---

**Last Updated** : October 2025  
**Version** : 1.0  
**Status** : Data Preparation Phase
