
import pandas as pd
import seaborn as sns

data = pd.read_parquet("data.parquet")
plot = sns.lineplot(x="month_id", y="ged_decay", hue = "country_id", data = data)
plot.get_figure().savefig("out.png")
