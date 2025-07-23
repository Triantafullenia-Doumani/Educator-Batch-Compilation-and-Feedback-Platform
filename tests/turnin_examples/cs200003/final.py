import sys

def lektikos():
    global line, word
    state = 0
    word = ''
    while True:
        ch = infile.read(1)
        ch = ch.decode()
        word = word + ch

        if ch == '\n':
            line = line + 1
        if state == 0:
            if ch in [' ', '\t', '\n', '\r']:
                state = 0
                word = ''
            elif ch == '':
                return 'eoftk', ''
            elif ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
                state = 1
            elif ch in "0123456789":
                state = 2
            elif ch == '+':
                return '+tk', '+'
            elif ch == '-':
                return '-tk', '-'
            elif ch == '*':
                return '*tk', '*'
            elif ch == '/':
                state = 3
            elif ch == '%':
                return '%tk', '%'
            elif ch == '<':
                state = 4
            elif ch == '>':
                state = 5
            elif ch == '=':
                state = 6
            elif ch == '!':
                state = 7
            elif ch == ',':
                return ',tk', ','
            elif ch == ':':
                return ':tk', ':'
            elif ch == '(':
                return '(tk', '('
            elif ch == ')':
                return ')tk', ')'
            elif ch == '#':
                state = 8
            else:
                print("Error at line " + str(line) + ": wrong character")
                exit(0)
        elif state == 1:
            if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
                state = 1
            elif ch in "0123456789":
                state = 1
            else:
                #desmeymenes
                word = word[0:len(word) -1]
                infile.seek(infile.tell()-1, 0)
                if ch == '\n':
                    line = line - 1
                if word == 'main':
                    return 'maintk', 'main'
                elif word == 'def':
                    return 'deftk', 'def'
                elif word == 'global':
                    return 'globaltk', 'global'
                elif word == 'if':
                    return 'iftk', 'if'
                elif word == 'elif':
                    return 'eliftk', 'elif'
                elif word == 'else':
                    return 'elsetk', 'else' 
                elif word == 'while':
                    return 'whiletk', 'while'
                elif word == 'print':
                    return 'printtk', 'print'
                elif word == 'return':
                    return 'returntk', 'return' 
                elif word == 'input':
                    return 'inputtk', 'input'
                elif word == 'int':
                    return 'inttk','int' 
                elif word == 'and':
                    return 'andtk', 'and'
                elif word == 'or':
                    return 'ortk', 'or'
                elif word == 'not':
                    return 'nottk', 'not'
                else:
                    return 'idtk', word
        elif state == 2:
            if ch in "0123456789":
                state = 2
            else:
                word = word[0:len(word) -1]
                infile.seek(infile.tell()-1, 0)
                if ch == '\n':
                    line = line - 1
                if int(word) > 32767:
                    print("Error at line " + str(line) + ": " + word + " is too big")
                    exit(0)
                    
                return 'constanttk', word
        elif state == 3:
            if ch == '/':
                return '//tk', '//'
            else:
                print("Error at line " + str(line) + ": / was expected")
                exit(0)
        elif state == 4:
            if ch == '=':
                return '<=tk', '<='
            else:
                word = word[0:len(word) -1]
                infile.seek(infile.tell()-1, 0) 
                if ch == '\n':
                    line = line - 1
                return '<tk', '<'
        elif state == 5:
            if ch == '=':
                return '>=tk', '>='
            else:
                word = word[0:len(word) -1]
                infile.seek(infile.tell()-1, 0)
                if ch == '\n':
                    line = line - 1
                return '>tk', '>'
        elif state == 6:
            if ch == '=':
                return '==tk', '=='
            else:
                word = word[0:len(word) -1]
                infile.seek(infile.tell()-1, 0)
                if ch == '\n':
                    line = line - 1
                return '=tk', '='
        elif state == 7:
            if ch == '=':
                return '!=tk', '!='
            else:
                print("Error at line " + str(line) + ": = was expected")
                exit(0)
        elif state == 8:
            if ch == '{':
                return '#{tk', '#{'
            elif ch == '}':
                return '#}tk', '#}'
            elif ch == '#':
                state = 9
            elif ch == 'd':
                state = 11
            elif ch == 'i':
                state = 13
            else:
                print("Error at line " + str(line) + ":  unexpected character")
                exit(0)
        elif state == 9:
            if ch == '#':
                state = 10
            elif ch == '':
                print("Error at line " + str(line) + ":  unexpected eof inside comments")
                exit(0)
            else:
                state = 9
        elif state == 10:
            if ch == '#':
                state = 0
                word = ''
            elif ch == '':
                print("Error at line " + str(line) + ":  unexpected eof inside comments")
                exit(0)
            else:
                state = 9
        elif state == 11:
            if ch == 'e':
                state = 12
            else:
                print("Error at line " + str(line) + ":  unexpected character")
                exit(0)
        elif state == 12:
            if ch == 'f':
                return "#deftk", '#def'
            else:
                print("Error at line " + str(line) + ":  unexpected character")
                exit(0)
        elif state == 13:
            if ch == 'n':
                state = 14
            else:
                print("Error at line " + str(line) + ":  unexpected character")
                exit(0)
        elif state == 14:
            if ch == 't':
                return "#inttk", '#int'
            else:
                print("Error at line " + str(line) + ":  unexpected character")
                exit(0)



