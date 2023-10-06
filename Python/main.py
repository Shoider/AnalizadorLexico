import re

gramatica = {
    "T": "E",
    "E+T": "E",
    "E-T": "E",
    "i": "T",
    "(E)": "T"
}

identificadores = "abcdefghijklmnopqrstuvwxyz123456789"


def analizador():
    with open("Pruebas.txt", "r") as file:
        pruebas = file.readlines()

        for i in range(0, len(pruebas)):
            linea = i+1
            p = pruebas[i]
            p = p.split(";")
            breakpoint()
            cont = 0
            for el in p:

                cont += 1
                el = el.replace("\n", "").strip()
                print(f"\n*********** Linea: {linea}    Token {cont} -> {el} ************")
                el = el.replace('.', "")
                prueba = analizador_lexico(el)
                if prueba == False:
                    continue

                else:
                    analizador_sintactico(prueba)

                print("*****************************************************")


def get_alphanumeric_substrings(prueba):
    pattern = r'\w+'
    substrings = re.findall(pattern, prueba)
    return substrings


def analizador_lexico(prueba):
    # Obtener identificadores
    if prueba[0] == "+" or prueba[0] == "-":
        prueba = prueba[1:]

    substrings = get_alphanumeric_substrings(prueba)

    for el in substrings:

        # Si contiene elementos que no pertenecen al alfabeto
        pattern = r'[^a-z0-9()+-]'
        match = re.search(pattern, prueba)
        if match:
            print("\nError Lexico -> Cadena contiene elementos que no pertenecen al alfabeto")
            return False

        if el[0].isnumeric() and (len(el) > 1 and not (el[1:].replace("(", "").replace(")", "").isnumeric())):
            print("\nError Lexico -> Cadena con identificador no valida")
            return False

        else:
            prueba = prueba.replace(el, "i")

    return prueba


def analizador_sintactico(prueba):
    pat = r'[^i0-9()+-]'
    prueba = re.sub(pat, '', prueba)

    prueba = prueba.replace("(+", "(").replace("(-", "(")
    if "i" in prueba:
        print(prueba)  # Imprimir token con identificadores sustituidos

    flag = False
    i = 0
    while i < len(prueba):
        sub = ""
        flag = False
        for j in range(i, len(prueba)):
            sub = sub + prueba[j]

            if sub in gramatica.keys():
                prueba = prueba.replace(sub, gramatica[sub], 1)
                print(prueba)
                flag = True
                break
        if flag:
            i = 0
        else:
            i = i + 1

        if i == len(prueba):
            break
    if prueba == "E":
        print("\nSintaxis reconocida por el Analizador sintáctico\n\n")

    else:
        print("\nError Sintáctico- sintaxis no reconocida\n\n")


analizador()
