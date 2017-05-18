#List of all typesets
typesets = []

#Load all data types for all item values
def loadTypes():
    typefile = open(r'dataTypes.txt', 'rt')
    lines = typefile.readlines()
    typefile.close()
    for line in lines:
        nice = line.strip().split('\t')
        typesets.append(nice)
        continue

#Get the data type of specific items
def fetchTypes(raw):
    loadTypes()
    cat = raw[0]
    sub = raw[1]
    #Search for the typeset using category and subcategory to filter
    for typeset in typesets:
        if typeset[0] == cat:
            if typeset[1] == sub:
                maketype = typeset[2]
                modeltype = typeset[3]
                moneytype = typeset[4]
                return maketype, modeltype, moneytype
            else:
                continue
        else:
            continue
    return


#Provides details
class Details:
    def __init__(self, sku, values, types):
        self.sku = sku
        self.values = values
        self.cat = values[0]
        self.sub = values[1]
        self.make = values[2]
        self.model = values[3]
        self.price = values[4]
        self.labels = types
        self.maketype = types[0]
        self.modeltype = types[1]
        self.currencytype = types[2]



