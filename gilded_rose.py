# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
    def normal_update(self, item):

        if item.sell_in < 0:
            if item.quality > 0:
                item.quality -= 2
            else:
                item.quailty = 0
 
        item.sell_in -= 1
        item.quality -=1

    def AgedBrie_update(self, item):
        item.sell_in -= 1
        item.quality +=1 
        if item.quality > 50:
            item.quality = 50

    def Sufuras_update(self, item):
        return

    def Concert_update(self, item):

        if item.sell_in > 0:
            if item.sell_in < 11:
                item.quality += 2

            elif item.sell_in < 6:
                item.quality += 3

            else:
                item.quality += 1
        else:
            item.quality = 0
        if item.quality > 50:
            item.quality = 50

        item.sell_in -= 1


    def Conjured_update(self, item):

        if item.sell_in < 0:
            if item.quality > 0:
                item.quality -= 4
            else:
                item.quailty = 0

        item.sell_in -= 1
        item.quality -=2

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.AgedBrie_update(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.Concert_update(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.Sufuras_update(item)
            elif item.name == "Conjured Mana Cake":
                self.Conjured_update(item)
            else: #Normal
                self.normal_update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)