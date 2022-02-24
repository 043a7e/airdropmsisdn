import hashlib

targetstart = input('Enter the target hash start fragment: ')
targetend = input('Enter the target hash end fragment: ')
rawareas = input('Enter possible target area codes separated by a comma: ')
areacodelist = rawareas.split(',')


for areacode in areacodelist:
    line = '0'
    while int(line) < 10000000:
        targetphone = '1' + areacode + str(line).zfill(7)
        targettest = hashlib.sha256(targetphone.encode())
        starthashcheck = targettest.hexdigest() [0:5]
        endhashcheck = targettest.hexdigest() [-5:]
        if starthashcheck == targetstart.lower() and endhashcheck == targetend.lower():
            print('Your target\'s phone number is possibly:', targetphone)
            break
        else:
            line = int(line) + 1
