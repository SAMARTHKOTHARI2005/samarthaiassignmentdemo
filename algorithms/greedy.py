import heapq
from utils.metrics import SearchResult

def greedy(problem, heuristic):
    pq = []
    counter = 0
    heapq.heappush(pq, (0, counter, problem.initial_state()))
    nodes = 0

    while pq:
        _, _, state = heapq.heappop(pq)
        nodes += 1

        if problem.is_goal(state):
            return SearchResult(state, problem.compute_cost(state), nodes)

        for child in problem.successors(state):
            counter += 1
            h = heuristic(problem, child)
            heapq.heappush(pq, (h, counter, child))

    return None