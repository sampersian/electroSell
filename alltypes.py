import readInventory
import details

#Save the dictionary of data types for each sku
typeDict = {}

#Adds each products data type to a dictionary with its sku as the key
for product in readInventory.products:
    types = details.fetchTypes(product.info)
    sku = product.sku
    typeDict.setdefault(sku, types)
