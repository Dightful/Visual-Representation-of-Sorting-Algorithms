import ThirdFile
import time

def insertionSort(arr,dict1,file,x,y,w2,w, grouped):
    start_time1 = time.time()
    for index in range(1, len(arr)):
        currentValue = arr[index]
        currentPosition = index

        while currentPosition > 0 and arr[currentPosition - 1] > currentValue:
            arr[currentPosition] = arr[currentPosition -1]
            currentPosition = currentPosition - 1

        arr[currentPosition] = currentValue

        if grouped > 0:
            new_dict = {}
            for i in range(len(arr)):
                key = arr[i]
                item = (dict1[key])
                new_dict[key] = item
            items = list(new_dict.items())
            random_dict = {}
            print("####################################################")
            print(new_dict)
            for i in items:
                #print(i)
                dict5 = (i[1])
                #print(dict5)
                dict6 = list(dict5.items())
                for i,j in dict6:
                    random_dict[i] = j
            print(random_dict)
            ThirdFile.creating_image(random_dict,file,x,y,w2)

        else:
            new_dict = {}
            for i in range(len(arr)):
                key = arr[i]
                item = (dict1[key])
                new_dict[key] = item
            #print(new_dict)
            print()
            ThirdFile.creating_image(new_dict,file,x,y,w2)

    print("DONEEEEEEEE")
    time_taken= time.time() - start_time1
    w.time_take(time_taken)

# arr = [6,4,5,2,9,1]
# insertionSort(arr,{6:1,4:2,5:3,2:4,9:5,1:6},"s","b","bh",5,1)


#32x32 in 21.8 seconds