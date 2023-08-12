import ThirdFile
import time

def heapify(arr, N, i,dict1,file,x,y, w2,grouped):
    
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        print(arr)
        # swap
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
            ThirdFile.creating_image(new_dict,file,x,y,w2)

        # Heapify the root.
        heapify(arr, N, largest,dict1,file,x,y, w2, grouped)
 
# The main function to sort an array of given size
 


def heapSort(arr,dict1,file,x,y, w2, w,grouped):
    start_time1 = time.time()
    N = len(arr)
 
    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i, dict1,file,x,y, w2,grouped)
 
    # One by one extract elements
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0, dict1,file,x,y, w2,grouped)

    #here
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
        ThirdFile.creating_image(new_dict,file,x,y,w2)


    print("DONEEEEEEEE")
    time_taken= time.time() - start_time1
    w.time_take(time_taken)

 

# arr = [440, 830, 350, 234, 153, 793, 151, 60, 650, 598, 937, 669, 808, 191, 925, 572, 345, 155, 801, 706, 508, 832, 1018, 57, 723, 784, 944, 682, 595, 304, 96, 18, 616, 807, 948, 881, 264, 179, 695, 858, 905, 668, 256, 749, 996, 943, 825, 4, 10, 931, 253, 709, 448, 400, 829, 182, 404, 299, 277, 868, 1003, 254, 550, 538, 687, 755, 983, 731, 314, 526, 670, 592, 20, 933, 235, 893, 176, 984, 802, 844, 383, 227, 714, 631, 407, 679, 906, 393, 997, 125, 479, 67, 761, 398, 561, 94, 187, 529, 780, 1024, 587, 228, 947, 365, 496, 326, 591, 654, 929, 777, 418, 566, 283, 203, 680, 849, 152, 803, 1015, 545, 614, 966, 36, 910, 265, 470, 459, 258, 271, 809, 702, 52, 373, 84, 112, 78, 870, 200, 565, 938, 949, 519, 362, 782, 149, 642, 64, 638, 942, 499, 429, 458, 386, 722, 667, 907, 159, 542, 252, 588, 681, 671, 281, 85, 433, 306, 211, 136, 381, 492, 838, 516, 287, 659, 101, 106, 767, 419, 177, 778, 495, 343, 255, 924, 1011, 779, 822, 1004, 371, 274, 168, 551, 813, 690, 80, 164, 872, 532, 118, 209, 770, 288, 837, 40, 790, 763, 698, 646, 170, 604, 568, 490, 914, 31, 432, 82, 290, 544, 270, 814, 146, 377, 335, 346, 958, 817, 823, 752, 517, 969, 502, 641, 630, 173, 764, 2, 140, 124, 332, 581, 344, 700, 965, 267, 699, 55, 307, 352, 579, 415, 337, 884, 443, 694, 703, 90, 5, 160, 652, 926, 940, 762, 826, 49, 53, 452, 644, 342, 16, 25, 150, 903, 874, 141, 520, 973, 437, 768, 172, 1000, 624, 839, 665, 162, 710, 540, 514, 593, 927, 242, 430, 861, 505, 273, 625, 455, 347, 323, 887, 692, 171, 503, 321, 998, 574, 586, 537, 585, 651, 138, 810, 163, 609, 892, 666, 375, 976, 358, 360, 11, 192, 284, 123, 946, 578, 241, 747, 1002, 580, 266, 108, 733, 560, 1008, 596, 859, 957, 366, 708, 389, 704, 628, 62, 558, 794, 656, 876, 385, 387, 295, 715, 974, 962, 658, 175, 420, 107, 19, 110, 1012, 523, 712, 325, 678, 751, 243, 959, 626, 772, 509, 786, 319, 423, 226, 247, 315, 69, 132, 800, 72, 518, 21, 819, 775, 131, 655, 676, 634, 457, 367, 648, 447, 968, 109, 139, 883, 422, 105, 194, 584, 465, 289, 229, 724, 66, 1006, 854, 589, 246, 167, 14, 396, 932, 960, 357, 354, 961, 376, 726, 205, 895, 967, 836, 30, 583, 922, 909, 852, 232, 33, 399, 833, 536, 535, 297, 512, 75, 548, 43, 374, 736, 117, 397, 873, 216, 157, 444, 189, 917, 318, 741, 128, 156, 394, 556, 76, 1017, 324, 857, 99, 408, 866, 87, 835, 363, 725, 272, 102, 771, 600, 351, 987, 716, 734, 338, 766, 711, 488, 251, 129, 541, 378, 417, 231, 413, 58, 691, 993, 309, 206, 888, 390, 978, 721, 923, 612, 748, 534, 142, 1001, 851, 577, 291, 618, 494, 438, 954, 427, 878, 696, 461, 528, 56, 454, 992, 738, 416, 622, 442, 104, 521, 41, 862, 392, 950, 911, 891, 460, 531, 590, 120, 45, 989, 320, 783, 169, 472, 986, 190, 348, 262, 402, 739, 660, 899, 964, 215, 369, 119, 280, 991, 63, 403, 199, 877, 818, 880, 292, 15, 28, 464, 456, 834, 450, 97, 913, 953, 546, 640, 86, 563, 728, 639, 804, 223, 717, 990, 483, 756, 7, 1009, 1016, 475, 547, 330, 26, 282, 860, 867, 303, 93, 65, 35, 451, 37, 481, 737, 928, 758, 54, 597, 441, 742, 135, 657, 785, 789, 61, 515, 388, 478, 356, 380, 328, 647, 510, 29, 806, 863, 1020, 482, 158, 51, 248, 820, 401, 662, 815, 220, 934, 1019, 473, 605, 683, 439, 305, 426, 855, 525, 620, 491, 361, 497, 293, 875, 746, 238, 42, 916, 91, 935, 732, 100, 322, 208, 316, 327, 71, 527, 980, 73, 569, 759, 945, 428, 853, 249, 685, 896, 137, 446, 533, 126, 412, 613, 279, 339, 890, 956, 915, 83, 636, 186, 677, 384, 370, 421, 178, 994, 827, 567, 894, 183, 218, 610, 1013, 507, 552, 278, 161, 530, 230, 727, 261, 1005, 39, 856, 645, 921, 828, 918, 904, 982, 38, 1007, 301, 3, 693, 850, 204, 608, 846, 936, 684, 882, 134, 869, 70, 285, 500, 122, 296, 864, 181, 260, 617, 919, 504, 607, 130, 188, 98, 672, 908, 619, 476, 701, 797, 795, 576, 981, 411, 635, 8, 972, 559, 564, 47, 298, 6, 317, 50, 329, 511, 705, 615, 92, 68, 202, 349, 382, 963, 480, 195, 88, 627, 562, 239, 575, 468, 213, 259, 17, 334, 1010, 27, 127, 340, 221, 13, 474, 121, 406, 359, 103, 744, 688, 845, 466, 897, 740, 831, 9, 233, 643, 424, 353, 1022, 197, 811, 219, 210, 372, 222, 760, 573, 939, 225, 198, 46, 841, 463, 889, 379, 145, 975, 294, 341, 750, 553, 493, 707, 144, 269, 425, 522, 449, 485, 601, 886, 735, 805, 193, 788, 757, 554, 930, 821, 245, 898, 410, 308, 594, 487, 217, 154, 240, 570, 774, 995, 395, 453, 985, 286, 599, 611, 501, 776, 445, 24, 730, 637, 901, 988, 555, 920, 302, 166, 174, 180, 477, 313, 409, 900, 32, 840, 765, 44, 979, 81, 543, 12, 720, 754, 971, 621, 848, 629, 824, 842, 798, 633, 95, 816, 955, 79, 355, 115, 196, 111, 224, 791, 207, 686, 1021, 743, 471, 912, 467, 165, 769, 48, 257, 787, 133, 539, 781, 263, 431, 843, 300, 310, 623, 22, 244, 606, 391, 871, 557, 489, 673, 414, 212, 498, 275, 276, 214, 1014, 74, 649, 311, 113, 653, 941, 902, 469, 970, 147, 312, 364, 674, 143, 462, 148, 675, 486, 435, 697, 484, 582, 753, 237, 999, 368, 571, 549, 434, 977, 689, 799, 792, 405, 664, 114, 185, 436, 268, 879, 796, 952, 719, 729, 336, 812, 1, 250, 201, 34, 116, 847, 663, 23, 333, 513, 77, 236, 745, 885, 773, 718, 602, 184, 865, 632, 603, 331, 951, 506, 89, 59, 524, 1023, 713, 661]
# heapSort(arr,{},"the",12,2,3,4)
# print(arr)
# heapify
# so make every child smaller than every parent
# remove highest point