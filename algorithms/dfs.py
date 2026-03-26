from utils.metrics import SearchResult

def dfs(problem):
    stack = [problem.initial_state()]
    visited = set()
    nodes = 0

    while stack:
        state = stack.pop()
        nodes += 1

        key = tuple(sorted(state.items()))
        if key in visited:
            continue
        visited.add(key)

        if problem.is_goal(state):
            return SearchResult(state, problem.compute_cost(state), nodes)

        for child in problem.successors(state):
            stack.append(child)

    return None