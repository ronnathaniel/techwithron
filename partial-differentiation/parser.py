
from models import Equation, Term
from const import DEBUG
from util import ask, log



def main():
    equation = ask('Enter Equation', deflt='3x^2+9xy')
    variable = ask('Variable to differentiate in terms of', 'x')
    # equation = map(lambda s: ,equation.split(' '))
    equation = equation.split()
    for i, term in enumerate(equation):
        log(term)
        if i % 2:
            continue
        coef = ''
        vars = {}
        exp = False
        for j, t in enumerate(term):
            log('char t - ', t)
            if t.isnumeric():
                log('exp - ', exp)
                if exp:
                    vars[term[j-2]] = t
                    log('setting', term[j-2], 'to', t)
                else:

                    coef += f'{t}'
                exp = False
            elif isinstance(t, str):
                if not exp:
                    exp = True
                # if t == '^':
                #     log('got carrot ^, idx=', j)
                #     pass
                elif t.isalpha():
                    vars[term[j-1]] = 1
                        # xy^2

        try:
            coef = int(coef)
        except ValueError:
            coef = 1
        log(coef)
        log(vars)
        equation[i] = Term(coef, vars)

    equation = Equation(equation)
    log('before: ', equation)
    equation.differentiate_eq(variable)
    log('after: ', equation)


main()

