from planning import planning
from people import People

functions = []
def register(func):
    functions.append(func)

def nobody():
    planning([], 1)
register(nobody)

def ifNobodyNoResult():
    result = planning([], 1)
    assert len(result[0]) == 0
register(ifNobodyNoResult)

def planningLength():
    result = planning([], 2)
    assert len(result) == 2
register(planningLength)

def oneAlwaysAvailable():
    p = People([True, True])
    result = planning([p], 2)
    assert len(result[0]) == 1
register(oneAlwaysAvailable)

def oneNeverAvailable():
    p = People([False, False])
    result = planning([p], 2)
    assert len(result[0]) == 0
    assert len(result[1]) == 0
register(oneNeverAvailable)

def threeAlwaysAvailable():
    p = People([True])
    result = planning([p, p], 1, 1)
    assert len(result[0]) == 1
register(threeAlwaysAvailable)


def tests():
    for f in functions:
        print f.__name__
        f()


tests()
