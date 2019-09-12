computer_amount = int(input('Jumlah Komputer: '))
service_time = int(input('Service Time: '))
drop_off = str(input('drop off: '))
Pick_Up = str(input('pick up: '))

if (computer_amount == 1 or computer_amount == 2):
    base_fee = 50
    additional_fee = 0
elif(computer_amount >= 3 and computer_amount <= 10):
    base_fee = 100
    additional_fee = 10
else:
    base_fee = 500
    additional_fee = 10

if (service_time < 9 or service_time > 21):
    base_fee = base_fee*2

if((drop_off == True) and (Pick_Up == True) ):
    Total_base_fee = base_fee - (base_fee*0.015)
    print("$" + str(Total_base_fee))
else:
    print(base_fee)