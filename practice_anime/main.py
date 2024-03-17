import random
def main():
  teams = []
  anime_char = ["Hinata", "Naruto", "Goku",
                "Eren", "Levi", "Mikasa",
                "Monkey", "Gon","Sasuke"]
  user = int(input("Enter 1 to chose your characters,Enter 2  choose 3 characters: "))
  num = 0
  user
  if user == 1:
    print(anime_char)
    for i in range(0,3):
        user_in = input("Enter the name of the characters: ")
        check = check_char(anime_char, user_in)
        if check == True:
            teams.append(user_in)
            anime_char.remove(user_in)
        else:
            raise Exception("Sorry anime character not in list." )
    swap = input("Would you like to swap your characters: ")
    if swap == 'y':
       print("Your team: ", teams)
       print("other characters available: ", anime_char)
       while True:
          user_change = input("Enter the character you want to change: ")
          swap_char = input("Enter the anime character you want to swap: ")
          check = check_char(anime_char, user_change)
          if check == True:
            anime_char.append(swap_char)
            teams.remove(swap_char)
            teams.append(user_change)
            anime_char.remove(user_change)
            continue_user = input("Would you like to continue: ")
            if continue_user == 'n':
               break
            else:
               continue
          else:
             continue
    print(teams)
    print(anime_char)
  if user == 2:
    num = 0
      #we want to use random.choice three time
    while num < 3:
       teams.append(random.choice(anime_char))
       num += 1
    print(teams)
def check_char(anime_char, user_in):
    for i in range(0, len(anime_char)):
        if(user_in == anime_char[i]):
            return True
    return False
main()