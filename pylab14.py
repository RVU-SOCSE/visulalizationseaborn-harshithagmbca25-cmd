Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:/Users/RVUW268/OneDrive/Desktop/14prog_5ds_salaries.csv")
df.columns
Index(['work_year', 'experience_level', 'employment_type', 'job_title',
       'salary', 'salary_currency', 'salary_in_usd', 'employee_residence',
       'remote_ratio', 'company_location', 'company_size'],
      dtype='str')
df.skew(numeric_only=True)
work_year        -1.016374
salary           28.937932
salary_in_usd     0.536401
remote_ratio      0.149454
dtype: float64
df.kurt(numeric_only=True)
work_year           1.127965
salary           1147.567390
salary_in_usd       0.834006
remote_ratio       -1.925036
dtype: float64
sns.histplot(df["salary"])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sns.histplot(df["salary"])
NameError: name 'sns' is not defined
sns.histplot(df["salary"])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sns.histplot(df["salary"])
NameError: name 'sns' is not defined
>>> import seaborn as sns
>>> sns.histplot(df["salary"])
<Axes: xlabel='salary', ylabel='Count'>
>>> plt.show()
>>> sns.histplot(df["salary"],kde=True)
<Axes: xlabel='salary', ylabel='Count'>
>>> plt.show()
>>> sns.distplot(df["salary"])

Warning (from warnings module):
  File "<pyshell#13>", line 1
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

<Axes: xlabel='salary', ylabel='Density'>
>>> 
>>> import pandas as pd
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> df2 = pd.read_csv(r"C:/Users/RVUW268/OneDrive/Desktop/10prog_4laptops.csv")
>>> sns.pairplot(df2)
<seaborn.axisgrid.PairGrid object at 0x0000025853B39FD0>
>>> plt.show()
>>> 
