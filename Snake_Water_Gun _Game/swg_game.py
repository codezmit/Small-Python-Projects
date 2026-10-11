import random

print(" Enter your choice:\n s=Snake , w=Water, g= Gun" )


computer_choice = random.choice([-1, 0 , 1])
user_choice = input("Enter Your Choice:")
choice = str.lower(user_choice)
user_dic = {"s": 1, "w":0, "g":-1}
user_value = user_dic[choice]
computer_dic = {1:"Snake", 0 :"Water",-1: "Gun"}
print(f"Your Choice is:{computer_dic[user_value]}\nComputer Chose: {computer_dic[computer_choice]}")

if(computer_choice==user_value):
  print("It's a Draw!")

else:
  if(computer_choice==-1 and user_value==1):
    print("You loose!")
  elif(computer_choice==-1 and user_value==0):
    print("You Win!")
  
  if(computer_choice==0 and user_value==1):
    print("You loose!")
  elif(computer_choice==0 and user_value==-1):
    print("You Win!")

  if(computer_choice==1 and user_value==-1):
    print("You Win!")
  elif(computer_choice==1 and user_value==0):
    print("You loose!")

