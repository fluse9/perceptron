import random
from perceptron import Perceptron


neuron1_weight = random.random()
neuron2_weight = random.random()
bias_weight = random.random()
learning_iterations = 100
perceptron = Perceptron(neuron1_weight, neuron2_weight, bias_weight)

def learn():
    for _ in range(learning_iterations) :
        perceptron.learn(1, 1, 1)
        perceptron.learn(1, 0, 0)
        perceptron.learn(0, 1, 0)
        perceptron.learn(0, 0, 0)

def test():
    input1 = 0
    input2 = 1
    perceptron.test(input1, input2)

def run():
    test()
    learn()

run()