import numpy as np
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LinearRegression, PoissonRegressor


class Regression:
    def __init__(self):
        self.select_cols = []
        self.dummy_cols = []
        self.y_col = ''

    def get_split(self, df, split):
        df_train = df[split]
        df_test = df[~split]
        y_train = df_train[self.y_col]
        x_train = df_train.drop(self.y_col, axis=1)
        y_test = df_test[self.y_col]
        x_test = df_test.drop(self.y_col, axis=1)
        return y_train, x_train, y_test, x_test

    def time_split(self, df):

        df = df[self.select_cols]
        df = pd.get_dummies(df, columns=self.dummy_cols, drop_first=True)
        y = df[self.y_col]
        x = df.drop(self.y_col, axis=1)

        results = {}
        i = 0
        n_splits = 5
        tscv = TimeSeriesSplit(n_splits)
        for fold, (train_index, test_index) in enumerate(tscv.split(x)):
            X_train, X_test = x.iloc[train_index], x.iloc[test_index]
            y_train, y_test = y.iloc[train_index], y.iloc[test_index]
            model = LinearRegression()
            res = model.fit(X_train, y_train)
            results[str(i)] = {'parameters': {X_train.columns[j]: res.coef_[j] for j in range(len(res.coef_))},
                               'rsquared': res.score(X_train, y_train), 'intercept': res.intercept_}
            i += 1
        return results

    def poisson_regression(self, df, split=0.7):
        split = np.random.rand(len(df)) < split
        df = df[self.select_cols]
        df = pd.get_dummies(df, columns=self.dummy_cols, drop_first=True)
        y_train, x_train, y_test, x_test = self.get_split(df, split)
        model = PoissonRegressor()
        result = model.fit(x_train, y_train)
        x_train.to_csv('x_train.csv')
        result_dict = {'model': result, 'score': result.score(x_train, y_train), 'intercept': result.intercept_,
                       'parameters': {x_train.columns[j]: result.coef_[j] for j in range(len(result.coef_))}}
        return result_dict


















