import customtkinter as ctk
numbers = [0,1,2,3,4,5,6,7,8,9]
signs = ["+", "-", "x", "/", "(", ")"]
#   Defining important functions

#       Conversion functions
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
        

#   Converting String to array
def extract(st):
    brackets = []
    tmpValue = ''
    eq=[]
    counter=0

    i = 0
    while i < len(st):
        l = st[i]
        if l in signs:
            if l == "(":
                brackets.append(i)
                if tmpValue != '' and len(brackets) == 1:
                    eq.append(tmpValue)
                    eq.append("x")
                    tmpValue = ''
                counter+=1
                for j in range(i+1, len(st)):
                    k = st[j]
                    if k == "(":
                        counter+=1
                    elif k == ")":
                        counter-=1
                        if counter == 0:
                            bracketString = st[brackets[0]+1: j]
                            tmpValue += extract(bracketString)
                            i=j
                            brackets=[]
                            try:
                                newTmp = st[i+1]
                                if newTmp not in signs or newTmp == "(":
                                    eq.append(tmpValue)
                                    tmpValue=''
                                    eq.append('x')
                            except:
                                eq.append(tmpValue)
                                i+=1
                                return solve(eq)
                            break
                        if j == len(st)-1 and counter>0:
                            print("SYNTAX ERROR: No closing bracket found")
                            return "ERROR"

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
    if len(arr) % 2 == 0:
        print("This can't work:", arr)
        return
    elif len(arr) == 1:
        return convert(arr[0])
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
                res = str(res)
                arr.pop(in1)
                arr.pop(in1)
                arr.pop(in1)
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
        result = extract(equation)
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