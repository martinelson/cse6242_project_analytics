
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from regression import Regression

scaler = MinMaxScaler()
x = Regression()

df = x.read_csv("trips_summary_covid_pub.csv")
df['date'] = pd.to_datetime(df['date'])
df['pre_covid'] = (df.date < "12/19/2020").astype("int")
df = df.loc[df.pre_covid == 0]
df['cases'] = scaler.fit_transform(df['cases'].values.reshape(-1,1))


# TOTAL REVENUE MODEL
x.select_cols = ['pickup_community_area', 'hour', 'week_day', 'cases', 'total_revenue']
x.dummy_cols = ['pickup_community_area', 'hour', 'week_day']
x.y_col = 'total_revenue'

res_revenue = x.time_split(df)

# TOTAL COUNT MODEL
x.select_cols = ['pickup_community_area', 'hour', 'week_day', 'cases', 'count']
x.y_col = 'count'

res_count = x.time_split(df)

# TOTAL SECONDS MODEL
x.select_cols = ['pickup_community_area', 'hour', 'week_day', 'cases', 'trip_seconds_tot']
x.y_col = 'trip_seconds_tot'

res_seconds = x.time_split(df)

# TOTAL TIP MODEL
x.select_cols = ['pickup_community_area', 'hour', 'week_day', 'cases', 'tip_tot']
x.y_col = 'tip_tot'

res_tip = x.time_split(df)

# AVERAGING FOLDS FUNCTION
def get_results(res):
    result = {'rsquared': 0, 'intercept': 0, 'coef': {}}
    for fold in res.keys():
        result['rsquared'] += res[fold]['rsquared']
        result['intercept'] += res[fold]['intercept']
        for k, v in res[fold]['parameters'].items():
            if k not in result['coef']:
                result['coef'][k] = v
            else:
                result['coef'][k] += v

    result['rsquared'] = result['rsquared'] / len(res)
    result['intercept'] = result['intercept'] / len(res)

    for k, v in result['coef'].items():
        result['coef'][k] = v / len(res)
    return result


# MODEL RESULTS
result_revenue = get_results(res_revenue)
print(result_revenue)
result_count = get_results(res_count)
print(result_count)
result_seconds = get_results(res_seconds)
print(result_seconds)
result_tip = get_results(res_tip)
print(result_tip)

# CONVERT TO CSV
data = []
community = [i+1 for i in range(77)]
hours = [i for i in range(24)]
day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# for i in community:














