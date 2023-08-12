import ThirdFile
import time
def selectionSort(arr,dict1,file,x,y,w2,w, grouped):
    start_time1 = time.time()
    delete_arr = []
    for i in range(len(arr)):
        delete_arr.append(arr[i])
    for i in range(len(arr)):
        delete_arr = arr[i:]
        minimum = min(delete_arr)
        minimum_index = arr.index(minimum)
        first_item = delete_arr[0]
        first_item_index = arr.index(first_item)
        arr[minimum_index], arr[first_item_index] = arr[first_item_index], arr[minimum_index]
        delete_arr.pop(0)
        
        new_dict = {}
        for i in range(len(arr)):
            key = arr[i]
            item = (dict1[key])
            new_dict[key] = item
        if grouped > 0:
            #arr to dictionary for displaying - dne this before in the change_pixels function
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
            print(new_dict)
            print()
            ThirdFile.creating_image(new_dict,file,x,y,w2)




    print("DONEEEEEEEE")
    time_taken= time.time() - start_time1
    w.time_take(time_taken)

#find min element of 0,4 and then swap it with position 0
#do this for 1,4 2,4 ... till sorted
