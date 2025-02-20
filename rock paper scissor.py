import random
rock=''''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper= '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissor='''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) 
'''
images=[rock,paper,scissor]
user_choice=int(input("enter your choice:type 0 for rock,1 for paper,2 for scissors."))
print(images[user_choice])
comp_choice=random.randint(0,2)
print("comp choose")
print(images[comp_choice])
if user_choice==comp_choice:
        print("draw match")
elif user_choice==0 and comp_choice==2:
        print("you win")
elif user_choice==2 and comp_choice==0:
        print("comp wins")
elif comp_choice>user_choice:
    print("you loose")
elif comp_choice<user_choice:
    print("you win")
else:
    print("comp wins")
