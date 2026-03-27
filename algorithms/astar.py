import heapq
from utils.metrics import SearchResult

def astar(problem, heuristic):
    pq = []
    counter = 0
    start = problem.initial_state()
    heapq.heappush(pq, (0, counter, 0, start))
    nodes = 0

    while pq:
        _, _, g, state = heapq.heappop(pq)
        nodes += 1

        if problem.is_goal(state):
            return SearchResult(state, g, nodes)

        for child in problem.successors(state):
            counter += 1

            # incremental cost
            new_g = g + (problem.compute_cost(child) - problem.compute_cost(state))

            h = heuristic(problem, child)
            f = new_g + h

            heapq.heappush(pq, (f, counter, new_g, child))

    return None