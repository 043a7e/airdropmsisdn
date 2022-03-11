import hashlib

targetstart = input('Enter the target hash start fragment: ')
targetend = input('Enter the target hash end fragment: ')
rawareas = input('Enter possible target area codes separated by a comma: ')
print('Checking provided area codes.  Will report results upon completion.')
areacodelist = rawareas.split(',')
phonematch = []

for areacode in areacodelist:
    line = '0'
    print('Searching area code ' + areacode + ' for target...')
    while int(line) < 10000000:
        targetphone = '1' + areacode + str(line).zfill(7)
        targettest = hashlib.sha256(targetphone.encode())
        starthashcheck = targettest.hexdigest() [0:5]
        endhashcheck = targettest.hexdigest() [-5:]
        if starthashcheck == targetstart.lower() and endhashcheck == targetend.lower():
            print(targetphone + ' matches hash fragments.  Still checking...')
            phonematch.append(targetphone)
        line = int(line) + 1
    while int(line) == 10000000:
        if not phonematch:
            print('Target phone number not found in this area code set.  Please try another area code set.')
            break
        else:
            break
            
if phonematch:
    print('Your target\'s phone number may be:')
    for match in phonematch:
        print(match)
