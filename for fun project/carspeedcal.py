a = 10
b = 12

c = a + b / 2
print(c)

print("slkm/h")
sl = input("speed limit >> ")
print(sl + "km/h")

print("s1km/h")
s1 = input("enter s1 >> ")
print(s1+ "km/h")

print("s2km/h")
s2 = input("enter s2 >> ")
print(s2 + "km/h")
speeding = False


#######main code

is1 = int(s1)
is2 = int(s2)


an = (is1 + is2) / 2 
print(an)

spd = int(an) - int(sl)
if an > int(sl) :
    print("speeding")
    print("you are " + str(spd) + "km/h faster than the speed limit")
    speeding = True
elif an <= int(sl):
    print("not speeding")

fd = int(sl)
td = int(sl) + 10
ftd = int(sl) + 15

if speeding == True:
    print("speedlim : " + sl + "km/h")
    
    print("50$ = " + str(fd))
    
    print("100$ = " + str(td))
                                    
    print("150$ = " + str(ftd))
elif int(an) < fd and int(an) > td:
    print("you need to pay 50$")
elif int(an) < td and int(an) > ftd:
    print("you need to pay 100$")
elif int(an) < ftd:
    print("you need to pay 150$")