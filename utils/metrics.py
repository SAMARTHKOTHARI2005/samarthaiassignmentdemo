from dataclasses import dataclass

@dataclass
class SearchResult:
    solution: dict
    cost: int
    nodes_expanded: int