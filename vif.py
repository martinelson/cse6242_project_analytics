from statsmodels.stats.outliers_influence import variance_inflation_factor


def vif_filtering(x):
    vif_df = pd.DataFrame()
    vif_df['variables'] = x.columns
    vif_df['VIF'] = [variance_inflation_factor(x.values, i) for i in range(x.shape[1])]
    return vif_df
