import pandas as pd
from regression import Regression

x = Regression()
df_predict = pd.read_csv('x_test_v2.csv').fillna(0).astype(int)

# READ DATASET
df = pd.read_csv("trips_summary_covid_pub.csv")
df['date'] = pd.to_datetime(df['date'])

# FILTER PRE AND POST PANDEMIC
df['pre_covid'] = (df.date < "12/19/2020").astype("int")
df_pre_covid = df.loc[df.pre_covid == 1]
df = df.loc[df.pre_covid == 0]
df = df.loc[df['total_revenue'] > 0]
df_pre_covid = df_pre_covid.loc[df_pre_covid['total_revenue'] > 0]


# TOTAL REVENUE MODEL
x.select_cols = ['pickup_community_area', 'hour', 'total_revenue']
x.dummy_cols = ['pickup_community_area', 'hour']
x.y_col = 'total_revenue'

res_revenue = x.poisson_regression(df, 0.7)

# TOTAL REVENUE PRE COVID
x.select_cols = ['pickup_community_area', 'hour', 'total_revenue']
x.y_col = 'total_revenue'

res_revenue_pre = x.poisson_regression(df_pre_covid, 0.7)

# TOTAL COUNT MODEL
x.select_cols = ['pickup_community_area', 'hour', 'count']
x.y_col = 'count'

res_count = x.poisson_regression(df, 0.7)

# TOTAL COUNT PRE COVID
x.select_cols = ['pickup_community_area', 'hour', 'count']
x.y_col = 'count'

res_count_pre = x.poisson_regression(df_pre_covid, 0.7)

# TOTAL SECONDS MODEL
x.select_cols = ['pickup_community_area', 'hour', 'trip_seconds_tot']
x.y_col = 'trip_seconds_tot'

res_seconds = x.poisson_regression(df, 0.7)

# TOTAL TIP MODEL
x.select_cols = ['pickup_community_area', 'hour', 'tip_tot']
x.y_col = 'tip_tot'

res_tip = x.poisson_regression(df, 0.7)

print(res_revenue)
print(res_revenue_pre)
print(res_count)
print(res_count_pre)
print(res_seconds)
print(res_tip)

# df_predict_cases['cases'] = scaler.transform(df_predict_cases['cases'].values.reshape(-1,1))

y_rev = res_revenue['model'].predict(df_predict)
y_rev_pre = res_revenue_pre['model'].predict(df_predict)
y_count = res_count['model'].predict(df_predict)
y_count_pre = res_count_pre['model'].predict(df_predict)
y_sec = res_seconds['model'].predict(df_predict)
y_tip = res_tip['model'].predict(df_predict)

df_predict['rev_post'] = y_rev
df_predict['rev_pre'] = y_rev_pre
df_predict['count_post'] = y_count
df_predict['count_pre'] = y_count_pre
df_predict['seconds'] = y_sec
df_predict['tip'] = y_tip

df_predict['rev_per_trip'] = df_predict['rev_post'] / df_predict['count_post']
df_predict['rev_per_trip_pre'] = df_predict['rev_pre'] / df_predict['count_pre']
df_predict['sec_per_trip'] = round(df_predict['seconds'] / df_predict['count_post'],)
df_predict['tip_per_trip'] = df_predict['tip'] / df_predict['count_post']
df_predict['diff_pre_post'] = df_predict['rev_per_trip'] - df_predict['rev_per_trip_pre']

df_predict.to_csv('poisson_output.csv')














