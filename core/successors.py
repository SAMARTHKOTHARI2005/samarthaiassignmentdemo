import copy
import random
from core.constraints import is_valid

def successors(problem, state):
    course = select_mrv(problem, state)

    preferred_slots = course["preferred"]
    candidate_slots = preferred_slots if preferred_slots else problem.slots

    rooms = problem.rooms[:]
    slots = candidate_slots[:]

    random.shuffle(rooms)
    random.shuffle(slots)

    for room in rooms:
        for slot in slots:
            if is_valid(problem, state, course, room, slot):
                new_state = copy.deepcopy(state)
                new_state[course["id"]] = (room["id"], slot)
                yield new_state


def select_mrv(problem, state):
    unassigned = [
        s for s in problem.sessions if s["id"] not in state
    ]

    def options(course):
        count = 0

        preferred_slots = course["preferred"]
        candidate_slots = preferred_slots + problem.slots

        for room in problem.rooms:
            for slot in candidate_slots:
                if is_valid(problem, state, course, room, slot):
                    count += 1

        return count if count > 0 else float("inf")

    return min(unassigned, key=options)