#Import the GUI toolkit
from tkinter import *

#Creates the page of items for a specific class
class Page(Frame):
    def __init__(self, master, items):
        Frame.__init__(self, master)
        self.config(bg='black')
        for item in items:
            table = Frame(self, bg='gray15')
            desc1 = Label(table, text=item.sub, bg='gray', fg='navy', height=1, font='Arial 12')
            desc1.pack(side=LEFT)
            desc = Label(table, text=" "+item.make+" - "+item.model, bg='gray15', fg='white', height=1, font='Arial 11')
            desc.pack(side=LEFT)
            plate = Button(table, text="INFO", bg='orange', command=lambda sku=item.sku: self.showprofile(sku))
            plate.config(fg='black', font='Arial 12', height=2)
            plate.pack(side=RIGHT)
            table.pack(fill=X)
        self.place(relx=0, rely=0, relheight=1, relwidth=1)
    #Shows the profile for the given sku
    def showprofile(self, sku):
        import profile
        profile.item_profile(sku)

#Displays the page for the specified category
def show_page(cat):
    import app
    window = app.window
    Page(window, cat)