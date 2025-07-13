import sys
import os

if (len(sys.argv) < 2):
     print("Give a filename as the second command line argument.")
     sys.exit(-1) #stop program
file=open(sys.argv[1],'r')

counter = 1
keywords = [
    'main',
    'def',
    '#def',
    '#int',
    'global',
    'if',
    'elif',
    'else',
    'while',
    'print',
    'return',
    'input',
    'int',
    'and',
    'or',
    'not'
]

#Keywords
main_token = 200
def_token = 201
global_token = 202
if_token = 203
elif_token = 204
else_token = 205
while_token = 206
print_token = 207
return_token = 208
input_token = 209
int_token = 210
and_token = 211
or_token = 212
not_token = 213
hashtagdef_token = 214
hashtagint_token = 215

#Symbols
space = 0
digit = 1
letter = 2
plus = 3
minus = 4
smaller = 5
larger = 6
equal = 7
multiply = 8
divide = 9
modulo = 10
lparen = 11
rparen =12
lblock = 13
rblock = 14
next_line = 15
quote = 16
eof = 17
colon = 18
comma = 19
hashtag = 20
non_symbol = 21
exclamation = 22

#tokens
digit_token=100
id_token=101
plus_token=102
minus_token=103
smaller_token=104
larger_token=105
equal_token=106
multiply_token=107
divide_token=108
modulo_token = 109
lparen_token=110
rparen_token=111
lblock_token=112
rblock_token=113
smallerORequal_token=114
largerORequal_token=115
eof_token=116
colon_token=117
comma_token=118
assign_token=119
quote_token=120
different_token=121
hashtag_token=122

#state
state_start=0
state_digit=1
state_letter=2
state_comments=3
state_equal=4
state_exclamation=5
state_smaller=6
state_larger=7
state_division=8
state_hashtag=9
state_closing_hashtag=10


#Errors
error_with_symbol=300
error_digit_letter=301
error_with_hashtag=302
error_eof=303
error_with_slash=304
error_with_characters=305
error_with_limit=306
error_with_exclamation=307
error_with_percent = 308
error_with_block = 309


diagram = [
    #state_start
    [state_start,state_digit,state_letter,plus_token,minus_token,state_smaller,
    state_larger,state_equal,multiply_token,state_division,modulo_token,lparen_token,
    rparen_token,error_with_block,error_with_block,state_start,quote_token,eof_token,
    colon_token,comma_token,state_hashtag,error_with_symbol,state_exclamation],
    #state_digit
    [digit_token,state_digit,error_digit_letter,digit_token,digit_token,
    digit_token,digit_token,digit_token,digit_token,digit_token,digit_token,digit_token,
    digit_token,digit_token,digit_token,digit_token,digit_token,digit_token,digit_token,
    digit_token,digit_token,error_with_symbol,digit_token],
    #state_letter
    [id_token,state_letter,state_letter,id_token,id_token,id_token,id_token,id_token,
    id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,
    id_token,id_token,id_token,id_token,error_with_symbol,id_token],
    #state_comments
    [state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,
    state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,
    state_comments,state_comments,state_comments,state_comments,state_comments,error_eof,
    state_comments,state_comments,state_closing_hashtag,state_comments,state_comments],
    #state_equal
    [assign_token,assign_token,assign_token,assign_token,assign_token,assign_token,assign_token,equal_token,
    assign_token,assign_token,assign_token,assign_token,assign_token,assign_token,assign_token,assign_token,
    assign_token,assign_token,assign_token,error_with_symbol,assign_token,assign_token,assign_token],
    #state_exclamation
    [error_with_exclamation,error_with_exclamation,error_with_exclamation,error_with_exclamation,error_with_exclamation,error_with_exclamation,
    error_with_exclamation,different_token,error_with_exclamation,error_with_exclamation,error_with_exclamation,error_with_exclamation,error_with_exclamation,
    error_with_exclamation,error_with_exclamation,error_with_exclamation,error_with_exclamation,error_with_exclamation,error_with_exclamation,error_with_symbol,
    error_with_exclamation,error_with_exclamation,error_with_exclamation],
    #state_smaller
    [smaller_token,smaller_token,smaller_token,smaller_token,smaller_token,smaller_token,smaller_token,smallerORequal_token,smaller_token,smaller_token,
    smaller_token,smaller_token,smaller_token,smaller_token,smaller_token,smaller_token,smaller_token,smaller_token,smaller_token,smaller_token,
    smaller_token,smaller_token, error_with_symbol, smaller_token],
    #state_larger
    [larger_token,larger_token,larger_token,larger_token,larger_token,larger_token,larger_token,largerORequal_token,larger_token,larger_token,larger_token,
    larger_token,larger_token,larger_token,larger_token,larger_token,larger_token,larger_token,larger_token,larger_token,larger_token,larger_token,error_with_symbol,
    larger_token],
    #state_division
    [error_with_slash,error_with_slash,error_with_slash,error_with_slash,error_with_slash,error_with_slash,error_with_slash,error_with_slash,error_with_slash,
    divide_token,error_with_slash,error_with_slash,error_with_slash,error_with_slash,error_with_slash,error_with_slash,error_with_slash,error_with_slash,
    error_with_slash,error_with_slash,error_with_slash,error_with_slash,error_with_symbol,error_with_slash],
    #state_hashtag
    [error_with_hashtag,error_with_hashtag,state_letter,error_with_hashtag,error_with_hashtag,error_with_hashtag,error_with_hashtag,
     error_with_hashtag,error_with_hashtag,error_with_hashtag,error_with_hashtag,error_with_hashtag,error_with_hashtag, lblock_token, rblock_token,
     error_with_hashtag,error_with_hashtag,error_with_hashtag,error_with_hashtag,error_with_hashtag, state_comments, error_with_hashtag, error_with_hashtag],
    #closing_hashtag
    [state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,
    state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,state_comments,
    state_start,error_with_symbol,state_comments]
]

