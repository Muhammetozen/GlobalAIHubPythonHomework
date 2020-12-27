print("User Identification Program")
o=int(input("How many entire user?"))
for i in range(o):
    y=str(input("Please enter firs name= "))
    j=str(input("Please enter last name= "))
    z=int(input("please enter date of birt(just year)= "))
    x=int(input("Please enter age"))
    if x<= 18:
        print("i+1. user")
        h=print("You can not go out because it is too dangerous")
        list= [y,j,z,x,h]
        continue
    else:
        print("i+1. user")
        h=print("You can go out to the street")
        list= [y,j,z,x,h]
        print(y+j+z+x+h)
        break
    print(list)
