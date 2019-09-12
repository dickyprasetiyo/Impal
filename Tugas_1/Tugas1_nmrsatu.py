a = int(input('Nilai A= '))
b = int(input('Nilai B= '))
c = int(input('Nilai C= '))

if(a==b==c):
    print('Sama Sisi')
elif(a==b or a ==c or b ==c):
    print('Sama kaki')
else:
    print('Sembarang')

if(a*a == b*b + c*c):
    print('Siku Siku')
elif(b*b == a*a + c*c):
    print('Siku Siku')
elif(c*c == a*a + b*b):
    print('Siku Siku')
