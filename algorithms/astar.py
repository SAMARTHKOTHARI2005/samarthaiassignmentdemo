import heapq
from utils.metrics import SearchResult

def astar(problem, heuristic):
    pq = []
    counter = 0
    heapq.heappush(pq, (0, counter, 0, problem.initial_state()))
    nodes = 0

    while pq:
        _, _, g, state = heapq.heappop(pq)
        nodes += 1

        if problem.is_goal(state):
            return SearchResult(state, g, nodes)

        for child in problem.successors(state):
            counter += 1
            new_g = problem.compute_cost(child)
            h = heuristic(problem, child)
            f = new_g + h
            heapq.heappush(pq, (f, counter, new_g, child))

    return None