import ThirdFile
import time

def partition(array, low, high,dict1,file,x,y, w2, w, grouped):
    
    # Choose the rightmost element as pivot
    pivot = array[high]
 
    # Pointer for greater element
    i = low - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            

            #creating_images_in_sorting_stage.creating_image(new_dict,file,x,y,w2)
 
    # Swap the pivot element with
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    
    if grouped > 0:
            #arr to dictionary for displaying - dne this before in the change_pixels function
            new_dict = {}
            for ij in range(len(array)):
                key = array[ij]
                item = (dict1[key])
                new_dict[key] = item
            items = list(new_dict.items())
            random_dict = {}
            for ij in items:
                #print(i)
                dict5 = (ij[1])
                #print(dict5)
                dict6 = list(dict5.items())
                for ij,jj in dict6:
                    random_dict[ij] = jj
            
            ThirdFile.creating_image(random_dict,file,x,y,w2)

    else:
            new_dict = {}
            for ij in range(len(array)):
                key = array[ij]
                item = (dict1[key])
                new_dict[key] = item
            print(new_dict)
            print()
            ThirdFile.creating_image(new_dict,file,x,y,w2)

    # Return the position from where partition is done
    return i + 1
    
 
# Function to perform quicksort
def quickSort(array, low, high,dict1,file,x,y, w2, w, grouped):
    start_time1 = time.time()
    quickSort.start_time1 = time.time()
    quick_sort(array, low, high,dict1,file,x,y, w2, w, grouped)
    
    print("DONEEEEEEEE")
    time_taken= time.time() - start_time1
    w.time_take(time_taken)
 
def quick_sort(array, low, high,dict1,file,x,y, w2, w, grouped):#,dict1,file,x,y, w2, w):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high,dict1,file,x,y, w2, w, grouped)
 
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1,dict1,file,x,y, w2, w, grouped)
        

 
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high,dict1,file,x,y, w2, w, grouped)
        
# arr = [6,4,5,2,9,1]
# quickSort(arr,0,len(arr)-1,{6:1,4:2,5:3,2:4,9:5,1:6},"s","b","bh",5,1)