
#Implementation of single neuron
# inputs =[1, 2, 3, 4]
# weights = [0.2, 0.8, -0.5, 0.3]
# bias = 2
# output= 0
# for i in range(len(inputs)):
#     output += inputs[i]*weights[i]
# print(output + bias)
# -----------------------------------

#Implementation of 4 inputs and 3 neurons

# inputs = [1, 2, 3, 4]
# weights = [[0.2, 0.8, 0.5, 1.0], [0.2, 0.8, 0.5, 1.0],[0.2, 0.8, 0.5, 1.0]]
# biases = [2, 2, 2]
# outputs = []
# for neuron_weights, neuron_bias in zip(weights, biases):
#     neuron_op = 0
#     for n_input, weight in zip(inputs, neuron_weights):
#         neuron_op += n_input*weight
#     outputs.append(neuron_op + neuron_bias)
#
#
# print(outputs)

# ----------------------------
# import numpy as np
#
# lol = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
# print(lol.shape)


# -----------------------------------

# Dot product

import numpy as np
# inputs = [1, 2, 3, 4]
# weight = [0.1, 0.2, 0.3, 0.4]
# bias = 1
#
# output = np.dot(weight, inputs) + bias
# print(output)
# ---------------------

# Dot product in a layer
#
# inputs = [1, 2, 3, 4]
# weights = [[0.1, 0.2, 0.3, 0.4],[0.1, 0.2, 0.3, 0.4],[0.1, 0.2, 0.3, 0.4]]
# biases = [1, 1, 1]
#
# op = np.dot(weights, inputs) + biases
# print(op)

# -------------------------------------------------