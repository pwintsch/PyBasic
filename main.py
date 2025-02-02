# Create a class named CodeLine which contains a line number and a string of code.


class CodeLine:
    def __init__(self, line_number, code):
        self.line_number = line_number
        self.code = code

# Create a class named Program which contains a list of CodeLine objects.

class Program:
    def __init__(self):
        self.code_lines = []

    # create a method thats a CodeLine object to the list of CodeLine objects but only if the line number does not exist in the list. return an error if it does
    def add_code_line(self, code_line):
        for line in self.code_lines:
            if line.line_number == code_line.line_number:
                print(f"Error: Line {code_line.line_number} already exists")
                return
        self.code_lines.append(code_line)

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
        self.code_lines.sort(key=lambda x: x.line_number)
        # print the line number and code for each code line in the list of code lines
        for code_line in self.code_lines:
            print (f"{code_line.line_number:<7} {code_line.code}")


# Create a function that takes a string and splits it into a array of strings each time a character is a separator from an array of chars representing the seperators. The separator becomes a single element in the array of strings.

def split_string(string, separators):
    words = []
    word = ""
    for char in string:
        if char in separators:
            if word:
                words.append(word)
                if char != " ": # if the separator is a space, don't add it to the words list
                    words.append(char)
                word = ""
        else:
            word += char
    if word:
        words.append(word)
    return words



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
            words = split_string(code, " +-*/()")
            if words[0].isdigit():
                line_number = int(words[0])
                code = " ".join(words[1:])
                code_line = CodeLine(line_number, code)
                program.add_code_line(code_line)
            else:
                print("Error: Line number is missing")



def main():
    loop_input()

if __name__ == "__main__":
    main()

# Run the program by typing the following command in the terminal
# python main.py