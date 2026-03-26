def is_valid(problem, state, session, room, slot):
    # capacity
    if room["capacity"] < session["capacity"]:
        return False

    # unavailable
    if slot in session["unavailable"]:
        return False

    for s_id, (r, sl) in state.items():
        # room conflict
        if r == room["id"] and sl == slot:
            return False

        existing = problem.session_map[s_id]

        # instructor conflict
        if existing["instructor"] == session["instructor"] and sl == slot:
            return False

    return True