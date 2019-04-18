import ast
from collections import defaultdict
from difflib import SequenceMatcher

from .checker import Checker

__all__ = ['parse', 'compare', 'Checker']

__version__ = '0.0.1'


def parse(source: str) -> 'Checker':
    chk = Checker()
    tree = ast.parse(source)
    # print(ast.dump(tree))
    chk.visit(tree)
    return chk


def compare(a: str, b: str):
    file_a, file_b = map(parse, [a, b])
    points = []
    items = defaultdict(list)

    for ka, va in file_a.scope_nodes.items():
        max_sim = 0
        for kb, vb in file_b.scope_nodes.items():
            sim = SequenceMatcher(None, va, vb).ratio()
            items[ka].append((kb, sim))
            if sim > max_sim:
                max_sim = sim
        points.append(max_sim)

    return {
        'ratio': sum(points) / len(points),
        'scopes': items,
    }
