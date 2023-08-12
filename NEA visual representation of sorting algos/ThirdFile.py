from PIL import Image
def creating_image(random_dict,file,x_value,y_value,w2):
	count2 = 0
	im = Image.open(file)
	x_value = int(x_value)
	y_value = int(y_value)
	for i in range(x_value):
		for j in range(y_value):
			try:
				item = list(random_dict.keys())[count2]
				#print(random_dict[item])
				rgb_values = random_dict[item]
				#opening up the image as im
				im.putpixel((i, j), (rgb_values[0], rgb_values[1], rgb_values[2]))
				count2 += 1
			except:
				pass

	file_name = file[0:-4]#removing .png so that _randomized can be added onto the end
	file_name = file_name + "_randomized.png"
	im.save(file_name)#works did this with dan
	w2.display_randomized2(file_name)




