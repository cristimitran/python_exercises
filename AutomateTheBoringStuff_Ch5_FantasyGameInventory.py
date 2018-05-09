inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inv, addedItems):
    for i in addedItems:
        for j in inv.copy():
            if i == j:
                inv[j] += 1
            else:
                inv.setdefault(i, 1)
    return inv

# or
# def addToInventory(inv, addedItems):
#     for i in addedItems:
#         inv.setdefault(i, 0)
#         inv[i] +=1
#     return inv


def displayInventory(stuff):
    print("Inventory:")
    item_total = 0
    for k, v in stuff.items():
        item_total += v
        print(str(v) + " " + str(k))
    print("Total number of items: " + str(item_total))


newInv = addToInventory(inv, dragonLoot)
displayInventory(newInv)
