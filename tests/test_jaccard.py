import ast
import types
from pathlib import Path

# extract the jaccard_similarity function from app.py without importing
source = Path('app.py').read_text()
tree = ast.parse(source)
for node in tree.body:
    if isinstance(node, ast.FunctionDef) and node.name == 'jaccard_similarity':
        func_ast = ast.Module([node], [])
        namespace = {}
        exec(compile(func_ast, filename='app.py', mode='exec'), namespace)
        jaccard_fn = namespace['jaccard_similarity']
        break
else:
    raise AssertionError('jaccard_similarity not found')

# create a lightweight module-like object with the function
app = types.SimpleNamespace(jaccard_similarity=jaccard_fn)


def test_jaccard_similarity_basic():
    result = app.jaccard_similarity([1, 2, 3], [3, 4])
    assert result == 0.25


def test_jaccard_similarity_edge_cases():
    assert app.jaccard_similarity([1, 2], [3, 4]) == 0
    assert app.jaccard_similarity([1, 2], [1, 2]) == 1
