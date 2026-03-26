from data.input import load_data
from core.successors import successors
from core.cost import compute_cost
from core.constraints import is_valid

from algorithms.dfs import dfs
from algorithms.ucs import ucs
from algorithms.greedy import greedy
from algorithms.astar import astar

from heuristics.h1 import h1
from heuristics.h2 import h2

from utils.printer import print_timetable


class Problem:
    def __init__(self, sessions, rooms):
        self.sessions = sessions
        self.rooms = rooms
        self.slots = list(range(10))

        self.session_map = {s["id"]: s for s in sessions}

    def initial_state(self):
        return {}

    def is_goal(self, state):
        return len(state) == len(self.sessions)

    def successors(self, state):
        return successors(self, state)

    def compute_cost(self, state):
        return compute_cost(self, state)

    def is_valid(self, state, session, room, slot):
        return is_valid(self, state, session, room, slot)


def run():
    sessions, rooms = load_data(
        "data/courses_sample.csv",
        "data/rooms_sample.csv"
    )

    problem = Problem(sessions, rooms)

    print("\nDFS")
    res = dfs(problem)
    print_timetable(res.solution, rooms, problem.slots)

    print("\nUCS")
    res = ucs(problem)
    print_timetable(res.solution, rooms, problem.slots)

    print("\nGreedy (h1)")
    res = greedy(problem, h1)
    print_timetable(res.solution, rooms, problem.slots)

    print("\nA* (h2)")
    res = astar(problem, h2)
    print_timetable(res.solution, rooms, problem.slots)


if __name__ == "__main__":
    run()