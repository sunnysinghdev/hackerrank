print("---Start-----")

def jumpingOnClouds(c):
    #Recursive call for jump
    minVal = [99999]
    jump(0, c, (), minVal)
    
    if minVal[0] != 99999:
        return minVal[0]
    return 0


def jump(index, arr, path, minimum):
    if index > len(arr) - 1 or arr[index] == 1:
        if path[-1] == len(arr) - 1: 
            #print('path = ' + ",".join(map(str,path)))
            if(minimum[0] > len(path) - 1 ):
                minimum[0] = len(path) - 1
        return
    path = path + (index,)
    #p1 +=str(index)
    #jump one step
    jump(index + 1, arr, path, minimum)
    #jump two step
    jump(index + 2, arr, path, minimum)
     

input7_4 = [0, 0, 1, 0, 0, 1, 0]
input6_3 = [0, 0, 0, 0, 1, 0]
c = [0, 1, 0, 0, 0, 1, 0]
fail1 = [   0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 
            0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 
            1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 
            0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 1, 0, 1, 0, 0]

#print(jumpingOnClouds(c))
print(jumpingOnClouds(fail1))
