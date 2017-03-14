#-*- Coding:utf8 -*-

itemsA = {"蘋果", "香蕉", "鳳梨", "芭樂"}#這是第一個集合
itemsB = {"鳳梨", "蘋果", "水梨", "蓮霧"}#這是第二個集合
item_un = itemsA.union(itemsB)
item_inter = itemsA.intersection(itemsB)
item_diff = item_un.difference(item_inter)
lst = list(item_diff)
lst.sort()
print(lst)
