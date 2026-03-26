import copy
from core.constraints import is_valid

def successors(problem, state):
    session = select_mrv(problem, state)

    for room in problem.rooms:
        for slot in problem.slots:
            if is_valid(problem, state, session, room, slot):
                new_state = copy.deepcopy(state)
                new_state[session["id"]] = (room["id"], slot)
                yield new_state


def select_mrv(problem, state):
    unassigned = [
        s for s in problem.sessions if s["id"] not in state
    ]

    def options(session):
        count = 0
        for room in problem.rooms:
            for slot in problem.slots:
                if is_valid(problem, state, session, room, slot):
                    count += 1
        return count if count > 0 else float("inf")

    return min(unassigned, key=options)