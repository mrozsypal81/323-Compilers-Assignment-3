"""
Compiler Assignment 1 - Lexical Analysis

Purpose:
    Read input file
    Build lexeme from input
    Using Finite State Machine

Function:
    openSourceFile: accept file input and return a string of its content
    removeComment : accept string input and return that string without comment part
    tokenize      : accept string input and return a list of meanful lexeme

Process
    Program start at main.py
    Step 1: input file is passed in openSourceFile method. 
            "content" = All character in the file will be returned
    Step 2: Process "content" to create lexeme list
    Step 3: Create output file with all element in lexeme list from step 2 

"""

from Lexer import *
# import Lexer
def openSourceFile(fileName):
    # ===============================================
    # print("=" * 50)
    # print(f"Read Source code from file".upper())
    # print("=" * 50)
    # ===============================================

    with open(fileName, 'r') as file:
        content = file.read()

    return content


def main():
    # ===============================================
    # print("=" * 50)
    # print(f"Step 1: read source file in and store in string 'lex'".upper())
    # print("=" * 50)
    # ===============================================

    content = openSourceFile('test.lang')
    # print('content = ', content)





    # ===============================================
    # print("=" * 50)
    # print(f"Step 2: create lexeme from the string 'lex'".upper())
    # print("=" * 50)
    # ===============================================

    # Create Object 'lex' which is Lexer type/class, initialize with source code
    lex = Lexer(content)

    # Process tokenize and return lexeme
    lexeme = lex.tokenize()





    # ===============================================
    # print("=" * 50)
    # print(f"Step 3: Generate output file.upper())
    # print("=" * 50)
    # ===============================================
    
    # Please delete the outputLexer.txt file before every compiles
    output = open('outputLexer.txt', 'a')
    print('#' * 30)

    output.write('\n\n')
    output.write('===============================================\n')
    output.write('Output file start here\n')
    output.write('This part is added to separate every time compile if output file is not deleted\n')
    output.write('===============================================\n')
    output.write('\n\n')
    output.write('TOKEN \t\t\tLEXEME\n\n')
    i = 0
    while i < len(lexeme):

        # print(f'lexeme {i} = ', lexeme[i].keys, ' = ', lexeme[i]values)
        # print(f'lexeme {i} = ', lexeme[i])
        output.write(f'{list(lexeme[i].keys())[0]:<12} = \t{list(lexeme[i].values())[0]}\n')
        i += 1
    print('#' * 30)

    
main()


