import pandas as pd

df = pd.read_csv("../data/output/predicted_demand.csv")

alerts = df[df['predicted_units_next_week'] < 10]

if not alerts.empty:
    for _, row in alerts.iterrows():
        print(f"Alert: Low demand expected at Store {row['store_id']} for Product {row['product_id']} – Only {row['predicted_units_next_week']:.1f} units.")

else:
    print("No alerts. All products have sufficient demand.")
