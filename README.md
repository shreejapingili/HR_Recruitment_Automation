# HR Recruitment Reporting Automation System

## Project Overview

The HR Recruitment Reporting Automation System is an end-to-end automation project designed to streamline recruitment reporting and analytics processes. Organizations often receive hundreds of candidate applications, making manual tracking and reporting time-consuming and error-prone. This project automates candidate data processing, validation, KPI calculation, report generation, and dashboard creation to provide actionable recruitment insights.

The solution uses Python for data processing and automation, OpenPyXL for Excel report generation, and Power BI for interactive dashboard visualization.

---

## Business Problem

HR teams spend significant time manually:

* Collecting candidate application data
* Validating candidate information
* Tracking recruitment metrics
* Preparing recruitment reports
* Monitoring hiring performance

Manual reporting can lead to delays, inconsistencies, and limited visibility into recruitment effectiveness.

This project addresses these challenges by automating the complete recruitment reporting workflow.

---

## Objectives

* Automate candidate data processing
* Validate and clean recruitment datasets
* Calculate recruitment KPIs automatically
* Generate Excel-based recruitment reports
* Produce recruiter summary reports
* Visualize recruitment performance using Power BI
* Reduce manual reporting effort and improve decision-making

---

## Technologies Used

### Programming & Automation

* Python
* Pandas
* OpenPyXL

### Reporting & Visualization

* Microsoft Excel
* Power BI

### Additional Concepts

* Data Validation
* Data Cleaning
* KPI Analysis
* Process Automation
* Logging & Error Handling

---

## Dataset Information

The dataset contains candidate recruitment records including:

| Column           |
| ---------------- |
| Candidate_ID     |
| Name             |
| Department       |
| Position         |
| Interview_Status |
| Offer_Status     |
| Joining_Status   |

The project processes 500+ candidate records for recruitment analysis.

---

## Data Validation Performed

The automation pipeline validates:

* Missing candidate names
* Missing department information
* Duplicate candidate records
* Invalid recruitment statuses
* Data consistency checks

---

## Data Cleaning

The system automatically:

* Removes duplicate records
* Handles missing values
* Standardizes recruitment status values
* Creates a cleaned dataset for analysis

---

## Recruitment KPIs Calculated

### Application Metrics

* Total Applications

### Selection Metrics

* Selected Candidates
* Interview Conversion Rate

### Offer Metrics

* Offers Released
* Offer Acceptance Rate

### Joining Metrics

* Joined Candidates
* Joining Rate

### Department Metrics

* Department-wise Hiring Distribution

---

## Automated Outputs

### Recruitment Excel Report

Generated automatically using OpenPyXL and includes:

* Total Applications
* Selected Candidates
* Offers Released
* Joined Candidates
* Recruitment KPI Summary

### Recruiter Summary Report

Automatically generated text report containing recruitment statistics and hiring performance summaries.

### Process Logs

Execution logs are generated for monitoring and troubleshooting automation runs.

---

## Power BI Dashboard

### Dashboard Features

#### KPI Cards

* Total Applications
* Selected Candidates
* Offers Released
* Joined Candidates
* Interview Conversion Rate
* Offer Acceptance Rate

#### Visualizations

* Recruitment Funnel
* Department-wise Hiring Analysis
* Interview Status Distribution
* Offer Status Distribution
* Joining Status Analysis
* Position-wise Applications
* Department vs Position Matrix
* Hiring Heatmap
* Recruitment Trends

#### Interactive Filters

* Department
* Position
* Interview Status

---

## Business Insights Generated

The dashboard enables HR teams to:

* Monitor recruitment funnel performance
* Identify departments with highest hiring activity
* Track candidate drop-off rates
* Analyze offer acceptance trends
* Measure recruitment efficiency
* Improve hiring decision-making




