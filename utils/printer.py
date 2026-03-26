def print_timetable(state, rooms, slots, problem):
    DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    TIMES = [f"{9+i}-{10+i}" for i in range(10)]

    grid = {}

    for slot in slots:
        day = DAYS[slot // len(TIMES)]
        time = TIMES[slot % len(TIMES)]

        if day not in grid:
            grid[day] = {}

        grid[day][time] = {r["id"]: "-" for r in rooms}

    for course_id, (room, slot) in state.items():
        day = DAYS[slot // len(TIMES)]
        time = TIMES[slot % len(TIMES)]

        course = problem.session_map[course_id]
        instructor = course["instructor"]

        grid[day][time][room] = f"{course_id} ({instructor})"

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