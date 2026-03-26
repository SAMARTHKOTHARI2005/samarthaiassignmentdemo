import csv

def parse_list(x):
    if x == "":
        return []
    return list(map(int, x.split("|")))

def load_data(course_file, room_file):
    courses = []
    with open(course_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            courses.append({
                "id": row["course_id"],
                "instructor": row["instructor_id"],
                "sessions": int(row["sessions_per_week"]),
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

    sessions = []
    for c in courses:
        for i in range(c["sessions"]):
            sessions.append({
                "id": f"{c['id']}_{i+1}",
                "course": c["id"],
                "instructor": c["instructor"],
                "capacity": c["capacity"],
                "preferred": c["preferred"],
                "unavailable": c["unavailable"]
            })

    return sessions, rooms