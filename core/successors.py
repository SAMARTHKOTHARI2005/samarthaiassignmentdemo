import copy
from core.constraints import is_valid

def successors(problem, state):
    course = select_mrv(problem, state)

    # ✅ PRIORITY: use preferred slots first
    preferred_slots = course["preferred"]

    # fallback if empty
    candidate_slots = preferred_slots if preferred_slots else problem.slots

    for room in problem.rooms:
        for slot in candidate_slots:
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
        candidate_slots = preferred_slots if preferred_slots else problem.slots

        for room in problem.rooms:
            for slot in candidate_slots:
                if is_valid(problem, state, course, room, slot):
                    count += 1

        return count if count > 0 else float("inf")

    return min(unassigned, key=options)