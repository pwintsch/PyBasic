# Create a class named CodeLine which contains a line number and a string of code.
from tokenizer import split_string, string_separators, lexerize, command_types
from parser import parse_tokens, ParseResult
from interpreter import Interpreter, interpreter_commands


class BasicMachine(object):
    def __init__(self):
        self.variables = {}
        self.program = Program()

    def list(self):
        self.program.print_code()

    def run(self):
        self.program.instructions.sort(key=lambda x: x.line_number)
        for code_line in self.program.instructions:
            print ("running... ", f"{code_line}")
            program_command=interpreter_commands[code_line.tokens[0].value](code_line.tokens[1:])     
            program_command.call()


class Instruction:
    def __init__(self, line_number, tokens):
        self.line_number = line_number
        self.tokens = tokens

    def __str__(self):
        s=""
        for token in self.tokens:
            s=s+str(token)+" "
        return f"{self.line_number:<7} {s}"

# Create a class named Program which contains a list of CodeLine objects.

class Program:
    def __init__(self):
        self.instructions = []

    # create a method thats a CodeLine object to the list of CodeLine objects but only if the line number does not exist in the list. return an error if it does
    def add_code_line(self, instruction):
        for line in self.instructions:
            if line.line_number == instruction.line_number:
                print(f"Error: Line {instruction.line_number} already exists")
                return
        self.instructions.append(instruction)

    # create a method that takes a line number as parameter and removes the code line with that line number from the list of code lines. return an error if the line number does not exist.
    def remove_code_line(self, line_number):
        for line in self.code_lines:
            if line.line_number == line_number:
                self.code_lines.remove(line)
                print(f"Line {line_number} removed")
                return
        print(f"Error: Line {line_number} does not exist")

    def print_code(self):
        # sort the list of code lines by line number
        self.instructions.sort(key=lambda x: x.line_number)
        # print the line number and code for each code line in the list of code lines
        for code_line in self.instructions:
            print (f"{code_line}")


# create a function that loops capturing an input string until the user types "exit" and if the first word is a number split the string into a line number and code and add it to the code block.

def loop_input():
    cpu = BasicMachine()
    while True:
        code = input("> ")
        upperCode = code.upper()
        if upperCode == "EXIT":
            break
        elif upperCode == "LIST":
            cpu.list()
        elif upperCode == "RUN":
            cpu.run()
        elif upperCode == "CLEAR":
            cpu.program.code_lines = []
            print("Program cleared - all lines removed")
        elif upperCode.isdigit():
            cpu.program.remove_code_line(int(upperCode))
        else:
            words = split_string(code, string_separators())
            if words[0].isdigit():
                line_number = int(words[0])
                token_list = lexerize(words[1:])
                if token_list:
                    result=parse_tokens(token_list)
                    if result.tree:
                        code_line = Instruction(line_number, result.tree)
                        cpu.program.add_code_line(code_line)
                    else:
                        print("Error: Invalid syntax")
            elif words[0].upper() in command_types:
                token_list = lexerize(words)
                if token_list:
                    result=parse_tokens(token_list)
                    if result.tree:
#                        print ("Executing command:", result.tree[0].value)
#                        print(result.tree)
#                        inter = Interpreter(None)
#                        print (inter.visit(result.tree[1].expression))                     
                        direct_command=interpreter_commands[result.tree[0].value](result.tree[1:])     
                        direct_command.call()                  
                    else:
                        print("Error: Invalid syntax")
            else:
                print("Error: Line number is missing")



def main():
    loop_input()

if __name__ == "__main__":
    main()

# Run the program by typing the following command in the terminal
# python main.py