
def create_inventory(lista):
    inv=dict()
    for valor in set(lista):
        mohoho= lista.count(valor)
        inv[valor]=mohoho
    return inv




def add_items(inventory, items):
    for element in items:
        if element in inventory:
            inventory[element] += 1
        else:
            inventory[element] = 1
    return inventory




def decrement_items(inventory, items):
    for element in items:
        if inventory[element] > 0:
           if element in inventory:
            inventory[element] -= 1
           else:
            inventory[element] = 1
        else:
            inventory[element] = 0
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
        return inventory
    else:
        return inventory

def list_inventory(inventory):
  goodsoup=[]
  for key,value in inventory.items():
     if value>0:
         yanose= (key,value)
         goodsoup.append(yanose)
  return goodsoup




   
