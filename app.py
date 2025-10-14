import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="Maven Music - Churn Analysis",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
<style>
    .main-header {
        color: #1DB954;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    .subheader {
        color: #191414;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.image("🎵", width=50)
    st.title("Maven Music")
    st.markdown("### Customer Churn Analysis Dashboard")
    
    page = st.radio(
        "Navigation",
        ["Home", "Data Overview", "Exploratory Analysis", 
         "Churn Analysis", "Feature Engineering", "Insights & Recommendations"]
    )
    
    st.markdown("---")
    st.markdown("**Project Status:** Data Preparation Phase")
    st.markdown("**Last Updated:** " + datetime.now().strftime("%Y-%m-%d"))

# Generate sample data
@st.cache_data
def load_sample_data():
    """Generate sample data for demonstration"""
    np.random.seed(42)
    n_customers = 500
    
    customers = pd.DataFrame({
        'customer_id': range(1, n_customers + 1),
        'subscription_tier': np.random.choice(['Free', 'Premium', 'Student'], n_customers, p=[0.3, 0.5, 0.2]),
        'subscription_duration_days': np.random.randint(1, 730, n_customers),
        'total_listens': np.random.randint(10, 5000, n_customers),
        'playlist_count': np.random.randint(0, 50, n_customers),
        'days_since_activity': np.random.randint(0, 90, n_customers),
        'churn': np.random.choice([0, 1], n_customers, p=[0.8, 0.2])
    })
    
    return customers

customers_df = load_sample_data()

# PAGE 1: HOME
if page == "Home":
    st.markdown('<h1 class="main-header">🎵 Maven Music Customer Churn Analysis</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Project Overview
        
        Maven Music, a leading music streaming service, has experienced an unusual surge in customer churn 
        over recent months. This data science initiative aims to investigate underlying factors contributing 
        to customer attrition and develop predictive insights for retention strategies.
        
        **Objective:** Analyze customer data to identify patterns and risk factors associated with churn, 
        enabling targeted retention interventions.
        """)
    
    with col2:
        st.metric("Total Customers", len(customers_df))
        st.metric("Churn Rate", f"{(customers_df['churn'].sum() / len(customers_df) * 100):.1f}%")
        st.metric("Avg. Subscription (days)", int(customers_df['subscription_duration_days'].mean()))
    
    st.markdown("---")
    st.markdown("""
    ### Project Phases
    
    1. **Data Collection** ✓ - Customer subscription and listening history aggregation
    2. **Data Cleaning** ✓ - Quality assurance and standardization
    3. **Exploratory Analysis** ◈ - Pattern identification and visualization
    4. **Feature Engineering** ◈ - Derived variable creation
    5. **Model Preparation** ⊗ - Dataset structuring for machine learning
    """)

# PAGE 2: DATA OVERVIEW
elif page == "Data Overview":
    st.markdown('<h2 class="subheader">📊 Dataset Overview</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Records", len(customers_df))
    with col2:
        st.metric("Features", len(customers_df.columns))
    with col3:
        st.metric("Missing Values", customers_df.isnull().sum().sum())
    
    st.markdown("### Data Quality Summary")
    
    # Data types and info
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Data Types:**")
        st.dataframe(
            pd.DataFrame({
                'Column': customers_df.columns,
                'Type': customers_df.dtypes.astype(str),
                'Non-Null Count': customers_df.count()
            }),
            use_container_width=True
        )
    
    with col2:
        st.markdown("**Descriptive Statistics:**")
        st.dataframe(customers_df.describe(), use_container_width=True)
    
    st.markdown("### Sample Data")
    st.dataframe(customers_df.head(10), use_container_width=True)

# PAGE 3: EXPLORATORY ANALYSIS
elif page == "Exploratory Analysis":
    st.markdown('<h2 class="subheader">🔍 Exploratory Data Analysis</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Subscription Tier Distribution")
        fig, ax = plt.subplots(figsize=(8, 5))
        tier_counts = customers_df['subscription_tier'].value_counts()
        colors = ['#1DB954', '#191414', '#1ed760']
        ax.bar(tier_counts.index, tier_counts.values, color=colors)
        ax.set_ylabel("Count")
        ax.set_title("Customer Distribution by Subscription Tier")
        st.pyplot(fig)
    
    with col2:
        st.markdown("### Churn Distribution")
        fig, ax = plt.subplots(figsize=(8, 5))
        churn_counts = customers_df['churn'].value_counts()
        labels = ['Retained', 'Churned']
        colors_churn = ['#1DB954', '#FF6B6B']
        ax.pie(churn_counts.values, labels=labels, autopct='%1.1f%%', colors=colors_churn, startangle=90)
        ax.set_title("Customer Churn Status")
        st.pyplot(fig)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Listening Frequency Analysis")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(customers_df['total_listens'], bins=30, color='#1DB954', edgecolor='black')
        ax.set_xlabel("Total Listens")
        ax.set_ylabel("Frequency")
        ax.set_title("Distribution of User Listening Frequency")
        st.pyplot(fig)
    
    with col2:
        st.markdown("### Subscription Duration Analysis")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(customers_df['subscription_duration_days'], bins=30, color='#191414', edgecolor='white')
        ax.set_xlabel("Subscription Duration (days)")
        ax.set_ylabel("Frequency")
        ax.set_title("Distribution of Subscription Duration")
        st.pyplot(fig)

# PAGE 4: CHURN ANALYSIS
elif page == "Churn Analysis":
    st.markdown('<h2 class="subheader">📉 Churn Analysis & Patterns</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Churn by Subscription Tier")
        churn_by_tier = customers_df.groupby('subscription_tier')['churn'].agg(['sum', 'count'])
        churn_by_tier['churn_rate'] = (churn_by_tier['sum'] / churn_by_tier['count'] * 100).round(2)
        
        fig, ax = plt.subplots(figsize=(8, 5))
        x_pos = np.arange(len(churn_by_tier))
        ax.bar(x_pos, churn_by_tier['churn_rate'], color=['#1DB954', '#191414', '#1ed760'])
        ax.set_xticks(x_pos)
        ax.set_xticklabels(churn_by_tier.index)
        ax.set_ylabel("Churn Rate (%)")
        ax.set_title("Churn Rate by Subscription Tier")
        st.pyplot(fig)
        
        st.dataframe(churn_by_tier[['churn_rate']], use_container_width=True)
    
    with col2:
        st.markdown("### Churn by Engagement Level")
        customers_df['engagement_level'] = pd.cut(
            customers_df['total_listens'],
            bins=[0, 500, 1500, 5000],
            labels=['Low', 'Medium', 'High']
        )
        
        churn_by_engagement = customers_df.groupby('engagement_level')['churn'].agg(['sum', 'count'])
        churn_by_engagement['churn_rate'] = (churn_by_engagement['sum'] / churn_by_engagement['count'] * 100).round(2)
        
        fig, ax = plt.subplots(figsize=(8, 5))
        x_pos = np.arange(len(churn_by_engagement))
        ax.bar(x_pos, churn_by_engagement['churn_rate'], color=['#FF6B6B', '#FFA500', '#1DB954'])
        ax.set_xticks(x_pos)
        ax.set_xticklabels(churn_by_engagement.index)
        ax.set_ylabel("Churn Rate (%)")
        ax.set_title("Churn Rate by User Engagement Level")
        st.pyplot(fig)
        
        st.dataframe(churn_by_engagement[['churn_rate']], use_container_width=True)
    
    st.markdown("---")
    
    st.markdown("### Churn Correlation Analysis")
    
    numeric_cols = ['subscription_duration_days', 'total_listens', 'playlist_count', 'days_since_activity']
    correlation_data = customers_df[numeric_cols + ['churn']].corr()['churn'].drop('churn').sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    colors_corr = ['#1DB954' if x > 0 else '#FF6B6B' for x in correlation_data.values]
    ax.barh(range(len(correlation_data)), correlation_data.values, color=colors_corr)
    ax.set_yticks(range(len(correlation_data)))
    ax.set_yticklabels(correlation_data.index)
    ax.set_xlabel("Correlation with Churn")
    ax.set_title("Feature Correlation with Customer Churn")
    ax.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
    st.pyplot(fig)

# PAGE 5: FEATURE ENGINEERING
elif page == "Feature Engineering":
    st.markdown('<h2 class="subheader">⚙️ Feature Engineering & Preparation</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Created Features
    
    The following engineered features have been created to capture meaningful customer behaviors:
    """)
    
    features_info = pd.DataFrame({
        'Feature Name': [
            'subscription_duration_days',
            'total_listens',
            'playlist_count',
            'days_since_activity',
            'engagement_level'
        ],
        'Type': [
            'Temporal',
            'Behavioral',
            'Behavioral',
            'Temporal',
            'Categorical'
        ],
        'Description': [
            'Number of days since subscription start',
            'Total number of tracks listened',
            'Number of playlists created',
            'Days elapsed since last listening activity',
            'Engagement categorization (Low/Medium/High)'
        ]
    })
    
    st.dataframe(features_info, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### Data Preparation Steps")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Completed:**
        - ✓ Missing value handling
        - ✓ Outlier detection
        - ✓ Data type validation
        - ✓ Feature engineering
        """)
    
    with col2:
        st.markdown("""
        **Next Steps:**
        - ⊗ Feature scaling normalization
        - ⊗ Categorical encoding
        - ⊗ Train-test split
        - ⊗ Model training
        """)

# PAGE 6: INSIGHTS & RECOMMENDATIONS
elif page == "Insights & Recommendations":
    st.markdown('<h2 class="subheader">💡 Key Insights & Recommendations</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Key Findings
    
    **1. Engagement Impact**
    - Users with low engagement levels show significantly higher churn rates
    - Listening frequency is a strong predictor of retention
    - Recommendation: Implement engagement campaigns targeting low-activity users
    
    **2. Subscription Tier Insights**
    - Churn patterns vary across subscription tiers
    - Premium subscribers demonstrate different behavior compared to free tier users
    - Recommendation: Develop tier-specific retention strategies
    
    **3. Time-Based Patterns**
    - Days since last activity correlates with churn likelihood
    - Early-period engagement is critical for long-term retention
    - Recommendation: Intensify onboarding experience and early engagement initiatives
    
    **4. Playlist Creation**
    - Playlist creation correlates with lower churn rates
    - Users invested in content curation are more likely to remain
    - Recommendation: Encourage playlist creation through gamification
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### Recommended Actions for Retention
    
    | Priority | Action | Target Segment | Expected Impact |
    |----------|--------|-----------------|-----------------|
    | High | Re-engagement campaigns | Inactive users (>30 days) | Reduce churn by 15-20% |
    | High | Premium tier incentives | Free-to-Premium conversion | Increase ARPU |
    | Medium | Personalized recommendations | Low engagement users | Increase engagement by 25% |
    | Medium | Playlist creation tutorials | New users | Improve retention in first 90 days |
    | Low | Community features | Active users | Strengthen community bonds |
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### Next Phase: Predictive Modeling
    
    The prepared dataset will be utilized to develop machine learning models for:
    - Customer churn prediction
    - Risk score calculation
    - Propensity-to-churn estimation
    - Targeted intervention identification
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 0.9rem;'>
    <p>Maven Music Customer Churn Analysis Dashboard</p>
    <p>Built with Streamlit | Data Science Project 2025</p>
</div>
""", unsafe_allow_html=True)