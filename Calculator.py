import customtkinter as ctk
import os, sys




numbers = [0,1,2,3,4,5,6,7,8,9]
signs = ["+", "-", "x", "/", "(", ")"]



#All this Function does is find the icon
# def resource_path(relative_path):
#     if hasattr(sys, "_MEIPASS"):
#         return os.path.join(sys._MEIPASS, relative_path)
#     return os.path.join(os.path.abspath("."), relative_path)


#   Defining important functions

#       Conversion functions: Basically turns a string to a number or float. Pretty simple
def convert(str):
    if "." in str:
        try:
            str = float(str)
            return str
        except:
            print("Syntax error, this can't be a float")
            return str
    else:
        try:
            str = int(str)
            return str
        except:
            print("SYNTAX ERROR: ", str)
            return str
        

#   This function is the heart of the code.
# It takes a string(equation) as input and converts it to an array containing the individual elements of the equation
def toArr(st):
    #Local variables used in the function
    brackets = []
    tmpValue = ''
    eq=[]
    counter=0

    #Loops through a given string
    i = 0
    while i < len(st):
        l = st[i]
        #Checks if "l" is a sign
        if l in signs:
            #This handles parantheses
            if l == "(":
                brackets.append(i)
                if tmpValue != '' and len(brackets) == 1:
                    eq.append(tmpValue)
                    eq.append("x")
                    tmpValue = ''
                counter+=1
                #starts a sub loop that basically extracts everything inside brackets and solves that first
                for j in range(i+1, len(st)):
                    k = st[j]
                    #For handling nested brackets
                    if k == "(":
                        counter+=1
                    elif k == ")":
                        counter-=1 #This line just makes sure we close at the right bracket
                        if counter == 0:
                            #Extracts string within a bracket and solves it
                            bracketString = st[brackets[0]+1: j]
                            tmpValue += toArr(bracketString)
                            i=j
                            brackets=[]
                            #Checks the next char in the string
                            try:
                                newTmp = st[i+1]
                                #If next char is a number or bracket - Put a "x" between them
                                if newTmp not in signs or newTmp == "(":
                                    eq.append(tmpValue)
                                    tmpValue=''
                                    eq.append('x')
                            #If there isn't it breaks the main loop and sends the array to the solve function
                            except:
                                eq.append(tmpValue)
                                i+=1
                                return solve(eq)
                            #Just breaks the sub -loop when a bracket is closed
                            break
                        #Checks if all brackets are closed
                    if j == len(st)-1 and counter>0:
                        bracketString = st[brackets[0]+1:]
                        print(bracketString)
                        eq.append(toArr(bracketString))
                        return solve(eq)

            #################################
            #This section handles every other sign
            elif l != "-" and tmpValue == "":
                print("SYNTAX ERROR")
                return None
            elif l == '-' and tmpValue == "":
                tmpValue += l
            else:
                if tmpValue != "":
                    eq.append(tmpValue)
                tmpValue = ""
                eq.append(l)
            #################################
        else:
            tmpValue += l
        if i == len(st) - 1 and tmpValue != "":
            eq.append(tmpValue)
            # print("Final append of tmpValue:", tmpValue, 'eq after append:', eq)
        i += 1 
    res = str(solve(eq))
    return res



#       Looping solve function to handle multiple equations in using BODMAS

def solve(arr):
    print(arr)
    if len(arr) % 2 == 0:
        print("This can't work:", arr)
        return
    elif len(arr) == 1:
        return arr[0]
    else:
        if "/" in arr:
            return divide(arr, arr.index('/'))
        elif "x" in arr:
            return multiply(arr, arr.index("x"))
        elif "-" in arr:
            return subtract(arr, arr.index("-"))
        elif "+" in arr:
            return add(arr, arr.index("+"))
                

#Operational Functions                

#   Dividing function
def divide(arr, index):
    if index == 0 or index == len(arr)-1:
        print(f"SYNTAX ERROR - Look at the equation and tell me what's wrong: {' '.join(arr)}")
        return
    else:
        in1 = index-1
        in2 = index+1
        in3 = index
        if arr[in1] in signs or arr[in2] in signs:
            print(f"SYNTAX ERROR - Look at the equation and tell me what's wrong: {' '.join(arr)}")
            return
        else:
            num1 = convert(arr[in1])
            num2 = convert(arr[in2])
            if num2 != 0:
                res =  num1/num2
                arr.pop(in1)
                arr.pop(in1)
                arr.pop(in1)
                if int(res) == res:
                    res = int(res)
                res = str(res)
                arr.insert(in1, res)
                return solve(arr)
            else:
                print("You can't divide by 0: INFINITY ERROR")

