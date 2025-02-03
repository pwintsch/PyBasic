# Create a class named CodeLine which contains a line number and a string of code.
from tokenizer import split_string, string_separators, lexerize
from parser import parse_tokens

class Command:
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
        self.commands = []

    # create a method thats a CodeLine object to the list of CodeLine objects but only if the line number does not exist in the list. return an error if it does
    def add_code_line(self, command):
        for line in self.commands:
            if line.line_number == command.line_number:
                print(f"Error: Line {command.line_number} already exists")
                return
        self.commands.append(command)

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
        self.commands.sort(key=lambda x: x.line_number)
        # print the line number and code for each code line in the list of code lines
        for code_line in self.commands:
            print (f"{code_line}")


# create a function that loops capturing an input string until the user types "exit" and if the first word is a number split the string into a line number and code and add it to the code block.

def loop_input():
    program = Program()
    while True:
        code = input("> ")
        upperCode = code.upper()
        if upperCode == "EXIT":
            break
        elif upperCode == "LIST":
            program.print_code()
        elif upperCode == "RUN":
            print("Running the program")
        elif upperCode == "CLEAR":
            program.code_lines = []
            print("Program cleared - all lines removed")
        elif upperCode.isdigit():
            program.remove_code_line(int(upperCode))
        else:
            words = split_string(code, string_separators())
            if words[0].isdigit():
                line_number = int(words[0])
                token_list = lexerize(words[1:])
                if token_list:
                    parse_tokens(token_list)
                    code_line = Command(line_number, token_list)
                    program.add_code_line(code_line)
            else:
                print("Error: Line number is missing")



def main():
    loop_input()

if __name__ == "__main__":
    main()

# Run the program by typing the following command in the terminal
# python main.py