# Вычислить число Пи c заданной точностью d

import math
d = int(input('Введить кол-во знаков после запятой: '))
print(round(math.pi, d))