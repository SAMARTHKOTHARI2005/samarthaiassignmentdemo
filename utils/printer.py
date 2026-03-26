def print_timetable(state, rooms, slots):
    grid = {s: {r["id"]: "-" for r in rooms} for s in slots}

    for session, (room, slot) in state.items():
        grid[slot][room] = session

    print("\nFinal Timetable:\n")

    header = "Slot\t" + "\t".join([r["id"] for r in rooms])
    print(header)

    for slot in slots:
        row = [str(slot)]
        for r in rooms:
            row.append(grid[slot][r["id"]])
        print("\t".join(row))