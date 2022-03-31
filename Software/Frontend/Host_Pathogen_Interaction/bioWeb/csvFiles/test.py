x=[1,2,3,4,5,6,7,8,9,10,100]
mi=5
ma=15

y = [mi+t*((ma-mi)/(max(x)-min(x))) for t in x]
print(y)