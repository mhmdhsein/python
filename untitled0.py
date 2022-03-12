from tkinter import*
from json import*
from time import*
def pasclik(*args):
    txt2.delete(0,'end')
def userclik(*args):
    txt.delete(0,'end')
def submit():
    
    with open('s.json')as f:
        dct=load(f)
    enter=txt.get()
    if(len(enter)<4):
          messagebox.showinfo('submit message','username less than 4 character!')
          return
    enter2=txt2.get()
    if(len(enter)<8):
          messagebox.showinfo('submit message','password less than 8 character!')
          return
    if(enter not in dct):
        dct[enter]=enter2
        with open('s.json','w')as f:
               dump(dct,f)   
               messagebox.showinfo('submit message','submit done')
    else:
        messagebox.showinfo('submit message','username was submit!try again 10 second later')
        sleep(10)
def login():
      with open('s.json')as f:
        dct=load(f)
        enter=txt.get()
        enter2=txt2.get()
      if(enter in dct):
            if(dct[enter]==enter2):
                 messagebox.showinfo('login message','welcome')
                 btm_logout.configure(state='normal')
                 btm_login.configure(state='disable')
                 btm_submit.configure(state='disable')
            else:
                  messagebox.showinfo('login message','wrong password!you can try again 10 second later')
                  sleep(10)
      else:
            messagebox.showinfo('login message','username was not submit until now!you can try again 10 second later ')
            sleep(10)
def delete():
    with open('s.json')as f:
        dct=load(f)
        enter=txt.get()
        enter2=txt2.get()
        if(enter in dct):
            if(dct[enter]==enter2):
                dct.pop(enter)
                with open('s.json','w')as f:
                        dump(dct,f)
                        messagebox.showinfo('delete message','your account delete now!')
            else:
                  messagebox.showinfo('delete message','wrong password!try again 10 second later')
                  sleep(10)
        else:
              messagebox.showinfo('delete message','username not exist!try again 10 second later')
              sleep(10)
def logout():
        if(submit['state']==disable and loginp['state']==disable):
            messagebox.showinfo('logout message','logout done!')
            btm_delete.configure(state='normal')
            btm_submit.configure(state='normal')
            btm_login.configure(state='normal')
            btm_logout.configure(state='disable')
            return
win=Tk()
win.title('star')
win.geometry('350x200')
idi=Label(win,text='username:')
idi.place(relx=0.0,rely=0.0)
txt=Entry(win,width=22)
txt.insert(0,'enter username')
txt.bind('<Button-1>',userclik)
txt.place(relx=0.20,rely=0)



ff=Label(win,text="pasword:")
ff.place(relx=0.0,rely=0.18)
txt2=Entry(win,width=22)
txt2.insert(0,'enter pasword')
txt2.bind('<Button-1>',pasclik)
txt2.place(relx=0.20,rely=0.18)


btm_submit=Button(win,text='submit',bg='#ff1111',command=submit)
btm_submit.place(relx=0.10,rely=0.80)



btm_login=Button(win,text='login',bg='#7fff00',command=login)
btm_login.place(relx=0.30,rely=0.80)


btm_delete=Button(win,text='delete',bg='#00ffff',command=delete)
btm_delete.place(relx=0.50,rely=0.80)



btm_logout=Button(win,text='logout',bg='#ff8c00',command=logout,state='disable')
btm_logout.place(relx=0.70,rely=0.80)
win.mainloop()