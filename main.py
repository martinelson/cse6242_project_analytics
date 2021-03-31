import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import linear_model
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm


# creating scaling and regression model variables
scaler = MinMaxScaler()
model = linear_model.LinearRegression()
train_split = 0.7
test_split = 0.3
vif_filter_value = 5

# reading in dataset and dropping columns
df = pd.read_csv("trips_summary_test.csv")

drop_cols = ['date', 'year', 'week_year', 'day_year', 'count', 'fare_tot', 'tip_tot', 'additional_tot', 'trip_total_tot']
df.drop(drop_cols, axis=1, inplace=True)

# categorical / dummy variables
dummy_cols = ['month', 'week_day', 'hour', 'pickup_community_area']
df = pd.get_dummies(df, columns=dummy_cols, drop_first=True)


# splitting data and scaling
np.random.seed(0)
df_train, df_test = train_test_split(df, train_size=train_split, test_size=test_split, random_state=100)

# scaling all numerical columns
scale_cols = ['trip_seconds_tot', 'trip_miles_tot', 'total_revenue']

df_train[scale_cols] = scaler.fit_transform(df_train[scale_cols])
df_test[scale_cols] = scaler.fit_transform(df_test[scale_cols])

print(df_train.head())

y_train = pd.DataFrame(df_train["total_revenue"])
x_train = df_train.drop('total_revenue', axis=1)
y_test = pd.DataFrame(df_test["total_revenue"])
x_test = df_test.drop('total_revenue', axis=1)


# checking multicollinearity via VIF
def vif_filtering(x):
    vif_df = pd.DataFrame()
    vif_df['variables'] = x.columns
    vif_df['VIF'] = [variance_inflation_factor(x.values, i) for i in range(x.shape[1])]
    return vif_df


# will need to take a look at VIF scores and remove until below a threshold
vif_x_train = vif_filtering(x_train)
vif_x_train = vif_x_train.sort_values(by="VIF", ascending=False)

# vif of trip_miles over 86
x_train = x_train.drop('trip_miles_tot', axis=1)
x_test = x_test.drop('trip_miles_tot', axis=1)


vif_x_train = vif_filtering(x_train)
vif_x_train = vif_x_train.sort_values(by="VIF", ascending=False)

# vif of trip_seconds over 10
x_train = x_train.drop('trip_seconds_tot', axis=1)
x_test = x_test.drop('trip_seconds_tot', axis=1)

vif_x_train = vif_filtering(x_train)
vif_x_train = vif_x_train.sort_values(by="VIF", ascending=False)

print(vif_x_train.head())

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












