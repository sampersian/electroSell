import readInventory

#Create the cart dictionary
cart = {}

#Adds a certain number of a sku to the cart
def add(sku, n):
    if sku in cart:
        cart[sku] += 1
    else:
        cart.setdefault(sku, n)

#Deletes the sku from the cart
def remove(sku):
    del cart[sku]


from tkinter import *
#Creates the window that displays the users order and allows manipulation of the items
class OrderPage(Frame):
    def __init__(self, master, items):
        Frame.__init__(self, master)
        self.config(bg='black')
        #Creates the column title row for the order
        headers = Frame(self, bg='gray')
        h1 = Label(headers, text="SKU", height=1, width=6, bg='gray', font='Arial 11').pack(side=LEFT)
        h2 = Label(headers, text="Description", height=1, width=24, bg='gray', font='Arial 11', anchor=W).pack(
            side=LEFT)
        h3 = Label(headers, text="Price", height=1, width=5, bg='gray', font='Arial 11').pack(side=LEFT)
        h4 = Label(headers, text="Qty", height=1, width=3, bg='gray', font='Arial 11').pack(side=LEFT)
        #Holds the total price of all items on the order
        total = 0
        #Counts the total number of items in the order
        quantity = 0
        headers.pack(fill=X)
        #Displays each item in the order frame with several control buttons
        for item in items:
            item = readInventory.skuDict[item]
            total += (int(item.price) * items[item.sku])
            quantity += items[item.sku]
            table = Frame(self, bg='white')
            desc1 = Label(table, text=item.sku, fg='darkgreen', bg='gray15', height=1, width=6, font='Arial 11')
            desc1.pack(side=LEFT)
            desc2 = Label(table, text=item.cat + ":" + item.make, bg='gray15', fg='white', height=1, width=24,
                          font='Arial 11', anchor=W)
            desc2.pack(side=LEFT)
            desc3 = Label(table, text="$" + item.price, bg='gray15', fg='white', height=1, width=5, font='Arial 11', )
            desc3.pack(side=LEFT)
            desc4 = Label(table, text=items[item.sku], bg='gray15', fg='white', height=1, width=3, font='Arial 11', )
            desc4.pack(side=LEFT)
            #Shows the item profile for the item
            plate = Button(table, text="INFO", bg='orange', command=lambda sku=item.sku: self.showprofile(sku))
            plate.config(fg='black', font='Arial 12', height=1)
            plate.pack(side=RIGHT)
            #Reduces the quantity of this item in the order by 1 or deletes it if there's only one left, reloads window
            rem = Button(table, text="-1", bg='maroon', command=lambda sku=item.sku: self.down(sku))
            rem.config(fg='white', font='Arial 12', height=1)
            rem.pack(side=RIGHT)
            #Adds one more of this sku to the order, reloads window
            plus = Button(table, text="+1", bg='navy', command=lambda sku=item.sku: self.up(sku))
            plus.config(fg='white', font='Arial 12', height=1)
            plus.pack(side=RIGHT)
            table.pack(fill=X)
        #If the cart is empty the tell the user the list is empty
        if len(items) == 0:
            empty = Label(self, text="No Items Have Been Added.", height=1, font='Arial 12')
            empty.pack(fill=X)
        #Otherwise create a totals bar at the bottom totalling price and quantity
        else:
            totals = Frame(self, bg='gray')
            t1 = Label(totals, text="-", height=1, width=6, bg='gray', font='Arial 11')
            t1.pack(side=LEFT)
            t2 = Label(totals, text="Total", height=1, width=24, bg='gray', font='Arial 11', anchor=E)
            t2.pack(side=LEFT)
            t3 = Label(totals, text="$" + str(total), height=1, width=5, bg='gray', font='Arial 11')
            t3.pack(side=LEFT)
            t4 = Label(totals, text=str(quantity), height=1, width=3, bg='gray', font='Arial 11')
            t4.pack(side=LEFT)
            final = Button(totals, text='Submit', bg='black', fg='white', height=2, width=10, command=place)
            final.pack(side=RIGHT)
            totals.pack(fill=X)
        self.place(relx=0, rely=0, relheight=1, relwidth=1)
    #Shows item profile for the given sku
    def showprofile(self, sku):
        import profile
        profile.item_profile(sku)
    #Adds one more of this sku to the order, reloads window
    def up(self, sku):
        add(sku, 1)
        show()
    #Reduces the quantity of this item in the order by 1 or deletes it if there's only one left, reloads window
    def down(self, sku):
        if cart[sku] == 1:
            del cart[sku]
        else:
            cart[sku] -= 1
        show()

#Reloads the order window
def show():
    import app
    app.pageTitle.config(text="Order Summary")
    window = app.window
    OrderPage(window, cart)

#Places the order, updates inventory and clears the cart
def place():
    skus = []
    import inventory
    for c in cart:
        inventory.sell(int(c), int(cart[c]))
        for x in range(0, int(cart[c])):
            skus.append(c)
    cart.clear()
    record(skus)

#Records the order id and each sku in the order into the orders file
def record(order_list):
    orders_file = open("orders.csv", 'r+')
    lines = orders_file.readlines()
    order_id = str(1000 + len(lines))
    orders_file.write(order_id+",")
    for x in order_list:
        orders_file.write(str(x) + ",")
    orders_file.write("\n")
    orders_file.close()
    summary(order_id, order_list)

#Tell user their order id
def summary(order_id, order_list):
    total = 0
    import app
    for l in order_list:
        pr = app.skuDict[l]
        print(pr)
        total += int(pr.price)
    dow = Frame(app.window, bg='black')
    mes = Label(dow, text='Thank you for your order. Your order ID is: '+order_id, anchor=S)
    mes.pack(fill=BOTH)
    bill = Label(dow, text='Your total is: $'+str(total), anchor=S)
    bill.pack(fill=BOTH)
    dow.place(relx=0, rely=0, relheight=1, relwidth=1)

