class Perceptron:
    def __init__(self, neuron1_weight, neuron2_weight, bias_weight):
        self.learning_rate = 1
        self.bias = 1
        self.weights = {
            'neuron1': neuron1_weight,
            'neuron2': neuron2_weight,
            'bias': bias_weight
        }

    def calculate_output(self, input1, input2):
        return input1 * self.weights['neuron1'] + input2 * self.weights['neuron2'] + self.bias * self.weights['bias']
    
    def apply_activation_function(self, output):
        return 1 if output > 0 else 0
    
    def recalculate_weights(self, input1, input2, output, expected_output):
        error = expected_output - output
        self.weights['neuron1'] += error * input1 * self.learning_rate
        self.weights['neuron2'] += error * input2 * self.learning_rate
        self.weights['bias'] += error * self.bias * self.learning_rate

    def learn(self, input1, input2, expected_output):
        output = self.calculate_output(input1, input2)
        output = self.apply_activation_function(output)
        self.recalculate_weights(input1, input2, output, expected_output)

    def test(self, input1, input2):
        output = self.calculate_output(input1, input2)
        output = self.apply_activation_function(output)
        print(f'Output: {input1} xor {input2} is {output}')

        return output
