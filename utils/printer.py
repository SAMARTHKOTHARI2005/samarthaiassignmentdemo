def print_timetable(state, rooms, slots, problem):
    DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]

    # ✅ 10 time slots per day
    TIMES = [f"{9+i}-{10+i}" for i in range(10)]

    grid = {}

    # Initialize grid
    for slot in slots:
        day = DAYS[slot // len(TIMES)]
        time = TIMES[slot % len(TIMES)]

        if day not in grid:
            grid[day] = {}

        grid[day][time] = {r["id"]: "-" for r in rooms}

    # Fill assignments
    for session_id, (room, slot) in state.items():
        day = DAYS[slot // len(TIMES)]
        time = TIMES[slot % len(TIMES)]

        session = problem.session_map[session_id]
        instructor = session["instructor"]

        grid[day][time][room] = f"{session_id} ({instructor})"

    # Print formatted timetable
    print("\n================ FINAL TIMETABLE ================\n")

    for day in DAYS:
        print(f"\n===== {day} =====")

        header = ["Time"] + [r["id"] for r in rooms]
        print("\t".join(header))

        for time in TIMES:
            row = [time]
            for r in rooms:
                row.append(grid[day][time][r["id"]])
            print("\t".join(row))