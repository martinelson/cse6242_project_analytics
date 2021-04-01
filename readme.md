**Base Case - No Date Filter**

| df = df **NO FILTER** |                  |                              |             |
|-----------------------|------------------|------------------------------|-------------|
| Dep. Variable:        | total_revenue    | R-squared (uncentered):      | 0.655       |
| Model:                | OLS              | Adj. R-squared (uncentered): | 0.655       |
| Method:               | Least Squares    | F-statistic:                 | 1.203e+04   |
| Date:                 | Thu, 01 Apr 2021 | Prob (F-statistic):          | 0.00        |
| Time:                 | 09:52:18         | Log-Likelihood:              | -6.8208e+06 |
| No. Observations:     | 734002           | AIC:                         | 1.364e+07   |
| Df Residuals:         | 733886           | BIC:                         | 1.364e+07   |
| Df Model:             | 116              |                              |             |
| Covariance Type:      | nonrobust        |                              |             |
|                       |                  |                              |             |


**Test Case 1 - Before the Pandemic**
| df = df[df.date < "12/1/2019"] |                  |                              |             |
|--------------------------------|------------------|------------------------------|-------------|
| Dep. Variable:                 | total_revenue    | R-squared (uncentered):      | 0.727       |
| Model:                         | OLS              | Adj. R-squared (uncentered): | 0.727       |
| Method:                        | Least Squares    | F-statistic:                 | 4901.       |
| Date:                          | Thu, 01 Apr 2021 | Prob (F-statistic):          | 0.00        |
| Time:                          | 09:46:58         | Log-Likelihood:              | -1.8228e+06 |
| No. Observations:              | 198393           | AIC:                         | 3.646e+06   |
| Df Residuals:                  | 198285           | BIC:                         | 3.647e+06   |
| Df Model:                      | 108              |                              |             |
| Covariance Type:               | nonrobust        |                              |             |
|                                |                  |                              |             |

**Test case 2 - After the pandemic**
| df = df[df.date >  "12/1/2019"] **AFTER THE PANDEMIC** |                  |                              |             |
|--------------------------------------------------------|------------------|------------------------------|-------------|
| Dep. Variable:                                         | total_revenue    | R-squared (uncentered):      | 0.631       |
| Model:                                                 | OLS              | Adj. R-squared (uncentered): | 0.631       |
| Method:                                                | Least Squares    | F-statistic:                 | 8079.       |
| Date:                                                  | Thu, 01 Apr 2021 | Prob (F-statistic):          | 0.00        |
| Time:                                                  | 09:57:15         | Log-Likelihood:              | -4.9815e+06 |
| No. Observations:                                      | 534317           | AIC:                         | 9.963e+06   |
| Df Residuals:                                          | 534204           | BIC:                         | 9.964e+06   |
| Df Model:                                              | 113              |                              |             |
| Covariance Type:                                       | nonrobust        |                              |             |
|                                                        |                  |                              |             |