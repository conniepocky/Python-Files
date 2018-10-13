from guizero import *
#create window
app = App(title="Cv Search")
name = Text(app, text="Cv Search", size=40, font="Times New Roman", color="lightgreen")
cv = TextBox(app, width=50)
def search():
    if cv == "fff":
       name.set("noice")
    else:
        name.set()
        print(cv)
cvSearch = PushButton(app, command=search, text="Search")
app.display()
