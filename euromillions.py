import requests
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import numpy as np

# from propiedades import obtener_propiedades_numeros

# Obtener datos de Euromillones
url = "https://euromillions.api.pedromealha.dev/draws"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
data = response.json()

# PROCESANDO
numeros_sin_espacio = []
for resultado in data:
    numeros = resultado["numbers"]
    numeros_sin_espacio.append(numeros)
# print(numeros_sin_espacio)
# Now, numeros_sin_espacio contains lists of integers instead of strings


# Obtener propiedades de los números
# propiedades_numeros = obtener_propiedades_numeros(numeros_sin_espacio)


# Imprimir las propiedades
# for propiedades_numero in propiedades_numeros:
#     print(f"Número: {propiedades_numero['numero']}")
#     print(f"Es par: {propiedades_numero['es_par']}")
#     print(f"Es impar: {propiedades_numero['es_impar']}")
#     print(f"Es primo: {propiedades_numero['es_primo']}")
#     print(f"Es entero: {propiedades_numero['es_entero']}")
#     print(f"Es natural: {propiedades_numero['es_natural']}")
#     print("Es racional:", propiedades_numero["es_racional"])
#     print("Es irracional:", propiedades_numero["es_irracional"])
#     print("Es real:", propiedades_numero["es_real"])
#     print("Es compuesto:", propiedades_numero["es_compuesto"])
#     print("Es positivo:", propiedades_numero["es_positivo"])
#     print("Es negativo:", propiedades_numero["es_negativo"])
#     print("Es decimal finito:", propiedades_numero["es_decimal_finito"])
#     print("Es cardinal:", propiedades_numero["es_cardinal"])
#     print("Es ordinal:", propiedades_numero["es_ordinal"])

# numeros_tf = tf.constant(numeros_sin_espacio, dtype=tf.int32)

# Verificar la forma del tensor
# print("Forma del tensor:", numeros_tf.shape)

# # Imprimir el tensor
# print("Tensor:")
# print(numeros_tf)

# Etiquetas (lo que intentamos predecir, en este caso, el próximo conjunto de números)
etiqueta_entrenamiento = [
    10,
    20,
    41,
    43,
    45,
    2,
    12,
]  # o cualquier otro conjunto de números
# Crear datos de entrada
X_entrenamiento = np.array(numeros_sin_espacio, dtype=np.int32)

# Etiquetas de entrenamiento (lo que intentamos predecir, en este caso, el próximo conjunto de números)
y_entrenamiento = np.array(
    [
        [10, 20, 41, 43, 45]
        # Agrega más conjuntos según sea necesario
    ],
    dtype=np.int32,
)

# Ajustar etiquetas para tener la misma cantidad de muestras que X_entrenamiento
replicado_y = np.tile(
    y_entrenamiento, (X_entrenamiento.shape[0] // y_entrenamiento.shape[0] + 1, 1)
)
y_entrenamiento = replicado_y[: X_entrenamiento.shape[0], :]

# Verificar las formas de los datos
print("Forma de X_entrenamiento:", X_entrenamiento.shape)
print("Forma de y_entrenamiento:", y_entrenamiento.shape)

# Crear el modelo para predecir un conjunto de 5 números
model = Sequential()
model.add(Dense(128, input_dim=5, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dense(5, activation="linear"))  # Ajustar el número de neuronas a 5

# Compilar el modelo
model.compile(
    optimizer=Adam(learning_rate=0.00001),
    loss="mean_squared_error",
    metrics=["mse"],
)

# Entrenar el modelo
model.fit(X_entrenamiento, y_entrenamiento, epochs=300, verbose=1)

# Datos para hacer predicciones (puedes usar otros datos para evaluar el modelo)
datos_prediccion = np.array([[10, 20, 41, 43, 45]], dtype=np.int32)

# Hacer predicciones
prediccion = model.predict(datos_prediccion)

# Imprimir la predicción
print("Predicción:", prediccion)
