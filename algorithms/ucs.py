import heapq
from utils.metrics import SearchResult

def ucs(problem):
    pq = []
    counter = 0
    heapq.heappush(pq, (0, counter, problem.initial_state()))
    nodes = 0

    while pq:
        cost, _, state = heapq.heappop(pq)
        nodes += 1

        if problem.is_goal(state):
            return SearchResult(state, cost, nodes)

        for child in problem.successors(state):
            counter += 1
            new_cost = problem.compute_cost(child)
            heapq.heappush(pq, (new_cost, counter, child))

    return None