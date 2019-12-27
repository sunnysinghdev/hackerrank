s_s="abcbc"
s_l = set()
counter = 0
def simple(sb, st, ln, level, path):
    if sb not in s_s:
       return
    #s_l.add(sb)

    global counter
    counter += 1
    print("fc",st, ln, level,sb)
    if st+ln > len(s_s) or len(s_s[st: st+ln]) < 1:
        if sb == s_s:
            print("fullmatch!", s_s[st: st + ln], path)
            s_l.add(path)

        #else:
            #print("return! ", s_s)
        #print("fr",st, ln, level, sb)
        return
    pick = s_s[st: st + ln]
    
    if pick in sb or sb == "":
        path += pick +'-'
    pr_sb = sb + pick
    simple(pr_sb, st + 1, ln, level+1, path)
    
    #ps_sb = sb[1:]
    #if ps_sb in s_s:
    simple(sb, st, ln+1, 100+level+1, path)
    
    #print("fr",st, ln, level, sb)

def sub_string(s, n):
    if len(s) < 1:
        if len(n)>1:
            pass
            #l.add(n)
        return
    #print(s)
    sub_string(s[1:], n+s[0])
    sub_string(s[1:], n)

    #sub_string(s[1:])
    #sub_string(s[2:3])
    
    #for c in 
    #sub_string(s[2:])
l = []
def trace1(n, start, end, l):
    if start >= end or len(s[start:end]) < 1:
        if n == s:
            print(n)
        return
    newc = s[start:end]
    sbstr = n+newc
    print(newc, sbstr, l)
    #trace(n, start+1, end+1, l+1)
    trace(sbstr, start+1, end+1, 2)
    
    newc = s[start -1 :]
    sbstr = n[0:len(n) - len(newc)]
    print(newc, sbstr, l+1)
    if newc in sbstr:
        #print(newc, n, l)
        trace(newc, start - 1, end, 4)
    #trace()


def trace(n, start, cLength, l):
    if (start >= start + cLength ) or (start + cLength) > len(s) or len(s[start: start + cLength]) < 1:
        if n == s:
            print('return == ', n)
        else:
            print('return =', n)
        return
    newc = s[start: start + cLength]
    sbstr = n+newc
    #print(newc, sbstr, l)
    print("f1({0}, {1}, c={2}) = {3} -  newc={4}".format(sbstr, start + 1, cLength, n, newc))
    trace(sbstr, start+1, cLength, 2)
    
    newc = s[start - 1:]
    sbstr = n#n[0:len(n) - len(newc)+1]
    #print(newc, sbstr, l+1)
    if newc in sbstr:
        #print(newc, n, l)
        print("f2({0}, {1}, c{2}) = {3} -  newc={4}".format(sbstr, start - 1, len(newc), n, newc))
        trace(sbstr, start -1, len(newc), 4)
    #trace()


def find_path(sb, path):
    #print(sb)
    if len(sb) == len(s):
        if ''.join(path) == s:
            s_set.append(path)
            #print("match")
        return
    nextchar = s[len(sb)]
    if nextchar not in sb:
        #add
        #sb += nextchar
        #path += nextchar + '(L)->'
        path += (nextchar,)
        find_path(sb + nextchar, path)
    else:
        #concat
        #if nextchar != '':
        #path += nextchar + '->'
        #find_path(sb + nextchar, path)
        
        concatStr = ""
        for i in range(len(sb), len(s)):
            temp_str = concatStr + s[i]
            if temp_str in sb:
                concatStr = temp_str
            else:
                break
        #if concatStr in sb:
        #path += concatStr[0] + '(L)->'
        path += (concatStr[0],)
        find_path(sb + concatStr[0], path)
        
        if len(concatStr) > 1:
            #path += concatStr + '(R)->'
            path += (concatStr,)
            find_path(sb + concatStr, path)
        #elif len(concatStr) == 1:
        
        # else:
        #     return

sb = ""
n =  ""
#s = "abcbcbcbc"
s = "acbbqbbqbb"
a_dollar = 1
b_dollar = 2
#trace("", 0, 1, 0)
#simple("",0,1, 1,"Path = ")
s_set = []#set()
find_path("", ())
#print(s_l, counter)
minVal = 999999999
for path in s_set:
    #print(path)
    cost = 0
    for sb in path:
        if cost > minVal:
            break
        if len(sb) == 1:
            cost += a_dollar
        else:
            cost += b_dollar
    if minVal > cost:
        minVal = cost
        print(''.join(path), minVal)
print(minVal)

