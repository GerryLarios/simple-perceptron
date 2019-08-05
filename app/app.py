from perceptron import Perceptron

if __name__ == "__main__":
    # AND GATE [DEFAULT]
    perceptron_and = Perceptron()
    perceptron_and.learn()
    perceptron_and.print_hyperparameters()
    perceptron_and.view_net()

    # OR GATE
    perceptron_or = Perceptron(gate = 'OR')
    perceptron_or.learn()
    perceptron_or.print_hyperparameters()
    perceptron_or.view_net()