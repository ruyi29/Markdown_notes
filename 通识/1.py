import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# features = [2,5,8,8,13,15,17,19,21,24]
# target = [12,31,45,52,79,85,115,119,135,145]

features = np.array([2,5,8,8,13,15,17,19,21,24]).reshape(-1, 1)
target = np.array([12,31,45,52,79,85,115,119,135,145]).reshape(-1, 1)

# 绘制散点图
plt.scatter(features, target)
plt.xlabel('Features')
plt.ylabel('Target')
plt.title('Scatter Plot')
plt.show()

# 简单线性回归
regression = LinearRegression()  
model = regression.fit(features,target)

# 预测
new_feature = np.array([10]).reshape(-1, 1)  
# new_feature是一个包含新特征值的NumPy数组。这个数组可以是一维数组或多维数组，但需要通过.reshape(-1, 1)方法将其转换为二维数组形式
print(model.predict(new_feature))