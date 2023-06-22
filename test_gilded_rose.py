# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    """Testing the gildedrose class"""

    def test_float_input(self):
        """Tests decimals as input"""

        items = [Item("Normal", 1.5 , 2),
                 Item("Normal2", 1, 2.5)]

        gilded_rose = GildedRose(items)
        days = 1

        for day in range(days):
            gilded_rose.update_quality()

        self.assertEqual(0.5, items[0].sell_in)
        self.assertEqual(1.5, items[1].quality)

    def test_norm_default(self):
        """Tests normal item's normal operation"""

        items = [Item("+5 Dexterity Vest", 1, 2)]
        gilded_rose = GildedRose(items)
        days = 1
        for day in range(days):
            gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(1, items[0].quality)


    def test_norm_expired(self):
        """Tests when normal item expires"""

        items = [Item("+5 Dexterity Vest", 0, 2)]
        gilded_rose = GildedRose(items)

        days = 1
        for day in range(days):

            gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_agebrie_default(self):
        """Tests Aged Brie normal operation"""

        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)

        days = 2
        for day in range(days):

            gilded_rose.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_agedbrie_expired(self):
        """Tests Aged Brie expires"""

        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)

        days = 1

        for day in range(days):
            gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)


    def test_agedbrie_qual50(self):
        """Tests if after updating it 
        quality will exceed 50"""
        items = [Item("Aged Brie", 0, 1)]
        gilded_rose = GildedRose(items)

        days = 50
        for day in range(days):

            gilded_rose.update_quality()

        self.assertEqual(-50, items[0].sell_in)
        self.assertEqual(50 , items[0].quality)

    def test_sulfuras_defualt(self):
        """Tests to see if numbers change"""
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80),
                 Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)

        days = 2
        for day in range(days):

            gilded_rose.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80 , items[0].quality)

        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(80 , items[1].quality)

    def test_concert(self):
        """"Testing all variations in price"""

        items = [Item("Backstage passes to a TAKAL80ETC concert", 20, 0),
                 Item("Backstage passes to a TAFKAL80ETC concert", 11, 0),
                    Item("Backstage passes to a TAFKAL80ETC concert", 6, 0),
                    Item("Backstage passes to a TAFKAL80ETC concert", 0, 30)]
        gilded_rose = GildedRose(items)

        days = 1
        for day in range(days):
            gilded_rose.update_quality()
        
        # 11 or more sell days
        self.assertEqual(19, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
        # 10 - 6 sell days
        self.assertEqual(10, items[1].sell_in)
        self.assertEqual(2, items[1].quality)
        # 5 - 0 sell days
        self.assertEqual(5, items[2].sell_in)
        self.assertEqual(3, items[2].quality)
        #Item 3 -- after concert
        self.assertEqual(-1, items[3].sell_in)
        self.assertEqual(0, items[3].quality)

    def test_conjured(self):
        """Testing all variations in price"""
        items = [Item("Conjured Mana Cake", 1, 2),
                 Item("Conjured Mana Cake", 0, 4)]
        gilded_rose = GildedRose(items)

        days = 1
        for day in range(days):

            gilded_rose.update_quality()

        # Test regular operation
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
        # Test expired operation
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(0, items[1].quality)


if __name__ == '__main__':
    unittest.main()
