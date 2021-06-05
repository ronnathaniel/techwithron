
from const import DEBUG

def ask(question: str, *options: list, deflt = None):
    q = input(f'{question}: ')
    if not q and deflt:
        q = deflt
    return q


def log(*s):
    if DEBUG:
        for st in s:
            # print('st-', type(st))
            if not st:
                continue
            print(st)