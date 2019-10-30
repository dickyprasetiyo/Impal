a = float(input('Nilai A= '))
b = float(input('Nilai B= '))
c = float(input('Nilai C= '))
a = round(a)
b = round(b)
c = round(c)
if(a < b+c and b < a+c and c < b+c) and (a>0 and b>0 and c>0):
    if(a==b==c):
        print('Sama Sisi')
    elif(a==b or a ==c or b ==c):
        print('Sama kaki')
    elif(a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b):
        print('Siku Siku')
    else:
        print('Segitiga Bebas')
else:
    print('Tidak ada segitiga yang bisa dibangun')
