"""
Lexer = Lexical Analyser
     Break source code to token that identify by the language
     1. Read source code
     2. Break to word list
     3. Initial datatype to every word in the list - Make token
"""

# ===============================================
# print("=" * 50)
# print(f"Declare function".upper())
# print("=" * 50)
# ===============================================
def removeComment(sourceCode): pass
def isIdentifier(lexeme): pass
def numberHandler(numberString): pass
def wholeWordHandler(wholeWordString): pass
def partialWordHandler(partialWordString): pass
def library(): pass

class Lexer(object):
     def __init__(self, sourceCode):
          self.sourceCode = sourceCode

     # tokenize method - create token from file input
     def tokenize(self):
          # print('This line in tokenize')
          # Initial parameter.
          keywordList, operator, separator, separatorList, allSpecialKeys = library()

          sourceCode = self.sourceCode

          # ===============================================
          # print("=" * 50)
          # print(f"Step2: Remove all comment".upper())
          # print("=" * 50)
          # ===============================================
          sourceCode, checkSingleQuotes = removeComment(sourceCode)
          # print('checkSingleQuotes = ', checkSingleQuotes)

          # All lexeme will stored in lexeme list 
          lexeme = []

          # Split source file to words and store in wordList
          wordList = sourceCode.split()
     
          # Check every single word in word list and append to lexeme
          for word in wordList:

               # Check whole word is key word, word not contain any key =============
               
               if word in keywordList:
                    key, value = wholeWordHandler(word)
                    lexeme.append({f'{key}': f'{value}'})
                    continue

               # Word contain key ==============================================
               else:
                    begin = 0
                    i = 0

                    while i < len(word):
                         # Found double keyword Operator
                         if i + 1 < len(word) and (word[i] + word[i+1]) in operator:

                              # whatever before keyword is a lexeme
                              if len(word[begin:i]) >= 1 :
                                   key, value = wholeWordHandler(word[begin:i])
                                   lexeme.append({f'{key}': f'{value}'})

                              # Double keyword is a lexeme
                              lexeme.append({'OPERATOR': f'{word[i]+word[i+1]}'})

                              begin = i+2
                              i = begin

                         # Found single keyword Operator
                         elif word[i] in operator: 
                              # print ('i in SINGLE keyword BEFPORE process = ', i)

                              # Whatever before i is a Lexeme
                              if len(word[begin:i]) >= 1:
                                   key, value = wholeWordHandler(word[begin:i])
                                   lexeme.append({f'{key}': f'{value}'})

                              # Single keyword is a Operator
                              lexeme.append({'OPERATOR': f'{word[i]}'})

                              begin = i+1
                              i = begin
                         
                         # Found Separator

                         elif word[i] in separatorList: 

                              # Whatever before i is a lexeme
                              if len(word[begin:i]) >= 1:
                                   key, value = wholeWordHandler(word[begin:i])
                                   lexeme.append({f'{key}': f'{value}'})

                              # Single keyword is a Separator
                              lexeme.append({'SEPARATOR': f'{word[i]}'})

                              begin = i+1
                              i = begin

                         # no key word found, from the last keyword to end is a lexeme
                         else:
                              if i == len(word) - 1:
                                   if len(word[begin:(i+1)]) >= 1:
                                        key, value = wholeWordHandler(word[begin:(i+1)])
                                        lexeme.append({f'{key}': f'{value}'})

                                        i += 1

                              else:
                                   i += 1
                    
                    

          return lexeme

          # else:
          #      print('Separator miss match')

# ===============================================
# print("=" * 50)
# print(f"Define function".upper())
# print("=" * 50)
# ===============================================

def removeComment(sourceCode):
     if '!' not in sourceCode:
          return sourceCode, True
     else:

          # commentIdx store all index of '!' in sourceCode
          commentIdx = []
          for i in range(len(sourceCode)):
               if sourceCode[i] == '!':
                    commentIdx.append(i)

          # Check for miss match '!' pair
          if len(commentIdx) % 2 != 0:
               # print("'!' pair miss match")
               return -1, False
          else:
               if len(commentIdx) >= 2:
                    # print('commentIdx = ', commentIdx)
                    i = 0
                    while i < len(commentIdx):
                         # print('i = ', i)
                         begin = commentIdx[i]
                         end = commentIdx[i+1]
                         # print('begin = ', begin)
                         # print('end = ', end)
                         sourceCode = sourceCode.replace(sourceCode[begin:end], (int(end) - int(begin))*' ')
                         i += 2
                         
                    # print('sourceCode = ', sourceCode)
                    return sourceCode, True
