
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import forestci
import pandas as pd

features = lambda d: d.values[:,1:]
outcome = lambda d: d.values[:,0]

data:pd.DataFrame = pd.read_parquet("data.parquet").fillna(0)
train,test = train_test_split(data,shuffle=False)
print(features(train).shape)
print(features(test).shape)
classifier = RandomForestClassifier().fit(features(train), outcome(train))

out = test.copy()

out["preds"] = classifier.predict(features(test))
out["ci"] = forestci.random_forest_error(classifier, features(train), features(test))

had_pred = out.loc[(slice(None,None),481),:]
