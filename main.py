import random

def gamewin(comp,you):

  if comp == you :
        return None
  elif comp == 's':
        if you == 'w':
            return False
        if you == 'g':
            return True
  elif comp == 'w':
        if you == 'g':
            return False
        if you == 's':
            return True
  elif comp == 'g':
        if you == 's':
            return False
        if you == 'w':
            return True

print("COMP TURN: Snake(s) Water(w) Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp='s'
elif randNo == 2:
    comp='w'
elif randNo == 3:
    comp='g'

you= input("Your turn : Snake(s) Water(w) Gun(g)? ")
a = gamewin(comp,you)

print(f"COMPUTER COOSE {comp}")
print(f"YOU COOSE {you}")

if a== None:
    print("The game is tie!!!!!!!!!!!!!!!")
elif a:
    print("You win!!!!!!!!!!!!!!!!!!!!!")
else :
    print("You loose!!!!!!!!!!!!!!!!!!!!!!!")
