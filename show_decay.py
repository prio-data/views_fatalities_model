import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_parquet("data.parquet")
has_ged = (data
        .reset_index()
        .groupby("country_id")["ged"]
        .any()
        .reset_index()
        .values
        .astype(int)
    )

first_has_ged = data.loc[(slice(None,None), has_ged[has_ged[:,1].astype(bool),0][0]),:]
first_month = (first_has_ged
        .reset_index()
        .groupby("ged")["month_id"]
        .min()
        .reset_index()
        .values
        .astype(int)
    )
first_month = int(first_month[first_month[:,0].astype(bool),1])

plot_data = first_has_ged.loc[first_month-3:first_month+48]

fig = (sns
        .lineplot(x = "month_id", y = "ged_decay", data = plot_data)
        .get_figure()
        )

plt.axvline(first_month,0, 1, color="red")
plt.title("Line shows GED ns event")
plt.savefig("decay.png")
