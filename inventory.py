#Loads the inventory count data
countFile = 'counts.txt'
file = open(countFile,'rt')
lines = file.readlines()
file.close()

#Dictionary for counts by sku
counts = {}

loaded = False
#Load sku inventory counts into a dictionary
def load():
    for line in lines:
        raw = line.strip().split('\t')
        what = int(raw[0])
        amount = int(raw[1])
        counts.setdefault(what, amount)

if loaded is False:
    load()
    loaded = True

#Records updated inventory values into the counts file
def record(counts):
    fresh = open(countFile, 'w')
    for count in counts:
        line = str(count)+"\t"+str(counts[count])+"\n"
        fresh.write(line)
    fresh.close()

#Reduce the qty of an item and update inventory
def sell(sku, qty):
    was = counts[sku]
    now = int(was) - int(qty)
    counts[sku] = now
    record(counts)

#Increase the qty of an item and update inventory
def buy(sku, qty):
    was = counts[sku]
    now = int(was) + int(qty)
    counts[sku] = now
    record(counts)

#Get an inventory count for a specific SKU
def search(sku):
    return(counts[sku])
