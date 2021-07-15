from tkinter import *
import time


# Форматувати вікно
root = Tk()
# Ставимо розмір і положення лівого кута вікна
root.geometry("1600x800+0+0")
# Заголовок вікна
root.title("Time to Dota 2")

# Змінна, яка буде використовуватися пізніше
text_Input = StringVar()
operator = ""

# У нас є рамка всередині вікна об'єкта root, ширина 1600 і висота 50
Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

# Ще один кадр 1200 х 700
f1 = Frame(root, width=1200, height=700, bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

# це отримує час
localtime = time.asctime(time.localtime(time.time()))
# Ось великий заголовок в ярлику
lblInfo = Label(Tops, font=('simplifica', 50, 'bold'), text="Time to Dota 2", fg="Steel Blue", bd=10, anchor='w')
# Це показує мітку і поміщає її в рядок 0, стовпець 0
lblInfo.grid(row=0, column=0)
# Це ще одна мітка для часу в рядку 1, в тому ж стовпці, що і до
lblInfo = Label(Tops, font=('simplifica', 20), text=localtime, fg="Steel Blue",
                bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

# Це поміщає цифру в змінну text_Input = StringVar (), яку ми бачили раніше
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

# Ця функція створює рамку і робить її видимою
def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="black")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

# Це конструктор для кожної кнопки калькулятора
# Коли ви викликаєте цю функцію, вона повертає кнопку
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj
# Це основне додаток для калькулятора
class app(Frame):
    def __init__(self):
       # Це створює рамку для калькулятора
        Frame.__init__(self)
        self.option_add("*Font", "arial 20 bold")
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Calculator")
       # Це змінна для отримання значення наступного об'єкта введення
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg='darkgray').pack(side=TOP, expand=YES, fill=BOTH)

        for clearBut in (["CE"], ["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(""))
       # Тут ми створюємо всі кнопки, передаючи
        for numBut in ("789/", "456*", "123-", "0.+"): # for each of this strings
            functionNum = iCalc(self, TOP) # this is the frame for each string of three symmbols
            for char in numBut: # for every number of symbol in each line ("789" for ex.)
               # Створюється кнопка
                button(functionNum, LEFT, char, lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))
        equalButton = iCalc(self, TOP)
        for iEqual in "=":
            if iEqual == "=":
                btniEqual = button(equalButton, LEFT, iEqual)
                btniEqual.bind("<ButtonRelease-1>", lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEqual = button(equalButton, LEFT, iEqual, lambda storeObj=display, s='%s' % iEqual: storeObj.set(storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


app().mainloop()
root.mainloop()