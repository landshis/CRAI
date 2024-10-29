import ast

def tokenize_code(code):
    return [node.__class__.__name__ for node in ast.walk(ast.parse(code))]

def extract_features(data):
    return [tokenize_code(code) for code in data]
