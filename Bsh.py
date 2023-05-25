import numpy as np
import scipy.stats as sts
from openpyxl import load_workbook
from statsmodels.stats.api import lilliefors

# здесь мы загружаем данные из экселя и формируем список
wb = load_workbook('tables.xlsx')
sheet = wb.get_sheet_by_name('Sheet 1')
data = sheet.values
data = list(data)
result = []
for i in data:
    result.append(i[0])
result.pop(0)

# задание 6
# Для математического ожидания
def mean_confidence_interval(x, gamma=0.95):
    x = np.asarray(x)
    n = len(x)
    a, s = np.mean(x), sts.sem(x)
    h = s * sts.t.ppf((1 + gamma) / 2, n - 1)
    return a - h, a + h


print(mean_confidence_interval(result))


#  Ответ: (-0.004735288942678219, 0.0032716149760495077)

# Для дисперсии
def var_confidence_interval(x, gamma=0.95):
    x = np.asarray(x)
    n = len(x)
    chi_1 = sts.chi2(df=n - 1).ppf((1 + gamma) / 2)
    chi_2 = sts.chi2(df=n - 1).ppf((1 - gamma) / 2)
    var = np.var(x, ddof=1)
    b1 = (n - 1) * var / chi_1
    b2 = (n - 1) * var / chi_2
    return b1, b2


print(var_confidence_interval(result))


#  Ответ: (0.001997499651831089, 0.0025367769990080613)


# задание 10 - уровень значимости гипотезы о нормальном законе распределения
k, p = lilliefors(result)
print('k: %.3f p-value: %.3f' % (k, p))
#  Ответ: k: 0.124 p-value: 0.001
