print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

together_name = name1.lower()+name2.lower()

Score1 = together_name.count("t") + together_name.count("r") + together_name.count("u") + together_name.count("e")

Score2 = together_name.count("l") + together_name.count("o") + together_name.count("v")+ together_name.count("e")

Total_score=f"{Score1}{Score2}"

if int(Total_score) <=10 or int(Total_score)>=90:
  print(f"Your score is {Total_score}, you go together like coke and mentos.")
elif int(Total_score) >=40 and int(Total_score)<=50:
  print(f"Your score is {Total_score}, you are alright together.")
else:
  print(f"Your score is {Total_score}.")
