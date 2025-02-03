from tokenizer import OperatorType, CommandType, TokenType
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


def initialise_grammarbook ():
    let_grammar = [GrammarNode(GrammarNodeType.COMMAND, CommandType.LET), GrammarNode(GrammarNodeType.VARIABLE, 0), GrammarNode(GrammarNodeType.OPERATOR, OperatorType.EQUAL), GrammarNode(GrammarNodeType.EXPRESSION, 0)]
    print_grammar = [GrammarNode(GrammarNodeType.COMMAND, CommandType.PRINT), GrammarNode(GrammarNodeType.EXPRESSION, 0)]
    grammar_book[grammar_rules.LET] = let_grammar
    grammar_book[grammar_rules.PRINT] = print_grammar


# Create a parse_tree class that contains a list of nodes and a method to add a node to the list of nodes

class ParseTree:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def __str__(self):
        s = ""
        for node in self.nodes:
            s = s + str(node) + " "
        return s

    def __repr__(self):
        s = ""
        for node in self.nodes:
            s = s + str(node) + " "
        return s



def parse_tokens(tokens):
    initialise_grammarbook()
    selected_grammar = None
    for grammar_rule in grammar_book.values():
        if grammar_rule[0].node_type == GrammarNodeType.COMMAND and \
          tokens[0].token_type == TokenType.COMMAND and \
          grammar_rule[0].type_id == tokens[0].token_type_id:
            selected_grammar = grammar_rule
            break
    if selected_grammar == None:
        print("Error: No matching grammar rule found")
    else:
        # Build parse tree based on selected grammar and tokens
        print("Building parse tree")
        