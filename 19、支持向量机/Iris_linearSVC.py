#使用线性支持向量机分类鸢尾花
from sklearn import datasets, svm
from sklearn.model_selection import GridSearchCV
import numpy as np
iris=datasets.load_iris()
x=iris.data; y=iris.target
clf=svm.LinearSVC(C=1,max_iter=10000)
clf.fit(x,y); yh=clf.predict(x); print(yh)
print("预测的准确率：",clf.score(x,y))
