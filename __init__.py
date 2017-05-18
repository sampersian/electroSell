'''
Sam Persian
CS 1411
11/20/2014

Description:
An electronic ordering program with with a GUI allowing the user to browse inventory, view product information and
submit a custom order.

Given:
-Text file containing inventory data: 'inventory.txt'
-Text file containing data types: 'dataTypes.txt'
-Text file containing inventory counts: 'counts.txt'
-CSV file containing past orders: 'orders.csv'

Analysis:
    Input: An inventory of items
    Input: Items Chosen from the inventory
    Output: An order containing items from the inventory
    Output: An updated 'counts.txt' file
    Output: A summary that shows the order number and total cost

Method:
#Reads in each line of inventory data
#Creates several objects from the lines of inventory data
#Load the gui toolkit
#Make Root Window
#Adds a button for every category in the entire inventory
#Configures everything inside the root window
#Displays the root window on the screen
#Allows the user to indefinitely:
    #Open pages of any category
    #See the profile of any item
    #Create/Manage an order of items
    #Search for an item by its sku
    #Submit Orders
#When orders are submitted:
    #Inventory counts are updated
    #Order id and each product sku are recorded to a line in the orders file
    #User is presented with their order id and total cost
    #The order is cleared and ready for new items


Test Case 1:
1. Run this module in the python shell
2. Click 'Audio' Category
>Audio Page is loaded with it's items
3. Click on 'INFO' Button in "Headphones Beats by Dre - Executive" Row
> Product profile for item in step 3 is shown in window titled "Product Info" Note: Quantity: 145, Price:299
4. Click on "Add to Order" in profile window
5. Click on 'Furniture' Category
>Furniture Page is loaded with it's items
6. Click on 'INFO' Button in "Office Serta - Executive Chair" Row
> Product profile for item in step 6 is shown in window titled "Product Info" Note: Price: 199
7. Click on "Add to Order" in profile window
8. Click on Show Order
> Order is displayed and both items I added to order are displayed. Note: Total $: 498, Total Quantity: 2
9. Click on "Submit"
> 'counts.txt' File is updated
> Line is added to csv file for order
> Order summary is shows.  Note: Order ID = 1006, Total=$498
10. Click 'Audio' Category
>Audio Page is loaded with it's items
11. Click on 'INFO' Button in "Headphones Beats by Dre - Executive" Row
> Product profile for item in step 10 is shown in window titled "Product Info" Note: Quantity: 144, Price:299
12. Click on 'Close'
> GUI closes, program ends.

Test Case 2:
1. Run this module in the python shell
2. Click 'Cameras' Category
>Cameras Page is loaded with it's items
3. Click on 'INFO' Button in "Photo Nikon - D3200" Row
> Product profile for item in step 3 is shown in window titled "Product Info" Note: Price=$500, SKU=420958
4. Click on "Add to Order" in profile window
5. Click on 'Media' Category
>Media Page is loaded with it's items
6. Click on 'INFO' Button in "Movie Miracle - Action" Row
> Product profile for item in step 6 is shown in window titled "Product Info" Note: Price= $12, SKU=420938, QTY=17
7. Click on "Add to Order" in profile window
8. Click on Show Order
> Order is displayed and both items I added to order are displayed. Note: Total $: 512, Total Quantity: 2
9. Click on "+" Button in "Media:Miracle" Row
> Quantity for "Media:Miracle" instantly changes to 2
> Total Price is updated to $524, Total Quantity is now 3
10. Click on "-" Button in "Cameras:Nikon" Row
> "Cameras:Nikon" Row Disappears
> Total Price is updated to $24, Total Quantity is now 2
10. Click on "-" Button in "Media:Miracle" Row
> "Media:Miracle" Row Quantity is now 1
> Total Price is updated to $12, Total Quantity is now 1
11. Click on "Submit"
> 'counts.txt' File is updated
> Line is added to csv file for order
> Order summary is shows.  Note: Order ID = 1007, Total=$12
12. Click on 'Close'
> GUI closes, program ends.

Test Case 3:
1. Run this module in the python shell
2. Click 'SKU Search' Category
>SKU Search window appears in window above "show order" button
3. Enter '999' in Entry box in search window
4. Click "Search" Button
> Message "Invalid SKU" appears, entry box empties itself
5. Enter '420938' in Entry Box
6. Click "Search Button"
> Product profile for the Media item "Miracle" is displayed Note: QTY = 16, SKU=420938
7. Click on 'Close'
> GUI closes, program ends.

Test Case 4:
1. Run this module in the python shell
2. Click on "Show Order"
> "Order Summary" Window appears with the message "No Items Have Been Added"
3. Click "SKU Search"
> SKU Search window appears in window above "show order" button
4. Enter "420955" in Entry Box
5. Click "Search"
> Product profile for "Apple ipad mini" is displayed.  Note: SKU:420955
6. Click "Add to Order"
> Nothing happens to the Order Summary Window
7. Click "Show Order"
> Order Summary window is updated to have the item "Tablets:Apple" with a QTY of 1
> Total Price is now $400, Total Quantity is now 1
8. Click "-" Button in "Tablets:Apple" row
> Order Summary window is updated and now has 0 items and displays the message "No Items Have Been Added"
9. Click "Close"
>GUI closes, program ends.
'''


#Open the GUI
import app
app.launch()
