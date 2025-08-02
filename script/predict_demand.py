import pandas as pd
from joblib import load
import xgboost as xgb

df = pd.read_csv("../data/processed/master_df.csv")

features = [
    'units_sold', 'stock_level', 'promo_effectiveness', 'transport_efficiency',
    'staff_cost_per_unit', 'lag_units_sold', 'roll3_units_sold',
    'day_of_week', 'is_weekend', 'season', 'store_id_encoded', 'product_id_encoded'
]

X = df[features].dropna()
model = xgb.XGBRegressor()
model.load_model("../model/regressor_xgb.model")
df['predicted_units_next_week'] = model.predict(X)

df.to_csv("../data/output/predicted_demand.csv", index=False)
print("Demand predictions saved to predicted_demand.csv")
