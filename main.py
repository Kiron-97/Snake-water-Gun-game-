welcome= "Welcome to snake water gun game "
print(welcome.center(66, "*"))
print()
name=input("Enter Your Name:")
print()

print("Rules of the game:\n\n1. Snake drinks water \n2, Water disfunctions gun \n3. Gun shoots snake ")
print()

print("Snake=1\nWater=2\nGun=3")
print()

while True:
 print()
 value=int(input("Enter Your Choice:"))
 print()

 if value>3 or value<1:
  raise ValueError(f"{name}, Invalid Input!")
  
 if value==1:
  print(f"{name} chooses : Snake ")
 elif value==2:
  print(f"{name} chooses : Water ")
 elif value==3:
  print(f"{name} chooses : Gun ")
  
 import random
 computer_choice= ["Snake","Water", "Gun"]
 comp=random.choice(computer_choice)
 print("Compuer chooses :", comp)

 print()

 if comp=="Snake" and value==1:
  print("'Draw'")
 elif comp=="Water" and value==2:
  print("'Draw'")
 elif comp=="Gun" and value==3:
  print("'Draw'")
   
 elif comp=="Snake" and value==3 or comp=="Water" and value==1 or comp=="Gun" and value==2 :
  print("'You Win'")
 else:
  print("'You Lose'")
