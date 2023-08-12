import ThirdFile
import time

def bucketSort(arr,dict1,file,x,y,w2,w, grouped):

    start_time1 = time.time()
    arr_use = arr
    arr2 = []
    for i in arr_use:
        arr2.append(int(i))
    
    def larger(calculation,x3,dict1,file,x,y,w2, grouped):
        arr = []
        for ii in x3:
            jj= ii*calculation
            #print(jj, type(jj))
            jjj = round(jj)
            arr.append(jjj)
        print(arr)
        testD = []
        for i in arr:
            if i in testD:
                #print(i)
                pass
            else:
                testD.append(i)

        if grouped > 0:
            new_dict = {}
            for i in range(len(arr)):
                key = arr[i]
                item = (dict1[key])
                new_dict[key] = item
            items = list(new_dict.items())
            random_dict = {}
            for i in items:
                #print(i)
                dict5 = (i[1])
                #print(dict5)
                dict6 = list(dict5.items())
                for i,j in dict6:
                    random_dict[i] = j
            ThirdFile.creating_image(random_dict,file,x,y,w2)

        else:
            new_dict = {}
            for i in range(len(arr)):
                key = arr[i]
                item = (dict1[key])
                new_dict[key] = item
            ThirdFile.creating_image(new_dict,file,x,y,w2)
            ####PRINTING METHOD

    def insertionSort(b):
        for i in range(1, len(b)):
            up = b[i]
            j = i - 1
            while j >= 0 and b[j] > up: 
                b[j + 1] = b[j]
                j -= 1
            
            b[j + 1] = up
        return b     
                
    def bucketSort(xx,dict1,file,x,y,w2, grouped):
        arr = []
        slot_num = 10 # 10 means 10 slots, each
                    # slot's size is 0.1
        for i in range(slot_num):
            arr.append([])
        # Put array elements in different buckets 
        for j in xx:
            index_b = int(slot_num * j) 
            arr[index_b].append(j)
        # Sort individual buckets 
        for i in range(slot_num):
            arr[i] = insertionSort(arr[i])
        # concatenate the result
        k = 0
        for i in range(slot_num):
            for j in range(len(arr[i])):
                xx[k] = arr[i][j]
                larger(calculation,xx,dict1,file,x,y,w2, grouped)
                k += 1
        return x

    # Driver Code
    maxI = (max(arr2))
    length = len(str(maxI))
    calculation = 10**length
    # get length and then add that many 0s
    x2 = []
    for i in arr2:
        n = i/calculation
        x2.append(n)
    (bucketSort(x2,dict1,file,x,y,w2, grouped))
    #larger(calculation,x3,dict1,file,x,y,w2, grouped)
    print("DONEEEEEEEE")
    time_taken= time.time() - start_time1
    w.time_take(time_taken)

