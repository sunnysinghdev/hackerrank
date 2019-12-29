import sys
s = ""
minCost = 99999999
a_dollar = 0
b_dollar = 0
lines = dict()
MAX_VALUE_CONST = 99999999
memDict = dict()
sys.setrecursionlimit(2147483647)


def printLine(l, s):
    if l in lines:
        lines[l] += (s,)
    else:
        lines[l] = (s,)
def buildString(a, b, s1):
    #
    # Write your code here.
    #
    global s
    global s_set
    global a_dollar
    global b_dollar
    global minCost
    global memDict
    global counter
    global substringDict
    substringDict = dict()
    counter = 0
    memDict = dict()
    minCost = MAX_VALUE_CONST
    s_set = []
    s = s1.replace('\n','')
    a_dollar = a
    b_dollar = b
    #if len(s) > 25000:
    #init_substring()
    #find_path("", (), 0, 1)
    c_cost = find_cost("",(), 0, 1, "")
    #c_cost_2 = 0
    # if len(postProcess) > 1:
    #         c_cost_2 = find_cost("",postProcess[1], postProcess[2], postProcess[3], postProcess[4])
    #print('New Cost', c_cost_2)


    #print("Huee=", c_cost)

    return c_cost

def min_cost(path):
    #print(path)
    cost = 0
    for sb in path:
        if len(sb) == 1:
            cost += a_dollar
        else:
            cost += b_dollar
    return cost

counter = 0

def find_cost(sb, path, lcost, l, node):
    global minCost
    global a_dollar
    global b_dollar
    global counter
    total_cost = 0
    #print(path)
    #print(counter, l)
    # if l >= 3766:
    #     print("return ---")
    #     postProcess = (sb, path, lcost, l, node)
    #     return lcost
    
    if sb in memDict:
        #print("return ", sb)
        return memDict[sb]
    if lcost > 0 and lcost >= minCost:
        #print("Cost", lcost)
        return lcost 

        #pass
    
    
    if sb == s:
        #print(' '.join(path))
        cost = min_cost(path)
        if cost < minCost:
            minCost = cost
        return 0
    
        #pass

    nextchar = s[len(sb)]
    #concat
    concatStr = ""
    
    for i in range(len(sb), len(s)):
        temp_str = concatStr + s[i]
        if temp_str in sb:
            concatStr = temp_str
        else:
            break
    
    concat_cost = MAX_VALUE_CONST
    add_cost = 0
    if len(concatStr) > 1 and len(concatStr) >= (b_dollar - a_dollar):
        if len(concatStr) > 1 :
            #print(concatStr)
            counter += 1

            lp = path + (concatStr,)
            concat_cost = find_cost(sb + concatStr, lp, lcost +b_dollar, l + 1, concatStr)
            concat_cost = b_dollar + concat_cost

        counter += 1
        lp = path + (nextchar,)
        add_cost = find_cost(sb + nextchar, lp, lcost+a_dollar, l + 1, nextchar)
        add_cost = a_dollar + add_cost
    else:
        counter += 1
        lp = path + (nextchar,)
        add_cost = find_cost(sb + nextchar, lp, lcost+a_dollar, l + 1, nextchar)
        add_cost = a_dollar + add_cost 

        if len(concatStr) > 1 :
            #print(concatStr)
            counter += 1

            lp = path + (concatStr,)
            concat_cost = find_cost(sb + concatStr, lp, lcost +b_dollar, l + 1, concatStr)
            concat_cost = b_dollar + concat_cost

    if concat_cost == MAX_VALUE_CONST:
        total_cost = add_cost
    elif len(concatStr) > 1 and b_dollar == a_dollar:
        total_cost = concat_cost
    else:
        if add_cost > concat_cost:
            total_cost = concat_cost
        else:
            total_cost = add_cost
    
    memDict[sb] = total_cost
    return total_cost

#-------------------------------------------------------------------------
def test_case20():
    f = open("case20.txt", 'r')
    case = f.readline()
    f.close()

    f = open('case20_a.txt','r')
    case_a = f.readline()
    f.close()

    f = open('case20_b.txt','r')
    case_b = f.readline()
    f.close()

    #ans = 771187
    printv(buildString(6647, 6650, case), 771187)
    #ans = 2514362
    printv(buildString(7246, 7246, case_a), 2514362)
    #ans = 24025545
    printv(buildString(3195, 3198, case_b), 24025545)
    

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

def test_case11():
    ot = (400809,729904,32225646)
    f = open("case11.txt", 'r')
    case = f.readline().replace('\n','')
    num = int(case)
    for i in range(num):
        #print(i)
        valstr = f.readline().replace('\n','')
        nums = valstr.split(' ')
        line = f.readline().replace('\n','')
        #if i == 2:
            #print(nums)
        printv(buildString(int(nums[1]), int(nums[2]), line), ot[i])

#--------------------------------------------
counter = 0
#test_case0()
print("Calls=", counter)
print('')
#---------------------------------------------
counter = 0
memDict = dict()
#test_case1()
print("Calls=", counter, "Min cost", minCost)
print('')
#--------------------------------------------
counter = 0
memDict = dict()
#test_case5()
print("Calls=", counter)
print('')
#--------------------------------------------
counter = 0
memDict = dict()
test_case20()
print("Calls=", counter)
print('')
#---------------------------------------------
#--------------------------------------------
counter = 0
memDict = dict()

#test_case11()
print("Calls=", counter)
print('')
#---------------------------------------------
#ex  "0123456789"
#ex = "aabbcaabbcbccbc"
counter = 0
ex = "aabbcaabbcbccbc"
#print("Result =", buildString(1, 6, ex))
#print("Call", counter)
#printDict()
