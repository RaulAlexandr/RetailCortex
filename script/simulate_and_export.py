import pandas as pd

df = pd.read_csv("../data/output/predicted_demand.csv")

def simulate_transport_budget(df, percent_change=20):
    df['transport_cost_per_unit'] *= (1 + percent_change / 100)
    df['profit_margin'] = df['price_per_unit'] - df['transport_cost_per_unit'] - df['staff_cost_per_unit']
    return df

df_sim = simulate_transport_budget(df.copy(), percent_change=10)
df_sim.to_csv("../data/output/simulation_result.csv", index=False)
print("Simulation result saved to simulation_result.csv")
