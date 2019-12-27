
s = ""
minCost = 9999999999
a_dollar = 0
b_dollar = 0
lines = dict()
def find_path(sb, path, lcost, l):
    global minCost
    global a_dollar
    global b_dollar
    #print(sb)
    printLine(l, sb)
    if lcost > 0 and lcost >= minCost:
        pass
        # return
    if sb == s:
        #s_set.append(path)
        cost = min_cost(path)
        if cost < minCost:
            minCost = cost

        return
        
    nextchar = s[len(sb)]
   
    if nextchar not in sb:
    #path += nextchar + '(L)->'
        lp = path + (nextchar,)
        #print(' ' , nextchar,"(l)", end=" ")
        printLine(l, nextchar+'L')
        find_path(sb + nextchar, lp, lcost+a_dollar, l +1)
    else:
        
        
        #concat
        concatStr = ""
        
        for i in range(len(sb), len(s)):
            temp_str = concatStr + s[i]
            if temp_str in sb:
                concatStr = temp_str
            else:
                break
            
        if len(concatStr) > 1:
            #path += concatStr + '(R)->'
            lp = path + (concatStr,)
            #print(' ' * l, concatStr,"(r)")
            printLine(l, concatStr+'R')
            find_path(sb + concatStr, lp, lcost +b_dollar, l + 1)
        
        lp = path + (nextchar,)
        #print(' ',nextchar,"(l)")
        printLine(l, nextchar + 'L')
        find_path(sb + nextchar, lp, lcost+a_dollar, l + 1)

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
    minCost = 9999999999
    s_set = []
    s = s1
    a_dollar = a
    b_dollar = b
    find_path("", (), 0, 1)

    return minCost

def min_cost(path):
    #print(path)
    cost = 0
    for sb in path:
        if len(sb) == 1:
            cost += a_dollar
        else:
            cost += b_dollar
    return cost

#-------------------------------------------------------------------------
def test_case20():
    f = open("case20.txt", 'r')
    case = f.readline()
    #ans = 771187
    printv(buildString(6647, 6650, case), 771187)
    f.close()

    f = open('case20_a.txt','r')
    case_a = f.readline()
    #ans = 2514362
    printv(buildString(7246, 7246, case_a), 2514362)
    f.close()

    f = open('case20_b.txt','r')
    case_b = f.readline()
    #ans = 24025545
    printv(buildString(3195, 3198, case_b), 24025545)
    f.close()
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


#--------------------------------------------
#test_case0()
#print('')
#test_case1()
#print('')
#test_case5()
#print('')
#test_case20()
#ex  "0123456789"
ex = "aabbcaabbcbccbc"
buildString(1, 2, ex)
for l in lines:
    left = ()
    right = ()
    other = ()
    for sb in lines[l]:
        try:
            if sb[-1] == 'R':
                right +=(sb[0:-1],)
            elif sb[-1] == 'L':
                left +=(sb[0:-1],)
            else:
                other += (sb,)
        except:
            pass
    lstr = ""
    for lft in left:
        lstr += lft + "," 
    rstr = ""
    for rgt in right:
        rstr += rgt + ","
    ostr = ""
    for rgt in other:
        ostr += rgt + ","
    print(l, lstr, " "*3, ostr, " "*3, rstr)
    print(" ")

#print(s[0:-2])
#print(findMaxSubStr("abcd", "acabdd"))