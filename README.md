# Beyond the First Click: Funnel Retention & Predictive CLV Strategy (SQL + Power BI + Python + Streamlit)

## TL;DR
**Problem:** Revenue growth depends on retaining high-value customers, but revenue concentration and churn exposure were not clearly quantified.

**Approach:**
* Modeled customer funnel stages using SQL
* Identified revenue concentration and leakage points
* Built a **Random Forest** model to predict **Customer Lifetime Value (CLV)**
* Deployed an **AI-style Streamlit** simulator for business insight generation

**Result:** 
- **8% of customers** generate **45% of total revenue**
- **$3.49M** in revenue exposed to churn risk
- **43%** of revenue linked to customers showing churn signals
- **Top 20 high-value customers** identified using predictive CLV modeling

**Business Impact:**
Shift from reactive churn reporting → proactive revenue prioritization

## Dashboard Preview
Power BI dashboard with:
- Customer segmentation
- Repeat-purchase patterns
- Fraud overlaps
- Revenue-at-risk

Designed as a quick-scan interface for stakeholder decision-making.

![crm dashboard preview](crm_dashboard_preview.png)

## Table of Contents
 * [Overview](#overview)
 * [Tools Used](#tools-used)
 * [Dataset Snapshot](#dataset-snapshot)
 * [Key Funnel Insights & Business Impact](#key-funnel-insights--business-impact)
 * [Strategic Implications](#strategic-implications)
 * [AI-Powered CLV Insight Simulator (Streamlit)](#ai-powered-clv-insight-simulator-streamlit)
 * [What I'd Explore Next](#what-id-explore-next)
 * [What This Project Demonstrates](#what-this-project-demonstrates)
 * [Strategic Takeaway](#strategic-takeaway)
 * [Let's Connect](#lets-connect)

## Overview
This project analyzes the full **e-commerce customer lifecycle**, from acquisition to repeat purchase behavior, and quantifies revenue concentration, churn exposure, and retention leverage points.

The workflow includes:
* SQL-based funnel and cohort segmentation
* Revenue-at-risk analysis
* Fraud and churn overlay detection
* Predictive Customer Lifetime Value (CLV) modeling
* Deployment of an AI-style decision-support app

**The Goal:** Enable data-driven retention strategies that maximize long-term profitability.

## Tools Used
- **MySQL:** Funnel & segmentation logic
- **Microsoft Excel:** Data cleaning and validation
- **Power BI:** Dashboard design, and storytelling
- **Scikit-Learn (Random Forest):** Predictive CLV modeling
- **Streamlit:** Deployment of interactive insight simulator

## Dataset Snapshot
```markdown
|Metric                  |Value       |
|------------------------|------------|
|Total Customers         | 4529       |
|Average Age             | 48.1 Years |
|Number of Countries     | 10         |
|Average Order Value     | 108.54     |
|Average Orders/Customer | 10.02      |
```

## Key Funnel Insights & Business Impact
**Funnel Concentration**
* A small **high-value funnel segment (8%)** contributes nearly half of total revenue.
* These users sit deeper in the funnel but still show elevated churn risk → retention priority. 

**Funnel Leakage (Revenue at Risk)**
> Churn risk was defined as customers with declining purchase frequency and extended inactivity beyond the cohort median.

* **43% of revenue** comes from customers showing churn signals.
* Indicates drop-offs after initial conversion, not acquisition issues.

**Risk Overlay (Fraud + Churn)**
* Fraud flags cluster around late-stage funnel users with declining engagement.
* Suggests disengagement and risk rise together, impacting profitability.

**Category Funnel Performance**
* Home & Sports show strong repeat conversion.
* Fashion shows high entry but weaker funnel progression → acquisition-heavy, retention-light.

## Strategic Implications
* Prioritize retention campaigns for high-value churn-risk segments
* Reallocate marketing budget from acquisition-heavy categories (Fashion) to retention-strengthened categories
* Introduce fraud monitoring checkpoints in the late-stage funnel for users

## AI-Powered CLV Insight Simulator (Streamlit)
An interactive web application was built to simulate AI-generated business insights for the top 20 predicted high-value customers.

The app: 
* Displays predicted high-CLV customers
* Visualizes CLV distribution
* Generates marketing and retention recommendations
* Demonstrates deployment of analytics into a usable business interface

Live App : [Launch App](https://shrey0561-beyond-the-first-click-custome-genai-simulator-ryznlg.streamlit.app/)

This bridges analytics and product thinking, moving beyond dashboards into deployable insight systems.

## What I'd Explore Next
- **LTV Prediction Modeling:** Estimate customer lifetime value using purchase patterns
- **Retention Simulation:** Test loyalty-program changes and model uplift scenarios
- **Win-back analysis:** Identify traits of customers who return after churning

## What This Project Demonstrates
* End-to-end customer analytics workflow (SQL → BI → ML → Deployment)
* Revenue-focused segmentation and funnel analysis
* Ability to quantify churn exposure and revenue concentration
* Application of machine learning to business value prediction
* Translation of predictive outputs into stakeholder-facing tools
* Product mindset: deploying insights, not just analyzing data

## Strategic Takeaway
Instead of treating churn as a reporting metric, this project reframes retention as a revenue optimization problem.
By identifying high-value customers early and quantifying revenue at risk, businesses can:
* Allocate marketing budget more efficiently
* Prioritize retention over broad acquisition
* Reduce revenue volatility
* Improve long-term customer profitability

## Let's Connect
I'm building my career in data analytics and love uncovering business insights through customer behavior and segmentation. Feel free to reach out via:

* [GitHub](https://github.com/Shrey0561)
* [LinkedIn](https://www.linkedin.com/in/shreya-srinath-879a66205/)
* [Notion](https://www.notion.so/Data-Analyst-Portfolio-221ebe151fdd801e9445e32590b67758?source=copy_link)

I'm always open to conversations, mentorship, or entry-level opportunities.
