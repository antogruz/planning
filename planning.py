def get_people_available(people, moment):
    return [p for p in people if p.is_available(moment)]

def planning(people, planning_length, max_coworkers=2):
    return [get_people_available(people, i)[:max_coworkers] for i in range(planning_length)]

