from tkinter import *
from tkinter import messagebox
from random import randint
import pyperclip

tk = Tk()
tk.geometry('1200x900')
tk.title('PyPM')

# Variables
res = StringVar()
res.set('Password')
l = 10
alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
alphaSpec = 'abcdefghijklmnopqrstuvwxyz0123456789,;:=?./+ù%[]{}&é"\'§è!çà-()'
isSpecial = False

def setL(newValue):
  global l, lenLab
  if (newValue < 8):
    return messagebox.showerror("Error", "Password length cannot be < 8")
  elif (newValue > 25):
    return messagebox.showerror("Error", "Password length cannot be > 25")
  l = newValue
  lenLab['text'] = str(l)

def setIfSpecial():
  global isSpecial, radio
  isSpecial = not isSpecial
  if (radio['text'] == ' '):
    radio['text'] = 'X'
  else:
    radio['text'] = ' '

def generate():
  global isSpecial, res, alphaSpec, alpha
  a = []
  for i in range(0, l):
    if (isSpecial):
      a.append(alphaSpec[randint(0, len(alphaSpec) - 1)])
    else:
      a.append(alpha[randint(0, len(alpha) - 1)])
  print(''.join(a))
  res.set(''.join(a))

def toClip():
  global res
  tk.clipboard_clear()
  return tk.clipboard_append(res.get())

print('Loul')
print('Constantin')
print('merge')

# Canvas
cleft = Canvas(tk, bg='#212121')
cleft.grid()

cright = Canvas(tk)
cright.grid(column=1, row=0)

# password generator
cres = Canvas(cright)
cres.grid()

result = Entry(cres, textvariable=res, width=25, font="Helvetica 20 bold", justify='center')
result.grid()

cpy = Button(cres, command=toClip, text='Copy')
cpy.grid(column=1, row=0)

clen = Canvas(cright)
clen.grid()

minusBtn = Button(clen, text='-', command=lambda: setL(l - 1))
minusBtn.grid(row=0, column=0)

lenLab = Label(clen, text=str(l), font="Helvetica 18 bold")
lenLab.grid(row=0, column=1)

plusBtn = Button(clen, text='+', command=lambda: setL(l + 1))
plusBtn.grid(row=0, column=2)

cspec = Canvas(cright)
cspec.grid()

radio = Button(cspec, text=' ', command=setIfSpecial)
radio.grid()

specLab = Label(cspec, text='Contains special characters', font="Helvetica 18 bold")
specLab.grid(row=0, column=1)

genBtn = Button(cright, text='Generate', command=generate)
genBtn.grid()

# loop
tk.mainloop()
