deposit = int(input("Deposit:"))
desiredAmmount = int(input("Desired money:"))
interest = int(input("Interest:"))
interest = interest / 100
count = 0
while(True):
    deposit = (interest / 12) * deposit + deposit
    count += 1
    if(deposit >= desiredAmmount):
        break
print(count)
