import hashlib

targetstart = input('Enter the target hash start fragment: ')
targetend = input('Enter the target hash end fragment: ')
print('Checking all area codes US and Canada.  Results will report on completion.')
areacodelist = [201, 202, 203, 204, 205, 206, 207, 208, 209, 210,
    212, 213, 214, 215, 216, 217, 218, 219, 224, 225, 226, 228, 229,
    231, 234, 239, 240, 242, 246, 250, 251, 252, 253, 254, 256, 260,
    262, 264, 267, 268, 269, 270, 276, 281, 284, 289, 301, 302, 303, 
    303, 304, 305, 306, 307, 308, 309, 310, 312, 314, 315, 316, 317, 
    318, 319, 320, 321, 323, 325, 330, 336, 337, 339, 340, 345, 347, 
    351, 352, 360, 361, 386, 401, 402, 403, 404, 405, 406, 407, 408, 
    409, 410, 412, 413, 414, 415, 416, 417, 418, 419, 423, 424, 425, 
    430, 432, 434, 435, 438, 440, 441, 443, 450, 456, 469, 473, 478, 
    479, 480, 484, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 
    510, 512, 513, 514, 515, 516, 517, 518, 519, 520, 530, 540, 541, 
    551, 559, 561, 563, 567, 570, 571, 573, 574, 580, 585, 586, 600,
    601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 612, 613, 614, 
    615, 616, 617, 618, 619, 620, 623, 626, 630, 631, 636, 641, 646, 
    647, 649, 650, 651, 660, 661, 662, 664, 670, 671, 678, 682, 684, 
    700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 712, 713,
    714, 715, 716, 717, 718, 719, 720, 724, 727, 731, 732, 734, 740,
    754, 757, 758, 760, 762, 763, 765, 767, 769, 770, 772, 773, 774,
    775, 778, 780, 781, 784, 785, 786, 787, 800, 801, 802, 803, 804,
    805, 806, 807, 808, 809, 810, 812, 813, 814, 815, 816, 817, 818,
    819, 828, 829, 830, 831, 832, 843, 845, 847, 848, 850, 856, 857,
    858, 859, 860, 862, 863, 864, 865, 866, 868, 869, 870, 876, 877,
    878, 888, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
    912, 913, 914, 915, 916, 917, 918, 919, 920, 925, 928, 931, 936, 
    937, 939, 940, 941, 947, 949, 951, 952, 954, 956, 970, 971, 972, 
    973, 978, 979, 980, 985, 989]
phonematch = []

for areacode in areacodelist:
    line = '0'
    print('Searching area code ' + str(areacode) + ' for target...')
    while int(line) < 10000000:
        targetphone = '1' + str(areacode) + str(line).zfill(7)
        targettest = hashlib.sha256(targetphone.encode())
        starthashcheck = targettest.hexdigest() [0:5]
        endhashcheck = targettest.hexdigest() [-5:]
        if starthashcheck == targetstart.lower() and endhashcheck == targetend.lower():
            phonematch.append(targetphone)
            print(targetphone + ' matches hash fragments.  Still checking...')
        line = int(line) + 1
    while int(line) == 10000000:
        break
            
if phonematch:
    print('Your target\'s phone number may be:')
    for match in phonematch:
        print(match)
else:
    print('Target phone number not found in this area code set.  Target phone may use another country code.')
