from collections import defaultdict, Sequence
from ast import NodeVisitor, Str, Expr, Module


# noinspection PyPep8Naming
class Checker(NodeVisitor):

    def __init__(self):
        super().__init__()
        self.scopes = []
        self.scope_nodes = defaultdict(list)

    @staticmethod
    def mark_docstring_sub_nodes(node):
        def _mark_docstring_nodes(body):
            if body and isinstance(body, Sequence):
                for n in body:
                    if isinstance(n, Expr) and isinstance(n.value, Str):
                        n.is_docstring = True

        node_body = getattr(node, 'body', None)
        _mark_docstring_nodes(node_body)
        node_orelse = getattr(node, 'orelse', None)
        _mark_docstring_nodes(node_orelse)

    @staticmethod
    def is_docstring(node):
        return getattr(node, 'is_docstring', False)

    def append_to_scope(self, node):
        if self.scopes:
            stack_name = '.'.join(self.scopes)
            self.scope_nodes[stack_name].append(node.__class__.__name__)

    def process_scope(self, node, name=None):
        self.scopes.append(name or node.name)
        self.generic_visit(node)
        self.scopes.pop()

    def generic_visit(self, node):
        self.mark_docstring_sub_nodes(node)

        if self.is_docstring(node):
            return

        if not isinstance(node, Module):
            self.append_to_scope(node)
        return super().generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.append_to_scope(node)
        self.process_scope(node)
        return node

    def visit_FunctionDef(self, node):
        self.append_to_scope(node)
        self.process_scope(node)
        return node

    def visit_ClassDef(self, node):
        self.append_to_scope(node)
        self.process_scope(node)
        return node

    def visit_Module(self, node):
        self.process_scope(node, '__main__')
        return node