def start_rule():
    global token, word
    
    token, word = lektikos()
    
    def_main_part()
    call_main_part()

def def_main_part():
    global token, word
    
    declare_globals()
    
    while token == 'deftk':
        token, word = lektikos()
        def_function()
        
def declare_globals():
    global token, word

    if token == '#inttk':
        token, word = lektikos()
        id_list("variable")

def id_list(type):
    global token, word

    if token == 'idtk':
        addEntity(word, type)
        token, word = lektikos()
        while token == ',tk':
            token, word = lektikos()
            if token == 'idtk':
                addEntity(word, type)
                token, word = lektikos()
            else:
                print("Error at line " + str(line) + ":  expected id after ,")
                exit(0)
                
        
def def_function():   
    global token, word
    global hasReturn
    
    if token == 'idtk':
        functionName = word
        
        addEntity(functionName, "function")
        addScope(functionName)
        
        token, word = lektikos()
        if token == '(tk':
            token, word = lektikos()
            id_list("parameter")
            if token == ')tk':
                token, word = lektikos()
                if token == ':tk':
                    token, word = lektikos()
                    if token == '#{tk':
                        token, word = lektikos()
                        declarations()
                        
                        while token == 'deftk':
                            token, word = lektikos()
                            def_function()
                        
                        startquad = nextquad()
                        lastEntity = len(symbolTable[1][2]) -1
                        symbolTable[1][2][lastEntity].append(startquad)
                        
                        hasReturn = False
                        genquad("begin block", functionName, "_", "_")
                        globals_locally()
                        statements()
                        
                        genquad("end block", functionName, "_", "_")
                        
                        if hasReturn == False:
                            print("Error at line " + str(line) + ":  expected return in function")
                            exit(0)
                            
                        framelenth = symbolTable[0][3]
                        symbolTable[1][2][lastEntity].append(framelenth)
                        deleteScope()
                        
                        if token == '#}tk':
                            token, word = lektikos()
                        else:
                            print("Error at line " + str(line) + ":  expected #}")
                            exit(0)
                    else:
                        print("Error at line " + str(line) + ":  expected #{")
                        exit(0)
                else:
                    print("Error at line " + str(line) + ":  expected :")
                    exit(0)
            else:
                print("Error at line " + str(line) + ":  expected )")
                exit(0)
        else:
            print("Error at line " + str(line) + ":  expected (")
            exit(0)
    else:
        print("Error at line " + str(line) + ":  expected id")
        exit(0)


def globals_locally():
    global token, word
    
    while token == 'globaltk':
        token, word = lektikos()
        id_list("globals_locally")
    
def declarations():
    global token, word
    
    while token == '#inttk':
        token, word = lektikos()
        id_list("variable")
        
def statements():
    global token, word
    
    statement()

    while token == 'idtk' or token == 'printtk' or token == 'returntk' or token == 'iftk' or token == 'whiletk':
        statement()

def statement(): 
    global token, word
    
    if token == 'idtk' or token == 'printtk' or token == 'returntk':
        simple_statement()
    elif token == 'iftk' or token == 'whiletk':
        structured_statement()
    else:
        print("Error at line " + str(line) + ":  expected start of statement")
        exit(0)
        
