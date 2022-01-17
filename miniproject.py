from tkinter import *
import os
import random
 
# Designing window for registration
 
def register():
    global screen1
    screen1 = Toplevel(main_screen)
    screen1.title("Register")
    screen1.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(screen1, text="Please enter details below", bg="blue").pack()
    Label(screen1, text="").pack()
    username_lable = Label(screen1, text="Username * ")
    username_lable.pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    password_lable = Label(screen1, text="Password * ")
    password_lable.pack()
    password_entry = Entry(screen1, textvariable=password, show='*')
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=game).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()

num=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','100','101','102','200','201','895','654','789','325','104','123','455','789','951','456','753','1236','4589','7885','12654','254441','7885152','444525','456123789','15998741','1530000','4158554','47851249521','8451284512','7845129562','8451948569']
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
word=['Mango','apple','gun','fan','laptop','tv','appear', 'apple', 'are', 'area', 'arm', 'army', 'around', 'arrive', 'art', 'as', 'ask', 'at', 'attack', 'aunt', 'autumn', 'away','baby', 'back', 'bad', 'bag', 'ball', 'bank', 'base', 'basket', 'bath', 'be', 'bean', 'bear','cake', 'call', 'can', 'candle', 'cap', 'car', 'card', 'care', 'careful', 'careless','double', 'down', 'draw', 'dream', 'dress', 'drink', 'drive', 'drop', 'dry', 'duck', 'dust', 'duty','evening', 'event', 'ever', 'every', 'everyone','yard', 'yell', 'yesterday', 'yet', 'you', 'young', 'your']
words=["Apocalyptic","Equilibrium","Mitigate","Serpentine","Bamboozled","Exquisite","Nefarious","Silhouette","Bizarre","Flippant","Onomatopoeia","Sinister","Blasphemy","Gerrymandering","Persnickety","Statuesque","Bumblebee","Hyperbolic","Phosphorous","Stoicism","Capricious","Hypnosis","Picturesque","Synergistic","Clandestine","Incognito","Plebeian","Tectonic","Cognizant","Indigo","Quadrinomial","Totalitarian","Conundrum","Insidious","Quintessential","Trapezoid","Corrosion","Kaleidoscope","Rambunctious","Ubiquitous","Crestfallen","Kleptomania","Reptilian","Vermillion","Dastardly","Languish","Sabotage","Villainous","Diabolical","Luminescence","Sanctimonious","Whimsical","Dwindling","Melancholy","Scrupulous","Wizardry","Effervescent","Mercurial","Serendipity","Zigzag"]
from tkinter import messagebox
def time():
    global TimeLeft,score,miss
    if(TimeLeft >=11):
        pass
    else:
        timelabelcount.configure(fg="red")
    if(TimeLeft>0):
        TimeLeft-=1
        timelabelcount.configure(text=TimeLeft)
        timelabelcount.after(1000,time)
    else:
        gameplaylabel.configure(text='Hit={} | Miss={} | Total Score={}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Notification','for play again hit Retry button')
        if(rr==True):
            score=0
            TimeLeft=60
            miss=0
            timelabelcount.configure(text=TimeLeft)
            wordlabel.configure(text=letters[0])
            wordlabel.configure(text=num[0])
            wordlabel.configure(text=word[0])
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)
def startgame(event):
    global score,miss
    if(TimeLeft == 60):
        time()
    gameplaylabel.configure(text='')
    if(wordentry.get()==wordlabel["text"]):
        score+=1
        scorelabelcount.configure(text=score)
        print("Score: ",score)
    else :
        miss+=1
        print("Miss: ",miss)
    random.shuffle(num)
    random.shuffle(letters)
    random.shuffle(word)
    random.shuffle(words)
    if(score>=0 and score<3):
        wordlabel.configure(text=letters[0])
    elif(score>=3 and score<6):
        wordlabel.configure(text=num[0])
    elif(score>=6 and score<10):
        wordlabel.configure(text=word[0])
    elif(score>=10):
        wordlabel.configure(text=words[0])
    wordentry.delete(0,END)
from tkinter import *
import random
def game():
    root=Tk()
    root.geometry('800x600+300+50')
    root.configure(bg='black')
    root.title('Speed Type test')
    global TimeLeft,score,miss,timelabelcount,gameplaylabel,wordlabel,wordentry,scorelabelcount
    score=0
    TimeLeft=60
    miss=0

    head=Button(root,text = 'SPEED TYPING TEST',font=('airal',25,'italic bold'),bg='grey',fg='black')
    head.pack(side=TOP, pady = 10)

    random.shuffle(words)
    wordlabel=Label(root,text=letters[0],font=('airal',25,'italic bold'),bg='black',fg= 'white')
    wordlabel.place(x=350,y=200)


    scorelabel=Label(root,text='Your Score:',font=('airal',15,'italic bold'),bg='black',fg='white')
    scorelabel.place(x=15,y=100)
    scorelabelcount=Label(root,text=score,font=('airal',15,'italic bold'),bg='black',fg='white')
    scorelabelcount.place(x=40,y=140)


    timelabel=Label(root,text='Time Left:',font=('airal',15,'italic bold'),bg='black',fg='white')
    timelabel.place(x=650,y=100)
    timelabelcount=Label(root,text=TimeLeft,font=('airal',15,'italic bold'),bg='black',fg='white')
    timelabelcount.place(x=700,y=140)


    gameplaylabel=Label(root,text="Type word and press Enter button",font=('airal',15,'italic bold'),bg='black',fg='white')
    gameplaylabel.place(x=250,y=450)


    wordentry=Entry(root,font=('airal',25,'italic bold'),bd=5,justify='center')
    wordentry.place(x=225,y=250)
    wordentry.focus()



    root.bind("<Return>",startgame)

    root.mainloop()

main_account_screen()
