import tkinter as tk
import customtkinter as ctk
import re

root = tk.Tk()
root.geometry('690x395')
root.title('Calculator')
root.resizable(False, False)


def display_input(_input):
    input_box.insert(index=tk.INSERT, string=_input)
    display_result()

def display_result():
    try:
        calculation = input_box.get()

        if re.search(pattern=r'[+\-\/\*\%]', string=calculation):
            result = eval(calculation)
            result_lb.config(text=f'={result}')
        
        else:
            result_lb.config(text="")

    except Exception as error:
        print(error)

def delete_input():
    index = input_box.index(tk.INSERT) - 1 
    input_box.delete(index)
    display_result()
    input_box.config(font=('Bold', 28))
    result_lb.config(font=('Bold', 17))

def clear_input():
    input_box.delete(0, tk.END)
    result_lb.config(text="")
    input_box.config(font=('Bold', 28))
    result_lb.config(font=('Bold', 17))

def toggle_theme():
    if root.cget('bg') == '#d9d9d9':
        root.tk_setPalette('black')
        input_box.config(bg='black')
        theme_btn.configure(text="⚫",text_color='white', fg_color= "black", hover_color='black')

    else:
        root.tk_setPalette('#d9d9d9')
        theme_btn.configure(text='⚫', text_color='black', fg_color='#d9d9d9', hover_color='#d9d9d9')

def show_result():
    input_box.config(font=('Bold', 16))
    result_lb.config(font=('Bold', 30))

input_box = tk.Entry(root, font=('Bold', 28),justify=tk.RIGHT, bd=0, bg='#d9d9d9')
input_box.place(x=15, y=10, width=660, height=70)

result_lb = tk.Label(root, font=('Bold', 17), fg='green', anchor=tk.E, bg='#d9d9d9')
result_lb.place(x=15, y=85, width=660, height=50)

#========
# ROW 1
#========

clearBtn = ctk.CTkButton(master=root, text='C', width=120, height=35, font=('Bold', 24), fg_color='#eac5d8', corner_radius=5, text_color='red', command=clear_input)
clearBtn.place(x=15, y= 145)

openBrcBtn = ctk.CTkButton(master=root, text='(', width=120, height=35, font=('Bold', 24), fg_color='#D1CCDC', corner_radius=5, text_color='#424C55', command=lambda: display_input(_input='('))
openBrcBtn.place(x=150, y= 145)

closeBrcBtn = ctk.CTkButton(master=root, text=')', width=120, height=35, font=('Bold', 24), fg_color='#D1CCDC', corner_radius=5, text_color='#424C55', command=lambda: display_input(_input=')'))
closeBrcBtn.place(x=285, y= 145)

perBtn = ctk.CTkButton(master=root, text='%', width=120, height=35, font=('Bold', 24), fg_color='#D1CCDC', corner_radius=5, text_color='#424C55', command=lambda: display_input(_input='%'))
perBtn.place(x=420, y= 145)

backBtn = ctk.CTkButton(master=root, text='<', width=120, height=35, font=('Bold', 24), fg_color='#eac5d8', corner_radius=5, text_color='red', command=delete_input)
backBtn.place(x=555, y= 145)

#========
# ROW 2
#========

sevenBtn = ctk.CTkButton(master=root, text='7', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='7'))
sevenBtn.place(x=15, y= 195)

eightBtn = ctk.CTkButton(master=root, text='8', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='8'))
eightBtn.place(x=150, y= 195)

nineBtn = ctk.CTkButton(master=root, text='9', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='9'))
nineBtn.place(x=285, y= 195)

divideBtn = ctk.CTkButton(master=root, text='÷', width=120, height=35, font=('Bold', 24), fg_color='#D1CCDC', corner_radius=5, text_color='#424C55', command=lambda: display_input(_input='/'))
divideBtn.place(x=420, y= 195)

rootBtn = ctk.CTkButton(master=root, text='√', width=120, height=35, font=('Bold', 24), fg_color='#D1CCDC', corner_radius=5, text_color='#424C55', command=lambda: display_input(_input='√'))
rootBtn.place(x=555, y= 195)


#========
# ROW 3
#========

fourBtn = ctk.CTkButton(master=root, text='4', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='4'))
fourBtn.place(x=15, y= 245)

fiveBtn = ctk.CTkButton(master=root, text='5', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='5'))
fiveBtn.place(x=150, y= 245)

sixBtn = ctk.CTkButton(master=root, text='6', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='6'))
sixBtn.place(x=285, y= 245)

multiplyBtn = ctk.CTkButton(master=root, text='×', width=120, height=35, font=('Bold', 24), fg_color='#D1CCDC', corner_radius=5, text_color='#424C55', command=lambda: display_input(_input='*'))
multiplyBtn.place(x=420, y= 245)

squareBtn = ctk.CTkButton(master=root, text='x²', width=120, height=35, font=('Bold', 24), fg_color='#D1CCDC', corner_radius=5, text_color='#424C55')
squareBtn.place(x=555, y= 245)


#========
# ROW 4
#========

oneBtn = ctk.CTkButton(master=root, text='1', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='1'))
oneBtn.place(x=15, y= 295)

twoBtn = ctk.CTkButton(master=root, text='2', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='2'))
twoBtn.place(x=150, y= 295)

threeBtn = ctk.CTkButton(master=root, text='3', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='3'))
threeBtn.place(x=285, y= 295)

minusBtn = ctk.CTkButton(master=root, text='-', width=120, height=35, font=('Bold', 24), fg_color='#D1CCDC', corner_radius=5, text_color='#424C55', command=lambda: display_input(_input='-'))
minusBtn.place(x=420, y= 295)

equalsBtn = ctk.CTkButton(master=root, text='=', width=120, height=95, font=('Bold', 24), fg_color='#ffa62b', corner_radius=5, text_color='white', command=show_result)
equalsBtn.place(x=555, y= 295)


#========
# ROW 5
#========

twoZeroBtn = ctk.CTkButton(master=root, text='00', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='00'))
twoZeroBtn.place(x=15, y= 345)

zeroBtn = ctk.CTkButton(master=root, text='0', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='0'))
zeroBtn.place(x=150, y= 345)

dotBtn = ctk.CTkButton(master=root, text='.', width=120, height=35, font=('Bold', 24), fg_color='#82c0cc', corner_radius=5, text_color='black', command=lambda: display_input(_input='.'))
dotBtn.place(x=285, y= 345)

plusBtn = ctk.CTkButton(master=root, text='+', width=120, height=35, font=('Bold', 24), fg_color='#D1CCDC', corner_radius=5, text_color='#424C55', command=lambda: display_input(_input='+'))
plusBtn.place(x=420, y= 345)


theme_btn = ctk.CTkButton(root, text='⚫',font=('Bold',40), width=35, height=35, fg_color="#d9d9d9", text_color='black', hover_color='#d9d9d9', command=toggle_theme)
theme_btn.place(x=0, y=-10)


root.mainloop(), 