# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        
    def update_quality(self):

        for item in self.items:
            #my_item = Normal(item)

            if item.name == "Aged Brie":
                my_item = AgedBrie(item) 
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                my_item = Concert(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                my_item = Sulfuras(item)
            elif item.name == "Conjured Mana Cake":
                my_item = Conjured(item)
            else: #Normal
                my_item = Normal(item)


            my_item.virtual_update()
        

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def virtual_update(self):
        pass

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Normal(Item):
    
    def __init__(self, item):
        self.item = item
    
    
    def virtual_update(self):
        if self.item.sell_in < 0:
            if self.item.quality > 0:
                self.item.quality -= 2
            else:
                self.item.quailty = 0
        
        self.item.sell_in -= 1
        self.item.quality -=1         


class AgedBrie(Item):

    def __init__(self, item):
        self.item = item

    def virtual_update(self):
        self.item.sell_in -= 1
        self.item.quality +=1 
        if self.item.quality > 50:
            self.item.quality = 50

class Concert(Item):
    
    def __init__(self, item):
        self.item = item    

    def virtual_update(self):
        if self.item.sell_in > 0:
            if self.item.sell_in < 11:
                self.item.quality += 2
        
            elif self.item.sell_in < 6:
                self.item.quality += 3
            
            else:
                self.item.quality += 1
        else:
            self.item.quality = 0
        if self.item.quality > 50:
            self.item.quality = 50

        self.item.sell_in -= 1      

class Sulfuras(Item):

    def __init__(self, item):
        self.item = item

    def virtual_update(self):
        return

class Conjured(Item):

    def __init__(self, item):
        self.item = item

    def virtual_update(self):
        if self.item.sell_in < 0:
            if self.item.quality > 0:
                self.item.quality -= 4
            else:
                self.item.quailty = 0
        
        self.item.sell_in -= 1
        self.item.quality -=2  

