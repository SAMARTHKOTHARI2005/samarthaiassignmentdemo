def compute_cost(problem, state):
    cost = 0
    for s_id, (room, slot) in state.items():
        session = problem.session_map[s_id]
        if slot not in session["preferred"]:
            cost += 1
    return cost