import csv
from people import People
from planning import planning as get_planning

planning_length = 54


def get_peoples():
    result, teams_availability = get_teams_availability()
    with open('data/people.csv', 'rb') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            name = row[0]
            team = row[1]
            # motivation = row[2]
            result.append(People(teams_availability[team], name=name))
    return result


def get_teams_availability():
    teams_availability = {}
    with open('data/teams.csv', 'rb') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            teams_availability[row[0]] = [True for i in range(0, planning_length)]
            for not_availability in row[1].split(','):
                teams_availability[row[0]][int(not_availability) - 1] = False
    result = []
    return result, teams_availability


def print_planning(planning):
    key = 1
    for moment in planning:
        workers = ""
        for worker in moment:
            workers += worker.name+" "
        print(key, workers)
        key += 1

if __name__ == '__main__':
    peoples = get_peoples()
    print_planning(get_planning(peoples, planning_length, 2))
