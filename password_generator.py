#Password genarator
import random as r
#All the Available Alphabets to genenrate a password
Alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','I','H','E','F','G','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#All the Available digits to generate a password
Numbers=[0,1,2,3,4,5,6,7,8,9]
#All the Available Special symbols to generate a password
Special_Symbols=['!','@','#','$','%','^','&','*']
length_of_password=int(input("Enter password length: "))
while(length_of_password<=8):
        print("The minimum password length is 8 ")
        length_of_password=int(input("Enter password length: "))
No_of_Alphabets = int(input("Enter Number of Alphabets you want :"))
No_of_SpecialCharacters = int(input("Enter Number of Special Characters you want :"))
No_of_Digits = int(input("Enter Number of Digits you want :"))
password= [ ]
#For Required number of Alphabets into the password
for i in range(1,No_of_Alphabets+1):
    letter=r.choice(Alphabets)
    password.append(letter)
#For Required number of Special Characters into the password
for i in range(1,No_of_SpecialCharacters+1):
    letter=r.choice(Special_Symbols)
    password.append(letter)
#For Required number of Integer Numbers into the password
for i in range(1,No_of_Digits+1):
    letter= str (r.choice(Numbers))
    password.append(letter)
r.shuffle(password)
#password = "".join(password)
#print("The random Passord is:" + password)
Final_Password=" "
for letter in password:
    Final_Password += letter
len_of_FinalPassword=len(Final_Password)
if length_of_password != len_of_FinalPassword:
     print("The length of password is not matched with FinalPassword length.Make sure length should be equal!")
else:
     print("The Random Password is",Final_Password)        
#Developed by
print("Developed by: https://github.com/Santhoshi0708")