def simple_statement(): 
    global token, word
    
    if token == 'idtk':
        id = word
        token, word = lektikos()
        assignment_stat(id)
    elif token == 'printtk':
        token, word = lektikos()
        print_stat()
    elif token == 'returntk':
        token, word = lektikos()
        return_stat()

def structured_statement():
    global token, word
    
    if token == 'iftk':
        token, word = lektikos()
        if_stat()
    elif token == 'whiletk':
        token, word = lektikos()
        while_stat()

def assignment_stat(id):
    global token, word
    
    findEntity(id, "variable")
    if token == '=tk':
        token, word = lektikos()
        if token == 'inttk':
            token, word = lektikos()
            if token == '(tk':
                token, word = lektikos()
                if token == 'inputtk':
                    token, word = lektikos()
                    if token == '(tk':
                        token, word = lektikos()
                        if token == ')tk':
                            token, word = lektikos()
                            if token == ')tk':
                                token, word = lektikos()
                                genquad("inp", id, "_", "_")
                            else:
                                print("Error at line " + str(line) + ":  expected )")
                                exit(0)
                        else:
                            print("Error at line " + str(line) + ":  expected )")
                            exit(0)
                    else:
                        print("Error at line " + str(line) + ":  expected (")
                        exit(0)
                else:
                    print("Error at line " + str(line) + ":  expected input")
                    exit(0)
            else:
                print("Error at line " + str(line) + ":  expected (")
                exit(0)
        else:
            place = expression()
            genquad(":=", place, "_", id)
    else:
        print("Error at line " + str(line) + ":  expected =")
        exit(0)


def print_stat():
    global token, word
    
    if token == '(tk':
        token, word = lektikos()
        place = expression()
        genquad("out", place, "_", "_")
        if token == ')tk':
            token, word = lektikos()
        else:
            print("Error at line " + str(line) + ":  expected sdfsfsdfsdf)")
            exit(0)
    else:
        print("Error at line " + str(line) + ":  expected (")
        exit(0)
        
def return_stat():
    global token, word
    global hasReturn
    
    hasReturn = True
    place = expression()
    
    genquad("retv", place, "_", "_")

def if_stat():
    global token, word

    true, false = condition()

    if token == ':tk':
        token, word = lektikos() 
        if token == '#{tk':
            token, word = lektikos()
            
            backpatch(true, nextquad())
            statements()
            
            jump = makelist(nextquad())
            genquad("jump", "_", "_", "_")
            
            if token == '#}tk':
                token, word = lektikos()
            else:
                print("Error at line " + str(line) + ":  expected #}")
                exit(0)
        else:
            backpatch(true, nextquad())
            statement()
            jump = makelist(nextquad())
            genquad("jump", "_", "_", "_")
    else:
        print("Error at line " + str(line) + ":  expected :")
        exit(0)
    
    backpatch(false, nextquad())
    while token == 'eliftk':
        token, word = lektikos()
        true, false = condition()
        if token == ':tk':
            token, word = lektikos() 
            if token == '#{tk':
                token, word = lektikos()
                
                backpatch(true, nextquad())
                
                statements()
                
                j = makelist(nextquad())
                genquad("jump", "_", "_", "_")
                jump = merge(jump, j)
            
                backpatch(false, nextquad())
                
                if token == '#}tk':
                    token, word = lektikos()
                else:
                    print("Error at line " + str(line) + ":  expected #}")
                    exit(0)
            else:
                backpatch(true, nextquad())
                
                statement()
                
                j = makelist(nextquad())
                genquad("jump", "_", "_", "_")
                jump = merge(jump, j)
            
                backpatch(false, nextquad())
        else:
            print("Error at line " + str(line) + ":  expected :")
            exit(0)
                
    if token == 'elsetk':
        token, word = lektikos()
        if token == ':tk':
            token, word = lektikos() 
            if token == '#{tk':
                token, word = lektikos()
                statements()
                if token == '#}tk':
                    token, word = lektikos()
                else:
                    print("Error at line " + str(line) + ":  expected #}")
                    exit(0)
            else:
                statement()
        else:
            print("Error at line " + str(line) + ":  expected :")
            exit(0)
    
    backpatch(jump, nextquad())