def check_keywords(current_char, word):
    if(current_char == id_token):
        if(word in keywords):
            if(word == 'main'):
                current_char = main_token
            elif(word == 'def'):
                current_char = def_token
            elif(word == '#def'):
                current_char = hashtagdef_token
            elif(word == '#int'):
                current_char = hashtagint_token
            elif(word == 'global'):
                current_char = global_token
            elif(word == 'if'):
                current_char = if_token
            elif(word == 'elif'):     
                current_char = elif_token
            elif(word == 'else'):
                current_char = else_token
            elif(word == 'while'):
                current_char = while_token
            elif(word == 'print'):
                current_char = print_token
            elif(word == 'return'):
                current_char = return_token
            elif(word == 'input'):
                current_char = input_token
            elif(word == 'int'):
                current_char = int_token
            elif(word == 'and'):
                current_char = and_token
            elif(word == 'or'):
                current_char = or_token
            elif(word == 'not'):
                current_char = not_token
    return current_char

def errors(state):
    if (state == error_digit_letter):
        print("Error with digit and letter.")
    elif(state == error_with_hashtag):
        print("Error with '#'. ")
    elif(state ==error_with_characters):
          print("Too many characters.")
    elif(state == error_with_slash):
        print("Error with '/'. ")
    elif(state == error_with_symbol):
        print("Error with symbol. ")
    elif(state == error_eof):
        print("End of file. ")
    elif(state == error_with_limit):
        print("Number is outside of interval. ")
    elif(state == error_with_exclamation):
        print("Error with exclamation mark; != expected.")
    elif(state == error_with_block):
         print("Error with block: #{ or #} expected.")

def lex():
    global counter
    state = state_start
    token = []
    word = ''
    counterline = counter

    while(state >= 0 and state <= 10):
        character = file.read(1)
        print(f"Read character: {character}, current state: {state}")  # Debug output
        if(character == ' ' or character == '\t'):
            character_token = space
        elif(character.isdigit()):
            character_token = digit
        elif((character >= 'a' and character <='z') or (character >= 'A' and character <= 'Z')):
            character_token = letter
        elif(character == '+'):
            character_token = plus
        elif(character == '-'):
            character_token = minus 
        elif(character == '<'):
            character_token = smaller
        elif(character == '>'):
            character_token = larger
        elif(character == '='):
            character_token = equal
        elif(character == '*'):
            character_token = multiply
        elif(character == '/'):
            character_token = divide
        elif(character == '%'):
             character_token = modulo
        elif(character == '('):
            character_token = lparen
        elif(character == ')'):
            character_token = rparen
        elif(character == '{'):
             character_token = lblock
        elif(character == '}'):
             character_token = rblock
        elif(character == '\n'):
            counterline += 1
            character_token = next_line
        elif(character == '"'):
            character_token = quote
        elif(character == ''):
            character_token = eof
            break
        elif(character == ':'):
            character_token = colon
        elif(character == ','):
            character_token = comma
        elif(character == '#'):
            character_token = hashtag
        elif(character == '!'):
            character_token = exclamation
        else:
            character_token = non_symbol
        
        state = diagram[state][character_token]
        print(f"Transitioned to state: {state}, word so far: {word}")  # Debug output
        if(len(word) < 30):
               if(state == state_comments or state == state_start or state == state_closing_hashtag):
                    word = ''
               else:
                    word = word + character
        else:
            state = error_with_characters

    if(state == id_token or state == digit_token or state == smaller_token or state == larger_token or state == assign_token):
          if(character == '\n'):
               counterline =- 1
          character=file.seek(file.tell()-1,0)
          word = word[:-1]

    if(state == digit_token):
          if(int(word) > 32767 or int(word) < -32767):
               state = error_with_limit

    new_state = check_keywords(state, word)
    state = new_state
    errors(state)

    token.append(state)
    token.append(word)                 
    token.append(counterline)
    counter = counterline
    print(f"Generated token: {token}")  # Debug output
    return token


## intermediate code ################################
global listQuads
listQuads = []
listQuadsIntCode = []
listOfTemps=[]
listOfScopes = []
quadCount = 1


def generateQuad(op, x, y, z):
     global listQuads
     global quadCount

     newQuad = [quadCount, op, x, y, z]
     listQuads.append(newQuad)
     print(f"Generated quad: {newQuad}")  # Debugging output
     quadCount += 1
     listQuadsIntCode.append(newQuad)

     return newQuad

def getQuadCount(): 
     global quadCount
     return quadCount

def mergeLists(list1, list2):
     newList = list1 + list2

     return newList

