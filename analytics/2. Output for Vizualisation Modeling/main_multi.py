import pandas as pd
from regression import Regression

x = Regression()

df = pd.read_csv("trips_summary_covid_pub.csv")
df['date'] = pd.to_datetime(df['date'])
df['pre_covid'] = (df.date < "12/19/2020").astype("int")
df = df.loc[df.pre_covid == 0]


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
covid_cases = 1046

# INTERCEPT
i_revenue = result_revenue['intercept']
i_count = result_count['intercept']
i_seconds = result_seconds['intercept']
i_tip = result_tip['intercept']

# COVID CASES
p_revenue = result_revenue['coef']['cases'] * covid_cases
p_count = result_count['coef']['cases'] * covid_cases
p_seconds = result_seconds['coef']['cases'] * covid_cases
p_tip = result_tip['coef']['cases'] * covid_cases

for i in community:

    c_revenue = 0
    c_count = 0
    c_seconds = 0
    c_tip = 0

    # COMMUNITY AREA
    if i > 1:
        pickup_area = 'pickup_community_area_' + str(i)
        c_revenue = result_revenue['coef'][pickup_area]
        c_count = result_count['coef'][pickup_area]
        c_seconds = result_seconds['coef'][pickup_area]
        c_tip = result_tip['coef'][pickup_area]

    # HOUR
    for j in hours:
        hour_rev_val = 0
        hour_count_val = 0
        hour_second_val = 0
        hour_tip_val = 0

        if j > 0:
            hour = 'hour_' + str(j)
            hour_rev_val = result_revenue['coef'][hour]
            hour_count_val = result_count['coef'][hour]
            hour_second_val = result_seconds['coef'][hour]
            hour_tip_val = result_tip['coef'][hour]

        # WEEK
        for k in day_of_week:
            week_rev_val = 0
            week_count_val = 0
            week_second_val = 0
            week_tip_val = 0

            if k != 'Friday':
                week = 'week_day_' + k
                week_rev_val = result_revenue['coef'][week]
                week_count_val = result_count['coef'][week]
                week_second_val = result_seconds['coef'][week]
                week_tip_val = result_tip['coef'][week]

            revenue = round(i_revenue + p_revenue + c_revenue + hour_rev_val + week_rev_val,)
            count = round(i_count + p_count + c_count + hour_count_val + week_count_val,)
            seconds = round(i_seconds + p_seconds + c_seconds + hour_second_val + week_second_val,)
            tip = round(i_tip + p_tip + c_tip + hour_tip_val + week_tip_val,)

            row = {'community': i, 'hour': j, 'week_day': k, 'count': count,
                   'seconds': seconds, 'tip': tip, 'revenue': revenue}
            data.append(row)

df = pd.DataFrame(data)

df.to_csv('model_output.csv')