def while_stat():
    global token, word
    
    label = nextquad()
    true, false = condition()
    if token == ':tk':
        token, word = lektikos() 
        if token == '#{tk':
            token, word = lektikos()
            
            backpatch(true, nextquad())
            statements()
            genquad("jump", "_", "_", label)
            backpatch(false, nextquad())
            if token == '#}tk':
                token, word = lektikos()
            else:
                print("Error at line " + str(line) + ":  expected #}")
                exit(0)
        else:
            backpatch(true, nextquad())
            statement()
            genquad("jump", "_", "_", label)
            backpatch(false, nextquad())
    else:
        print("Error at line " + str(line) + ":  expected :")
        exit(0)
 
 
def expression():
    global token, word
    
    optional_sign()
    place = term()
    
    while token == '+tk' or token == '-tk':
        addOp = word
        token, word = lektikos()
        place2 = term()
        
        w = newtemp()
        genquad(addOp, place, place2, w)
        place = w
    return place
def term():
    global token, word
    
    place = factor()
    
    while token == '*tk' or token == '//tk' or token == '%tk':
        mulOp = word
        if mulOp == '//':
            mulOp = '/'
        token, word = lektikos()
        place2 = factor()
        
        w = newtemp()
        genquad(mulOp, place, place2, w)
        place = w
    
    return place

def factor():
    global token, word
    
    if token == 'constanttk':
        place = word
        token, word = lektikos()
        return place
    elif token == '(tk':
        token, word = lektikos()
        place = expression()
        if token == ')tk':
            token, word = lektikos()
            return place
    elif token == 'idtk':
        place = word
        token, word = lektikos()
        place = id_tail(place)
        return place
    else:
        print("Error at line " + str(line) + ":  expected integer, ( or id")
        exit(0)
        
def id_tail(place):
    global token, word
    
    if token == '(tk':
        findEntity(place, "function")
        token, word = lektikos()
        actual_par_list()
        w = newtemp()
        genquad("par", w, "RET", "_")
        genquad("call", place, "_", "_")
        place = w
        if token == ')tk':
            token, word = lektikos()
        else:
            print("Error at line " + str(line) + ":  expected )")
            exit(0)
    else:
        findEntity(place, "variable")
        
    return place
            
def actual_par_list():
    global token, word
    
    if token != ')tk':
        place = expression()
        genquad("par", place, "CV", "_")
        while token == ',tk':
            token, word = lektikos()
            place = expression()
            genquad("par", place, "CV", "_")

def condition():
    global token, word
    
    true, false = bool_term()
    while token == 'ortk':
        
        backpatch(false, nextquad())
        token, word = lektikos()
        true2, false2 = bool_term()
        
        true = merge(true, true2)
        false = false2
        
    return true, false

def bool_term():
    global token, word
    
    true, false = bool_factor()
    while token == 'andtk':
        backpatch(true, nextquad())
        token, word = lektikos()
        
        true2, false2 = bool_factor()
        
        true = true2
        false = merge(false, false2)
        
    return true, false
        
def bool_factor():
    global token, word
    
    if token == 'nottk':
        token, word = lektikos()
        
        place1 = expression()
        if token == '>tk' or token == '<tk' or token == '<=tk' or token == '>=tk' or token == '==tk' or token == '!=tk':
            relOp = word
            if relOp == '!=':
                relOp = '<>'
            if relOp == '==':
                relOp = '='
            token, word = lektikos()
            place2 = expression()
            
            false = makelist(nextquad())
            genquad(relOp, place1, place2, "_")
            true = makelist(nextquad())
            genquad("jump", "_", "_", "_")
            
            return true, false
    else:
        place1 = expression()
        if token == '>tk' or token == '<tk' or token == '<=tk' or token == '>=tk' or token == '==tk' or token == '!=tk':
            relOp = word
            if relOp == '!=':
                relOp = '<>'
            if relOp == '==':
                relOp = '='
            token, word = lektikos()
            place2 = expression()
            
            true = makelist(nextquad())
            genquad(relOp, place1, place2, "_")
            false = makelist(nextquad())
            genquad("jump", "_", "_", "_")
            
            return true, false
        else:
            print("Error at line " + str(line) + ":  expected relop")
            exit(0)
    
