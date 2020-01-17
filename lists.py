#LIST
choco = ['kitkat','bounty','mars','snickers','galaxy','diary milk']
print(len(choco))
print(choco.reverse())
choco.append('kopiko')
print(choco.index('mars'))
print(len(choco))
print(choco)
for cho in choco:
    if 'kopiko' in cho:
        print('i love it')
    else:
        print('meh \t'  + cho)
chochoos=choco.sort()
print(chochoos)
        
