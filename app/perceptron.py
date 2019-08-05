import random

class Perceptron(object):
    data_gate = []
    weights = []
    umbral = 0
    learning_rate = 0
    learning = True
    iterations = 0
    gate = 'AND'

    def __init__(self, gate='AND' ,**kwargs):
        self.gate = gate
        self.data_gate = kwargs.get('data_gate', [])
        self.umbral = kwargs.get('umbral', random.random())
        self.weights = kwargs.get('weights', [random.random(), random.random()])
        self.learning_rate = kwargs.get('learning_rate', 0.1)

    def AND_GATE(self):
        self.data_gate = [[1,1,1], [1,0,0], [0,1,0], [0,0,0]]

    def OR_GATE(self):
        self.data_gate = [[1,1,1], [1,0,1], [0,1,1], [0,0,0]]

    def learn(self):
        self.__check_data()
        while self.learning:
            self.iterations = self.iterations + 1
            self.learning = False
            for pattern in self.data_gate:
                a = self.__calculate_total_input(pattern)
                y = self.__activation_function(a)
                d = self.__get_d(pattern)
                self.__change_weights(d, y, pattern)

    def view_net(self):
        for pattern in self.data_gate:
            d = self.__get_d(pattern)
            a = self.__calculate_total_input(pattern)
            y = self.__activation_function(a)
            print(f'{pattern[0]} {self.gate} {pattern[1]} = {d} PERCEPTRON: {y}')

    def print_hyperparameters(self):
        print(f'ITERATIONS: {self.iterations}')
        print(f'Weigth [0]:  {self.weights[0]}')
        print(f'Weigth [1]:  {self.weights[1]}')
        print(f'Umbral: {self.umbral}')
        print(f'Learning rate: {self.learning_rate}')
        print(f'DATA: {self.data_gate}')
    
    def __activation_function(self, a):
        if a > 0:
            return 1
        else:
            return 0

    def __calculate_total_input(self, pattern):
        a = 0
        entries = len(pattern) - 1
        for entry in range(entries):
            x = pattern[entry]
            w = self.weights[entry]
            a = a + self.__multiply_entry(x, w)
        return a + self.umbral
    
    def __change_weights(self, d, y, pattern):
        error = self.__calculate_error(d, y)
        if error != 0:
            entries = len(pattern) - 1
            for entry in range(entries):
                self.weights[entry] = self.__calculate_new_weight(self.weights[entry], error, pattern[entry])
            self.umbral = self.__calculate_new_umbral(self.umbral, error)
            self.learning = True

    def __calculate_new_umbral(self, last_umbral, error):
        return last_umbral + self.learning_rate * error * 1

    def __calculate_new_weight(self, last_weight, error, entry):
        return last_weight + self.learning_rate * error * entry

    def __calculate_error(self, d, y):
        return d - y

    def __get_d(self, pattern):
        return pattern[len(pattern) - 1]

    def __multiply_entry(self, x, w):
        return (x * w)

    def __check_data(self):
        if (len(self.data_gate) == 0):
            self.__assing_gate()

    def __assing_gate(self):
        if self.gate == 'OR':
            self.OR_GATE()
        else:
            self.gate = 'AND'
            self.AND_GATE()