def optional_sign():
    global token, word
    
    if token == '+tk' or token == '-tk':
        addOp = word
        token, word = lektikos()
        word = addOp + word

def call_main_part():
    global token, word
    
    genquad("begin block", "main", "_", "_")
    if token == '#deftk':
        token, word = lektikos()
        if token == 'maintk':
            token, word = lektikos()
            declarations()
            statements()
            genquad("halt", "_", "_", "_")
            genquad("end block", "main", "_", "_")
        else:
            print("Error at line " + str(line) + ":  expected main")
            exit(0)
    else:
        print("Error at line " + str(line) + ":  expected #def")
        exit(0)



infile = open(sys.argv[1], "rb")
line = 1
token = ''
word = ''


quads = []
counter = 1
counterQuads = 0


def nextquad():
    global counterQuads
    
    return counterQuads

def genquad(op, x, y, z):
    global quads, counterQuads
    
    label = nextquad()
    quads.append([label, op, x, y, z])
    counterQuads = counterQuads + 1
    

def newtemp():
    global counter
    
    tempVar = "T_" + str(counter)
    counter = counter + 1
    addEntity(tempVar, "variable")
    return tempVar

def emptylist():
    return []

def makelist(x):
    return [x]


def merge(list1, list2):
    return list1 + list2

def backpatch(list1, z):
    global quads

    for label in list1:
        for i in range(len(quads)):
            if label == quads[i][0]:
                quads[i][4] = z
                break

def printQuads():
    global quads
    
    outfile = open(sys.argv[1]+".int", "w")
    for i in range(len(quads)):
        #print(str(quads[i][0]) + ":" + str(quads[i][1]) + "," + str(quads[i][2]) + "," + str(quads[i][3]) + "," + str(quads[i][4]))
        outfile.write(str(quads[i][0]) + ":" + str(quads[i][1]) + "," + str(quads[i][2]) + "," + str(quads[i][3]) + "," + str(quads[i][4])+"\n")



symbolTable = []
nestingLevel = 0
hasReturn = False

def addScope(name):
    global symbolTable, nestingLevel
    
    symbolTable = [[name, nestingLevel, [], 12]] + symbolTable
    
    nestingLevel = nestingLevel + 1
    
def deleteScope():
    global symbolTable, nestingLevel
    global quads, lastConverted
    global outfileSym
    
    outfileSym.write("Symbol table\n")
    for i in range(nestingLevel):
        outfileSym.write(str(symbolTable[i]) + "\n")
    outfileSym.write("\n\n")
    
    guadsToConvert = quads[lastConverted+1:]
    convertToFinal(guadsToConvert)
    lastConverted = len(quads) - 1
    
    symbolTable = symbolTable[1: nestingLevel]
    nestingLevel = nestingLevel - 1
    
    
def addEntity(name, type):
    global symbolTable
    
    if type == "globals_locally":
        findEntity(name, type)
        
    if name == symbolTable[0][0]:
        print("Error at line " + str(line) + ": " + name + " is already defined as the name of the scope")
        exit(0)
    entitiesList = symbolTable[0][2]
    for i in range(len(entitiesList)):
        entity = entitiesList[i]
        if entity[0] == name:
            print("Error at line " + str(line) + ": " + name + " is already defined in this scope")
            exit(0)
            
    if type == "variable":
        offset = symbolTable[0][3]
        entity = [name, offset]
        symbolTable[0][2].append(entity)
        symbolTable[0][3] = symbolTable[0][3] + 4
    elif type == "parameter":
        offset = symbolTable[0][3]
        entity = [name, offset, "CV"]
        symbolTable[0][2].append(entity)
        symbolTable[0][3] = symbolTable[0][3] + 4    
    
    elif type == "globals_locally":
        entity = [name, "globals_locally"]
        symbolTable[0][2].append(entity)
    elif type == "function":
        entity = [name, "function"]
        symbolTable[0][2].append(entity)
    
