# DEVELOPER:

## Escobar Daniel - 318187952
## Reyes Pablo - 318217037
## Hernandez Brandon - 318263113

import re

## OUR GRAMMARR ##

key_words = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 
 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 
 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']

## REGEX SINTAXIS FOR ALPHABET
identifiers =  r'[a-zA-Z]'  

## REGEX SINTAXIS FOR INTEGERS NUMBERS
integers = r'-?[0-9]+'

## REGEX SINTAXIS FOR FLOAT NUMBERS
floats = r'-?[0-9]+(\.[0-9]+)?'

## REGEX SINTAXIS FOR STRINGS DELIMITED BY ""
strings = r'\"[^\"]*\"'

operators = ["==", "<", ">", "<=", ">=" , "!=", "!", "+" , "-" , "*" ,"/", "%", "++", "--" ]
asignation = "="
parentesis = ["(", ")"]
llaves = ["{", "}"]
corchetes = ["[", "]"]



def lexical_analyzer():
    ## Open the specified file
    with open("Pruebas.txt", "r") as file:
        test_file = file.readlines()

        ## Loop through the specified file
        for i in range(0, len(test_file)):
            contador_linea = i
            linea = test_file[contador_linea]
            element = linea.split(";")

            ## Delimited expressions
            cont = 0
            for expression in element:
                cont += 1
                expression = expression.replace("\n", "").strip()
                
                if(len(expression) > 1):
                    print(f"\n*********** Linea: {contador_linea}    Expresión No: {cont} -> {expression} ************")
                    expression = expression.replace(',', "")

                    ## LEXICAL ANALYZER FUNCTION
                    tokenized = analizador_lexico(expression)

                    # ERROR HANDLING
                    if tokenized == False:
                        continue

                    # IT IS LEXICALLY CORRECT
                    else:
                        print(tokenized)
                    print("*****************************************************")



def analizador_lexico(to_tokenize):
    
    # GET lexemes
    substrings = to_tokenize.split(' ')

    ## EXPRESION IS INVALID BECAUSE IT HASN´T MIN LENGTH
    if (len(substrings) == 1):
        print("\nError Lexico -> Cadena No contiene suficientes elementos")
        return False
    
    ## TOKENIZE PROCESS
    for lexeme in substrings:
        if lexeme in parentesis or lexeme in llaves or lexeme in llaves:
            to_tokenize = to_tokenize.replace(lexeme, "O/C")
        else:
            if lexeme.lower() in key_words:
                to_tokenize = to_tokenize.replace(lexeme, lexeme.upper())
            else:
                if  re.search(strings, lexeme.lower()):
                    to_tokenize = to_tokenize.replace(lexeme, "STRING")
                else:
                    if re.search(identifiers, lexeme.lower()):
                        to_tokenize = to_tokenize.replace(lexeme, 'ID')
                    else:
                        if lexeme in operators:
                            to_tokenize = to_tokenize.replace(lexeme, 'OP')
                        else:
                            if lexeme == asignation:
                                to_tokenize = to_tokenize.replace(lexeme, 'ASIG')
                            else:
                                if re.search(integers, lexeme.lower()):
                                    to_tokenize = to_tokenize.replace(lexeme, 'INT')
                                else:
                                    print("\nError Lexico -> La expresión contiene elementos que no pertenecen al alfabeto")
                                    return False

    return to_tokenize


lexical_analyzer()