def backpatch(quadList, quadIndex, label):
    if quadIndex >= len(quadList):
        print(f"Error: quadIndex {quadIndex} is out of range for quadList of length {len(quadList)}")  # Debugging output
        raise IndexError(f"quadIndex {quadIndex} out of range")
    
    if quadList[quadIndex][-1] == '_':
        quadList[quadIndex][-1] = label
        print(f"Backpatched quad at index {quadIndex} with label {label}")  # Debugging output
    else:
        print(f"Error: quad at index {quadIndex} does not have a placeholder, current quad: {quadList[quadIndex]}")  # Debugging output

def fillLastDash(listOfQuads, label):
    global listQuads
    print(f"Filling last dash with label: {label} for quads: {listOfQuads}")  # Debugging output
    for quadIndex in listOfQuads:
        if quadIndex >= len(listQuads):
            print(f"Error: quadIndex {quadIndex} is out of range for listQuads of length {len(listQuads)}")  # Debugging output
            raise IndexError(f"quadIndex {quadIndex} out of range")
        backpatch(listQuads, quadIndex, label)


## symbol table #################################
class Entity():
     def __init__(self):
          self.name=''
          self.type=''  
          self.variable=self.Variable()
          self.function=self.Function() 
          self.parameter=self.Parameter()
          self.temp=self.Temp()

     class Variable():
          def __init__(self):
               self.offset=0
     class Function():
          def __init__(self):
               self.frameLength=0 
               self.listArgument=[]
               self.nestingLevel=0
               self.startQuad=0 
     class Parameter():
          def __init__(self):
               self.offset=0
     class Temp():
          def __init__(self):
               self.offset=0

class Scope():
     def __init__(self): 
          self.name=''
          self.entities=[]
          self.nestingLevel=0

class Argument():
     def __init__(self):
          self.name=''
          self.type='Int'


def createNewEntity(object):
     global listOfScopes
     if len(listOfScopes)==0:
          return 
     ## listOfScopes is a global variable that keeps scopes in line. Last scope = current, etc...
     currentScope=listOfScopes[-1] 
     currentScope.entities.append(object)

def createNewArgument(object): 
     global listOfScopes
     if len(listOfScopes) == 0:
          return 
     currentScope = listOfScopes[-1] 
     currentScope.entities[-1].function.listArgument.append(object)

def createNewTemp():
     prefix='%'
     num_of_temps = len(listOfTemps)
     temp= prefix + str(num_of_temps+1)

     listOfTemps.append(temp)
     ent= Entity()
     ent.name=temp
     ent.type = 'TEMP'
     ent.temp.offset=calculateOffset()
     createNewEntity(ent)

     return temp


def createNewScope(name):
    global listOfScopes
    if len(listOfScopes) == 0:
        nextScope = Scope()
        nextScope.name=name
        nextScope.nestingLevel = 0
    else:
        currentScope = listOfScopes[-1]  
        nextScope = Scope()
        nextScope.name=name
        nextScope.nestingLevel = currentScope.nestingLevel + 1

    nextScope.entities = []
    listOfScopes.append(nextScope)
    print(f"Created new scope: {name}, nesting level: {nextScope.nestingLevel}")  # Debugging output

def calculateOffset():
     global listOfScopes
     if len(listOfScopes) == 0:
          return 
     currentScope=listOfScopes[-1]
     count=0
     if len(currentScope.entities)>0: 
          for temp in (currentScope.entities):
               if(temp.type=='VAR' or temp.type=='TEMP' or temp.type=='PARAM'):
                    count=count+1
     offset=12+(4*count)
     return offset

def calculateFramelength():
     global listOfScopes
     if len(listOfScopes)<2:
          return 
     
     previousScope=listOfScopes[-2]
     lastEntity=previousScope.entities[-1]
     lastEntity.function.frameLength=calculateOffset()


def addParameters(): 
     global listOfScopes
     if len(listOfScopes)<2:
          return 
     previousScope=listOfScopes[-2]
     
     for args in previousScope.entities[-1].function.listArgument:
          newEntity=Entity()
          newEntity.name=args.name
          newEntity.type='PARAM'
          newEntity.parameter.offset=calculateOffset()
          createNewEntity(newEntity)

def deleteScope():
     global listOfScopes
     if listOfScopes:
        scope = listOfScopes.pop()
        print(f"Deleted scope: {scope.name}")  # Debugging output


################### final ################################

def searchCombination(n):
     global listOfScopes
     print(f"Searching for: '{n}'")  # Debugging output
     for currentScope in reversed(listOfScopes):
          print(f"Searching in scope: '{currentScope.name}'")  # Debugging output
          for ent in currentScope.entities:
               print(f"Checking entity: '{ent.name}' with type '{ent.type}'")  # Debugging output
               if(ent.name==n):
                    print(f"Found '{n}' in scope: '{currentScope.name}'")  # Debugging output
                    return currentScope,ent
     raise ValueError(f"'{n}' not found in any scope")

final_file=open('final_file.asm','w')
final_file.write("\n\n\n")

