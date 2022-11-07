import re
import os

class SimpleCalculator:
    """
        A simple calculator to make:
        - multiplications
        - divisions
        - sums
        - subtratctions
        - potencies
        - logarithms
    """
    __historic = []

    # def __init__(self) -> None:
    #     self.historic []
    #     print(self.__historic)
    #     print(self.historic)

    @property
    def historic(self) -> list:
        return self.__historic

    @historic.setter
    def historic(self, register) -> None:
        self.__historic = register

    def save_history(self, register: str) -> None:
        history = self.historic
        history.append(register)
        self.historic = history
    

    def select_operation(self, expression:  str) -> None:
        if not expression:
            self.save_history('Expressão Vazia')
            return None
        
        args = re.findall(r'([\-]*\d)([\+\-\^\*\/])\(*(\-*\d)\)*(.*)', expression)
        if args == []:
            args = re.findall(r'()(log)\((\d)\)', expression)

        if args == []:
            self.save_history('Incorrect expression')
            return None
        
        args = list(args.pop(0))
        if args[-1] != '' and len(args) > 3:
            self.save_history('Incorrect expression')
            return None

        del args[-1]
        operation = args.pop(1)
        args = [int(x) for x in args]

        match operation:
            case '^':
                result = self.potency(*args)
            case '*':
                result = self.multiplication(*args)
            case '/':
                result  = self.division(*args)
            case '+':
                print(args)
                result = self.sum(*args)
                print(result)
            case '-':
                result = self.subtraction(*args)
            case 'log':
                result = self.log(args[2])
            case _:
                self.save_history('Incorrect expression')
                return None
        

        self.save_history(f'{expression} = {result}')


    def sum(self, num_1, num_2) -> float | int:
        return num_1 + num_2
    
    def subtraction(self, num_1, num_2) -> float | int:
        return num_1 - num_2

    def division(self, num_1, num_2) -> float | int:
        return num_1/num_2

    def multiplication(self, num_1, num_2) -> float | int:
        return num_1*num_2

    def potency(self, base, exponent) -> float | int:
        return base**exponent
    
    def log(self, logarithm) -> float | int:
        indice = 0
        while logarithm > 1:
            logarithm /= 2
            indice += 1
        return indice


if __name__ == "__main__":
    calculator = SimpleCalculator()
    # calculator.select_operation('1+1+3')
    # calculator.select_operation('1-1')
    # calculator.select_operation('1*1')
    # calculator.select_operation('11')
    # print(calculator.historic)

    while True:
        print('--------------- History -------------------')
        for history in calculator.historic[-9:]:
            print(f'>> {history}')

        print('\n\n\n')
        print('Digit your expression or type "exit" to finish calculator!')
        if len(calculator.historic) > 0:
            print(calculator.historic[-1])
        expression = input('> ')

        if expression.lower() == 'exit':
            break

        calculator.select_operation(expression=expression)

        os.system('cls' if os.name == 'nt' else 'clear')