


letters =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers=['0','1','2','3','4','5','6','7','8','9']

program_name = input("Please enter the name of your program: ")
file= open(program_name,'r')


#Katastaseis Pinaka Metavasewn

s_start = 0
q_letter = 1
q_number = 2
q_divide = 3
q_less = 4
q_greater = 5
q_assing = 6
q_not_equal = 7
q_hashtag = 8
q1_sxolia = 9
q2_sxolia = 10


#Xaraktires Pinaka Metavasewn

letter = 0
number = 1
plus = 2
minus = 3
multiply = 4
divide = 5
division_remainder = 6
less = 7
greater = 8
assing = 9
exclamatiom_mark = 10
comma = 11
colon = 12
left_parenthesis = 13
right_parenthesis = 14
hashtag = 15
left_brachet = 16
right_brachet = 17
white_char = 18
next_line = 19
EOF = 20
unknown_symbol = 21

#Desmeumenes Lekseis

bound_words = ['main','def','#def','#int','global','if','elif','else','while','print','return','input','int','and','or','not']

#Tokens

token = {
    'main_token': 0,
    'def_token': 1,
    '#def_token': 2,
    '#int_token': 3,
    'global_token': 4,
    'if_token': 5,
    'elif_token': 6,
    'else_token': 7,
    'while_token': 8,
    'print_token': 9,
    'return_token': 10,
    'input_token': 11,
    'int_token': 12,
    'and_token': 13,
    'or_token': 14,
    'not_token': 15,
    
    'ID_token': 100,
    'number_token': 101,
    'plus_token': 102,
    'minus_token': 103,
    'multiply_token': 104,
    'divide_token': 105,
    'division_remainder_token': 106,
    'less_token': 107,
    'greater_token': 108,
    'assing_token': 109,
    'exclamation_mark_token': 110,
    'comma_token': 111,
    'colon_token': 112,
    'left_parenthesis_token': 113,
    'right_parenthesis_token': 114,
    'comments_token': 115,
    'right_bracket_token': 116,
    'left_bracket_token': 117,
    'white_char_token': 118,
    'next_line_token': 119,
    'EOF_token': 120,
    'less_or_equal_token': 121,
    'greater_or_equal_token': 122,
    'not_equal_token': 123,
    'left_hashtag_bracket_token': 124,
    'right_hashtag_bracket_token': 125,
    'equal_token' : 126
}

hashtag_words = ['#int','#def']


#Errors

ERROR_UNKNOWN_SYMBOL = 1000
ERROR_MORE_THAN_30 = 1001
ERROR_INVALID_NUMBER = 1002
ERROR_LETTER_IN_NUMBERS = 1003
ERROR_WRONG_DEFINE = 1004
ERROR_COMMENTS_UNTIL_EOF= 1005




#Transition_Table

