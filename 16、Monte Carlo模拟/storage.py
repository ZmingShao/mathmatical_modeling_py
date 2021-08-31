#仓库管理问题，判定最佳进货量
from scipy.stats import poisson
a=2; b=3; lamda=10; p=1-a/b
u=poisson.ppf(1-a/b,lamda)  #求最佳订购量
p1=poisson.cdf(u-1,lamda)  #p1和p2是为验证最佳购进量
p2=poisson.cdf(u,lamda)
print(u,p1,p,p2)
