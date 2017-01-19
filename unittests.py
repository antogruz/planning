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

def twoAlwaysAvailable():
    p = People([True])
    result = planning([p, p], 1, 1)
    assert len(result[0]) == 1
register(twoAlwaysAvailable)

def number_of_working(people, planning):
    result = 0
    for moment in planning:
        for current_people in moment:
            if current_people == people:
                result += 1
    return result

def threeWithSameDistribution():
    p1 = People([True, True, True], name="p1")
    p2 = People([True, True, True], name="p2")
    p3 = People([True, True, True], name="p3")
    result = planning([p1, p2, p3], 3)
    assert number_of_working(p1, result) == number_of_working(p2, result)
    assert number_of_working(p1, result) == number_of_working(p3, result)
register(threeWithSameDistribution)


def threeWithDifferentMotivation():
    p1 = People([True, True, True], name="p1", motivation_score=3)
    p2 = People([True, True, True], name="p2", motivation_score=2)
    p3 = People([True, True, True], name="p3", motivation_score=1)
    result = planning([p1, p2, p3], 3)
    assert number_of_working(p1, result) == 3
    assert number_of_working(p2, result) == 2
    assert number_of_working(p3, result) == 1
register(threeWithDifferentMotivation)


def fivePlanning():
    all_true = [True for i in range(0, 6)]
    p1 = People(all_true, name="p1", motivation_score=3)
    p2 = People(all_true, name="p2", motivation_score=2)
    p3 = People(all_true, name="p3", motivation_score=1)
    p4 = People(all_true, name="p4", motivation_score=2)
    p5 = People(all_true, name="p5", motivation_score=1)
    result = planning([p1, p2, p3, p4, p5], 6)
    assert number_of_working(p1, result) >= number_of_working(p2, result)
    assert number_of_working(p1, result) >= number_of_working(p4, result)
    assert number_of_working(p2, result) >= number_of_working(p3, result)
    assert number_of_working(p4, result) >= number_of_working(p3, result)
    assert number_of_working(p2, result) >= number_of_working(p5, result)
    assert number_of_working(p4, result) >= number_of_working(p5, result)
register(fivePlanning)


def tests():
    for f in functions:
        print f.__name__
        f()


tests()