def loadValueRegister(v,r):
     global final_file
     global listOfScopes
     currentScope=listOfScopes[-1]

     try:

          if (v.isdigit()): # v is constant
               final_file.write(f"li t{r},{v}\n")
          else: # v is a variable
               (scope,ent) = searchCombination(v)

               if scope.nestingLevel == 0:
                     addr = "(gp)" if ent.type in ['VAR', 'TEMP'] else None
               elif scope.nestingLevel == currentScope.nestingLevel:
                     addr = "(sp)"
               elif scope.nestingLevel < currentScope.nestingLevel:
                    if ent.type=='VAR': 
                         final_file.write("lw t"+str(r)+",(t0)\n")
                    elif ent.type=='PARAM': 
                         final_file.write("lw t"+str(r)+",(t0)\n")

               if addr:
                    if ent.type == 'VAR':
                         final_file.write(f"lw t{r},-{ent.variable.offset}{addr}\n")
                    elif ent.type == 'PARAM':
                         final_file.write(f"lw t{r},-{ent.parameter.offset}{addr}\n")
                    elif ent.type == 'TEMP':
                         final_file.write(f"lw t{r},-{ent.temp.offset}{addr}\n")
     except Exception as e:
          print(f"Error loading variable {v} into register t{r}: {str(e)}")


def storeValueRegister(r, v):
     global final_file
     global listOfScopes
     currentScope=listOfScopes[-1]
     (scope,ent) = searchCombination(v)

     try:


               if scope.nestingLevel == 0:
                     addr = "(gp)" if ent.type in ['VAR', 'TEMP'] else None
               elif scope.nestingLevel == currentScope.nestingLevel:
                     addr = "(sp)"
               elif scope.nestingLevel > currentScope.nestingLevel:
                    if ent.type=='VAR': 
                         final_file.write("sw t"+str(r)+",(t0)\n")
                    elif ent.type=='PARAM': 
                         final_file.write("sw t"+str(r)+",(t0)\n")
               else:
                     raise ValueError("Variable scope handling not implemented for this scenario")

               if addr:
                    if ent.type == 'VAR':
                         final_file.write(f"sw t{r},-{ent.variable.offset}{addr}\n")
                    elif ent.type == 'PARAM':
                         final_file.write(f"sw t{r},-{ent.parameter.offset}{addr}\n")
                    elif ent.type == 'TEMP':
                         final_file.write(f"sw t{r},-{ent.temp.offset}{addr}\n")
     except Exception as e:
          print(f"Error storing variable {v} into register t{r}: {str(e)}")
          
          

def quadEndBlock(i):
     global listQuads

     for index in range(i, len(listQuads)):
         if listQuads[index][1] == 'end_block':
            return listQuads[index][0]  # return the number of the quad where end_block belongs to
     return -1  

def generateJumpQuad(quad):
    if quad[4] != '_':
        final_file.write("j L" + str(quad[4]) + '\n')
    else:
        final_file.write("j L" + str(len(listQuads)) + '\n')  # Fallback to the next quad


def generateRelopQuad(quad):
     loadValueRegister(quad[2],1)
     loadValueRegister(quad[3],2)
     if(quad[1]=='=='): #relop/branch
          final_file.write("beq t1,t2,L"+str(quad[4])+'\n')
     elif(quad[1]=='!='):
          final_file.write("bne t1,t2,L"+str(quad[4])+'\n')
     elif(quad[1]=='>'):
          final_file.write("bgt t1,t2,L"+str(quad[4])+'\n')
     elif(quad[1]=='<'):
          final_file.write("blt t1,t2,L"+str(quad[4])+'\n')
     elif(quad[1]=='>='):
          final_file.write("bge t1,t2,L"+str(quad[4])+'\n')
     elif(quad[1]=='<='):
          final_file.write("ble t1,t2,L"+str(quad[4])+'\n')

def generateArithmeticQuad(quad):
    op = quad[1]
    loadValueRegister(quad[2], 1)
    loadValueRegister(quad[3], 2)
    
    if op == '+':
        final_file.write("add t1,t1,t2\n")
    elif op == '-':
        final_file.write("sub t1,t1,t2\n")
    elif op == '*':
        final_file.write("mul t1,t1,t2\n")
    elif op == '//':
        final_file.write("div t1,t1,t2\n")
    elif op == '%':
         final_file.write("div t3, t1, t2\nmul t3, t3, t2\nsub t1, t1, t3\n")
    
    storeValueRegister(1, quad[4])