def findEntity(name, type):
    global symbolTable
    
    
    if type == "globals_locally":
        mainScope = len(symbolTable) - 1
        listEntities = symbolTable[mainScope][2]
        for j in range(len(listEntities)):
            entity = listEntities[j]
            if entity[0] == name:
                string = str(entity[1])
                if string == "function":
                    print("Error at line " + str(line) + ": " + name + " is a function")
                    exit(0)
                return entity, 0
        print("Error at line " + str(line) + ": " + name + " is not defined in symbol table as global")
        exit(0)
    else:
        for i in  range(len(symbolTable)):
            listEntities = symbolTable[i][2]
            for j in range(len(listEntities)):
                entity = listEntities[j]
                if entity[0] == name:
                    if type == "function":
                        string = str(entity[1])
                        if string != "function":
                            print("Error at line " + str(line) + ": " + name + " is not a function")
                            exit(0)
                    else:
                        string = str(entity[1])
                        if string == "function":
                            print("Error at line " + str(line) + ": " + name + " is a function")
                            exit(0)
                        
                        
                    return entity, symbolTable[i][1]
    
    
    print("Error at line " + str(line) + ": " + name + " is not defined in symbol table")
    exit(0)


def findEntityFinal(name):
    global symbolTable
    
    
    for i in  range(len(symbolTable)):
        listEntities = symbolTable[i][2]
        for j in range(len(listEntities)):
            entity = listEntities[j]
            if entity[0] == name:         
                if str(entity[1]) == "globals_locally":
                    globalScope = len(symbolTable) - 1
                    listEntities = symbolTable[globalScope][2]
                    for j in range(len(listEntities)):
                        entity = listEntities[j]
                        if entity[0] == name: 
                            return entity, 0
                else:
                    return entity, symbolTable[i][1]


    
def gnlvcode(x):
    global outfile
    global symbolTable
    
    nestingLevel = symbolTable[0][1]
    entity, nestingLevelX = findEntityFinal(x)
    
    outfile.write("lw t0, -4(sp)\n")
    for i in range(nestingLevel - nestingLevelX - 1):
        outfile.write("lw t0, -4(t0)\n")
    
    offset = entity[1]
    outfile.write("addi t0, t0, -" +str(offset) + "\n")
    

def loadvr(v, r):
    global outfile
    if v[0] in "0123456789+-":
        outfile.write("li t" + str(r) +  ", " + str(v) + "\n")
    else:
        entity, nestingLevelV = findEntityFinal(v)
        nestingLevel = symbolTable[0][1]
        
        if nestingLevel == nestingLevelV: 
            offset = entity[1]
            outfile.write("lw t" + str(r) +  ", -" + str(offset) + "(sp)\n")
        elif nestingLevelV == 0: 
            offset = entity[1]
            outfile.write("lw t" + str(r) +  ", -" + str(offset) + "(gp)\n")
        else:
            gnlvcode(v)
            outfile.write("lw t" + str(r) +  ", (t0)\n")
            

def storerv(r, v):
    global outfile
    
    entity, nestingLevelV = findEntityFinal(v)
    nestingLevel = symbolTable[0][1]
    
    if nestingLevel == nestingLevelV: 
        offset = entity[1]
        outfile.write("sw t" + str(r) +  ", -" + str(offset) + "(sp)\n")
    elif nestingLevelV == 0: 
        offset = entity[1]
        outfile.write("sw t" + str(r) +  ", -" + str(offset) + "(gp)\n")
    else:
        gnlvcode(v)
        outfile.write("sw t" + str(r) +  ", (t0)\n")            



