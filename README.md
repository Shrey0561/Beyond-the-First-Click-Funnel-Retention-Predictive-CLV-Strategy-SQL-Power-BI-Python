# Beyond the First Click: Customer Funnel & Retention Analysis (Power BI + SQL) 

## TL;DR
**Problem:** Revenue growth depends on retaining high-value customers, but churn-prone funnel segments were not clearly quantified.

**Process:** Modeled customer funnel stages and segmented users by churn and fraud risk to identify revenue concentration and leakage points.

**Result:** 
- **8% of customers** drive **45% of revenue**
- **$3.49M** in revenue exposed to churn risk
- Category-level funnel weaknesses identified

**Takeaway:** Funnel-based retention analysis reveals where customers drop off, which segments drive revenue, and where targeted retention strategies can deliver the highest ROI.

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
 * [GenAI Customer Insights Simulator](#genai-customer-insights-simulator)
 * [What I'd Explore Next](#what-id-explore-next)
 * [What This Project Demonstrates](#what-this-project-demonstrates)
 * [Let's Connect](#lets-connect)

## Overview
This project analyzes the **e-commerce customer funnel**, focusing on how users move from first purchase to repeat behavior and where revenue leakage occurs. Using SQL-based segmentation and a Power BI dashboard, I examined retention patterns, churn risk, fraud overlap, and category-level funnel performance to support business and marketing decision-making.

## Tools Used
- **MySQL:** Data modeling, cohort segmentation, churn & fraud logic
- **Microsoft Excel:** Data cleaning and validation
- **Power BI:** Dashboard design, interactivity, and storytelling

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
* Introduce fraud monitoring checkpoints in late-stage funnel users

## GenAI Customer Insights Simulator
Interactive Streamlit app showcasing top 20 predicted CLV customers.
Try it here: [Launch App](https://shrey0561-beyond-the-first-click-custome-genai-simulator-ryznlg.streamlit.app/)

## What I'd Explore Next
- **LTV Prediction Modeling:** Estimate customer lifetime value using purchase patterns
- **Retention Simulation:** Test loyalty-program changes and model uplift scenarios
- **Win-back analysis:** Identify traits of customers who return after churning

## What This Project Demonstrates
- Ability to build end-to-end customer analytics workflows (from SQL logic to Power BI dashboards)
- Exposure to segmentation, churn scoring, and fraud overlay techniques
- Understanding of how user behavior links to revenue risk and retention strategy
- Practice turning complex data into stakeholder-facing insights
- Ability to frame customer behavior through a funnel and retention lens, not just descriptive churn metrics

## Let's Connect
I'm building my career in data analytics and love uncovering business insights through customer behavior and segmentation. Feel free to reach out via:

* [GitHub](https://github.com/Shrey0561)
* [LinkedIn](https://www.linkedin.com/in/shreya-srinath-879a66205/)
* [Notion](https://www.notion.so/Data-Analyst-Portfolio-221ebe151fdd801e9445e32590b67758?source=copy_link)

I'm always open to conversations, mentorship, or entry-level opportunities.
