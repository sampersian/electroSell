#Import GUI Toolkit
from tkinter import *

#Contructs a products data into a window that is shown to the user
class Profile(Frame):
    def __init__(self, master, data, data_types, count):
        Frame.__init__(self, master, bg='gray16', bd='5')
        self.makeName = str(data.make)
        print(data)
        self.title = Label(self,
                           bd=0,
                           text="Product Info",
                           relief=SUNKEN,
                           fg='orange',
                           bg='gray16',
                           font='Arial 18 bold',
                           padx=5)
        self.title.place(relx=0,
                         rely=0.05,
                         relwidth=1,
                         relheight=0.1)

        self.maketype = Label(self,
                              bd=0,
                              text=data_types[0]+":",
                              relief=SUNKEN,
                              bg='white',
                              fg='navy',
                              font='arial 12',
                              padx=0,
                              anchor=E)
        self.maketype.place(relx=0,
                            rely=0.2,
                            relwidth=0.28,
                            relheight=0.1)
        self.make = Label(self,
                          bd=0,
                          text=data.make,
                          relief=SUNKEN,
                          bg='white',
                          fg='navy',
                          font='arial 12',
                          padx=5,
                          anchor=W)
        self.make.place(relx=0.28,
                        rely=0.2,
                        relwidth=0.72,
                        relheight=0.1)

        self.modeltype = Label(self,
                               bd=0,
                               text=data_types[1]+":",
                               relief=SUNKEN,
                               bg='white',
                               fg='navy',
                               font='arial 12',
                               padx=0,
                               anchor=E)
        self.modeltype.place(relx=0,
                             rely=0.3,
                             relwidth=0.28,
                             relheight=0.1)
        self.model = Label(self,
                           bd=0,
                           text=data.model,
                           relief=SUNKEN,
                           bg='white',
                           fg='navy',
                           font='arial 12',
                           padx=5,
                           anchor=W)
        self.model.place(relx=0.28,
                         rely=0.3,
                         relwidth=0.72,
                         relheight=0.1)

        self.subtype = Label(self,
                             bd=0,
                             text="Type:",
                             relief=SUNKEN,
                             bg='white',
                             fg='navy',
                             font='arial 12',
                             padx=0,
                             anchor=E)
        self.subtype.place(relx=0,
                           rely=0.4,
                           relwidth=0.28,
                           relheight=0.1)
        self.sub = Label(self,
                         bd=0,
                         text=data.sub,
                         relief=SUNKEN,
                         bg='white',
                         fg='navy',
                         font='arial 12',
                         padx=5,
                         anchor=W)
        self.sub.place(relx=0.28,
                       rely=0.4,
                       relwidth=0.72,
                       relheight=0.1)

        self.pricetype= Label(self,
                              bd=0,
                              text="Price:",
                              relief=SUNKEN,
                              bg='white',
                              fg='navy',
                              font='arial 12',
                              padx=0,
                              anchor=E)
        self.pricetype.place(relx=0,
                             rely=0.5,
                             relwidth=0.28,
                             relheight=0.1)
        self.price= Label(self,
                          bd=0,
                          text=data_types[2]+data.price,
                          relief=SUNKEN,
                          bg='white',
                          fg='navy',
                          font='arial 12',
                          padx=5,
                          anchor=W)
        self.price.place(relx=0.28,
                         rely=0.5,
                         relwidth=0.72,
                         relheight=0.1)

        self.sku_label= Label(self,
                              bd=0,
                              text="SKU:",
                              relief=SUNKEN,
                              bg='white', fg='navy',
                              font='arial 12',
                              padx=0,
                              anchor=E)
        self.sku_label.place(relx=0,
                             rely=0.6,
                             relwidth=0.28,
                             relheight=0.1)
        self.sku= Label(self,
                        bd=0,
                        text=data.sku,
                        relief=SUNKEN,
                        bg='white',
                        fg='navy',
                        font='arial 12',
                        padx=5,
                        anchor=W)
        self.sku.place(relx=0.28,
                       rely=0.6,
                       relwidth=0.72,
                       relheight=0.1)

        self.qty_label= Label(self,
                              bd=0,
                              text="Quantity:",
                              relief=SUNKEN,
                              bg='white',
                              fg='navy',
                              font='arial 12',
                              padx=0,
                              anchor=E)
        self.qty_label.place(relx=0,
                             rely=0.7,
                             relwidth=0.28,
                             relheight=0.1)
        self.qty= Label(self,
                        bd=0,
                        text=count,
                        relief=SUNKEN,
                        bg='white',
                        fg='navy',
                        font='arial 12',
                        padx=5,
                        anchor=W)
        self.qty.place(relx=0.28,
                       rely=0.7,
                       relwidth=0.72,
                       relheight=0.1)

        self.add = Button(self,
                          text="Add to Order",
                          bg='green',
                          command=lambda sku=data.sku: self.add_item(sku))
        self.add.config(fg='white',
                        font='Arial 12 bold')
        self.add.place(relx=0.2,
                       rely=0.85,
                       relwidth=0.6,
                       relheight=0.1)

        self.place(relx=0,
                   rely=0,
                   relheight=1,
                   relwidth=1)
    #Adds one of this specific sku to the order
    def add_item(self, sku):
        import order
        order.add(sku, 1)
#Creates the profile for a specific sku
def item_profile(sku):
    import book
    item = book.skuDict[sku]
    window = book.board
    count = book.counts[int(sku)]
    data_types = book.typeDict[sku]
    Profile(window, item, data_types, count)


