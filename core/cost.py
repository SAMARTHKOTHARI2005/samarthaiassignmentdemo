def compute_cost(problem, state):
    cost = 0
    for c_id, (room, slot) in state.items():
        course = problem.session_map[c_id]

        if slot not in course["preferred"]:
            cost += 1

    return cost