from parser import ASTNode, BinOp, Num
from tokenizer import TokenType


class NodeVisitor(object):
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')
    

class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.token_type == TokenType.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.token_type == TokenType.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.token_type == TokenType.TIMES:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.token_type == TokenType.DIVIDE:
            return self.visit(node.left) / self.visit(node.right)
    
    def visit_UnOp(self, node):
        if node.op.token_type == TokenType.PLUS:
            return +self.visit(node.expr)
        elif node.op.token_type == TokenType.MINUS:
            return -self.visit(node.expr)

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)