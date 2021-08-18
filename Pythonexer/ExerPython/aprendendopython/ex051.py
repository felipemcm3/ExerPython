p = int(input('Informe o primeiro termo da progressão'))
r = int(input('Informe a razão da progressão'))
print('A progressão do termo {} em razão {} é:'.format(p, r))
for t in range(10):
    print(p, end =' => ')
    p = p + r
print('\033[36mACABOU\033[m')
