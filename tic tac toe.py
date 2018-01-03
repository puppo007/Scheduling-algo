import random 
b = [0,1,2,3,4,5,6,7,8,9]
turn=1
def showBoard():
    print "| --|--","|-- |"
    print "|",b[1],"|",b[2],"|",b[3],"|"
    print "| --|--","|-- |"
    print "|",b[4],"|",b[5],"|",b[6],"|"
    print "| --|--","|-- |"
    print "|",b[7],"|",b[8],"|",b[9],"|"
    print "| --|--","|-- |"
   
def win():
    if b[1]=="X" and b[2]=="X" and b[3]=="X":
        return True
    if b[4]=="X" and b[5]=="X" and b[6]=="X":
        return True
    if b[7]=="X" and b[8]=="X" and b[9]=="X":
        return True
    if b[1]=="X" and b[4]=="X" and b[7]=="X":
        return True
    if b[2]=="X" and b[5]=="X" and b[8]=="X":
        return True
    if b[3]=="X" and b[6]=="X" and b[9]=="X":
        return True
    if b[1]=="X" and b[5]=="X" and b[9]=="X":
        return True
    if b[3]=="X" and b[5]=="X" and b[7]=="X":
        return True
    if b[1]=="O" and b[2]=="O" and b[3]=="O":
        return True
    if b[4]=="O" and b[5]=="O" and b[6]=="O":
        return True
    if b[7]=="O" and b[8]=="O" and b[9]=="O":
        return True
    if b[1]=="O" and b[4]=="O" and b[7]=="O":
        return True
    if b[2]=="O" and b[5]=="O" and b[8]=="O":
        return True
    if b[3]=="O" and b[6]=="O" and b[9]=="O":
        return True
    if b[1]=="O" and b[5]=="O" and b[9]=="O":
        return True
    if b[3]=="O" and b[5]=="O" and b[7]=="O":
        return True

def draw():
    for i in range(1,10):
        if b[i]!="X" and b[i]!="O":
            return False
    return True

def reset():
    for i in range (0,10):
        b[i]=i
    print "Player 1 Symbol is X"
    print "Player 2 Symbol is O"
    c=int(raw_input("Which Player Wants to go first 1 or 2: " ))
    showBoard()
    return c

print "Player 1 Symbol is X"
print "Player 2 Symbol is O"
n=int(raw_input("Which Player Wants to go first 1 or 2: " ))
turn=n
showBoard()
while True:
    if turn==1:
        print "Player",turn
        index=int(raw_input("Select Box: "))
        if index in range(1,10) and b[index]!="X" and b[index]!="O" :
            b[index]="X"
            showBoard()
            if win():
                print "Congratulations Player",turn,"Wins"
                a=raw_input("Do You Want to Play Again Y/N: ")
                if a=="y" or a=="Y":
                    turn=reset()
                elif a=="n" or a=="N":
                    break
            else:
                turn=2
            if draw():
                print "Game Draw!!"
                a=raw_input("Do You Want to Play Again Y/N: ")
                if a=="y" or a=="Y":
                    turn=reset()
                elif a=="n" or a=="N":
                    break
        else:
            print "Invalid Move Please select valid box"
            
    elif turn==2:
        print "Player",turn
        index=int(raw_input("Select Box: "))
        if index in range(1,10) and b[index]!="X" and b[index]!="O" :
            b[index]="O"
            showBoard()
            if win():
                print "Congratulations Player",turn,"Wins"
                a=raw_input("Do You Want to Play Again Y/N: ")
                if a=="y" or a=="Y":
                    turn=reset()
                elif a=="n" or a=="N":
                    break
            else:
                turn=1
            if draw():
                print "Game Draw!!"
                a=raw_input("Do You Want to Play Again Y/N: ")
                if a=="y" or a=="Y":
                    turn=reset()
                elif a=="n" or a=="N":
                    break
        else:
            print "Invalid Move Please select valid box"
            
