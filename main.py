import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from process_data import set_index, process_data
from model import train_model

train_data = pd.read_csv('dataset/train.csv')
test_data = pd.read_csv('dataset/test.csv')

set_index(train_data, 'Id')
set_index(test_data, 'Id')

x_train = process_data(train_data)
y_train = process_data(test_data)

Y = train_data['SalePrice']
x_train.drop(['SalePrice'], axis =1, inplace = True)

print("Shape of x_train is :", x_train.shape)
print("Shape of Y is :", Y.shape)

train_model(x_train, Y)
