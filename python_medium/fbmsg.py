import pandas as pd
import numpy as np

df_concat = pd.concat(
    [
        fb_messages[["user1", "msg_count"]],
        fb_messages[["user2", "msg_count"]].rename(columns={"user2": "user1"}),
    ],
    axis=0,
)
df1 = df_concat.groupby(["user1"])["msg_count"].sum().reset_index()
df1["rank"] = df1["msg_count"].rank(ascending=False)
result = df1[df1["rank"] <= 10][["user1", "msg_count"]].sort_values(
    "msg_count", ascending=False
)
