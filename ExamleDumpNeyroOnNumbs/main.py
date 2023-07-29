import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


training_in = np.array([[0, 0, 1],
                        [1, 1, 1],
                        [1, 0, 1],
                        [0, 1, 1]])
training_out = np.array([[0, 1, 1, 0]]).T
np.random.seed(1)

synaptic_weights = 2 * np.random.random((3, 1)) - 1

print('случайные веса:')
print(synaptic_weights)
for i in range(20000): #многократная пргонка весов для обучения нейронки
    input_layer = training_in
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    err = training_out-outputs
    adjustments = np.dot(input_layer.T, err *(outputs*(1-outputs)))

    synaptic_weights+= adjustments

print("веса после обучения")
print(synaptic_weights)

print("результат:")
print(outputs)

new_inputs = np.array([1,1,0]) # новая ситуация
output = sigmoid(np.dot(new_inputs, synaptic_weights))

print("новая ситуация:")
print(output)