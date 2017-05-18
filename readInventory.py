# Reads in each line of inventory data
file = open(r'inventory.txt', 'rt')
lines = file.readlines()
file.close()


sets = []
catalog = {}
products = []
catDict = {}
skuDict = {}

#Formats the inventory into sets of data
for line in lines:
    item_array = line.strip().split("\t")
    sets.append(item_array)

#Classifies a set of data as a Product and sets certain variables
class Product:
    def __init__(self, data):
        self.sku = data[0]
        self.cat = data[1]
        self.sub = data[2]
        self.make = data[3]
        self.model = data[4]
        self.price = data[5]
        self.info = [self.cat, self.sub, self.make, self.model, self.price]

#Sorts inventory into a couple different objects
for item in sets:
    #Makes a Product object for each data set
    new = Product(item)
    #Adds a Product object of this data set to the list of products
    products.append(Product(item))
    #Adds a dictionary entry for this product info
    catalog.setdefault(new.sku, new.info)
    #Adds a dictionary entry for this object
    skuDict.setdefault(new.sku, new)

#Creates a dictionary that separates the products by category
for product in products:
    cat = product.cat
    if cat not in catDict:
        catDict.setdefault(cat, [product])
    else:
        catDict[cat].append(product)

#Creates a sorted list of the category names
category_list = sorted(catDict.keys())


