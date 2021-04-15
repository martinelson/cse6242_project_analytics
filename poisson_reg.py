import pandas as pd
import numpy as np
from patsy.highlevel import dmatrices
import statsmodels.api as sm

select_cols = ['date', 'year', 'month', 'week_year', 'day_year', 'hour', 'pickup_community_area', 'count']
df = pd.read_csv("trips_summary_sql.csv")
df = df[select_cols]
df['date'] = pd.to_datetime(df['date'])
covid_filter = False

if covid_filter:
    # filtering out the pandemic
    df['pre_covid'] = (df.date < "12/1/2019").astype("int")
    df = df.loc[df.pre_covid == 0]

df = df.set_index('date')

split = np.random.rand(len(df)) < 0.85

df_train = df[split]

df_test = df[~split]

print(len(df_train))
print(len(df_test))

patsy_exp = """count~ month + week_year + day_year + hour + pickup_community_area"""

y_train, X_train = dmatrices(patsy_exp, df_train, return_type='dataframe')
y_test, X_test = dmatrices(patsy_exp, df_test, return_type='dataframe')

poisson_train = sm.GLM(y_train, X_train, family=sm.families.Poisson()).fit()

print(poisson_train.summary())

poisson_test = poisson_train.get_prediction(X_test)
poisson_test_summary = poisson_test.summary_frame()

print(poisson_test_summary)










