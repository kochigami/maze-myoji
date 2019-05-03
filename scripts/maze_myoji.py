#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools

# referred https://teratail.com/questions/44502, but it seems I don't have to use this

def maze(myoji):
    print("Maze Myoji...\n")
    
    # 3つずつに分割
    tmp_kanji_bytecode_list = list(myoji) # ['\xe5', '\xb0', '\x8f', '\xe7', '\x94', '\xb0', '\xe4', '\xb8', '\xad', '\xe8', '\xa5', '\xbf']
    kanji_bytecode_list = []
    for i in range(0, len(tmp_kanji_bytecode_list), 3):
        kanji_bytecode_list.append(tmp_kanji_bytecode_list[i]+tmp_kanji_bytecode_list[i+1]+tmp_kanji_bytecode_list[i+2])

    # kanji_bytecode_list: ['\xe5\xb0\x8f', '\xe7\x94\xb0', '\xe4\xb8\xad', '\xe8\xa5\xbf']
    l=len(kanji_bytecode_list) # 4

    # kanji_bytecode_listの4つの漢字のうち，どこからどこまで選ぶかをインデックスから決める
    for s, e in itertools.combinations(range(l), 2):
        tmp = kanji_bytecode_list[s:e+1]
        # 選んだ漢字を並べ替える
        for v in list(itertools.permutations(tmp, len(tmp))):
            tmp_kanji_list = []
            # v: ('\xe4\xb8\x8a',) や ('\xe8\xa5\xbf', '\xe4\xb8\xad', '\xe4\xb8\x8a')
            for k in range(len(v)):
                tmp_kanji_list.append(v[k])
                
            # tmp_kanji_list:
            # ['\xe5\xb0\x8f', '\xe7\x94\xb0'], ['\xe7\x94\xb0', '\xe5\xb0\x8f'], ['\xe5\xb0\x8f', '\xe7\x94\xb0', '\xe4\xb8\xad']...
            
            kanji=''
            for k in tmp_kanji_list:
                kanji += k
            print kanji # 小田, 田小, 小田中...
   
if __name__ == '__main__':
    # example of how to use: python maze_myoji.py 小田 中西

    # コマンドラインから名字を取得
    args = sys.argv
    myoji1 = args[1] # 小田
    myoji2 = args[2] # 中西
    myoji = myoji1 + myoji2 # 小田中西
    maze(myoji)
    
