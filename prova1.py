def prova(numero):
    code = str(numero)
    spessore = []
    for a in range(0, len(code)-1):
        if (code[a] == code[a+1] and code[a]!= code[a-1]):
            stroke = 2
        elif (code[a] != code[a+1] and code[a] == code[a-1]):
            stroke = 0
        elif (code[a] != code[a-1] and code[a] != code[a+1]):
            stroke = 1
        print code[a] + " = numero; " + str(stroke) + " = spessore."
        