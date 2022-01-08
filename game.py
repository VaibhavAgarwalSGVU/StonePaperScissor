from tkinter import *
from PIL import Image, ImageTk
from random import randint
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#9b59b6")

#picture
rock_img = ImageTk.PhotoImage(Image.open("ROCK1.png"))
paper_img = ImageTk.PhotoImage(Image.open("PAPER  - Copy.png"))
scissor_img = ImageTk.PhotoImage(Image.open("SCISSOR.png"))
user_label = Label(root,image=scissor_img)
comp_label = Label(root,image= rock_img)
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#score
playerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

#indicators
user_indicator= Label(root, font=50,text="PLAYER",bg="#9b59b6",fg="white")
comp_indicator= Label(root, font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg =Label(root, font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text']= x 
    #update
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)

def updateCompScore():
    score = int(computerScore['text'])
    score += 1
    computerScore['text'] = str(score)

#check winner
def checkWin(player,computer):
    if player == computer:
        updateMessage("TIE")
    elif player == "rock":
        if computer == "paper":
            updateMessage("LOOSE")
            updateCompScore()
        else:
            updateMessage("WIN")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("LOOSE")
            updateCompScore()
        else:
            updateMessage("WIN")    
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("LOOSE")
            updateCompScore()
        else:
            updateMessage("WIN")    
            updateUserScore()
    else:
        pass
#update choices
choices= ["rock","paper", "scissor"]
def updateChoice(x):

#forcomputer

    compChoice = choices[randint(0,2)]
    if compChoice =="rock":
        comp_label.configure(image=rock_img)
    elif compChoice =="paper":
        comp_label.configure(image=paper_img)
    else :
        comp_label.configure(image=scissor_img)
#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,compChoice)

#button
rock = Button(root,width=20,height=2,text="ROCK",
                bg="#FF3E4D",fg="white",command= lambda: updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",
                bg="#FF3E4D",fg="white",command= lambda: updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",
                bg="#FF3E4D",fg="white",command= lambda: updateChoice("scissor")).grid(row=2,column=3)

root.mainloop()