# print('This line in Lexer')

# def isExistKey(word, *key):


def isIdentifier(lexeme):
     if lexeme[0].isalpha():
          # print('first caracter is qualify')
          i = 1
          for i in range(len(lexeme)):
               # print('this line in for loop of lexeme')
               if lexeme[i].isalnum() or lexeme[i] == '$':
                    i += 1
                    continue
               else:
                    # print (lexeme, ' is not idetifier')
                    return False
          # print(lexeme, ' is an identifier')
          return True

def numberHandler(numString):
     try:
        numInt = int(numString)
        return True, numInt, "INT"
     except ValueError:
          try:
               numFloat = float(numString)
               return True, numFloat, "FLOAT"
          except ValueError:
               return False, -1, "NAN"

def wholeWordHandler(wholeWordString):
     # Check whole word is key word, operator, separator or number. 
     # The word is not a compound string which include leter or number with any of key
     
     keywordList, operator, separatorDict, separatorList, allSpecialKeys = library()
     isNumber, value, dataType = numberHandler(wholeWordString)

     if wholeWordString in keywordList:
          return 'KEYWORD', wholeWordString

     # Check wholeword is operator
     elif wholeWordString in operator:
          return 'OPERATOR', wholeWordString

     # Check wholeword is separator
     elif wholeWordString in separatorList:
          return 'SEPARATOR', wholeWordString

     # Check wholeword is number
     elif isNumber == True:
          return dataType, value
     
     # Check wholeword is identifier
     else:
          if isIdentifier(wholeWordString) == True:
               return 'IDENTIFIER', wholeWordString
          # The rest is Error
          else:
               return 'ERROR', wholeWordString

     # for key in allSpecialKeys:
     #      if key not in wholeWordString:
     #           # Check is wholeword is keyword
     #           if wholeWordString in keywordList:
     #                return 'KEYWORD', wholeWordString

     #           # Check wholeword is operator
     #           elif wholeWordString in operator:
     #                return 'OPERATOR', wholeWordString

     #           # Check wholeword is separator
     #           elif wholeWordString in separatorList:
     #                return 'SEPARATOR', wholeWordString

     #           # Check wholeword is number
     #           elif isNumber == True:
     #                return dataType, value
               
     #           # Check wholeword is identifier
     #           else:
     #                if isIdentifier(wholeWordString) == True:
     #                     return 'IDENTIFIER', wholeWordString
     #                # The rest is Error
     #                else:
     #                     return 'ERROR', wholeWordString



def partialWordHandler(partialWordString): pass

def library():
     # Define keyword
     keywordList =   [
     'int', 
     'float', 
     'bool', 
     'true', 
     'false', 
     'if', 
     'else', 
     'then', 
     'endif', 
     'while', 
     'whileend', 
     'do', 
     'doend', 
     'for', 
     'forend', 
     'input', 
     'output', 
     'and', 
     'or', 
     'not',
     ]

     # Define Operator
     operator = [
          '+',
          '-',
          '*',
          '/',
          '=',
          '>',
          '<',
          '%',
          '==',
          '>=',
          '<=',
     ]
     
     # Define Separator
     separatorDict = {

               # '(){}[],.:;
          'singleQuote'        : "'",
          'openParenthesis'    : '(',
          'closeParenthesis'   : ')',
          'openBrace'          : '{',
          'closeBrace'         : '}',
          'openBracket'        : '[',
          'closeBracket'       : ']',
          'comma'              : ',',
          'semicolon'          : ';',
     }
     
     # create separatorList from separator dictionary
     separatorList = list(separatorDict.values())

     # allSpecialKeys contain both operator and separator. Not include keyword
     allSpecialKeys = operator + separatorList

     return keywordList, operator, separatorDict, separatorList, allSpecialKeys
