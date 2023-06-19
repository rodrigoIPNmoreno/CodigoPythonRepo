#PARTE 1 CONSTRUIR MODELO DE CNN

#IMPORTAR LAS LIBRERIAS Y PAQUETES

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D # El otro tipo de capa que usa una red convolucional para reconocimiento de imágenes es MaxPooling2D(). Esta capa aplica un filtro que reduce la dimensionalidad de la imagen, esto es, la hace más pequeña. El objetivo es, por un lado, reducir el coste computacional.
from keras.layers import Flatten #La instrucción Flatten convierte los elementos de la matriz de imagenes de entrada en un array plano. Luego, con la instrucción Dense, añadimos una capa oculta (hidden layer) de la red neuronal
from keras.layers import Dense #cPosteriormente se usan el módulo Dense en conjunto con el método add para agregar entradas y salidas al modelo, así como la función de activación. El módulo SGD es un optimizador en Keras, y permite hacer uso del método del gradiente descendente para el entrenamiento del modelo

clasificador = Sequential()