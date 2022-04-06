from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)




password_letters=[random.choice(letters) for char in range(nr_letters)]

password_symbols=[random.choice(symbols) for char in range(nr_symbols)]

password_numbers=[random.choice(numbers) for char in range(nr_numbers)]

password_list = password_letters + password_symbols +password_numbers



random.shuffle(password_list)
print(password_list)
# password = ""
# for char in password_list:
#   password += char
password="".join(password_list)


# print(f"Your password is: {password}")


def generate():
    input_3.insert(0,password)
    pyperclip.copy(f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    a=input_1.get()
    b=input_2.get()
    c=input_3.get()
    new_dict={a:{
        "email":b,
        "password":c
    }}


    if len(a)==0 or len(b)==0:
        messagebox.showinfo(title="Bruh..",message="do not leave any fields")

    else:
        try:

            with open("spam.json", mode="r") as file:
                data=json.load(file)


        except (FileNotFoundError, json.decoder.JSONDecodeError):

            with open("spam.json", mode="w") as file:
                json.dump(new_dict,file,indent=4)
                # data.update(new_dict)

        else:
            data.update(new_dict)
            with open("spam.json", mode="w") as file:
                json.dump(data,file,indent=4)

        finally:

            input_1.delete(0, END)

            input_3.delete(0, END)






def new_var():
    website=input_1.get()
    try:
        with open("spam.json",mode="r")as file:
            load=json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Website", message=f"file does not exist")

    else:
        if website in load:
            email=load[website]["email"]
            password= load[website]["password"]
            messagebox.showinfo(title="Website", message=f"Email Id:{email}\nPassword:{password}")

        else:
            messagebox.showinfo(title="Website", message=f"Website does not exist")











# ---------------------------- UI SETUP ------------------------------- #


windows=Tk()
windows.config(padx=50,pady=50)
windows.title("Password generator")
image_1=PhotoImage(file="logo.png")

canvas=Canvas(width=200,height=200)
canvas.create_image(100,100,image=image_1)
canvas.grid(column=1,row=0)


label_1=Label(text="Website :")
label_1.grid(column=0,row=1,)



label_2=Label(text="Email/Username :")
label_2.grid(column=0,row=2)

label_3=Label(text="Password :")
label_3.grid(column=0,row=3)


input_1=Entry(width=17)
input_1.grid(column=1,row=1)
input_1.focus()


input_2=Entry(width=35)
input_2.grid(column=1,row=2,columnspan=2)
input_2.insert(0,"akashuhulekal@gmail.com")

input_3=Entry(width=17)
input_3.grid(column=1,row=3)

button_1=Button(text="Generate Password",command=generate)
button_1.grid(column=2,row=3)

button_2=Button(text="Add",width=36,command=save_password)
button_2.grid(column=1,row=4,columnspan=2)

button_3=Button(text="Find",command=new_var)
button_3.grid(column=2,row=1,)




windows.mainloop()