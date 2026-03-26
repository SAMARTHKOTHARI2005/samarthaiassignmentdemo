import csv

def parse_list(x):
    if x == "":
        return []
    return list(map(int, x.split("|")))

def load_data(course_file, room_file):
    sessions = []

    with open(course_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            sessions.append({
                "id": row["course_id"],  # ✅ now course itself is session
                "course": row["course_id"],
                "instructor": row["instructor_id"],
                "capacity": int(row["capacity_required"]),
                "preferred": parse_list(row["preferred_slots"]),
                "unavailable": parse_list(row["unavailable_slots"])
            })

    rooms = []
    with open(room_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rooms.append({
                "id": row["room_id"],
                "capacity": int(row["capacity"])
            })

    return sessions, rooms