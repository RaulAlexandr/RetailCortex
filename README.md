# RetailCortex: AI-Driven Forecasting & Simulation Suite (Simulated Retail Project)

This repository delivers an end-to-end **forecasting and decision intelligence platform** for multi-store retail chains, focused on **sales prediction, scenario simulation, and operational optimization**.

RetailCortex was developed as a personal initiative to demonstrate the structure, modeling flow, and business logic of a production-ready AI forecasting platform. 
All data and simulations are synthetic, but the codebase reflects how such a solution would be delivered in a real-world client engagement under NDA.

---

## Project Context

Retail chains often face crucial decisions like:

- How many units will sell next week?
- What if we reallocate budgets or close a store?
- Can we simulate the impact of operational actions before we act?

**RetailCortex** answers these questions through predictive modeling, simulation utilities, and visual dashboards — enabling data-driven operations across multiple stores.

This public version uses **synthetic data only**. 

---

## Tech Stack

- **Python 3.11**
- **Pandas**, **NumPy**, **scikit-learn**, **XGBoost**
- **Joblib** for model persistence
- **MLflow** for experiment tracking
- **Streamlit** for interactive dashboards

---

## Workflow

1. **Data Integration**
   - Unified CSV ingestion: sales, logistics, HR, budget, stock
   - Resulting master dataset: ~787,000 rows, 15+ engineered features

2. **Feature Engineering**
   - Lag values, rolling averages, % changes, day-of-week, store/product encoding

3. **Model Training**
   - **XGBRegressor** for next-week demand forecasting
   - **RandomForestClassifier** for transfer stock recommendation
   - **LogisticRegression** for promo budget increase decisions

4. **MLflow Tracking**
   - Parameters, metrics (MAE, RMSE, F1), versioning, and artifacts

5. **Operational Simulations**
   - `simulate_budget_change(store_id, delta)`
   - `simulate_store_closure(store_id)`

6. **Streamlit Dashboard**
   - Upload data, simulate scenarios, view KPIs, export results

7. **Deployment-Ready Scripts**
   - `predict_demand.py`, `simulate_and_export.py`, `send_alerts.py`

---

## Project Structure

- **RetailCortex/**
  - **app/**
    - `dashboard.py`
  - **data/**
    - `master_df_test_simulated.csv`
    - **processed/**
      - `master_df.csv`
    - **raw/**
      - `budget.csv`
      - `hr.csv`
      - `logistics.csv`
      - `sales.csv`
      - `stock_operations.csv`
  - **mlruns/**  _(MLflow tracking folders)_
  - **model/**
    - `classifier_rf_stock.model`
    - `log_model_promo_budget.joblib`
    - `log_model_scaler.joblib`
    - `regressor_xgb.model`
  - **notebooks/**
    - `notebook.ipynb`
  - **script/**
    - `predict_demand.py`
    - `send_alerts.py`
    - `simulate_and_export.py`

---

## Results Snapshot

Despite relying on synthetic data without true ground truth, the models captured robust patterns:

### 🔍 Model Results Summary

| Model               | Task                             | Metric   | Value |
|---------------------|----------------------------------|----------|-------|
| **XGBoost**         | Demand forecast (regression)     | MAE      | ~13.6 |
| **XGBoost**         | Demand forecast (regression)     | RMSE     | ~18.5 |
| **Random Forest**   | Stock transfer (classification)  | F1-Score | ~0.84 |
| **Logistic Reg.**   | Promo increase decision          | F1-Score | ~0.71 |

> These scores are based on **synthetic simulation data** and serve illustrative purposes only.  
> In real-world implementations using a similar architecture, performance was **significantly higher**, with MAE values below 4 and F1-scores consistently exceeding 0.93.

---

## Project Disclaimer

This project was designed as a simulation of a real-world AI solution for retail decision support.  
All data used is synthetic and all components have been rebuilt or simplified for public sharing.

The repository is intended for demonstration and educational purposes.  
While inspired by real operational challenges, it does not include proprietary data, confidential logic, or production infrastructure.

Several functionalities have been streamlined to focus on architecture clarity and modeling flow.

---

## How to Use

```bash 
# Launch dashboard
streamlit run app/dashboard.py

# Predict demand from test CSV
python scripts/predict_demand.py --input data/test_sample.csv --output data/predictions.csv
```

---

## Want Something Similar?

Need a pipeline that doesn't just model but solves business pain-points? I design:

- End-to-end forecasting platforms
- Simulation-based decision tools
- Lightweight data-to-insight pipelines
- Custom automation for internal ops

Contact: raul.devx@protonmail.com
