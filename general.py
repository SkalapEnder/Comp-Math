import Bisection
import FalsePosition
import IterationMethod
import NewtonMethod
import matplotlib.pyplot as plt

def main():
    precision = 1e-6
    max_iters = 20
    goal = 0
    
    result_Bisection, epsilon_Bisesction = Bisection.bisection(precision, max_iters, goal)
    result_False, epsilon_False = FalsePosition.falsePos(precision, max_iters, goal)
    result_Iterative, epsilon_Iterative = IterationMethod.iterative(precision, max_iters, goal)
    result_Newton, epsilon_Newton = NewtonMethod.newton(precision, max_iters, goal)
    
    outputGraph_Results(result_Bisection, result_False, result_Iterative, result_Newton, 'Answer')
    outputGraph_Results(epsilon_Bisesction, epsilon_False, epsilon_Iterative, epsilon_Newton, 'Epsilon')

def outputGraph_Results(list_Bisection, list_False, list_Iterative, list_Newton, name):
    iterations_Bisection, answers_Bisection = zip(*list_Bisection)
    iterations_False, answers_False = zip(*list_False)
    iterations_Iterative, answers_Iterative = zip(*list_Iterative)
    iterations_Newton, answers_Newton = zip(*list_Newton)

    plt.plot(iterations_Bisection, answers_Bisection, label='Bisection method')
    plt.plot(iterations_False, answers_False, label='False position method')
    plt.plot(iterations_Iterative, answers_Iterative, label='Iterative method')
    plt.plot(iterations_Newton, answers_Newton, label='Newton method')
    plt.xlabel('Iteration')
    plt.ylabel(name)
    plt.title(' x^3 + x^2 - 1 = 0 | Methods: Iteration vs. ' + name)
    plt.legend(loc = 4)
    plt.grid(True)
    plt.show()
    
if __name__ == '__main__':
    main()
