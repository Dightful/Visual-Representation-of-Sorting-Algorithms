import ThirdFile
import time
def cocktailSort(a,dict1,file,x,y,w2,w,grouped):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    print(a)
    while (swapped == True):
 
        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False
 
        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                
                a[i], a[i + 1] = a[i + 1], a[i]
                if grouped > 0:
                    #arr to dictionary for displaying - dne this before in the change_pixels function
                    new_dict = {}
                    for i in range(len(a)):
                        key = a[i]
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
                    for i in range(len(a)):
                        key = a[i]
                        item = (dict1[key])
                        new_dict[key] = item
                    print(new_dict)
                    print()
                    ThirdFile.creating_image(new_dict,file,x,y,w2)
                
                swapped = True
 
        # if nothing moved, then array is sorted.
        if (swapped == False):
            break
 
        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False
 
        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1
 
        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1, -1):
            if (a[i] > a[i + 1]):
                
                a[i], a[i + 1] = a[i + 1], a[i]
                if grouped > 0:
                    #arr to dictionary for displaying - dne this before in the change_pixels function
                    new_dict = {}
                    for i in range(len(a)):
                        key = a[i]
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
                    for i in range(len(a)):
                        key = a[i]
                        item = (dict1[key])
                        new_dict[key] = item
                    print(new_dict)
                    print()
                    ThirdFile.creating_image(new_dict,file,x,y,w2)



                swapped = True
 
        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start + 1

    print("DONEEEEEEEE")
    time_taken= time.time() - start_time1
    w.time_take(time_taken)

        
 
    