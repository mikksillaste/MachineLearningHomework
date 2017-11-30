class SkrappyKNN():
    def fit(self, x_train, y_train):
        pass

    def predict(self, x_test):
        pass

from sklearn import datasets
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= .5)


# from sklearn.neighbors import KNeighborsClassifier

my_classifier = SkrappyKNN()

my_classifier.fit(x_train, y_train)

prediction = my_classifier.predict(x_test)

print (accuracy_score(y_test, prediction))