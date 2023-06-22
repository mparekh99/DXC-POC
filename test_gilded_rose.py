# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)

    def test_normal_item_normal(self):
        items = [Item("+5 Dexterity Vest", 10, 20),
                 Item("Elixir of the Mongoose", 5, 7)]
        gilded_rose = GildedRose(items)

        days = 2
        for day in range(days):

            gilded_rose.update_quality()

        #Vest
        self.assertEqual(8, items[0].sell_in)
        self.assertEqual(18, items[0].quality)
        #Elixir
        self.assertEqual(3, items[1].sell_in)
        self.assertEqual(5, items[1].quality)

    def test_normal_item_expired(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)

        days = 12
        for day in range(days):

            gilded_rose.update_quality()

        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_AgedBrie_normal(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)

        days = 2
        for day in range(days):

            gilded_rose.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_AgedBrie_quality_50(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)

        days = 102
        for day in range(days):

            gilded_rose.update_quality()

        self.assertEqual(-100, items[0].sell_in)
        self.assertEqual(50 , items[0].quality)

    def test_Sulfuras_Ragnaros_normal(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80),
                 Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)

        days = 2
        for day in range(days):

            gilded_rose.update_quality()

        #Test to see if numbers don't change 
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80 , items[0].quality)
        #Test for change
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(80 , items[1].quality) 

    def test_Concert_ticket_normal(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
                 Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
                 Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)

        days = 8
        for day in range(days):

            gilded_rose.update_quality()

        #Item 1 --math
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(31, items[0].quality)
        #Item 2 -- if it goes past 50
        self.assertEqual(2, items[1].sell_in)
        self.assertEqual(50, items[1].quality)
        #Item 3 -- after concert
        self.assertEqual(-3, items[2].sell_in)
        self.assertEqual(0, items[2].quality)

    def test_Conjured_Mana_Cake(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)

        days = 2
        for day in range(days):

            gilded_rose.update_quality()

        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)


if __name__ == '__main__':
    unittest.main()
