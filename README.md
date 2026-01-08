# Sales Performance Analysis Web App

### Probabilistic & Behavioral Insights with Streamlit

## Overview

This project is a **Streamlit-based web application** designed to analyze **sales performance using probabilistic and behavioral metrics**.
It allows users to upload a sales dataset and interactively explore performance outcomes such as success rates, conditional probabilities, streak behavior, and distribution patterns.

The application is built with a **data science workflow mindset**—from ingestion and validation to metric computation and visualization—ensuring reliable, interpretable insights.

---

## Objectives

* Analyze sales outcomes using **probability-based metrics**
* Identify **patterns in success and failure**
* Provide **clean summaries and visual insights**
* Ensure **robust handling of incomplete or invalid inputs**

---

## Methodology & App Architecture

The application is structured into **six logical phases**, reflecting a standard analytical pipeline.

---

### **Phase 1: App Setup & User Input**

This phase initializes the Streamlit application and collects essential user inputs.

**Key Actions**

* Set app title and instructions
* Allow user selection (e.g., sales agent or entity)
* Enable dataset upload (CSV or Excel)

**Purpose**
To establish a valid starting point for analysis. All downstream processes depend on successful input selection and file upload.

---

### **Phase 2: Data Ingestion & Cleaning**

The uploaded dataset is read, validated, and minimally cleaned to ensure analytical consistency.

**Process Includes**

* Automatic file type detection (`.csv` or `.xlsx`)
* Schema validation for required columns:

  * `status`
  * `client`
  * `product`
  * `amount`
* Exception handling to prevent pipeline failure

**Purpose**
To guarantee data integrity and prevent misleading metrics due to missing or malformed data.

---

### **Phase 3: Core Performance Metrics**

This phase computes the core probabilistic and behavioral metrics used in the analysis.

**Metrics Computed**

* Success vs failure rates
* Client-type win rates
* Conditional win probabilities
* Longest success and failure streaks
* Spread and frequency measures

**Purpose**
To transform raw transactional data into **interpretable performance indicators** that explain sales behavior.

---

### **Phase 4: Summary Table**

All computed metrics are aggregated into a structured summary table.

**Purpose**

* Provide a centralized analytical narrative
* Support users who prefer tabular, metric-driven insights
* Serve as a foundation for interpretation and reporting

---

### **Phase 5: Data Visualization**

The app generates visual representations using the cleaned dataset.

**Visuals Include**

* Histograms
* Bar charts

**Purpose**
To reveal distribution patterns, performance concentration, and comparative trends that may not be obvious from tables alone.

---

### **Phase 6: Guardrails for Incomplete Input**

The application enforces logical guardrails to prevent unintended execution.

**Examples**

* Prevents analysis if no valid user/entity is selected
* Prompts corrective action before proceeding

**Purpose**
To maintain a clean user experience and avoid invalid or misleading outputs.

---

## Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Matplotlib / Streamlit visual components**

---

## Expected Dataset Format

The dataset should include (at minimum):

| Column Name | Description                               |
| ----------- | ----------------------------------------- |
| status      | Outcome indicator (e.g., success/failure) |
| client      | Client identifier or type                 |
| product     | Product or service sold                   |
| amount      | Transaction value                         |

---

## How to Run the App

```bash
pip install streamlit pandas numpy
streamlit run app.py
```

Upload a valid dataset when prompted and interact with the analysis through the web interface.

---

## Key Takeaways

* Demonstrates a **structured analytical pipeline**
* Emphasizes **probabilistic reasoning in sales analysis**
* Balances **technical rigor with usability**
* Suitable for **business intelligence, sales analytics, and data science portfolios**

---

## Future Enhancements

* Advanced probabilistic modeling (e.g., Markov chains)
* Time-series trend analysis
* Exportable reports
* User-defined metric selection

---
