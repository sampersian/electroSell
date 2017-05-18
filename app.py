#Import the things ill need to design the app
from tkinter import *
from readInventory import *

# Make Root Window
root = Tk()
root.overrideredirect(0)
root.title("Order Application")
root.geometry("1300x800")
root.configure(bg='black')
root.resizable(width=False, height=False)

#App Title Bar
banner = Frame(root, bg='gray')
banner_label = Label(banner, text="   Retail Catalog", fg='black', bg='#3399FF',
                     anchor=W, font="Arial 14 bold")

#This is where the category buttons go
button_bin = Frame(root)
equal = 1 / len(category_list)

#This is the whole middle window that changes when categories are opened, or the order is shown
main_page = Canvas(root, bg='black', highlightthickness=0)
pageTitle = Label(main_page, text="Select a Category", font="arial 16", bg='black', fg='white', anchor=S)
window = Frame(main_page, bg='black')
window.place(relx=0.025, rely=0.06, relwidth=0.95, relheight=0.9)

#Right Vertical Container
hub = Frame(root, bg='black')
#This is where product info, sku search go
board = Canvas(hub, bg='gray15', highlightthickness=0)
#This is where the main buttons will go
navpanel = Canvas(hub, bg='black', highlightthickness=0)

#Display the order page
def order():
    import order
    order.show()

#Search for a SKU (in board)
def sku_search():
    def findit():
        #Grabs whatever is in the entry box
        sku = qry.get()
        import profile
        #Checks if it could make a profile for the users entry
        try:
            #Opens the items profile if it can make it
            profile.item_profile(sku)
        #Displays an error message if the sku does not exist, clears the entry box
        except KeyError:
            Label(search_frame, text="Invalid SKU", bg='black', fg='red')\
                .place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.1)
            qry.delete(0, END)
        except ValueError:
            Label(search_frame, text="Invalid SKU", bg='black', fg='red')\
                .place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.1)
            qry.delete(0, END)
    #Builds the frame that will hold the search widgets, also builds the widgets
    search_frame = Frame(board, bg='black')
    direct = Label(search_frame, text="Enter SKU:", bg='black', fg='white', font='Arial 14 bold', anchor=E)
    direct.place(relx=0, rely=0.4, relwidth=0.4, relheight=0.1)
    qry = Entry(search_frame, bg='gray')
    qry.place(relx=0.4, rely=0.4, relwidth=0.3, relheight=0.1)
    #This triggers the search for a sku in the entire inventory
    submit = Button(search_frame, text='Search', bg='navy', fg='white',
                    command=findit)
    submit.place(relx=0.7, rely=0.4, relwidth=0.2, relheight=0.1)
    #Fills the board window with the search frame
    search_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

#Makes the button that displays the user's order when clicked
nav1 = Button(navpanel, bg='#00cc33', text='Show Order', font="arial 18", command=order)
#Makes the button that opens the sku search in the board window when clicked
nav2 = Button(navpanel, bg='#00ccff', text='SKU Search', font="arial 18", command=sku_search)
#Makes the button that quits the program when pressed
nav3 = Button(navpanel, bg='#cc6666', text='Close', font="arial 18", command=root.destroy)



#Adds the button that opens a category
class Category:
    name = None
    index = None
    items = None

    def __init__(self, name):
        self.name = name
        self.data = catDict[name]
        self.index = category_list.index(name)
        Control(self)

#Creates the button that opens the category's page when clicked
class Control(Button):
    def __init__(self, parent):
        Button.__init__(self, button_bin, text=parent.name, fg='white', bg='#660000', command=self.jump,
                        font='arial 12 bold')
        self.boss = parent
        self.place(relx=0, rely=equal * category_list.index(parent.name), relwidth=1, relheight=equal)
    #Shows the page in the main window
    def jump(self):
        pageTitle.config(text=self.boss.name)
        window.configure(bg='gray15')
        import page
        page.show_page(self.boss.data)

#Adds a button for every category in the entire inventory
for category in category_list:
    Category(category)


#Configures everything inside the root window
banner.place(rely=0, relwidth=1, relheight=0.04)
banner_label.place(rely=0, relx=0, relheight=1, relwidth=1)
button_bin.place(rely=0.04, relx=0, relwidth=0.2, relheight=0.96)
main_page.place(rely=0.04, relx=0.2, relwidth=0.45, relheight=0.96)
pageTitle.place(relx=0, rely=0, relwidth=1, relheight=0.06)
board.place(relx=0.01, rely=0.06, relwidth=0.95, relheight=0.5)
navpanel.place(relx=0.01, rely=0.6, relwidth=0.95, relheight=0.32)
nav1.place(relx=0.0, rely=0.0, relheight=0.25, relwidth=1)
nav2.place(relx=0.0, rely=0.25, relheight=0.25, relwidth=1)
nav3.place(relx=0.0, rely=0.75, relheight=0.25, relwidth=1)
hub.place(rely=0.04, relx=0.65, relwidth=0.35, relheight=0.96)

#Displays the root window on the screen
def launch():
    root.mainloop()


#launch()