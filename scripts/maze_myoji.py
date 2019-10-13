#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools

def maze(myoji):
    print("Maze Myoji...\n")

    myoji = myoji.decode('utf-8')
    myoji = list(myoji)
    myoji = [char.encode('utf-8') for char in myoji]
    # myoji: ['\xe5\xb0\x8f', '\xe7\x94\xb0', '\xe4\xb8\xad', '\xe8\xa5\xbf']
    
    count =0
    new_myoji_list = []
    # myojiリスト2つ，3つ，リストの数分まで組を順番につくる
    for i in range(2, len(myoji)+1):
        # 2つの文字の時
        # tmp: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        tmp=list(itertools.combinations(myoji,i))
        # j: (1, 2)
        for j in tmp:
            tmp2=list(itertools.permutations(j, len(j)))
            # tmp2: (1,2) (2,1)
            for k in tmp2:
                new_myoji=""
                for l in k:
                    new_myoji+=l
                if not(new_myoji in new_myoji_list):
                    new_myoji_list.append(new_myoji)
                    print new_myoji
                    count +=1
    print "The number of maze-myoji candidates is ... %d" % (count)

if __name__ == '__main__':
    # example of how to use: python maze_myoji.py 小田 中西

    # コマンドラインから名字を取得
    args = sys.argv
    myoji1 = args[1] # 小田
    myoji2 = args[2] # 中西
    maze(myoji1 + myoji2) # 小田中西
    
