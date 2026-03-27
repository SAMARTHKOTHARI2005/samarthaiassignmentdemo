def h2(problem, state):
    score = 0

    for session in problem.sessions:
        if session["id"] in state:
            continue

        valid = 0
        for room in problem.rooms:
            for slot in problem.slots:
                if problem.is_valid(state, session, room, slot):
                    valid += 1

        if valid > 0:
            score += 1 / (valid + 1)   # smoother
        else:
            score += 50   # strong dead-end penalty

    return score