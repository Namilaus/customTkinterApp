import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("800x440")

app.title("Flight Searcher")

def button_function():
    print("button pressed")
def aboutUs():
    for things in app.winfo_children():
        things.destroy()
    div = customtkinter.CTkFrame(master=app,border_color="light_color",height=4000,width=580)
    div.place(relx=0.25, rely=0.001)
    text = """
        Flight searcher is a free source app, 
        which helps people to find the possible cheapest flight.
        You have just to gives information about the flight and the make a 
        research about flight every hour,
        if the flight price is cheaper than price you entered,
        you would receive a email about it with the information about flight.                 
         
    """
    div.label = customtkinter.CTkLabel(master=app, width=100, height=50,
                                   text=text,
                                   corner_radius=8,
                                fg_color="green")
    div.label.place(relx=0.28,rely=0.33)
    displayMainComponents()



def flightGui():
    for things in app.winfo_children():
        things.destroy()
    div = customtkinter.CTkFrame(master=app,border_color="light_color",height=4000,width=580)
    div.place(relx=0.25, rely=0.001)
    div.label = customtkinter.CTkLabel(master=app, width=100, height=50,
                                   text="hallo world bruh",
                                   bg_color="red",
                                   corner_radius=10000)
    div.label.pack(side="top", padx=30, pady=30)
    displayMainComponents()

def displayMainComponents():
    div = customtkinter.CTkFrame(master=app,border_color="blue",height=4000,width=170)
    div.place(relx=0.01,rely=0.001)

    div.button = customtkinter.CTkButton(master=app,text="about us",
                                     width=150,
                                     height=50,
                                     command=aboutUs)
    div.button.place(relx=0.02,rely=0.5)

    div.buttonMain = customtkinter.CTkButton(master=app,
                                         width=150,
                                         height=50,
                                         text="search flight",
                                         command=flightGui)
    div.buttonMain.place(relx=0.02,rely=0.35)

displayMainComponents()
app.mainloop()