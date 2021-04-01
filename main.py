import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import statsmodels.api as sm


# creating scaling and regression model variables
model = linear_model.LinearRegression()
train_split = 0.7
test_split = 0.3

# reading in dataset and dropping columns
df = pd.read_csv("trips_summary_sql.csv")

#filtering out the pandemic
df = df[df.date < "12/1/2019"]

drop_cols = ['date', 'year', 'week_year', 'day_year', 'count', 'fare_tot', 'tip_tot', 'additional_tot', 'trip_total_tot']
df.drop(drop_cols, axis=1, inplace=True)

# categorical / dummy variables
dummy_cols = ['month', 'week_day', 'hour', 'pickup_community_area']
df = pd.get_dummies(df, columns=dummy_cols, drop_first=True)


# splitting data
np.random.seed(0)
df_train, df_test = train_test_split(df, train_size=train_split, test_size=test_split, random_state=100)


y_train = pd.DataFrame(df_train["total_revenue"])
x_train = df_train.drop('total_revenue', axis=1)
y_test = pd.DataFrame(df_test["total_revenue"])
x_test = df_test.drop('total_revenue', axis=1)

# vif of trip_miles over 86
x_train = x_train.drop('trip_miles_tot', axis=1)
x_test = x_test.drop('trip_miles_tot', axis=1)

# vif of trip_seconds over 10
x_train = x_train.drop('trip_seconds_tot', axis=1)
x_test = x_test.drop('trip_seconds_tot', axis=1)


# # fit the model
reg = model.fit(x_train, y_train)
coefs = reg.coef_
print(coefs)
intercept = reg.intercept_
print(intercept)
score = reg.score(x_train, y_train)
print(score)
# prediction = reg.predict(x_test)

# fit model via sm
model = sm.OLS(y_train, x_train)
results = model.fit()
print(results.params)
print(results.summary())

# LEFT TODO:
# plot error distribution