def final():
     global listOfScopes 
     global listQuads
     global final_file
     i=0
     current_scope=listOfScopes[-1]

     for quad in listQuads:
          final_file.write("L" + str(quad[0]) + ':\n')
          quad_type = quad[1]

          if quad_type == 'jump':
               generateJumpQuad(quad)

          elif quad_type in ['==', '!=', '>', '<', '>=', '<=']:
               generateRelopQuad(quad)

          elif quad_type in ['+', '-', '*', '//', '%']:
               generateArithmeticQuad(quad)

          elif quad_type ==':=':
               loadValueRegister(quad[2],1)
               storeValueRegister(1,quad[4])

          elif quad_type =='ret':
               loadValueRegister(quad[2],1)
               final_file.write("lw t0,-8(sp)\n") 
               final_file.write("sw t1,(t0)\n")
               final_file.write("j L"+str(quadEndBlock(quad[0]))+"\n") # find quad with endBlock

          elif quad_type =='input':
               final_file.write("li a7,5\n") # read from keyboard
               final_file.write("ecall\n")
               final_file.write("addi t1,a0, 0\n")
               storeValueRegister(1,quad[2]) 

          elif quad_type =='output':
               loadValueRegister(quad[2],1)  # load a variable on register 1
               final_file.write("addi a0,t1, 0\n")
               final_file.write("li a7,1\n")
               final_file.write("ecall\n")

          elif quad_type =='begin_block' and current_scope.nestingLevel != 0 :
               final_file.write("sw ra,(sp)\n")
               final_file.write("addi sp, sp, -4\n")  # Ensure stack pointer moves

          elif quad_type =='begin_block' and current_scope.nestingLevel == 0 :
               final_file.seek(0,os.SEEK_SET) # go to beginning of file
               final_file.write("j L"+str(quad[0])) # first label of the main program
               final_file.seek(0,os.SEEK_END) 
               
               final_file.write("addi sp,sp,"+str(calculateOffset()))
               final_file.write("addi gp,sp,0")

          elif quad_type =='end_block' and current_scope.nestingLevel!=0:
               final_file.write("lw ra,(sp)\n")
               final_file.write("addi sp, sp, 4\n")  # Ensure stack pointer restores
               final_file.write("jr ra\n")

          elif quad_type =='par':

               if(quad[3]=='CV'):
                    loadValueRegister(quad[2],0)
                    final_file.write("sw t0,-"+str(12+4*i)+"(fp)\n")
                    i+=1
               elif(quad[3]=='RET'):
                    (scope,ent)=searchCombination(quad[2])
                    final_file.write("addi t0,sp,-"+ent.temp.offset+"\n")
                    final_file.write("sw t0,-8(fp)\n")

          elif quad_type =='call':
               (scope,ent)=searchCombination(quad[2])
               if current_scope.nestingLevel==ent.function.nestingLevel:
                    final_file.write("lw t0,-4(sp)\n")
                    final_file.write("sw t0,-4(fp)\n")
               elif current_scope.nestingLevel<ent.function.nestingLevel:
                    final_file.write("sw sp,-4(fp)\n")

               final_file.write("addi sp,sp,"+str(ent.function.frameLength)+"\n")
               final_file.write("jal L" + str(len(listQuads)) + "\n")
               final_file.write("addi sp,sp,"+str(ent.function.frameLength)+"\n")
     

     listQuads.clear() 

########## syntax #########################################