transition_table = [
    #   a       | 1       |  +         |  -         |    *           |    /   |            %            |   <    |     >    |  =   |     !   |     ,       |     :       |          (               |         )             |  #     |         {           |         }          |'',\t   |   \n  |  EOF  
    # s_start 
    [q_letter, q_number, 'plus_token', 'minus_token', 'multiply_token', q_divide, 'division_remainder_token', q_less, q_greater, q_assing, q_not_equal, 'comma_token', 'colon_token', 'left_parenthesis_token', 'right_parenthesis_token', q_hashtag, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, s_start, s_start, 'EOF_token'],

    # q_letter  
    [q_letter, q_letter, 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token', 'ID_token'],  

    # q_number
    [ERROR_LETTER_IN_NUMBERS, q_number, 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token', 'number_token'], 

    # q_divide 
    [ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, 'divide_token', ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL,ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL,ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL,ERROR_UNKNOWN_SYMBOL], 

    # q_less 
    ['less_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_or_equal_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_token', 'less_token'],

    # q_greater 
    ['greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_or_equal_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token', 'greater_token'],

    # q_assing  
    ['assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'equal_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token', 'assing_token'],

    # q_not_equal  
    [ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL,ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, 'not_equal_token', ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL,ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL,ERROR_UNKNOWN_SYMBOL,ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL], 

    # q_hashtag 
    [q_letter, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL,ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL, q1_sxolia , 'left_hashtag_bracket_token', 'right_hashtag_bracket_token', ERROR_UNKNOWN_SYMBOL, ERROR_UNKNOWN_SYMBOL], 

    # q1_sxolia 
    [q1_sxolia,q1_sxolia,q1_sxolia, q1_sxolia, q1_sxolia, q1_sxolia, q1_sxolia, q1_sxolia, q1_sxolia,q1_sxolia, q1_sxolia, q1_sxolia, q1_sxolia, q1_sxolia, q1_sxolia, q2_sxolia, q1_sxolia, q1_sxolia, q1_sxolia, q1_sxolia],

    # q2_sxolia    
    [q2_sxolia,q2_sxolia,q2_sxolia, q2_sxolia, q2_sxolia, q2_sxolia, q2_sxolia, q2_sxolia, q2_sxolia,q2_sxolia, q2_sxolia, q2_sxolia, q2_sxolia, q2_sxolia, q2_sxolia,s_start, q2_sxolia, q2_sxolia, q2_sxolia,ERROR_COMMENTS_UNTIL_EOF],    
]



line = 1
def lex():
    
    global line
    linecounter = line

    current_state = s_start
    lex_output = []
    a_word = ''
    

    while(current_state >= 0 and current_state <= 10):
        inp = file.read(1)

        if(inp == ' ' or inp =='\t'):
            array_inp = white_char

        elif(inp in letters):
            array_inp = letter

        elif(inp in numbers):
            array_inp = number
            
        elif(inp == '+'):
            array_inp = plus

        elif(inp == '-'):
            array_inp = minus

        elif(inp == '*'):
            array_inp = multiply

        elif(inp == '/'):
            array_inp = divide

        elif(inp == '%'):
            array_inp = division_remainder

        elif(inp == '<'):
            array_inp = less

        elif(inp == '>'):
            array_inp = greater
        
        elif(inp == '='):
            array_inp = assing

        elif(inp == '!'):
            array_inp = exclamatiom_mark

        elif(inp == ','):
            array_inp = comma

        elif(inp == ':'):
            array_inp = colon

        elif(inp == ')'):
            array_inp = right_parenthesis

        elif(inp == '('):
            array_inp = left_parenthesis

        elif(inp == '#'):
            array_inp = hashtag
        
        elif(inp == '{'):
            array_inp = left_brachet

        elif(inp == '}'):
            array_inp = right_brachet

        elif(inp == ''):
            array_inp = EOF

        elif(inp == '\n'):
            array_inp = next_line
            linecounter += 1
            
        else:
            array_inp = unknown_symbol

        current_state = transition_table[current_state][array_inp]
        
        if type(current_state) == str:
            current_state = token[current_state]

        

        
        if(current_state != s_start and current_state != q1_sxolia and current_state != q2_sxolia):
            a_word += inp
        if(current_state == q1_sxolia):
            a_word = ''



    if(len(a_word)>30):
        a_word = a_word[:-1]
        inp = file.seek(file.tell()-1,0)
        current_state = ERROR_MORE_THAN_30




    if(current_state == token['ID_token'] or current_state == token['number_token']  or current_state == token['less_token'] or current_state == token['greater_token'] or current_state == token['assing_token']):
            if (inp == '\n'):
                    linecounter -= 1
            inp = file.seek(file.tell()-1,0)  

            a_word = a_word[:-1]

            
    
    if(current_state == token['ID_token']):
        check_hashtag = '#'
        if check_hashtag in a_word:
            if(a_word not in hashtag_words):
                current_state = ERROR_WRONG_DEFINE



    if(current_state == token['ID_token']):
                if(a_word in bound_words):
                        if(a_word == 'main'):
                            current_state = token['main_token']
                        if(a_word == 'def'):
                            current_state = token['def_token']
                        if(a_word == '#def'):
                            current_state = token['#def_token']
                        if(a_word == '#int'):
                            current_state = token['#int_token']
                        if(a_word == 'global'):
                            current_state = token['global_token']
                        if(a_word == 'if'):
                            current_state = token['if_token']
                        if(a_word == 'elif'):
                            current_state = token['elif_token']
                        if(a_word == 'else'):
                            current_state = token['else_token']
                        if(a_word == 'while'):
                            current_state = token['while_token']
                        if(a_word == 'print'):
                            current_state = token['print_token']
                        if(a_word == 'return'):
                            current_state = token ['return_token']
                        if(a_word == 'input'):
                            current_state = token ['input_token']
                        if(a_word == 'int'):
                            current_state = token['int_token']
                        if(a_word == 'and'):
                            current_state = token['and_token']
                        if(a_word == 'or'):
                            current_state = token['or_token']
                        if(a_word == 'not'):
                            current_state = token['not_token']
                            
                        

    if (current_state == token['number_token']):
                num = int(a_word)
                if ( num <= -32767 or num >= 32767 ):
                    current_state = ERROR_INVALID_NUMBER



                    
    if(current_state == ERROR_UNKNOWN_SYMBOL):
                print("ERROR: Invalid Language Symbol!")
                exit(1)
       
    if(current_state == ERROR_MORE_THAN_30):
                print("ERROR: More Than 30 Chars!")
                exit(1)
    if(current_state == ERROR_INVALID_NUMBER):
                print("ERROR: Number Out of Range!")
                exit(1)
    if(current_state == ERROR_LETTER_IN_NUMBERS):
                print("ERROR: Followed by a Letter After a Digit!")
                exit(1)
    if(current_state == ERROR_WRONG_DEFINE):
                print("ERROR: Wrong Define!")
                exit(1)
    if(current_state == ERROR_COMMENTS_UNTIL_EOF):
                print("ERROR: Comments until EOF")
                exit(1)



    lex_output.append(current_state)
    lex_output.append(a_word)
    lex_output.append(linecounter)
    line=linecounter
    
    return lex_output

# Endiamesos kodikas

AllQuads = []
countQuad = 0

T_i = 1
listOfTempVars = []

def nextQuad():
    global countQuad

    return countQuad

def genQuad(x, y, z, k):
     

    global AllQuads , countQuad
    
    list = []
    list = [nextQuad()]
    list += [x]
    list += [y]
    list += [z]
    list += [k]

    AllQuads += [list]

    countQuad +=1
    return list

def newTemp():

    global T_i , listOfTempVars 

    list = ['T_']
    list.append(str(T_i))
    tempVar = list[0] + list[1]
    T_i +=1

    entity = Entity()
    entity.name = tempVar
    entity.type = "temp"
    #entity.variable.offset = calculate_offset()
    new_Entity(entity)

    listOfTempVars += tempVar
    return tempVar


def emptyList():
     
    emptyQuadList = []

    return emptyQuadList

def makeList(x):
     
    x_list = [x]

    return x_list

def mergeList(first_list, second_list):

    merged_list = []
    merged_list += first_list + second_list

    return merged_list

def backPatch(list, x):
     
    global AllQuads

    for i in range(len(list)):
        for k in range(len(AllQuads)):
            if(list[i] == AllQuads[k][0] and AllQuads[k][4] == '_'):
                AllQuads[k][4] = x
                break
    return

#for elif 
def backPatch_withNo_break(list,  x):
     
    global AllQuads

    for i in range(len(list)):
        for k in range(len(AllQuads)):
            if(list[i] == AllQuads[k][0] and AllQuads[k][4] == '_'):
                AllQuads[k][4] = x
                
    return
#Print Endiameso
Endiam_file=open("endiam.int",'w')
def print_AllQuads():
    for i in range(len(AllQuads)):
        Endiam_file.write(str(AllQuads[i][0])+" | "+str(AllQuads[i][1])+" ,"+str(AllQuads[i][2])+" ,"+str(AllQuads[i][3])+" ,"+str(AllQuads[i][4]))
        Endiam_file.write('\n')
    Endiam_file.close()

#Pinakas Sumvolwn    
class Scope():
    def __init__(self):
        self.name = '' 
        self.listEntity = []
        self.nestingLevel = 0
        self.enclosingScope = None

class Argument():
    def __init__(self):
        self.name = ''
        self.type = 'Int'
        self.parMode = ''

class Entity():
    def __init__(self):
        self.name = ''
        self.type = ''
        self.variable = self.Variable()
        self.function = self.Function()
        self.parameter = self.Parameter()
        self.tempVar = self.TempVar()

    class Variable():
        def __init__(self):
            self.type = 'Int'
            self.offset = 0
    
    class Function():
        def __init__(self):
            self.type = ''  
            self.startQuad = 0         
            self.listArgument = []
            self.frameLength = 0  

        
    class Parameter():
        def __init__(self):
            self.mode = ''
            self.offset = 0
            self.mode = 'CV'
    
    class TempVar():
        def __init__(self):
            self.type = 'Int'
            self.offset = 0

current_scope = None

def new_Scope(name):
    global current_scope
    new_scope = Scope() 
    new_scope.name = name

    if current_scope:
        new_scope.nestingLevel = current_scope.nestingLevel + 1
    else:
        new_scope.nestingLevel = 0 

    new_scope.enclosingScope = current_scope
    current_scope = new_scope

def del_scope():
    global current_scope
    if current_scope:
        current_scope = current_scope.enclosingScope

def new_Entity(new_ent):
    global current_scope
    if current_scope:
        new_ent.tempVar.offset = calculate_offset()
        current_scope.listEntity.append(new_ent)


def new_Argument(next_arg):
    global current_scope
    if current_scope and current_scope.listEntity:
        current_scope.listEntity[-1].function.listArgument.append(next_arg)



def calculate_offset():
    global current_scope
    i = 0
    if current_scope and current_scope.listEntity :
        for entity in current_scope.listEntity:
            if entity.type in ['var', 'temp', 'par']:
                i += 1
    offset = 12 + (i*4)  
    return offset

def calculate_framelength():
    global current_scope
    
    if current_scope and current_scope.enclosingScope and current_scope.enclosingScope.listEntity:
        current_scope.enclosingScope.listEntity[-1].function.frameLength = calculate_offset()

    
def create_param():
    global current_scope
    if current_scope and current_scope.enclosingScope and current_scope.enclosingScope.listEntity:
        for argument in current_scope.enclosingScope.listEntity[-1].function.listArgument:
            new_ent = Entity()
            new_ent.name = argument.name
            new_ent.type = 'par'
            new_ent.parameter = new_ent.Parameter()
            new_ent.parameter.mode = argument.parMode
            new_ent.parameter.offset = calculate_offset()
            new_Entity(new_ent)

def start_Quad():
    global current_scope
    
    if current_scope and current_scope.enclosingScope and current_scope.enclosingScope.listEntity:
        current_scope.enclosingScope.listEntity[-1].function.startQuad = nextQuad()
    
def print_Stable():
    
    global current_scope
    pinakas_sumbolwn_file=open("pinakas_sumbolwn.sym",'a')
    a_scope = current_scope
    
    pinakas_sumbolwn_file.write("SCOPE: " + a_scope.name)
    pinakas_sumbolwn_file.write('\n')
    pinakas_sumbolwn_file.write("Nesting Level: " + str(a_scope.nestingLevel))
    pinakas_sumbolwn_file.write('\n')
    pinakas_sumbolwn_file.write("\tEntities:")
    pinakas_sumbolwn_file.write('\n')
    for entity in a_scope.listEntity:
        if entity.type == "var":
            pinakas_sumbolwn_file.write("\t" + entity.name + "\t" + entity.type + "\t" + entity.variable.type + "\t" + str(entity.variable.offset))
            pinakas_sumbolwn_file.write('\n')
        if entity.type == "par":
            pinakas_sumbolwn_file.write("\t" + entity.name + "\t" + entity.type + "\t" + entity.parameter.mode + "\t" + str(entity.parameter.offset))
            pinakas_sumbolwn_file.write('\n')
        if entity.type == "func":
            pinakas_sumbolwn_file.write("\t" + entity.name + "\t" + entity.type + "\t" + entity.function.type + "\t" + str(entity.function.startQuad) + "\t" + str(entity.function.frameLength))
            pinakas_sumbolwn_file.write('\n')
            pinakas_sumbolwn_file.write("\t\tArguments:")
            pinakas_sumbolwn_file.write('\n')
            for argument in entity.function.listArgument:
                pinakas_sumbolwn_file.write("\t\t" + argument.name + "\t" + argument.type + "\t" + argument.parMode)
                pinakas_sumbolwn_file.write('\n')
        if entity.type == "main":
            pinakas_sumbolwn_file.write("\t" + entity.name + "\t" + entity.type + "\t" + entity.function.type + "\t" + str(entity.function.startQuad) + "\t" + str(entity.function.frameLength))
            pinakas_sumbolwn_file.write('\n')
        if entity.type == "temp":
            pinakas_sumbolwn_file.write("\t" + entity.name + "\t" + entity.type + "\t" + entity.tempVar.type + "\t" + str(entity.tempVar.offset))
            pinakas_sumbolwn_file.write('\n')
        
    pinakas_sumbolwn_file.close()



#Syntaktikos Analytis

def syntax_an():
        global line
        global lexCall
        global elif_list
        global start_vars
        global del_pn_sumbolwn
        del_pn_sumbolwn = True
        lexCall = lex()
        line = lexCall[2]
        elif_list = []
        start_vars = []
        


        def program():
        

            new_Scope(program_name)
            declarations()
            functions()
            main_function()
            print_Stable()
            del_scope()
            
        
        def declarations():
            global lexCall

            while(lexCall[0] == token['#int_token']):
                lexCall = lex()

                id_list_Entity()

            return
        
        def global_declarations():
            global lexCall

            while(lexCall[0] == token['global_token']):
                lexCall = lex()

                id_list_Entity()

            return
        
        def id_list_Entity():
            global start_vars
            global main_vars
            global lexCall


            if(lexCall[0] == token['ID_token']):
                ID = lexCall[1]
                lexCall = lex()
                line = lexCall[2]
                
                entity = Entity()
                entity.name = ID
                entity.type = "var"
                entity.variable.offset = calculate_offset()
                new_Entity(entity)

                while(lexCall[0] == token['comma_token']):
                    lexCall = lex()
                    line = lexCall[2]

                    if(lexCall[0] == token['ID_token']):
                        ID = lexCall[1]
                        lexCall = lex()
                        line = lexCall[2]
                        
                        entity = Entity()
                        entity.name = ID
                        entity.type = "var"
                        entity.variable.offset = calculate_offset()
                        new_Entity(entity)

                    else:
                        print("ERROR: End with comma in id_list ",line)
                        exit(-1)

            return

        

        def id_list_Argument():
            global lexCall

            if(lexCall[0] == token['ID_token']):
                ID = lexCall[1]
                lexCall = lex()
                line = lexCall[2]
                
                argument = Argument()
                argument.name = ID
                argument.parMode = 'CV'
                new_Argument(argument)

                while(lexCall[0] == token['comma_token']):
                    lexCall = lex()
                    line = lexCall[2]

                    if(lexCall[0] == token['ID_token']):
                        ID = lexCall[1]
                        lexCall = lex()
                        line = lexCall[2]
                        

                        argument = Argument()
                        argument.name = ID
                        argument.parMode = 'CV'
                        new_Argument(argument)  

                    else:
                        print("ERROR: End with comma in id_list",line)
                        exit(-1)

            return

        def def_function():
            global lexCall
            global del_pn_sumbolwn

            if(lexCall[0] == token['def_token']):
                lexCall = lex()
                line = lexCall[2]

                if(lexCall[0] == token['ID_token']):
                    ID = lexCall[1]
                    lexCall = lex()
                    line = lexCall[2]

                    entity = Entity()
                    entity.name = ID
                    entity.type = "func"
                    entity.variable.offset = calculate_offset()
                    new_Entity(entity)

                    
                    if(lexCall[0] == token['left_parenthesis_token']):
                        lexCall = lex()
                        line = lexCall[2]
 
                        id_list_Argument()
                        
                        if(lexCall[0] == token['right_parenthesis_token']):
                            lexCall = lex()
                            line = lexCall[2]

                            if(lexCall[0] == token['colon_token']):
                                lexCall = lex()
                                line = lexCall[2]

                                if(lexCall[0] == token['left_hashtag_bracket_token']):
                                    lexCall = lex()
                                    line = lexCall[2]
                                    
                                    
                                    new_Scope(ID)
                                    create_param()
                                    declarations()
                                    functions()
                                    global_declarations()
                                    genQuad("begin_block", ID, "_", "_")
                                    start_Quad()
                                    code_block()
                                    genQuad("end_block", ID, "_", "_")
                                    calculate_framelength()
                                    if(del_pn_sumbolwn == True):
                                        open("pinakas_sumbolwn.sym", 'w').close()
                                        del_pn_sumbolwn = False
                                    print_Stable()
                                    del_scope()

                                    if(lexCall[0] == token['right_hashtag_bracket_token']):
                                        lexCall = lex()
                                        line = lexCall[2]
                                        
                                        return

                                    else:
                                        print("ERROR: No_right_hashtag_bracket",line)
                                        exit(-1)
                                else:
                                    print("ERROR: No_left_hashtag_bracket",line)
                                    exit(-1)
                            else:
                                print("ERROR: No_colon",line)
                                exit(-1)
                        else:
                            print("ERROR: No_right_parenthesis",line)
                            exit(-1)
                    else:
                        print("ERROR: No_left_parenthesis",line)
                        exit(-1)
                else:
                    print("ERROR: Incorrect build of function",line)
                    exit(-1)
            else:
                print("ERROR: Problem in function",line)
                exit(-1)

        def functions():
            
            global lexCall

            while(lexCall[0] == token['def_token']):
                
                def_function()

            return
        

        def code_block():
            global lexCall
            global line

            statement()
        
            while(lexCall[0] == token['ID_token'] or lexCall[0] == token['if_token'] or lexCall[0] ==token['while_token'] or lexCall[0]==token['return_token'] or lexCall[0]==token['print_token']):

                statement()

            return
        

        def statement():
            global lexCall

            if(lexCall[0] == token['ID_token']): # simple_statement
                    assignment_stat()
            elif(lexCall[0] == token['if_token']): # structured_statement
                    if_stat()
            elif(lexCall[0] ==token['while_token']): # structured_statement
                    while_stat()
            elif(lexCall[0]==token['return_token']): # simple_statement
                    return_stat()
            elif(lexCall[0]==token['print_token']): # simple_statement
                    print_stat()

            return


        def assignment_stat():
            global lexCall
            

            if(lexCall[0] == token['ID_token']):
                ID = lexCall[1]
                lexCall = lex()
                line = lexCall[2]

                if(lexCall[0] == token['assing_token']):
                    lexCall = lex()
                    line = lexCall[2]
            
                    if(lexCall[0] == token['int_token']):
                        lexCall = lex()
                        line = lexCall[2]

                        if(lexCall[0] == token['left_parenthesis_token']):
                            lexCall = lex()
                            line = lexCall[2]

                            if(lexCall[0] == token['input_token']):
                                lexCall = lex()
                                line = lexCall[2]

                                if(lexCall[0] == token['left_parenthesis_token']):
                                    lexCall = lex()
                                    line = lexCall[2]

                                    if(lexCall[0] == token['right_parenthesis_token']):
                                        lexCall = lex()
                                        line = lexCall[2]

                                        if(lexCall[0] == token['right_parenthesis_token']):
                                            lexCall = lex()
                                            line = lexCall[2]

                                            w = newTemp()
                                            genQuad("inp", w, "_", "_")
                                            genQuad("=",w, "_", ID)
                                            
                                            return
                                
                                
                                        else:
                                            print("ERROR: Unclosed input",line)
                                            exit(-1)

                                    else:
                                        print("ERROR: Unclosed input",line)
                                        exit(-1)

                                else:
                                    print("ERROR: Unclosed input",line)
                                    exit(-1)
                                
                            else:
                                print("ERROR: Forget 'input' ",line)
                                exit(-1)

                        else:
                            print("ERROR: No open input",line)
                            exit(-1)

                    else:
                        Eplace = expression()
                        genQuad("=", Eplace ,"_",ID)
                        return

                else:
                    print("ERROR: No '=' in assignment",line)
                    exit(-1)
                
            else:
                print("ERROR: No assignment",line)
                exit(-1)
                

        def if_stat():
            global lexCall
            global line
            global elif_list
            

            Btrue = []
            Bfalse = []


            if(lexCall[0] == token['if_token']):
                lexCall = lex()
                line = lexCall[2]
                global elif_list

                B = condition()
                Btrue = B[0]
                Bfalse = B[1]
                

                if(lexCall[0] == token['colon_token']):
                    lexCall = lex()
                    line = lexCall[2]

                    
                    backPatch(Btrue, nextQuad())
                    statement_or_block()

                    if_list = makeList(nextQuad())
                    genQuad("jump", "_", "_", "_")
                    backPatch(Bfalse, nextQuad())

                    elif_stat()


                    else_stat()
                    
                    backPatch(if_list,nextQuad())
                    backPatch_withNo_break(elif_list, nextQuad())
                    
                    return

                else:   
                    print("ERROR: no ':' at the end of if ",line)
                    exit(-1)
                
            else:
                 print("ERROR: Problem in  if",line)
                 exit(-1)


        def elif_stat():
            global lexCall
            global line
            global elif_list

            while(lexCall[0] == token["elif_token"]):
                lexCall = lex()
                line = lexCall[2]

                E = condition()
                Etrue = E[0]
                Efalse = E[1]
                

                if(lexCall[0] == token['colon_token']):
                    lexCall = lex()
                    line = lexCall[2]
                    
                    backPatch(Etrue, nextQuad())
                    statement_or_block()

                    elif_list += [nextQuad()]
                    genQuad("jump", "_", "_", "_")
                    

                    backPatch(Efalse, nextQuad())                    

                else:
                    print("ERROR: Forgot  ':' in  elif",line)
                    exit(-1)

            return

            

        def else_stat():
            global lexCall
            global line

            if(lexCall[0] == token["else_token"]):
                lexCall = lex()
                line = lexCall[2]

                if(lexCall[0] == token['colon_token']):
                    lexCall = lex()
                    line = lexCall[2]

                    statement_or_block()
        
                
                else:
                    print("ERROR: Forgot ':' in  else",line)
                    exit(-1)
            return
        
                

        def while_stat():
            global lexCall
            global line
            Btrue = []
            Bfalse = []

            if(lexCall[0] == token['while_token']):
                lexCall = lex()
                line = lexCall[2]
                Bquad = nextQuad()

                B = condition()
                Btrue = B[0]
                Bfalse = B[1]
                

                if(lexCall[0] == token['colon_token']):
                    lexCall = lex()
                    line = lexCall[2]
                    
                    backPatch(Btrue,nextQuad())
                    statement_or_block()
                    genQuad("jump", "_", "_", Bquad)
                    backPatch(Bfalse,nextQuad())
                    return

                   
                else:
                    print("ERROR: Forgot : in  while",line) 
                    exit(-1)

            else:
                print("ERROR: Problem in  while",line) 
                exit(-1)

                
        def return_stat():
            global lexCall
            global line

            if(lexCall[0] == token['return_token']):
                lexCall = lex()

                Eplace = expression()
                genQuad("retv", Eplace, "_", "_")

                return
            else:
                print("ERROR: Problem in return",line) 
                exit(-1)


        def statement_or_block():
            global lexCall
            global line

            if(lexCall[0] == token['left_hashtag_bracket_token']):
                lexCall = lex()
                line = lexCall[2]

                code_block()

                if(lexCall[0] == token['right_hashtag_bracket_token']):
                    lexCall = lex()
                    line = lexCall[2]
                    return

                else:
                    print("Error: No right_hashtag_bracket_token",line)

            else:
                statement()
                return

             


        def print_stat():
            global lexCall
            global line

            if(lexCall[0] == token['print_token']):
                lexCall = lex()
                line = lexCall[2]

                if(lexCall[0] == token['left_parenthesis_token']):
                    lexCall = lex()
                    line = lexCall[2]

                    Eplace = expression()
                    genQuad("out", Eplace, "_", "_")

                    if(lexCall[0] == token['right_parenthesis_token']):
                        lexCall = lex()
                        line = lexCall[2]

                    
                    else:
                        print("ERROR: Unclosed print",line)
                        exit(-1)
                
                else:
                    print("ERROR: Unopen print",line)
                    exit(-1)

            else:
                print("ERROR:Problem in  print",line)
                exit(-1)

            return 
        

                
        def expression():
                global lexCall
                global line
                
                optional_sign()
                
                T1place = term()
                

                while(lexCall[0] == token['plus_token'] or lexCall[0] == token['minus_token']):
                    plus_or_minus = ADD_OP()
                        
                    T2place = term()
                    w = newTemp()
                    genQuad(plus_or_minus, T1place, T2place, w)
                    T1place = w
                Eplace = T1place  

                return Eplace
            

        def optional_sign():
            global lexCall
            global line

            if(lexCall[0] == token['plus_token'] or lexCall[0] == token['minus_token']):
                ADD_OP()

            return


        def term():
            global lexCall
            global line

            F1place = factor()
                
            while(lexCall[0] == token['multiply_token'] or lexCall[0] == token['divide_token'] or lexCall[0] == token['division_remainder_token']): 

                mul_or_div_or_rem = mul_oper()

                F2place = factor()

                w = newTemp()
                genQuad(mul_or_div_or_rem, F1place, F2place, w)
                F1place = w
            Tplace = F1place

            return Tplace
        

        def ADD_OP():
            global lexCall
            global line

            if(lexCall[0] == token['plus_token']):
                add_op = lexCall[1]
                lexCall = lex()
                line = lexCall[2]
                        

            elif(lexCall[0] == token['minus_token']):
                add_op = lexCall[1]
                lexCall = lex()
                line = lexCall[2]
                        
            return add_op 
        
            
        def factor():
            global lexCall
            global line

            if(lexCall[0] == token['number_token']):
                    Fplace = lexCall[1]
                    lexCall = lex()
                    line = lexCall[2]
                    
                        
            elif(lexCall[0] == token['left_parenthesis_token']):
                    lexCall = lex()
                    line = lexCall[2]

                    Eplace = expression()
                    Fplace = Eplace
                        
                    if(lexCall[0] == token['right_parenthesis_token']):
                            lexCall = lex()
                            line = lexCall[2]
                                
                    else:
                        print("ERROR: Need right parenthesis after expression stin factor ",line)
                        exit(-1)
            elif(lexCall[0] == token['ID_token']):
                    idtail_inp = lexCall[1]
                    lexCall = lex()
                    line = lexCall[2]
                        
                    
                    Fplace = idtail(idtail_inp)
                        
            else:
                print("ERROR: Need expression or constant or variable in factor",line)
                exit(-1)

            return Fplace

        def mul_oper():
                global lexCall 
                global line
                
                if (lexCall[0] == token['multiply_token']):
                        mul_oper = lexCall[1]
                        lexCall = lex()
                        line = lexCall[2]
                        
                        
                elif (lexCall[0] == token['divide_token']):
                        mul_oper = lexCall[1]
                        lexCall = lex()
                        line = lexCall[2]

                elif (lexCall[0] == token['division_remainder_token']):
                        mul_oper = lexCall[1]
                        lexCall = lex()
                        line = lexCall[2]

                return  mul_oper 

        def idtail(x):
                global lexCall
                global line
                
                if(lexCall[0] == token['left_parenthesis_token'] ):
                        lexCall = lex()
                        line = lexCall[2]

                        actual_par_list()

                        w = newTemp()
                        genQuad("par", w, "RET", "_")
                        genQuad("call", x, "_", "_")
                        
                        if(lexCall[0] == token['right_parenthesis_token']):
                                lexCall = lex()
                                line = lexCall[2]

                                return w
                        else:
                            print("ERROR:Forgot to close after actualparlist in idtail",line)
                            exit(-1)
                        
                return x 

        def actual_par_list():
            global lexCall
            global line 
                
            Ex = expression()
            genQuad("par", Ex, "CV", "_")    
            while(lexCall[0] == token['comma_token']):
                    lexCall  = lex()
                    line = lexCall[2]
                        
                    Ex = expression()
                    genQuad("par", Ex, "CV", "_")
                        
            return

        def condition():
            global lexCall
            global line
            Btrue = []
            Bfalse = []


            Q1 = bool_term()
            Btrue = Q1[0]
            Bfalse = Q1[1]
            

            while(lexCall[0] == token['or_token']):
                    lexCall=lex()
                    line = lexCall[2]

                    backPatch(Bfalse,nextQuad())
                        
                    Q2 = bool_term()

                    Btrue = mergeList(Btrue, Q2[0])
                    Bfalse = Q2[1]
                        
            return Btrue, Bfalse
        

        def bool_term():
            global lexCall
            global line
            Qtrue = []
            Qfalse = []

            R1 = bool_factor()

            Qtrue = R1[0]
            Qfalse = R1[1]
                
            while(lexCall[0] == token['and_token']):
                    lexCall = lex()
                    line = lexCall[2]

                    backPatch(Qtrue, nextQuad())

                    R2 = bool_factor()

                    Qfalse = mergeList(Qfalse, R2[1])
                    Qtrue = R2[0]   
            return Qtrue, Qfalse

                    
                        
            return

        def bool_factor():
            global lexCall
            global line

            Rtrue = []
            Rfalse = []
                
            if(lexCall[0] == token['not_token']):
                lexCall = lex()
                line = lexCall[2]

                E1place = expression()
                        
                relop = REL_OP()  
                        
                E2place = expression()

                Rtrue = makeList(nextQuad())
                genQuad(relop, E1place, E2place, "_")
                Rfalse = makeList(nextQuad())
                genQuad("jump", "_", "_", "_")
                        
               
            else:
                        
                E1 = expression()
                        
                relop = REL_OP()  
                        
                E2 = expression()

                Rtrue = makeList(nextQuad())
                genQuad(relop, E1, E2, "_")
                Rfalse = makeList(nextQuad())
                genQuad("jump", "_", "_", "_")
                        
                        
            return Rtrue, Rfalse
        
        def REL_OP():
                global lexCall 
                global line
                
                if(lexCall[0] == token['equal_token']):
                        rel_op = lexCall[1]
                        lexCall = lex()
                        line = lexCall[2]
                                
                elif(lexCall[0] == token['less_token']):
                        rel_op = lexCall[1]
                        lexCall = lex()
                        line = lexCall[2]
                        
                        
                elif(lexCall[0] == token['greater_token']):
                        rel_op = lexCall[1]
                        lexCall = lex()
                        line = lexCall[2]
                        
                        
                elif(lexCall[0] == token['less_or_equal_token']):
                        rel_op = lexCall[1]
                        lexCall = lex()
                        line = lexCall[2]
                        
                        
                elif(lexCall[0] == token['greater_or_equal_token'] ):
                        rel_op = lexCall[1]
                        lexCall = lex()
                        line = lexCall[2]
                        
                        
                elif(lexCall[0] == token['not_equal_token']):
                        rel_op = lexCall[1]
                        lexCall = lex()
                        line = lexCall[2]
                        
                        
                else:
                        print("ERROR: Leipei = or < or > or <= or >= or != ",line)
                        exit(-1)
                return rel_op

            
        def main_function():
            global lexCall
            global line
            
             

            if(lexCall[0] == token['#def_token']):
                lexCall = lex()
                line = lexCall[2]

                if(lexCall[0] == token['main_token']):
                    ID = lexCall[1]
                    entity = Entity()
                    entity.name = ID
                    entity.type = "main"
                    entity.variable.offset = calculate_offset()
                    new_Entity(entity)

                    lexCall = lex()
                    line = lexCall[2]

                    new_Scope(ID)
                    create_param()
                    declarations()
                    genQuad("begin_block", "main", "_", "_")
                    start_Quad()
                    code_block()
                    genQuad('halt','_','_','_')
                    genQuad("end_block","main","_", "_")
                    calculate_framelength()
                    print_Stable()
                    del_scope()


                    if(lexCall[0] == token['EOF_token']):
                        lexCall = lex()
                        line = lexCall[2]  
                        return
                    
                    else:
                        print('ERROR: Out of main code_block without EOF',line)
                        exit(-1)

                else:
                    print('ERROR: No main after #def',line)
                    exit(-1)
            else:
                print('ERROR: Program with no Main',line)
                exit(-1)

        program()

        return
        

syntax_an()
print_AllQuads()
print("Done, check files 'endiam.int' and 'pinakas_sumbolwn.sym' for more info")
