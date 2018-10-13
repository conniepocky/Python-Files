from guizero import App, Text, TextBox, Slider, PushButton, Combo, Picture, CheckBox, ButtonGroup, info
def do_booking():
    info("Soda Sims", "Thank you for ordering using soda sims")
def change_text_size(slider_value):
    welcome_message.font_size(slider_value)
def say_my_name():
    welcome_message.set( my_name.get() )
app = App("Soda Sims")
welcome_message = Text(app, text="PLEASE TYPE YOUR NAME BELOW", size=15, font="Times New Roman", color="lightblue")
my_name = TextBox(app)
update_text = PushButton(app, command=say_my_name, text="Display my name")

text_size = Slider(app, command=change_text_size, start=10, end=80)

order_soda = Text(app, text="ORDER SODA BELOW", size=20, font="Times New Roman", color="lightblue")
film_choice = Combo(app, options=["Coca Cola", "Dr pepper", "Sprite"], grid=[0,1], align="left")
vip_seat = CheckBox(app, text="Bottle?", grid=[1,1], align="left")
row_choice = ButtonGroup(app, options=[ ["Quick Delivery?", "Q"], ["Meidium Delivery?", "M"],["Slow Delivery?", "S"] ],
selected="M", horizontal=True, grid=[2,1], align="left")
book_seats = PushButton(app, command=do_booking, text="Order", grid=[3,1], align="left")
soda = Picture(app, image="sodaGIFSIMS.gif")
app.display()