def syntax():
     global ret
     global counter
     ret=lex()
     counter=ret[2]

     def program():
          declarations()
          createNewScope('Function')
          functions()
          createNewScope('main')
          main()
          print("Finished parsing program")

     def declarations():
          global ret
          global counter
          while(ret[0]==hashtagint_token):
               if(ret[0] == hashtagint_token):
                    ret=lex()
                    counter=ret[2]
                    id_list(1)

     def id_list(option):
          global ret
          global counter
          if(ret[0]==id_token):
               name = ret[1]
               ret=lex()
               counter=ret[2]

               if(option == 1): #new entity is created if called from declarations
                    ent=Entity()
                    ent.name=name
                    ent.type='VAR'
                    ent.variable.offset=calculateOffset()
                    createNewEntity(ent)
               else: # it's an argument from a function in any other case
                    arg=Argument()
                    arg.name=name
                    createNewArgument(arg)

               while(ret[0]==comma_token):
                    ret=lex()
                    counter=ret[2]
                    if(ret[0]==id_token):
                         name = ret[1]
                         ret=lex()
                         counter=ret[2]

                         if(option == 1): 
                              ent=Entity()
                              ent.name=name
                              ent.type='VAR'
                              ent.variable.offset=calculateOffset()
                              createNewEntity(ent)
                         else: 
                              arg=Argument()
                              arg.name=name
                              createNewArgument(arg)
                    else:
                         print("error: missing id after comma",counter)
                         exit(-1)
          else:
               print("error: missing id in id_list", counter)
               exit(-1)
          print("Exiting id list")


     def functions():
          global ret
          print("Parsing functions")
          while(ret[0]==def_token):
               def_function()

     def main():
          global listOfScopes
          global ret
          global counter
          print("entering main function")
          if(ret[0]==hashtagdef_token):
               ret=lex()
               counter=ret[2]
               if(ret[0] == main_token):
                    ret=lex()
                    counter=ret[2]

                    ## new entity is created for the function
                    entity=Entity()
                    entity.name= 'main'
                    entity.type='Function'
                    currentScope=listOfScopes[-1]
                    entity.Function.nestingLevel=currentScope.nestingLevel+1 
                    
                    createNewEntity(entity)
                    createNewScope('main')


                    declarations()
                    generateQuad('begin_block', 'main', '_', '_')
                    code_block()
                    calculateFramelength()
                    generateQuad('end_block', 'main', '_', '_')
                    printSymbols(symfile)
                    final()
                    deleteScope()
               else:
                    print("error: missing main function",counter)
                    exit(-1)
          else:
               print("error: word '#def' missing",counter)
               exit(-1)
          print("Exiting main function")

     def def_function():
          global listOfScopes
          global ret
          global counter

          if(ret[0]==def_token):
               ret=lex()
               counter=ret[2]
               if(ret[0]==id_token):
                    functionName = ret[1]
                    ret=lex()
                    counter=ret[2]
                    if(ret[0]==lparen_token):
                         ret=lex()
                         counter=ret[2]

                         ## new entity is created for the function
                         entity=Entity()
                         entity.name=functionName
                         entity.type='Function'
                         currentScope=listOfScopes[-1]
                         entity.Function.nestingLevel=currentScope.nestingLevel+1 
                         print(f"Creating function entity: {entity.name}, nesting level: {entity.Function.nestingLevel}")  # Debugging outputt
                         
                         createNewEntity(entity)
                         id_list(0)
                         if(ret[0] == rparen_token):
                              ret=lex()
                              counter=ret[2]
                              if(ret[0] == colon_token):
                                   ret=lex()
                                   counter=ret[2]
                                   if(ret[0] == lblock_token):
                                        ret=lex()
                                        counter=ret[2]
                                        createNewScope(functionName)
                                        addParameters()
                                        declarations()
                                        functions()
                                        glob_decl()
                                        ## quad and scope is created for the function in this scope
                                        generateQuad('begin_block', functionName, '_', '_')
                                        code_block()
                                        calculateFramelength()
                                        generateQuad('end_block', functionName, '_', '_')
                                        printSymbols(symfile)
                                        final()
                                        deleteScope()
                                        
                                        if(ret[0]==rblock_token):
                                             ret=lex()
                                             counter=ret[2]
                                        else:
                                             print("error: missing '#}' after statements in def function",counter)
                                             exit(-1)
                                   else:
                                        print("error: missing '#{' before declarations",counter)
                                        exit(-1)
                              else:
                                   print("error: missing ':' after () of function",counter)
                                   exit(-1)
                         else:
                              print("error: missing ')' after name of function",counter)
                              exit(-1)
                    else:
                         print("error: missing '(' after name of function",counter)
                         exit(-1)
               else:
                    print("error: missing name of the function",counter)
                    exit(-1)
          else:
               print("error: word 'def' missing",counter)
               exit(-1)
          print("Exiting function definition")
     
     def glob_decl():
          global ret
          global counter
          while(ret[0] == global_token):
               ret=lex()
               counter=ret[2]
               id_list(1)

     def statement():
          global ret
          global counter
          if(ret[0] == print_token or ret[0] == return_token or ret[0] == id_token):
               simple_statement()
          elif(ret[0] == if_token or ret[0] == while_token):
               structured_statement()
          else:
               print("error: not correct statement", counter)
               exit(-1)

     def code_block():
          global ret 
          statement()
          while(ret[0]==print_token or ret[0]==return_token or ret[0]==id_token or ret[0]==if_token or ret[0]==while_token):
               statement()

     def simple_statement():
          global ret 

          if(ret[0]==id_token):
               assignment_stat()
          elif(ret[0]==print_token):
               print_stat()
          elif(ret[0]==return_token):
               return_stat()

     def structured_statement():
          global ret
          if(ret[0]==if_token):
               if_stat()
          elif(ret[0]==while_token):
               while_stat()

     def assignment_stat():
          global ret 
          global counter
          print("Entering assignment stat")
          if(ret[0]==id_token):
               id = ret[1]
               ret=lex()
               counter=ret[2]
               if(ret[0]==assign_token):
                    ret=lex()
                    counter=ret[2]
                    if(ret[0]==int_token):
                         ret=lex()
                         counter=ret[2]
                         generateQuad('input', id, '_', '_')
                         if(ret[0]==lparen_token):
                              ret=lex()
                              counter=ret[2]
                              if(ret[0]==input_token):
                                   ret=lex()
                                   counter=ret[2]
                                   if(ret[0]==lparen_token):
                                        ret=lex()
                                        counter=ret[2]
                                        if(ret[0]==rparen_token):
                                             ret=lex()
                                             counter=ret[2]
                                             if(ret[0]==rparen_token):
                                                  ret=lex()
                                                  counter=ret[2]
                                             else:
                                                  print("error: missing ')' in assignment_stat",counter)
                                                  exit(-1)
                                        else:
                                             print("error: missing ')' in assignment_stat",counter)
                                             exit(-1)
                                   else:
                                        print("error: missing '(' in assignment_stat",counter)
                                        exit(-1)
                              else:
                                   print("error: missing input in assignment_stat",counter)
                                   exit(-1)
                         else:
                              print("error: missing '(' in assignment_stat",counter)
                              exit(-1)
                    else:
                         Eplace = expression()
                         generateQuad(':=', Eplace, '_', id)
               else:
                    print("error: missing '=' after id",counter)
                    exit(-1)
          else:
               print("error: missing id",counter)
               exit(-1)
          print("Exiting assignment stat")

     def print_stat():
          global ret 
          global counter
          print("Entering print_stat")  # Debugging output

          if(ret[0]==print_token):
               ret=lex()
               counter=ret[2]
               if(ret[0]==lparen_token):
                    ret=lex()
                    counter=ret[2]
                    Eplace = expression()
                    generateQuad('output', Eplace, '_', '_')
                    if(ret[0]==rparen_token):
                         ret=lex()
                         counter=ret[2]
                    else:
                         print("error missing ')' in print_stat",counter)
                         exit(-1)
               else:
                    print("error: missing '(' in print_stat",counter)
                    exit(-1)
          else:
               print("error: missing print",counter)
               exit(-1)

          print("Exiting print_stat")  # Debugging output

     def return_stat():
          global ret 
          global counter
          print("entering return stat")
          if(ret[0]==return_token):
               print("found return token")
               ret=lex()
               counter=ret[2]
               Eplace = expression()
               generateQuad('ret', Eplace, '_', '_')
          else:
               print("error: missing return",counter)
               exit(-1)
          print("exiting return stat")

     def statement_or_block(cond, quad, ifVar, isInElifElse):
          global counter
          global ret
          global listQuads
          ifList = []
          if (ret[0] == lblock_token):
               ret=lex()
               counter = ret[2]
               statement()
               while(ret[0]==print_token or ret[0]==return_token or ret[0]==id_token or ret[0]==if_token or ret[0]==while_token):
                    statement()
               if (ifVar == 1): ## is called from if_stat
                    ifList = [len(listQuads)]
                    generateQuad('jump', '_', '_', '_')
               else: ## from while_stat
                    generateQuad('jump', '_', '_', quad)
               if (ifVar == 1 and isInElifElse == 1):
                    fillLastDash(ifList, len(listQuads))
               else:
                    fillLastDash(cond[1], len(listQuads))

               if (ret[0] == rblock_token):
                    ret=lex()
                    counter = ret[2]
               else:
                    print("error: missing '#}' after statements of statement_or_block",counter)
                    exit(-1)
          else:
               statement()
               if (ifVar == 1): ## is called from if_stat
                    ifList = [len(listQuads)]
                    generateQuad('jump', '_', '_', '_')
               else: ## called from while_stat
                    generateQuad('jump', '_', '_', quad)
               if (ifVar == 1 and isInElifElse == 1):
                    fillLastDash(ifList, len(listQuads))
               else:
                    fillLastDash(cond[1], len(listQuads))
          

     def if_stat():
          global ret
          global counter
          print("Entering if stat")
          if(ret[0]==if_token):
               ret=lex()
               counter=ret[2]
               cond = condition()
               fillLastDash(cond[0], len(listQuads))
               if(ret[0]==colon_token):
                    ret=lex()
                    counter=ret[2]
                    statement_or_block(cond, 0, 1, 0)
               else:
                    print("error: missing ':' after if",counter)
                    exit(-1)
               while(ret[0] == elif_token):
                         ret=lex()
                         counter=ret[2]
                         condition()
                         fillLastDash(cond[0], len(listQuads))
                         if(ret[0]==colon_token):
                              ret=lex()
                              counter=ret[2]
                              statement_or_block(cond, 0, 1, 1)
                         else:
                              print("error: missing ':' after elif",counter)
                              exit(-1)
               if (ret[0] == else_token):
                    ret=lex()
                    counter=ret[2]
                    if(ret[0]==colon_token):
                         ret=lex()
                         counter=ret[2]
                         statement_or_block(cond, 0, 1, 1)
          else:
               print("error: missing if condition",counter)
               exit(-1)
          print("Exiting if stat")

     def while_stat():
          global ret
          global counter
          if(ret[0]==while_token):
               ret=lex()
               counter=ret[2]
               wQuad = len(listQuads)
               cond = condition()
               fillLastDash(cond[0], len(listQuads))
               if(ret[0]==colon_token):
                    ret=lex()
                    counter=ret[2]
                    statement_or_block(cond, wQuad, 0, 0)
          else:
               print("error: missing while condition",counter)
               exit(-1)



     def expression():
          global ret
          global counter
          optional_sign()
          T1place=term()
          while(ret[0]==plus_token or ret[0]==minus_token):
               symbol=ADD_OP()
               T2place=term()

               t=createNewTemp()
               generateQuad(symbol,T1place,T2place,t)
               T1place=t
          
          Eplace = T1place
          print("Exiting expression with Eplace:", Eplace)  # Debugging output
          return Eplace 

     def term():
          global ret
          global counter
          print("Entering term")  # Debugging output
          Fplace=factor()

          while(ret[0]==multiply_token or ret[0]==divide_token or ret[0] == modulo_token):
               symbol=MUL_OP()
               F2place=factor()

               t = createNewTemp()
               generateQuad(symbol,Fplace,F2place,t)
               Fplace=t

          print("Exiting term with Fplace:", Fplace)  # Debugging output
          return Fplace

     def factor():
          global ret
          global counter
          if(ret[0]==digit_token):
               factor=ret[1]
               ret=lex()
               counter=ret[2]
          elif(ret[0]==lparen_token):
               ret=lex()
               counter=ret[2]
               Eplace=expression()
               factor=Eplace
               if(ret[0]==rparen_token):
                    ret=lex()
                    counter=ret[2]
               else:
                    print("error: missing ')' after expression in factor",counter)
                    exit(-1)
          elif(ret[0]==id_token):
               factor=ret[1]
               ret=lex()
               counter=ret[2]
               factor=idtail(factor)
          else:
               print("error: missing variable in factor",counter)
               exit(-1)
          print("Exiting factor with factor:", factor)  # Debugging output
          return factor

     def idtail(name):
          global ret
          global counter
          if(ret[0]==lparen_token):
               ret=lex()
               counter=ret[2]
               actual_par_list()
               t = createNewTemp()
               generateQuad('par', t, 'ret', '_')
               generateQuad('call', name, '_', '_')
               if(ret[0]==rparen_token):
                    ret=lex()
                    counter=ret[2]
                    return t
               else:
                    print("error: missing ')' in idtail",counter)
                    exit(-1)
          else:
               return name

     def actual_par_list():
          global ret
          global counter
          expr = expression()
          generateQuad('par',expr,'CV','_')
          while(ret[0] == comma_token):
               ret=lex()
               counter=ret[2]
               expr = expression()
               generateQuad('par',expr,'CV','_')

     def optional_sign():
          global ret
          global counter
          if(ret[0]== plus_token or ret[0]== minus_token):
               ADD_OP()

     def condition():
          global ret
          global counter
          Ctrue=[]
          Cfalse=[]

          bt1=bool_term()

          Ctrue=bt1[0]
          Cfalse=bt1[1]

          while(ret[0]==or_token):
               ret=lex()
               counter=ret[2]
               fillLastDash(Cfalse, len(listQuads))
               bt2=bool_term()
               Ctrue = mergeLists(Ctrue, bt2[0])
               Cfalse=bt2[1]
          return Ctrue,Cfalse

     def bool_term():
          global ret
          global counter
          BTtrue=[]
          BTfalse=[]

          bf1=bool_factor()

          BTtrue=bf1[0]
          BTfalse=bf1[1]

          while(ret[0]==and_token):
               ret=lex()
               counter=ret[2]

               fillLastDash(BTtrue, len(listQuads))
               bf2=bool_factor()
               BTfalse=mergeLists(BTfalse,bf2[1])
               BTtrue=bf2[0]

          return BTtrue,BTfalse


     def bool_factor():
          global ret
          global counter

          BFtrue=[]
          BFfalse=[]

          if (ret[0] == not_token):
               E1 = expression()
               relop = REL_OP()
               E2 = expression()
               BFtrue = [len(listQuads)]
               generateQuad(relop, E1, E2, '_')
               BFfalse = [len(listQuads)]
               generateQuad('jump', '_', '_', '_')
          else:
               E1 = expression()
               relop = REL_OP()
               E2 = expression()
               BFtrue= [len(listQuads)]
               generateQuad(relop, E1, E2, '_')
               BFfalse  = [len(listQuads)]
               generateQuad('jump', '_', '_', '_')
          return BFtrue,BFfalse
            
     def REL_OP():
          global ret
          global counter
          if(ret[0] == equal_token):
               relop=ret[1]
               ret=lex()
               counter=ret[2]
          elif(ret[0] == smaller_token):
               relop=ret[1]
               ret=lex()
               counter=ret[2]
          elif(ret[0] == smallerORequal_token):
               relop=ret[1]
               ret=lex()
               counter=ret[2]
          elif(ret[0] == different_token):
               relop=ret[1]
               ret=lex()
               counter=ret[2]
          elif(ret[0] == larger_token):
               relop=ret[1]
               ret=lex()
               counter=ret[2]
          elif(ret[0] == largerORequal_token):
               relop=ret[1]
               ret=lex()
               counter=ret[2]
          else:
               print("error: missing != , > , <,>=,<= ",counter)
               exit(-1)
          return relop

     def ADD_OP():
          global ret
          global counter
          if(ret[0] == plus_token):
               symbol=ret[1]
               ret=lex()
               counter=ret[2]
          elif(ret[0] == minus_token):
               symbol=ret[1]
               ret=lex()
               counter=ret[2]
          else:
               print("error: missing + or -", counter)
               exit(-1)

          return symbol

     def MUL_OP():
          global ret
          global counter

          if(ret[0] == multiply_token):
               symbol=ret[1]
               ret=lex()
               counter=ret[2]
          elif(ret[0] == divide_token):
               symbol=ret[1]
               ret=lex()
               counter=ret[2]
          elif(ret[0] == modulo_token):
               symbol=ret[1]
               ret=lex()
               counter=ret[2]
          else:
               print("error: missing *, /, or %", counter)
               exit(-1)

          return symbol

     program()

