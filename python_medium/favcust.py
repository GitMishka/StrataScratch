import pandas as pd


df = pd.merge(customers, orders, left_on='id', right_on='cust_id')


df = df[df['total_order_cost'] >= 100]
df = df =  (
    df.groupby(["id_x", "first_name", "city"])
    .agg({"id_y": "count", "total_order_cost": "sum"})
    .reset_index()
)
result = df[(df["id_y"] > 3) & (df["total_order_cost"] > 100)].drop(columns=['id_x'])