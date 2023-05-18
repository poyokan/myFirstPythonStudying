"""
coding utf-8
2021-9-30
"""

import numpy as np
from scipy import integrate


""" 
def sumsub(x,y):
    return x+y,x-y


#frompyfuncで新たな関数を作成
new_func = np.frompyfunc(sumsub,2,2)

#ndarrayを2つ作成
x = np.array([1,2,3])
y = np.array([3,2,1])

#frompyfuncで作った関数を使用
sum,sub = new_func(x,y)

print(sum,type(sum))
print(sub,type(sub))

 """


# def test(tuple2D):
#     print(tuple2D[0],tuple2D[1])

#     return 0

# test((1,2))

# test_vec = np.vectorize(test)
# test_vec([(3,4),(5,6)])





"""
参考
https://www.python.ambitious-engineer.com/archives/1333
"""




