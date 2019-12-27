import sys
sb_dict = dict()
def test_case20():
    try:

        print(sys.getrecursionlimit())
    except:
        print(sys.exc_info())
    finally:
        pass
        #f.close()
    return
    #ans = 771187
    #printv(buildString(6647, 6650, case), 771187)
    #f.close()

    # f = open('case20_a.txt','r')
    # case_a = f.readline()
    # f.close()

    # print(len(case_a))
    # for i in range(len(case_a)):
    #     sub_sequence = ""
    #     for j in range(i, len(case_a)):
    #         if sub_sequence + case_a[j] in case_a[0:i]:
    #             sub_sequence +=case_a[j]
    #             continue
    #         else:
    #             break
    #     if len(sub_sequence) > 1:
    #         sb_dict[str(i)+':'+str(j)] = sub_sequence

    # i = 0
    # for ss in sb_dict:
    #     if i > 10:
    #         break
    #     print(sb_dict[ss])
    #     i+=1

    # #ans = 2514362
    # #printv(buildString(7246, 7246, case_a), 2514362)

    # f = open('case20_b.txt','r')
    # case_b = f.readline()
    # #ans = 24025545
    # #printv(buildString(3195, 3198, case_b), 24025545)
    # f.close()

test_case20()