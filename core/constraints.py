def is_valid(problem, state, course, room, slot):
    # capacity
    if room["capacity"] < course["capacity"]:
        return False

    # unavailable slot
    if slot in course["unavailable"]:
        return False

    for c_id, (r, sl) in state.items():
        # room conflict
        if r == room["id"] and sl == slot:
            return False

        existing = problem.session_map[c_id]

        # instructor conflict
        if existing["instructor"] == course["instructor"] and sl == slot:
            return False

    return True