import ThirdFile
import time 
def bubbleSort(arr,dict1,file,x,y,w2, w, grouped):
	start_time1 = time.time()
	n = len(arr)

	# Traverse through all array elements
	for i in range(n-1):
		# range(n) also work but outer loop will repeat one time more than needed.

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

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
					# print("NEw DICT!")
					#print(new_dict)
					print()

					ThirdFile.creating_image(new_dict,file,x,y,w2)
				#print(arr)
	print("DONEEEEEEEE")
	
	#print(new_dict)
	print()
	print()
	time_taken= time.time() - start_time1
	w.time_take(time_taken)


	#12X14 TOOK 80S