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
    
class Command(object):
    def __init__(self,tokens):
        self.tokens = tokens

    def __str__(self):
        return f"{self.tokens[0].value}"
    
    def call():
        pass



class LetCommand(Command):
    def __init__(self,tokens):
        super().__init__(tokens)

    def __str__(self):
        return f"LET {self.variable} = {self.expression}"

    def call(self):
        print ("Executing LET command")
        # self.tokens[0].value = self.tokens[3].value


class PrintCommand(Command):
    def __init__(self,tokens):
        super().__init__(tokens)
        self.tokens = tokens

    def __str__(self):
        return f"PRINT {self.tokens}"

    def call(self):
        inter = Interpreter(None)
        print (inter.visit(self.tokens[0].expression))

interpreter_commands = {
    "LET": LetCommand,
    "PRINT": PrintCommand
}