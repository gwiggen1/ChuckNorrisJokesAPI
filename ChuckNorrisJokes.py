import requests
from tkinter import *
import customtkinter as ck

ck.set_appearance_mode('light')
ck.set_default_color_theme('green')

#From ChuckNorris.io (https://api.chucknorris.io/#!) API
#These Jokes are not my own I was just using this as practice using API

url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

#Use Your Key here
headers = {
	"accept": "application/json",
	"X-RapidAPI-Key": "cc51b5ab74msh13600e34d25d7dap19712bjsncc2e0e407899",
	"X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
}

#function for requesting joke
def new_joke():
	response = requests.request("GET",url,headers=headers)
	response1 = response.json()
	Joke = (response1['value'])
	lbl["text"] = Joke #Use tkinter to change text with less code

#Main Function
root = ck.CTk()
root.geometry("500x500")
root.title("Chuck Jokes")
root.resizable(height = "false", width= "false")

#Button
button = ck.CTkButton(root, text= "Tell Me Something Else", command = lambda: new_joke())
button.place(relx=.5,rely=.800,anchor=CENTER)
#Label
lbl = Label(root,font=("n",24),wraplength=450) #tkinter label used instead. lbl["text"] not available in customtkinter
lbl.place(relx=.5,rely=.360,anchor=CENTER)


root.mainloop()
