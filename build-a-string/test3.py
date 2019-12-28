import sys

s = ""
minCost = 9999999999
a_dollar = 0
b_dollar = 0
MAX_VALUE_CONST = 99999999
memDict = dict()
sys.setrecursionlimit(2147483647)

def min_cost(path):
    cost = 0
    for sb in path:
        if len(sb) == 1:
            cost += a_dollar
        else:
            cost += b_dollar
    return cost
    
def find_cost(sb, path, lcost, l, node):
    global minCost
    global a_dollar
    global b_dollar
    total_cost = 0
    
    if sb in memDict:
        return memDict[sb]

    if lcost > 0 and lcost >= minCost:
        return a_dollar
    
    if sb == s:
        #print(path)
        cost = min_cost(path)
        if cost < minCost:
            minCost = cost
        return 0
    else:
        nextchar = s[len(sb)]
    
        if nextchar not in sb:
            #--------Stright------------------------------------------------------
            lp = path + (nextchar,)
            
            single_node_cost = find_cost(sb + nextchar, lp, lcost+a_dollar, l +1, nextchar)
            single_node_cost = a_dollar + single_node_cost 
            total_cost = single_node_cost
            memDict[sb] = single_node_cost
            
            return  total_cost 
        else:
            #concat------Left------------------------------------------------------------
            concatStr = ""
            for i in range(len(sb), len(s)):
                temp_str = concatStr + s[i]
                if temp_str in sb:
                    concatStr = temp_str
                else:
                    break
            
            concat_cost = MAX_VALUE_CONST
            if len(concatStr) > 1:
                lp = path + (concatStr,)
                concat_cost = find_cost(sb + concatStr, lp, lcost +b_dollar, l + 1, concatStr)
                concat_cost = b_dollar + concat_cost
                

            #Add--------Right------------------------------------------------------------
            lp = path + (nextchar,)
            add_cost = find_cost(sb + nextchar, lp, lcost+a_dollar, l + 1, nextchar)
            add_cost = a_dollar + add_cost
           
            # Find optimal cost
            if concat_cost == MAX_VALUE_CONST:
                total_cost = add_cost
            else:
                if add_cost > concat_cost:
                    total_cost = concat_cost
                else:
                    total_cost = add_cost
            
            memDict[sb] = total_cost
        return total_cost
def buildString(a, b, s1):
    #
    # Write your code here.
    #
    global s
    global a_dollar
    global b_dollar
    global minCost
    global memDict
    global substringDict
    substringDict = dict()
    memDict = dict()
    minCost = MAX_VALUE_CONST
    s = s1
    a_dollar = a
    b_dollar = b
    c_cost = find_cost("",(), 0, 1, "")

    return c_cost



#-------------------------------------------------------------------------
def test_case20():
    f = open("case20.txt", 'r')
    case = f.readline().replace('\n','')
    #ans = 771187
    printv(buildString(6647, 6650, case), 771187)
    f.close()

    f = open('case20_a.txt','r')
    case_a = f.readline().replace('\n','')
    #ans = 2514362
    printv(buildString(7246, 7246, case_a), 2514362)
    f.close()

    f = open('case20_b.txt','r')
    case_b = f.readline().replace('\n','')
    print(len(case_b))
    f.close()

    #ans = 24025545
    try:
        printv(buildString(3195, 3198, case_b), 24025545)
    except:
        print(sys.exc_info())
def printv(s1, s2):
    print('Result = ' + str(s1) +' out ='+ str(s2))
def test_case0():
    printv(buildString(4, 5, "aabaacaba"), 26)
    printv(buildString(8, 9, "bacbacacb"), 42)
def test_case1():
    pass
    # 3
    # 10 2 3
    # caaahqcqes => 20
    case = 'caaahqcqes'
    printv(buildString(2, 3, case), 20)
    # 10 1 3
    # acbbqbbqbb => 10
    case = 'acbbqbbqbb'
    printv(buildString(1, 3, case), 10)
    # 10 2 4
    # cbabecbahe => 18
    case = 'cbabecbahe'
    printv(buildString(2, 4, case), 18)
    pass
def test_case5():
    
    case = 'caackncaacknggikncaacknggaacknggikncaackggikncaacknggaacknggikncakqoaacknggikncacggihikncaomhikncaom'
    #print(len(case))
    #65040
    printv(buildString(2709, 2712, case), 65040)
    
    #126246
    case = 'acbcrsjcrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcrsjrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcsbcbcrsjh'
    printv(buildString(7890, 7891, case), 126246)
    
    #268964
    case = 'abbciabbcabciabbcmabbciabbcahlbchgcmabbcmggcmababciabbcagerafrciabbcsrhgcmcabciabbchgcmabbcmsfabcmsr'
    printv(buildString(7078, 7078, case),268964)
#----------------------------------------------------------------------------




#--------------------------------------------
counter = 0
test_case0()
print("Calls=", counter)
print('')
#---------------------------------------------
counter = 0
memDict = dict()
test_case1()
print("Calls=", counter, "Min cost", minCost)
print('')
#--------------------------------------------
counter = 0
memDict = dict()
test_case5()
print("Calls=", counter)
print('')
#--------------------------------------------
counter = 0
memDict = dict()
test_case20()
print("Calls=", counter)
print('')
#---------------------------------------------
