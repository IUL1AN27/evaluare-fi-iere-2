with open('Desktop\INPUT.txt','r')as f:
    cop=list(f)
 a=0
print(f'NR. PRENUME NUME Nota 1 Nota a 2 Nota a 3 ')
with open('Desktop\REZERVA.txt','w') as b:
    for i in cop:
        campuri=i.split()
        print(i)
        b.write(i+'\n')
with open('Destop\Output.txt','w') as c:
    c.write('NR'' '+'PRENUME'+'NUME'+'Nota 1 '+'Nota a 2 '+'Nota a 3 '+'MEDIA'+'\n')
    for i in c:
        nota=i.split()
        y=nota[0]+' '+nota[1]+' ' +nota[2]
        media=str(float(nota[3])+float(nota[4])+float(nota[5]))
    with open('Desktop\Output.txt','a') as c:
            c.write(x)\
        x=y+''+media+'\n'			              
with open('Desktop\OUTPUT.txt','r') as f:
list3=f.readlines()