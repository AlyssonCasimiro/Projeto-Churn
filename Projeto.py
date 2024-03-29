# Tensorflow, Theano e Keras já foram instalados previamente

# Importando as bibliotecas
import numpy as np

import pandas as pd

import keras
from keras.models import Sequential
from keras.layers import Dense

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

# Importando os dados
dataset = pd.read_csv('Churn_Modelling.csv')

# Matriz de variaveis que influenciam no resultado
X = dataset.iloc[:,3:13].values
# Resultado
y = dataset.iloc[:, 13].values

# Resolvendo dados categoricos
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])

onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

# Dummy Variable Trap
X = X[:, 1:]



# Dividindo o dataset em treino e teste | treino = 80% e teste = 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# PEGA O TEST!!!! 

# Feature Scaling - Para evitar dominância entre variáveis, então trazemos todas a uma mesma magnitude
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Iniciando a Rede
classifier = Sequential()

# Implementando a primeira cabada e a primeira camada
# output_dim = (input + output) / 2 = 12/2 = 6
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 11))

# Implementando a segunda camada 
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))

# Implementando nossa saida
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

# Preparando nossa rede
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Rodando o treino
# Padrão 32 x 10
classifier.fit(X_train, y_train, batch_size = 32, nb_epoch = 10)

# Aplicando o modelo ao teste
y_pred = classifier.predict(X_test)

# Separando os que tem probabilidade maior que 0.5
y_pred = (y_pred > 0.5)

# PEGA O Y_PRED!!!

# Verificando os resultados

cm = confusion_matrix(y_test, y_pred)

# Validar!