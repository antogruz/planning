import operator


def planning(people, planning_length, max_coworkers=2):
    return Planning(people, planning_length, max_coworkers).get_planning()


class Planning:
    def __init__(self, people, planning_length, max_coworkers=2):
        self.people = people
        self.planning_length = planning_length
        self.max_coworkers = max_coworkers

    def get_planning(self):
        current_planning = []
        for i in range(self.planning_length):
            current_planning.append(self.get_people_available(i, current_planning)[:self.max_coworkers])
        return current_planning

    def get_people_available(self, moment, current_planning):
        people = self.order_people_by_participation(current_planning)
        return [p for p in people if p.is_available(moment)]

    def order_people_by_participation(self, current_planning):
        participation = {}
        for people in self.people:
            participation[people] = 0
        for moment in current_planning:
            for people in moment:
                participation[people] += 1
        sorted_people = [people for people, _ in sorted(participation.items(), key=operator.itemgetter(1))]
        return sorted_people

