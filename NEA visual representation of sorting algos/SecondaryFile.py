import PIL 
from PIL import Image
import random
import ast


dict1 = {}
def add_randomized(file_name):
    file_name = file_name[0:-4]#removing .png so that _randomized can be added onto the end
    file_name = file_name + "_randomized.png"
    return file_name

def resolution_finder(file, which_file):
    img = PIL.Image.open(file)

    # fetching the dimensions
    wid, hgt = img.size
    if which_file == False:
        # displaying the dimensions
        resolution = (str(wid) + "," + str(hgt))
        
        return resolution
    else:
        return wid, hgt

def rgb_of_pixel (img_path,x,y):
    im = Image.open(img_path).convert("RGB")
    r, g, b = im.getpixel((x,y))
    a = (r, g, b)
    return a 
def change_pixels(x_value,y_value,random_dict,file, grouped):
    if grouped > 0:
        items = list(random_dict.items())
        random_dict1 = {}
        for i in items:
            #print(i)
            dict5 = (i[1])
            dict6 = list(dict5.items())
            
            for i,j in dict6:
                random_dict1[i] = j
            for j in dict6:
                rgb_values = (j[1])
        random_dict = dict(random_dict1)

    count2 = 0
    im = Image.open(file)
    for i in range(x_value):
        for j in range(y_value):
            item = list(random_dict.keys())[count2]
            #print(random_dict[item])
            rgb_values = random_dict[item]
            #opening up the image as im
            im.putpixel((i, j), (rgb_values[0], rgb_values[1], rgb_values[2]))
            count2 += 1
    #print("random file created")
    file_r = add_randomized(file)
    im.save(file_r)
    return file_r

# def woo(num):
# 	print(num)

def connecting_randomDict_to_sort_algo(dict1,file,x,y,w2,w, sorting_algo,grouped):
    arr2 = []
    
    dict_ran = dict1#this is because dict1 is a string, this is because thats how you save it in a txt file
    dict1 = ast.literal_eval(dict_ran)
    for i in range(len(dict1)):
        arr2.append(list(dict1.keys())[i])


    import selection_sort 
    import bubble_sort    
    import insertion_sort 
    import cocktail_sortpy
    import shell_sort 
    import quick_sort 
    import radix_sort
    import heap_sort
    import bucket_sort
#print(dict1)

    if sorting_algo == "Insertion": 
        insertion_sort.insertionSort(arr2,dict1,file,x,y,w2,w,grouped)
    elif sorting_algo == "Cocktail": 
        cocktail_sortpy.cocktailSort(arr2,dict1,file,x,y,w2,w,grouped)
    elif sorting_algo == "Bubble":
        bubble_sort.bubbleSort(arr2,dict1,file,x,y,w2,w,grouped)
    elif sorting_algo == "Selection":
        selection_sort.selectionSort(arr2,dict1,file,x,y,w2,w,grouped)
    elif sorting_algo == "Shell": 
        shell_sort.shellSort(arr2,len(arr2),dict1,file,x,y,w2,w,grouped)
    elif sorting_algo == "Quick": 
        quick_sort.quickSort(arr2,0,(len(arr2)-1),dict1,file,x,y,w2,w,grouped)
    elif sorting_algo == "Radix":
        radix_sort.radixSort(arr2,dict1,file,x,y,w2,w,grouped)   
    elif sorting_algo == "Heap": 
        heap_sort.heapSort(arr2,dict1,file,x,y,w2,w,grouped)
    elif sorting_algo == "Bucket": 
        bucket_sort.bucketSort(arr2,dict1,file,x,y,w2,w,grouped)    


def runner(w2, loc, grouped):
    
    count = 0
    x, y = (resolution_finder(loc, True))

    for i in range(x):
        for j in range(y):
            count += 1
            dict1[count] = rgb_of_pixel(loc,i,j)

    #print(dict1)
    print()
    if grouped > 0:
        arr2 = list(dict1.items())
        new_arr = {}
        count = 0
        count2 = 1
        temp = {}
        for key, value in arr2:
            if count % grouped == 0 and count != 0:#2 is how many per thing
                new_arr[count2] = temp
                temp = {}
                count2 += 1
                temp.update({key:value})
            else:
                temp.update({key:value})
            count += 1
        new_arr[count2] = temp
        print(new_arr)
        #randomizing it
        items = list(new_arr.items())
        random_dict = {}
        random.shuffle(items)
        for key, value in items:
                random_dict[key] = value
      #  print(random_dict)
        print()

    else:
        random_dict = {}	
        items = list(dict1.items()) # List of tuples of (key,values)
        random.shuffle(items)
        for key, value in items:
            random_dict[key] = value
        print()



    file_name = change_pixels(x,y,random_dict,loc, grouped)


    w2.display_randomized2(file_name)

    with open ("values_needed_for_sorting_function.txt","w") as file:
        if grouped > 0:

            file.write(";" + str(random_dict)+";"+loc+","+str(x)+","+str(y))
            file.close()
        else:

            file.write(str(random_dict)+","+loc+","+str(x)+","+str(y))
            file.close()

