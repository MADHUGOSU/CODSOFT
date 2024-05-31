import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*','(',')','-','=','+']
print("password Generator")
lett=int(input("how many letters in your password\n"))
num=int(input("how many numbers in your password\n"))
sym=int(input("how many symbols in your password\n"))
p=""
for i in range(1,lett+1):
    pa=random.choice(letters)
    p=p+pa
for i in range(1,num+1):
    pa=random.choice(numbers)
    p=p+pa
for i in range(1,sym+1):
    pa=random.choice(symbols)
    p=p+pa
print(p)

