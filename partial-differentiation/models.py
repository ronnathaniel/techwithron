
from util import log

class Term:

    def __init__(self, coef: int = 0, vars: dict = None):
        self.coef = coef
        self.vars = vars

    def differentiate_term(self, var: str):
        exp = self.vars.get(var, '')
        if not exp:
            self.coef = 0
            return
        self.vars[var] = exp - 1
        self.coef *= exp

    def __repr__(self):
        if not self.coef:
            return '0'

        s = f'{self.coef}'
        for var, exp in self.vars.items():
            s += f'{var}^{exp}'
        return s


class Equation:

    def __init__(self, terms: list):
        # terms: [ <Term>, '+', <Term>, '-', ... ]
        self.terms = terms

    def differentiate_eq(self, var: str):
        for term in self.terms:
            log('term before', term)
            if isinstance(term, Term):
                term.differentiate_term(var)

    def __repr__(self):
        s = ''
        for term in self.terms:
            s += f'{term} '
        return s