#   Multiplying function
def multiply(arr, index):
    if index == 0 or index == len(arr)-1:
        print(f"SYNTAX ERROR - Look at the equation and tell me what's wrong: {' '.join(arr)}")
        return
    else:
        in1 = index-1
        in2 = index+1
        in3 = index
        if arr[in1] in signs or arr[in2] in signs:
            print(f"SYNTAX ERROR - Look at the equation and tell me what's wrong: {' '.join(arr)}")
            return
        else:
            num1 = convert(arr[in1])
            num2 = convert(arr[in2])
            res =  num1*num2
            res = str(res)
            arr.pop(in1)
            arr.pop(in1)
            arr.pop(in1)
            arr.insert(in1, res)
            return solve(arr)
        
#   Subtracting function
def subtract(arr, index):
    if index == 0 or index == len(arr)-1:
        print(f"SYNTAX ERROR - Look at the equation and tell me what's wrong: {' '.join(arr)}")
        return
    else:
        in1 = index-1
        in2 = index+1
        in3 = index
        if arr[in1] in signs or arr[in2] in signs:
            print(f"SYNTAX ERROR - Look at the equation and tell me what's wrong: {' '.join(arr)}")
            return
        else:
            num1 = convert(arr[in1])
            num2 = convert(arr[in2])
            res =  num1-num2
            res = str(res)
            arr.pop(in1)
            arr.pop(in1)
            arr.pop(in1)
            arr.insert(in1, res)
            return solve(arr)
    

#Addition function
def add(arr, index):
    if index == 0 or index == len(arr)-1:
        print(f"SYNTAX ERROR - Look at the equation and tell me what's wrong: {' '.join(arr)}")
        return
    else:
        in1 = index-1
        in2 = index+1
        in3 = index
        if arr[in1] in signs or arr[in2] in signs:
            print(f"SYNTAX ERROR - Look at the equation and tell me what's wrong: {' '.join(arr)}")
            return
        else:
            num1 = convert(arr[in1])
            num2 = convert(arr[in2])
            res =  num1+num2
            res = str(res)
            arr.pop(in1)
            arr.pop(in1)
            arr.pop(in1)
            arr.insert(in1, res)
            return solve(arr)
    

            
# Custom tkinter settings
btn_text = ["DEL", "C", "(", ")", 
            "7", "8", "9", "/",
            "4", "5", "6", "x",
            "1", "2", "3", "-",
            "0", ".", "=", "+"]
button_grid = []


#   Main frame
calculator = ctk.CTk()
calculator.title("Calculator")
calculator.geometry("250x430")
calculator.maxsize(250, 430)
calculator.minsize(186.5,322.5)
calculator.grid_rowconfigure(0, weight=1)
calculator.grid_rowconfigure(1, weight=10)
calculator.grid_columnconfigure(0, weight=1)
# icon_path = resource_path("favicon.ico")
# calculator.iconbitmap(icon_path)

# Display frame
display = ctk.CTkFrame(master=calculator, fg_color='white')
display.grid(row=0, column=0, sticky='nsew', pady=5)

# Display labels
display_label = ctk.CTkLabel(master=display, text="", text_color="black", fg_color='white', font=ctk.CTkFont(size=40), anchor='e')
display_label.pack(fill='both', expand=True, padx=10, pady=10)

#Input frame
input = ctk.CTkFrame(master=calculator)
input.grid(row=1, column=0, sticky='nsew')
input.grid_rowconfigure((0,1,2,3,4), weight=1)
input.grid_columnconfigure((0,1,2,3), weight=1)


#  Making buttons
def button_click(text):
    if text == "C":
        display_label.configure(text="")
    elif text == "DEL":
        current_text = display_label.cget("text")
        new_text = current_text[:-1]
        display_label.configure(text=new_text)
    elif text == "=":
        equation = display_label.cget("text")
        result = toArr(equation)
        display_label.configure(text=result)
    else:
        current_text = display_label.cget("text")
        new_text = current_text + text
        display_label.configure(text=new_text)
for i in range(5):
    row = []
    for j in range(4):
        btn = ctk.CTkButton(master=input, text=btn_text[i*4+j], command=lambda text=btn_text[i*4+j]: button_click(text))
        btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
        row.append(btn)
    button_grid.append(row)


calculator.mainloop()