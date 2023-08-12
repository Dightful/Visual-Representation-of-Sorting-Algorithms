import ThirdFile
import time
def shellSort(arr, n,dict1,file,x,y, w2, w, grouped):
    start_time1 = time.time()
    # code here
    gap=n//2
      
    while gap>0:
        j=gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j<n:
            i=j-gap # This will keep help in maintain gap value
              
            while i>=0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if arr[i+gap]>arr[i]:
                    i=-1
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
                    
                    if grouped > 0:
                        #arr to dictionary for displaying - dne this before in the change_pixels function
                        new_dict = {}
                        for ij in range(len(arr)):
                            key = arr[ij]
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
                        for ij in range(len(arr)):
                            key = arr[ij]
                            item = (dict1[key])
                            new_dict[key] = item
                        print(new_dict)
                        print()
                        ThirdFile.creating_image(new_dict,file,x,y,w2)

                i=i-gap # To check left side also
                            # If the element present is greater than current element 
            j+=1
        gap=gap//2
    print("DONEEEEEEEE")
    time_taken= time.time() - start_time1
    w.time_take(time_taken)

  
  
# #driver to check the code
# # arr2 = [6,4,5,2,9,1]
# # print("input array:",arr2)
  
# # shellSort(arr2,len(arr2))
# # print("sorted array",arr2)
 
# arr = [6,4,5,2,9,1]
# shellSort(arr,len(arr),{6:"bob",4:"hop",5:"hop",2:"hop",9:"hop",1:"df"},"s","b","bh",5,1)
# print(arr)