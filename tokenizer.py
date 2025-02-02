# Objective of this module is to tokenize the input text into a list of tokens where the input is an array of strings
# and the output is an array of tokens. The tokens are objects

from enum import Enum

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return f"{self.token_type}: {self.value}"
    


# Create a class called TokenType which contains the types of tokens that can be created. each type contains a TokenTypeValue, a subTypeValue and a string representation of the token sub type.

class TokenType:
    def __init__(self, token_type_value, token_type_subtype, token_type_string):
        self.token_type_value = token_type_value
        self.token_type_subtype = token_type_subtype
        self.token_type_string = token_type_string

    def __str__(self):
        return f"{self.token_type_value}: {self.token_type_string}"
    

# Create an Enum of token types that can be used to create tokens.

class TokenTypeValue(Enum):
    NUMBER = 1
    OPERATOR = 2
    PARENTHESIS = 3
    FUNCTION = 4
    VARIABLE = 5
    KEYWORD = 6
    STRING = 7
    WHITESPACE = 8
    COMMENT = 9
    NEWLINE = 10
    EOF = 11
    UNKNOWN = 12
    ASSIGNMENT = 13
    COMMA = 14
    COLON = 15
    SEMICOLON = 16
    DOT = 17
    INDENT = 18
    DEDENT = 19
    EOL = 20
    COMMAND = 21

# create an enum of Operator types that can be used to create tokens.

class OperatorType(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDE = 4
    EXPONENT = 5
    MODULUS = 6
    GREATER_THAN = 7
    LESS_THAN = 8
    GREATER_THAN_EQUAL = 9
    LESS_THAN_EQUAL = 10
    EQUAL = 11
    AND = 12
    OR = 13
    NOT = 14
    ASSIGN = 15
    OPENBRACKET = 16
    CLOSEBRACKET = 17
    OPENPARENTHESIS = 18
    CLOSEPARENTHESIS = 19

# create an dictionary of operator types that will be used to find the type of operator. One item for each operator type with a string corresponding to it

operator_types = {
    "+": OperatorType.PLUS,
    "-": OperatorType.MINUS,
    "*": OperatorType.TIMES,
    "/": OperatorType.DIVIDE,
    "^": OperatorType.EXPONENT,
    "MOD": OperatorType.MODULUS,
    ">": OperatorType.GREATER_THAN,
    "<": OperatorType.LESS_THAN,
    ">=": OperatorType.GREATER_THAN_EQUAL,
    "<=": OperatorType.LESS_THAN_EQUAL,
    "=": OperatorType.EQUAL,
    "AND": OperatorType.AND,
    "OR": OperatorType.OR,
    "NOT": OperatorType.NOT,
    "[": OperatorType.OPENBRACKET,
    "]": OperatorType.CLOSEBRACKET,
    "(": OperatorType.OPENPARENTHESIS,
    ")": OperatorType.CLOSEPARENTHESIS
}


# create an array of TokenType that will be used to find the type of token. Initialize the array with mathematical operators, parentheses, and whitespace.

token_types = [
    TokenType(TokenTypeValue.OPERATOR, "OPERATOR"),
    TokenType(TokenTypeValue.PARENTHESIS, "PARENTHESIS"),
    TokenType(TokenTypeValue.FUNCTION, "FUNCTION"),
    TokenType(TokenTypeValue.VARIABLE, "VARIABLE"),
    TokenType(TokenTypeValue.KEYWORD, "KEYWORD"),
    TokenType(TokenTypeValue.STRING, "STRING"),
    TokenType(TokenTypeValue.WHITESPACE, "WHITESPACE"),
    TokenType(TokenTypeValue.COMMENT, "COMMENT"),
    TokenType(TokenTypeValue.NEWLINE, "NEWLINE"),
    TokenType(TokenTypeValue.EOF, "EOF"),
    TokenType(TokenTypeValue.UNKNOWN, "UNKNOWN"),
    TokenType(Token

