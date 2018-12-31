x= int(input("how my choclates: "))
av = 10
i=1
while i<=x:
    if i>av:
        print("out of stock")
        break
    print("here is your choclate..." ,i)
    i+=1
print("bye")

for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)

print("bye")

for i in range(1,100):

    if i%2==0:
        pass
    else:
        print(i)