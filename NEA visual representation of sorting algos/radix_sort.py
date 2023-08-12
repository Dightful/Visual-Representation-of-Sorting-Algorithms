import ThirdFile
import time

def countingSort(arr, exp1,dict1,file,x,y, w2, grouped):
 
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

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

# Method to do Radix Sort
def radixSort(arr,dict1,file,x,y, w2, w, grouped): 
    start_time1 = time.time()
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        print(exp)
        countingSort(arr, exp,dict1,file,x,y, w2, grouped)
        exp *= 10


    print("DONEEEEEEEE")
    time_taken= time.time() - start_time1
    w.time_take(time_taken)
 
