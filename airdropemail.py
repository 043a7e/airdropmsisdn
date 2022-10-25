import hashlib

targetstart = input('Enter the target hash start fragment: ')
targetend = input('Enter the target hash end fragment: ')
emaildictionary = input('Drag your email dictionary here: ')
emaildictionary = emaildictionary.replace('\'', '').replace('\"', '')

with open(emaildictionary, 'r') as suspects:
    suspectssha2 = suspects.readlines()
    for line in suspectssha2:
        line = line.strip('\n')
        targettest = hashlib.sha256(line.encode())
        starthashcheck = targettest.hexdigest() [0:5]
        endhashcheck = targettest.hexdigest() [-5:]
        if starthashcheck == targetstart.lower() and endhashcheck == targetend.lower():
            match = line

print('Your target\'s email address may be: ' + match)
