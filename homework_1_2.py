#HOMEWORK 1

for i in range(0,5):
    value = input("enter a value :")
    print("format usage value is : {}".format(value),type(value))
    print(f"f-string usage value is :{value}",type(value))
    print("********************")



#HOMEWORK 2

myList=[]
firstName=input("enter your first name :")
lastName=input("enter your last name :")
Age=int(input("enter your age :"))
year=int(input("when were you born (only year) :"))
myList.append(firstName)
myList.append(lastName)
myList.append(Age)
myList.append(year)
for i in range(0,4):
    print(myList[i])
if Age < 18:
    print("you cannot go out because its too dangerous")
else:
    print("you can go out to the street")