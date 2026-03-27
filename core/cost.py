def compute_cost(problem, state):
    cost = 0

    DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    TIMES_PER_DAY = 10

    # ---------- Preferred slot penalty ----------
    for c_id, (room, slot) in state.items():
        course = problem.session_map[c_id]

        if course["preferred"] and slot not in course["preferred"]:
            cost += 2   # slightly higher weight

    # ---------- Daily load balancing ----------
    day_counts = {d: 0 for d in range(5)}

    for _, (_, slot) in state.items():
        day = slot // TIMES_PER_DAY
        day_counts[day] += 1

    avg = len(state) / 5 if state else 0

    for d in day_counts:
        cost += abs(day_counts[d] - avg) * 2   # weight = 2

    # ---------- Gap penalty (optional but strong improvement) ----------
    day_slots = {d: [] for d in range(5)}

    for _, (_, slot) in state.items():
        day = slot // TIMES_PER_DAY
        time = slot % TIMES_PER_DAY
        day_slots[day].append(time)

    for d in day_slots:
        times = sorted(day_slots[d])
        for i in range(1, len(times)):
            gap = times[i] - times[i-1]
            if gap > 1:
                cost += (gap - 1)   # penalize gaps

    return cost