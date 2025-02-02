# Objective of this module is to tokenize the input text into a list of tokens where the input is an array of strings
# and the output is an array of tokens. The tokens are objects

from enum import Enum

class Token:
    def __init__(self, token_type, token_sub_type, value):
        self.token_type = token_type
        self.token_sub_type = token_sub_type
        self.value = value

    def __str__(self):
        return f"{self.value}"
    
    def __repr__(self):
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

# create an enum of Commands that can be used to create tokens.

class CommandType(Enum):
    LET = 1
    PRINT = 2

# create a dictionary of command types that will be used to find the type of command. One item for each command type with a string corresponding to it

command_types = {
    "LET": CommandType.LET,
    "PRINT": CommandType.PRINT
}

# create an dictionary of operator types that will be used to find the type of operator. One item for each operator type with a string corresponding to it

operator_types = {
    "+": OperatorType.PLUS,
    "-": OperatorType.MINUS,
    "*": OperatorType.TIMES,
    "/": OperatorType.DIVIDE,
    "=": OperatorType.EQUAL
}

unsupported_operators = {
    "^": OperatorType.EXPONENT,
    "MOD": OperatorType.MODULUS,
    ">": OperatorType.GREATER_THAN,
    "<": OperatorType.LESS_THAN,
    ">=": OperatorType.GREATER_THAN_EQUAL,
    "<=": OperatorType.LESS_THAN_EQUAL,
    "AND": OperatorType.AND,
    "OR": OperatorType.OR,
    "NOT": OperatorType.NOT,
    "[": OperatorType.OPENBRACKET,
    "]": OperatorType.CLOSEBRACKET,
    "(": OperatorType.OPENPARENTHESIS,
    ")": OperatorType.CLOSEPARENTHESIS
}


def words_to_tokens(words):
    tokens = []
    for word in words:
        if word.isdigit():
            tokens.append(Token(TokenTypeValue.NUMBER, None, word))
        elif word in operator_types:
            tokens.append(Token(TokenTypeValue.OPERATOR, operator_types[word], word))
        elif word in command_types:
            tokens.append(Token(TokenTypeValue.COMMAND, command_types[word], word))
        elif is_valid_variable_name(word):
            tokens.append(Token(TokenTypeValue.VARIABLE, None, word))
        else:
            print(f"Error: {word} is not a valid token")
            tokens=[]
            break
    return tokens

# create a function that checks if a string is a valid variable name and returns a boolean value accordingly.

def is_valid_variable_name(string):
    return string.isidentifier()



# create a function that return a string containing all the operator types that are a single character.

def string_separators():
#    return " +-*/^><=().;[]"
    return " +-*/=" # only the operators that are supported for the moment


# Create a function that takes a string and splits it into a array of strings each time a character is a separator from an array of chars representing the seperators. The separator becomes a single element in the array of strings.

def split_string(string, separators):
    words = []
    word = ""
    for char in string:
        if char in separators:
            if word:
                words.append(word)
                word = ""            
            if char != " ":
                words.append(char)
        else:
            word += char
    if word:
        words.append(word)
    return words

