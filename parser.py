class Parser:

    alphabet = {'+','-','*','/','^'}

    @staticmethod
    def clean_expression(exprn):
        expression = exprn
        for i in range(len(expression)):
            if (expression[i] in Parser.alphabet) and expression[i+1]=='-':
                expression[i+1] = None
                expression[i+2] = -float(expression[i+2])
        expression = [term for term in expression if term != None]
        for i in range(len(expression)):
            if expression[i] not in Parser.alphabet:
                expression[i] = float(expression[i])
        for i in range(len(expression)):
            if expression[i] in Parser.alphabet:
                if expression[i] == '-':
                    expression[i] = '+'
                    expression[i+1] = -float(expression[i+1])
                elif expression[i] == '/':
                    if expression[i+1] == 0:
                        raise ZeroDivisionError('Ooops, you have a zero')
                    else:
                        expression[i] = '*'
                        expression[i+1] = 1/float(expression[i+1])
        return expression
    
    @staticmethod
    def evaluate(exprn):
        if Parser.alphabet.isdisjoint(set(exprn)):
            return exprn
        elif '^' in exprn:
            expression = exprn
            for term in range(len(expression)):
                if expression[term] == '^':
                    result = expression[term-1]**expression[term+1]
                    expression[term] = result
                    expression[term-1] = expression[term+1] = None
                    expression = [term for term in expression if term != None]
                    return Parser.evaluate(expression)
        elif '*' in exprn:
            expression = exprn
            for term in range(len(expression)):
                if expression[term] == '*':
                    result = expression[term-1]*expression[term+1]
                    expression[term] = result
                    expression[term-1] = expression[term+1] = None
                    expression = [term for term in expression if term != None]
                    return Parser.evaluate(expression)
        elif '+' in exprn:
            expression = exprn
            for term in range(len(expression)):
                if expression[term] == '+':
                    result = expression[term-1]+expression[term+1]
                    expression[term] = result
                    expression[term-1] = expression[term+1] = None
                    expression = [term for term in expression if term != None]
                    return Parser.evaluate(expression)
    
    @staticmethod
    def calculator(raw_exprn):
        allowed_symbols = ' 0123456789+-*/^'
        InputValueDetect = list(map(lambda x: x in allowed_symbols,raw_exprn))
        if False in InputValueDetect:
            raise ValueError('Bad Values Please use only numbers and basic operators and spaces between')
        else:
            a = raw_exprn.split(' ')
            b = Parser.clean_expression(a)
            c = Parser.evaluate(b)
            return c[0]

user_input_raw = input('Please type an expression (using spaces between operators and operands), or type exit to exit')

if user_input_raw == 'exit':
    quit()
else:
    print(Parser.calculator(user_input_raw))