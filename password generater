import random
letters= ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']
numbers=['0' , '1', '2' ,'3','4','5','6','7','8','9']
symbols=['@','!','#','$','%','^','&','*','('',)']
n_letters=int(input("welcome to the password generator! \nhow many letters would you like in your password?"))  
n_numbers=int(input("how many numbers would you like in ur password"))
n_symbols=int(input("how many symbol would you like in ur password"))
password=""
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password=password+char

for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password+=char
print(password)                            
