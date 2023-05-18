
import numpy as np
from numpy import sin
from numpy import tan
from numpy import cos


degree = 12
length = 100

rad = np.deg2rad(degree)


a_sin = sin(rad)*length
a_cos = cos(rad)*length
a_tan = tan(rad)*length

print(f"{length}*sin({degree}degree):",a_sin)
print(f"{length}*cos({degree}degree):",a_cos)
print(f"{length}*tan({degree}degree):",a_tan)


