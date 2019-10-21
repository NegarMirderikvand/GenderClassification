print ("Hello World")
from sklearn import tree
#[height,weight,shoe size]
X=[[181,80,44], [177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40]
    ,[155,60,38],[171,75,42],[181,85,43]]

Y= ['m','f','f','f','m','m','m','f','m','f','m']

clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)
prediction=clf.predict([[150,58,40]])
print(prediction)