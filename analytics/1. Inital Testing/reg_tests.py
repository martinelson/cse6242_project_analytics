
import numpy as np
import pandas as pd
from main import trip_regression
from statsmodels.tools.eval_measures import rmse


# set variables for model
select_cols = ['pickup_community_area', 'hour', 'week_day', 'total_revenue_log']
dummy_cols = ['pickup_community_area', 'hour', 'week_day']
y_col = 'total_revenue_log'
df = pd.read_csv("trips_summary_sql.csv")
covid_filter = False
random_filter = True
log_linear = True

if covid_filter:
    # filtering out the pandemic
    df['date'] = pd.to_datetime(df['date'])
    df['pre_covid'] = (df.date < "12/1/2019").astype("int")
    df = df.loc[df.pre_covid == 1]

if log_linear:
    df['total_revenue_log'] = np.log10(df['total_revenue'])

reg_model, reg_results, reg_x, reg_y = trip_regression(0.7, df, select_cols, dummy_cols, y_col, random_filter)

y_prediction = reg_results.predict(reg_x)

rmse_calc = rmse(reg_y, y_prediction)

print(rmse_calc)