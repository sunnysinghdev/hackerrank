def miniMaxSum(arr):
    maxVal = -99999999999
    minVal = 99999999999
    for i in range(5):
        for j in range(5):
            tempVal = arr[i]
            count = 0
            tp = (tempVal,)
            for k in range(5):
                index = (j + k) % 5
                if index != i:
                    tempVal+=arr[index]
                    tp +=(arr[index],)
                    count+=1
                if count>2:
                    break
            if tempVal > maxVal:
                maxVal = tempVal
            if tempVal < minVal:
                minVal = tempVal
    
    print(str(minVal) + ' ' +str(maxVal))

miniMaxSum([256741038, 623958417, 467905213, 714532089, 938071625])