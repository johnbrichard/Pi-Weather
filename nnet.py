from typing import List

import numpy
# for sigmoid function
import scipy.special


class NeuralNetwork:

    # initialize network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.onodes = outputnodes
        self.hnodes = hiddennodes

        # link weight matrices, wih and who
        # weights inside arrays are w_i_j, where link is from node i to j in the next layer
        # w11 w21
        # w12 w22 etc
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # learning rate
        self.lr = learningrate

        #  activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    # train network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)

        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)

        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        # output layer error is the (target - actual)
        output_errors = targets - final_outputs

        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))

        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))
        pass

    # query network
    def query(self, inputs_list):
        #  convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T

        #  calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)

        #  calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        #  calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)

        #  calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


# set node number to be passed to NeuralNetwork object
input_nodes = 3
output_nodes = 3
hidden_nodes = 3

# set learning rate to 0.3
learning_rate = 0.3

# instantiate NeuralNetwork object
n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

testList = [1.0, 0.5, -1.5]

# test query (doesn't mean anything useful yet)
print(n.query([75, 34, 10]))
