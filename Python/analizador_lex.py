import re

key_words = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
identifiers = [ 'abcdefghijklmnopqrstuvwxyz' ]
integers = [ '0123456789' ]
operators = ["==", "<", ">", "<=", ">=" , "!=", "!", "=", "+" , "-" , "*" ,"/", "%", "++", "--", "+=", "-=", "*=", "/=" ]

def analizador():
    with open("Pruebas.txt", "r") as file:
        test_file = file.readlines()

        for i in range(0, len(test_file)):
            contador_linea = i
            linea = test_file[contador_linea]
            p = linea.split(";")

            cont = 0
            for element in p:
                cont += 1
                element = element.replace("\n", "").strip()
                if(len(element) > 1):
                    print(f"\n*********** Linea: {contador_linea}    Elemento No: {cont} -> {element} ************")
                    element = element.replace('.', "")
                    prueba = analizador_lexico(element)
                    if prueba == False:
                        continue
                    else:
                        print(prueba)
                    print("*****************************************************")
                
                

#obtención de expresiones regulares
def get_alphanumeric_substrings(prueba):
    pattern = r'\w+'
    substrings = re.findall(pattern, prueba)
    return substrings


def analizador_lexico(prueba):
    # Obtener identificadores

    if prueba[0] == "+" or prueba[0] == "-":
        prueba = prueba[1:]

    substrings = prueba.split(' ')

    for element in substrings:
        
        if element.lower() in key_words:
            prueba = prueba.replace(element, element.upper())
        else:
            if re.search('^[A-Za-z_][A-Za-z0-9_]*', element.lower()):
                prueba = prueba.replace(element, 'ID')
            else:
                if element in operators:
                    prueba = prueba.replace(element, 'OP')
                else:
                    if re.search('^[0-9]', element.lower()):
                        prueba = prueba.replace(element, 'INT')
                    else:
                        print("\nError Lexico -> Cadena contiene elementos que no pertenecen al alfabeto")
                        return False

    return prueba


analizador()
