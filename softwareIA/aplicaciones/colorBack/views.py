from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from sklearn.externals import joblib
from os import remove
import json

# Create your views here.
import numpy as np
 
def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))
 
def sigmoid_derivada(x):
    return sigmoid(x)*(1.0-sigmoid(x))
 
def tanh(x):
    return np.tanh(x)
 
def tanh_derivada(x):
    return 1.0 - x**2

def reLU(x):
    return x * (x > 0)

def dReLU(x):
    return 1. * (x > 0)
 
 
class NeuralNetwork:
 
    def __init__(self, layers, activation='tanh'):
        if activation == 'sigmoid':
            self.activation = sigmoid
            self.activation_prime = sigmoid_derivada
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_prime = tanh_derivada
        else:
            self.activation = reLU
            self.activation_prime = dReLU
 
        # inicializo los pesos
        self.weights = []
        self.deltas = []
        # capas = [2,3,2]
        # rando de pesos varia entre (-1,1)
        # asigno valores aleatorios a capa de entrada y capa oculta
        for i in range(1, len(layers) - 1):
            r = 2*np.random.random((layers[i-1] + 1, layers[i] + 1)) -1
            self.weights.append(r)
        # asigno aleatorios a capa de salida
        r = 2*np.random.random( (layers[i] + 1, layers[i+1])) - 1
        self.weights.append(r)
 
    def fit(self, X, y, learning_rate=0.2, epochs=100000):
        # Agrego columna de unos a las entradas X
        # Con esto agregamos la unidad de Bias a la capa de entrada
        ones = np.atleast_2d(np.ones(X.shape[0]))
        X = np.concatenate((ones.T, X), axis=1)
        
        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]
 
            for l in range(len(self.weights)):
                    dot_value = np.dot(a[l], self.weights[l])
                    activation = self.activation(dot_value)
                    a.append(activation)
            # Calculo la diferencia en la capa de salida y el valor obtenido
            error = y[i] - a[-1]
            deltas = [error * self.activation_prime(a[-1])]
            
            # Empezamos en el segundo layer hasta el ultimo
            # (Una capa anterior a la de salida)
            for l in range(len(a) - 2, 0, -1): 
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_prime(a[l]))
            self.deltas.append(deltas)
 
            # invertir
            # [level3(output)->level2(hidden)]  => [level2(hidden)->level3(output)]
            deltas.reverse()
 
            # backpropagation
            # 1. Multiplcar los delta de salida con las activaciones de entrada 
            #    para obtener el gradiente del peso.
            # 2. actualizo el peso restandole un porcentaje del gradiente
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)
 
            if k % 10000 == 0: print('epochs:', k)
 
    def predict(self, x): 
        ones = np.atleast_2d(np.ones(x.shape[0]))
        a = np.concatenate((np.ones(1).T, np.array(x)), axis=0)
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a
 
    def print_weights(self):
        print("LISTADO PESOS DE CONEXIONES")
        for i in range(len(self.weights)):
            print(self.weights[i])
 
    def get_deltas(self):
        return self.deltas


def crearRed(id):
    error = 0
    try:

        clf = NeuralNetwork([3,3,1],activation ='tanh')
        nombre = 'modelo_' + str(id) + '_entrenadeo.pkl'
        path = 'softwareIA/aplicaciones/colorBack/files/' + nombre
        joblib.dump(clf, path)
    
    except:
        error = 1

    return error

def findPath(idRed):

    nombre = 'modelo_' + str(idRed) + '_entrenadeo.pkl'
    path = 'softwareIA/aplicaciones/colorBack/files/' + nombre

    return path

def entrenarRed(idRed, color, texto):
    try:
        #buscar ruta 
        path = findPath(idRed)

        # y obtener la red
        clf = joblib.load(path)

        #armar lista de color
        esto = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        listaInfo =[ ((int(esto[0]))/255) , ((int(esto[1]))/255), ((int(esto[2]))/255)]

        X = np.array([listaInfo])


        #armar text color
        if texto == 'Negro':
            y = np.array([[1]]) 
        else:
            y = np.array([[0]]) 

        

        #entrenar red 
        clf.fit(X, y, learning_rate=0.03,epochs=15001)
        joblib.dump(clf, path)
        #mostrar info de entrenamiento
        index=0
        for e in X:
            print("X:",e,"y:",y[index],"Network:",clf.predict(e))
            index=index+1
    except:
        return 1

    return 0


def consultRedIA(request,id,color):
    textColor = consultIA(id,color)
    data = {
        'Red': id,
        'BackgroundColor': color,
        'TextColor': textColor,
    }
    return HttpResponse(json.dumps(data),content_type="aplication/json")

def consultIA(id,color):

    #armar lista y matriz de paso
    esto = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    listaInfo = [ ((int(esto[0]))/255) , ((int(esto[1]))/255), ((int(esto[2]))/255)] #0-1
    
    X = np.array([listaInfo])


    #obtener la red sgun id
    clf = joblib.load(findPath(id))

    #predict segun la lista en la primera posicion del array
    print(X[0])
    res = clf.predict(X[0])
    print(res)



    #evaluar resultado
    res = abs(res)
    print(res)
    if res < 0.5:
        tipoColor = 'White'
    else:
        tipoColor = 'Black'
    
    return tipoColor


   
def deleteRedIA(id): 
    res = 0
    try:
        remove(findPath(id)) #meterle try cath
    except:
        res = 1

    return res