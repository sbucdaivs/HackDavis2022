from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

class CSVDataset():
    # load the dataset
    def __init__(self, path):
        # load the csv file as a dataframe
        df = read_csv(path)
        # store the inputs and outputs
        self.X = df.values[:, :-1]
        self.y = df.values[:, -1]
        # ensure input data is floats
        self.X = self.X.astype('float32')
        self.scaler = MinMaxScaler()
        self.scaler.fit(self.X)
        self.X = self.scaler.transform(self.X)
        # label encode target and ensure the values are floats
        y_int = []
        for val in self.y:
          if val == "low risk":
            y_int.append(0)
          if val == "mid risk":
            y_int.append(1)
          if val == "high risk":
            y_int.append(2)

        self.y = y_int

 
    # get indexes for train and test rows
    def get_splits(self, n_test=0.2):
        return train_test_split(self.X, self.y, test_size=0.2, random_state=42)

class ML_Model():

    def train_model(self):
        path = 'MaternalHealth.csv'
        self.dataset = CSVDataset(path)
        X_train, X_test, y_train, y_test = self.dataset.get_splits()
        self.clf = svm.SVC()
        # clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=50)
        self.clf.fit(X_train, y_train)
        y_pred = self.clf.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        # reg = LinearRegression().fit(X_train, y_train)

    def predict(self, patient_data):
        
        if len(patient_data[patient_data < self.dataset.scaler.data_min_]) > 0: return 2
        print(patient_data[patient_data > self.dataset.scaler.data_max_])
        if len(patient_data[patient_data > self.dataset.scaler.data_max_]) > 0: return 2

        patient_data = self.dataset.scaler.transform(patient_data)
        return self.clf.predict(patient_data)[0]
# # evaluate the model
# # y_pred = reg.predict(X_test)
# y_pred = clf.predict(X_test)
# # y_pred = [round(x) for x in y_pred]
# print(accuracy_score(y_test, y_pred))