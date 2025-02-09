from tokenizer import OperatorType, CommandType, TokenType, Token
from enum import Enum

grammar_book = {}


class GrammarNodeType(Enum):
    COMMAND = 1
    EXPRESSION = 2
    OPERATOR = 3
    VALUE = 4
    VARIABLE = 5

# create a dictionnary that give a text representation of the grammar node type
grammar_node_type_desc = {
    GrammarNodeType.COMMAND: "COMMAND",
    GrammarNodeType.EXPRESSION: "EXPRESSION",
    GrammarNodeType.OPERATOR: "OPERATOR",
    GrammarNodeType.VALUE: "VALUE",
    GrammarNodeType.VARIABLE: "VARIABLE"
}

class GrammarNode:
    def __init__(self, node_type, type_id):
        self.node_type = node_type
        self.type_id = type_id

    def __str__(self):
        return f"{grammar_node_type_desc [self.node_type]}: {self.type_id}"

    def __repr__(self):
        return f"{grammar_node_type_desc [self.node_type]}: {self.type_id}"
    

class grammar_rules(Enum):
    LET = 1
    PRINT = 2
    CALC = 3


def initialise_grammarbook ():
    let_grammar = [GrammarNode(TokenType.COMMAND, CommandType.LET), GrammarNode(TokenType.VARIABLE, 0), GrammarNode(TokenType.EQUAL, OperatorType.EQUAL), GrammarNode(GrammarNodeType.EXPRESSION, 0)]
    print_grammar = [GrammarNode(TokenType.COMMAND, CommandType.PRINT), GrammarNode(GrammarNodeType.EXPRESSION, 0)]
    calc_grammar = [GrammarNode(TokenType.COMMAND, CommandType.CALC), GrammarNode(GrammarNodeType.EXPRESSION, 0)]
    grammar_book[grammar_rules.LET] = let_grammar
    grammar_book[grammar_rules.PRINT] = print_grammar
    grammar_book[grammar_rules.CALC] = calc_grammar



class ASTNode(object):
    pass


class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"({self.left} {self.op} {self.right})"
    
class UnOp(ASTNode):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr
        self.token = op

    def __str__(self):
        return f"{self.op} {self.right}"
    

class Num(ASTNode):
    def __init__(self, value):
        self.value = float(value)

    def __str__(self):
        return f"{self.value}"
    

class ExprParser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token().token_type == token_type:
            self.index += 1
        else:
            self.error()

    def factor(self):
        token = self.current_token()
        if token.token_type == TokenType.PLUS:
            self.eat(TokenType.PLUS)
            node = UnOp(token, self.factor())
            return node
        elif token.token_type == TokenType.MINUS:
            self.eat(TokenType.MINUS)
            node = UnOp(token, self.factor())
            return node
        elif token.token_type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return Num(token.value)
        elif token.token_type == TokenType.OPEN_PARENTHESIS:
            self.eat(TokenType.OPEN_PARENTHESIS)
            node = self.parse_expression()
            self.eat(TokenType.CLOSE_PARENTHESIS)
            return node


    def term(self):
        node = self.factor()
        while self.current_token().token_type in (TokenType.TIMES, TokenType.DIVIDE):
            token = self.current_token()
            if token.token_type == TokenType.TIMES:
                self.eat(TokenType.TIMES)
            elif token.token_type == TokenType.DIVIDE:
                self.eat(TokenType.DIVIDE)
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def parse_expression(self):
        node = self.term()
        while self.current_token().token_type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token()
            if token.token_type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.token_type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
            node = BinOp(left=node, op=token, right=self.term())
        return node

    def parse(self):
        return self.parse_expression()

    def current_token(self):
        if self.index >= len(self.tokens):
            return Token(TokenType.EOF, 0, "") 
        return self.tokens[self.index]



class ParseResult:
    def __init__(self, result, remaining_tokens):
        self.tree = result
        self.remaining_tokens = remaining_tokens

    def __str__(self):
        return f"{self.success}: {self.error}"

    def __repr__(self):
        return f"{self.success}: {self.error}"
    

def parse_expression(tokens):
    result=[]
    expression_tokens=[TokenType.NUMBER, TokenType.PLUS, TokenType.MINUS, TokenType.TIMES, TokenType.DIVIDE, TokenType.OPEN_PARENTHESIS, TokenType.CLOSE_PARENTHESIS]
    index=0
    for token in tokens:
        if token.token_type in expression_tokens:
            index+=1
            result.append(token)
        else:
            break
    if len(result)==0:
        return ParseResult(None, tokens)
    else:
        expr_token=Token(TokenType.EXPRESSION, None, "")
        expr_tree=ExprParser(result).parse()
        expr_token.tokens=result
        expr_token.expression=expr_tree
    return ParseResult(expr_token, tokens[index:])



def parse_tokens(tokens):
    initialise_grammarbook()
    selected_grammar = None
    for grammar_rule in grammar_book.values():
        if grammar_rule[0].node_type == TokenType.COMMAND and \
          tokens[0].token_type == TokenType.COMMAND and \
          grammar_rule[0].type_id == tokens[0].token_type_id:
            selected_grammar = grammar_rule
            break
    if selected_grammar == None:
        print("Error: No matching grammar rule found")
        return ParseResult(None, tokens)
    else:
        # Build parse tree based on selected grammar and tokens
        token_index=0
        command=[]
        for node in selected_grammar:
            if tokens[token_index].token_type == node.node_type:
                command.append(tokens[token_index])   
                token_index+=1
            elif node.node_type == GrammarNodeType.EXPRESSION:
                result = parse_expression(tokens[token_index:])
                if not result.tree:
                    print("Error: Expression parse failed")
                    return ParseResult(None, tokens)
                else:
                    command.append(result.tree)  # replace this with custom node for expressions
                if result.remaining_tokens:
                    print("Error: Remaining tokens")
                    return ParseResult(None, tokens)
            elif node.node_type == GrammarNodeType.OPERATOR and tokens[token_index].token_type == TokenType.OPERATOR and tokens[token_index].token_type_id == node.type_id:
                command.append(tokens[token_index])
            else:
                print("Error: Unexpected token")
                return ParseResult(None, tokens)
        return ParseResult(command, tokens[token_index:])

    
        