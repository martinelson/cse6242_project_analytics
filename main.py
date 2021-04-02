import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import lintest


def trip_regression(train_split, df, select_cols, dummy_cols, y_col, random_filter):
    # reading in dataset and dropping columns

    df = df[select_cols]
    print(df.head())
    # categorical / dummy variables
    df = pd.get_dummies(df, columns=dummy_cols, drop_first=True)

    # splitting data
    np.random.seed(0)

    if random_filter:
        df_train, df_test = train_test_split(df, train_size=train_split, test_size=1-train_split, random_state=100)

        y_train = df_train[y_col]
        x_train = df_train.drop(y_col, axis=1)
        y_test = df_test[y_col]
        x_test = df_test.drop(y_col, axis=1)

    else:
        y = df[y_col]
        x = df.drop(y_col, axis=1)

        x_train = x[:int(x.shape[0] * train_split)]
        x_test = x[int(x.shape[0] * train_split):]
        y_train = y[:int(x.shape[0] * train_split)]
        y_test = y[int(x.shape[0] * train_split):]

    # fit model via sm
    model = sm.OLS(y_train, x_train)
    results = model.fit()
    print(results.summary())

    lintest.linearity_test(model, y_train, 2000)
    return model, results, x_train, y_train