def convertToFinal(quads):
    global outfile
    
    parNum = 0
    for i in range(len(quads)):
        outfile.write("L" + str(quads[i][0]) + ":\n");
        #print(str(quads[i][0]) + ":" + str(quads[i][1]) + "," + str(quads[i][2]) + "," + str(quads[i][3]) + "," + str(quads[i][4]))
        if quads[i][1] == "jump":
            outfile.write("b L" + str(quads[i][4])+"\n")
        elif quads[i][1] == "=":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("beq t1, t2 L" + str(quads[i][4])+"\n")
        elif quads[i][1] == "=":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("beq t1, t2 L" + str(quads[i][4])+"\n")
        elif quads[i][1] == "<>":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("bne t1, t2 L" + str(quads[i][4])+"\n")
        elif quads[i][1] == ">":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("bgt t1, t2 L" + str(quads[i][4])+"\n")
        elif quads[i][1] == "<":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("blt t1, t2 L" + str(quads[i][4])+"\n")
        elif quads[i][1] == ">=":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("bge t1, t2 L" + str(quads[i][4])+"\n")
        elif quads[i][1] == "<=":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("ble t1, t2 L" + str(quads[i][4])+"\n")
        elif quads[i][1] == ":=":
            loadvr(quads[i][2], 1)
            storerv(1, quads[i][4])
        elif quads[i][1] == "+":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("add t1, t1, t2\n")
            storerv(1, quads[i][4])
        elif quads[i][1] == "-":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("sub t1, t1, t2\n")
            storerv(1, quads[i][4])
        elif quads[i][1] == "*":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("mul t1, t1, t2\n")
            storerv(1, quads[i][4])
        elif quads[i][1] == "/":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("div t1, t1, t2\n")
            storerv(1, quads[i][4])
        elif quads[i][1] == "%":
            loadvr(quads[i][2], 1)
            loadvr(quads[i][3], 2)
            outfile.write("rem t1, t1, t2\n")
            storerv(1, quads[i][4])
        elif quads[i][1] == "retv":
            loadvr(quads[i][2], 1)
            outfile.write("lw t0, -8(sp)\n")
            outfile.write("sw t1, 0(t0)\n")
        elif quads[i][1] == "inp":
            outfile.write("li a7, 5\n")
            outfile.write("ecall\n")
            outfile.write("mv t1, a0\n")
            storerv(1, quads[i][2])
        elif quads[i][1] == "out":
            loadvr(quads[i][2], 1)
            outfile.write("mv a0, t1\n")
            outfile.write("li a7, 1\n")
            outfile.write("ecall\n")
            outfile.write("la a0, str_nl\n")
            outfile.write("li a7, 4\n")
            outfile.write("ecall\n") 
        elif quads[i][1] == "halt":
            outfile.write("li a0, 0\n")
            outfile.write("li a7, 93\n")
            outfile.write("ecall\n")    
        elif quads[i][1] == "begin block":
            if quads[i][2] == "main":
                outfile.write("Lmain:\n")
                framelenth = symbolTable[0][3]
                outfile.write("addi sp, sp, " + str(framelenth) + "\n")
                outfile.write("mv gp, sp\n")
            else:
                outfile.write("sw ra, 0(sp)\n")
        elif quads[i][1] == "end block":
            if quads[i][2] != "main":
                outfile.write("lw ra, 0(sp)\n")
                outfile.write("jr ra\n")
        elif quads[i][1] == "par":
            if parNum == 0:
                for j in range(i+1, len(quads)):
                    if quads[j][1] == "call":
                        entity, nestingLevelF = findEntityFinal(quads[j][2])
                        outfile.write("addi s0, sp, " + str(entity[3]) + "\n")
            
            if quads[i][3] == "CV":
                loadvr(quads[i][2], 0)
                outfile.write("sw t0, -" + str((12 +4*parNum)) + "(s0)\n")
                parNum = parNum + 1
            else:
                entity, nestingLevelV = findEntityFinal(quads[i][2])
                outfile.write("addi t0, sp, -" + str(entity[1]) + "\n")
                outfile.write("sw t0, -8(s0)\n")
                parNum = 0
        elif quads[i][1] == "call":
            outfile.write("sw sp, -4(s0)\n")
            entity, nestingLevelV = findEntityFinal(quads[i][2])
            outfile.write("addi sp, sp, " + str(entity[3]) + "\n")
            outfile.write("jal L" + str(entity[2]) + "\n")
            outfile.write("addi sp, sp, -" + str(entity[3]) + "\n")
                
            
            
            
        #outfile.write(str(quads[i][0]) + ":" + str(quads[i][1]) + "," + str(quads[i][2]) + "," + str(quads[i][3]) + "," + str(quads[i][4])+"\n")
    
outfile = open(sys.argv[1] + ".asm", "w")
outfileSym = open(sys.argv[1] + ".sym", "w")
outfile.write(".data\n")
outfile.write("str_nl: .asciz \"\\n\"\n")
outfile.write(".text\n")
outfile.write("j Lmain\n")
lastConverted = -1     
addScope("main")    
start_rule()
printQuads()
deleteScope()
