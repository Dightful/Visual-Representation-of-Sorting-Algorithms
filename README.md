# Visual-Representation-of-Sorting-Algorithms

This is the project i did for my A Level. It is application where you can choose a picture and the sorting algorithm that you want to sort the picture with. The pixels in the picture you selected will then be randomized, all displayed on the screen. Press start and the chosen sorting algorithm will sort the pixels into their original position. Different algorithms do it differently, bubble by going through the pixels comparing them. Or selection sort which repeatedly selects the smallest element from the unsorted part of the list and swaps it with the first element in the unsorted part of the list. 

The point of the program is to show how different sorting algorithms speeds are for different sizes of data (which in this case is a different resolutions of image). For example bubble is effective for low resolution images and really ineffective for high resolution images. Whereas a radix sort is less effective at smaller sizes (although still fast ) - but is extremely effective at larger images.
To make analyzing the different algorithms easier there is a automatic stopwatch which allows you to compare times, which starts when the algorithm starts and stops when algorithm is finished.
There is also a SQL database for times to be uploaded to so that they can be later compared to other times of same of different algorithms for the same size image, for example bubble sort and cocktail sort are very similar! It can also be used to compare the same algorithm but against different sizes of images. 
The sorting algorithms that are available:
- Bubble
- Insertion
- Cocktail
- Heap
- Quick
- Radix 
- Shell
- Selection
- Bucket

Summary:
It is a useful application to compare different sorting algorithms so that you can see what type of algorithm would be most effective/fastest for your data size. 

Note:
Any picture above size 1080x1920 does take a long time to sort due to there being over 2million items!