def intCode(file):
    for i in range(len(listQuadsIntCode)):
        quad = listQuadsIntCode[i]
        quadString=(str(quad[0]) + ":" + str(quad[1]) + " " + str(quad[2]) + " " + str(quad[3]) + " " + str(quad[4]) + "\n")
        file.write(quadString)

def printSymbols(file):
     global listOfScopes
   
     file.write("\n----------------------------------------------------------------------------------\n")
     for currentScope in reversed(listOfScopes):

          file.write("\nSCOPE: " + "name: " + currentScope.name + " nestinglevel: " + str(currentScope.nestingLevel))
          for ent in currentScope.entities:
               if ent.type == 'TEMP':
                    file.write("\n\tENTITY: " + "name: " + ent.name + " type: " + ent.type + " offset: " + str(ent.temp.offset))
               elif ent.type == 'VAR':
                    file.write("\n\tENTITY: " + "name: " + ent.name + " type: " + ent.type + " offset: " + str(ent.variable.offset))
               elif ent.type == 'PARAM':
                    file.write("\n\tENTITY: " + "name: " + ent.name + " type: " + ent.type + " offset: " +str(ent.parameter.offset))
               elif ent.type == 'Function':
                    file.write("\n\tENTITY: " + "name: " + ent.name + " type: " + ent.type + " frameLength: " +str(ent.function.frameLength))
                    for args in ent.function.listArgument:
                         file.write("\n\t\targument of function: " + "name: " + args.name)
     file.write("\n----------------------------------------------------------------------------------\n")

intfile=open('intfile.int','w')
symfile=open('symfile.sym','w')
syntax()
intCode(intfile)
intfile.close()
symfile.close()
final_file.close()
