#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools

# referred https://teratail.com/questions/44502, but it seems I don't have to use this

def maze(myoji):
    # 3つずつに分割
    tmp_kanji_bytecode_list = list(myoji)
    kanji_bytecode_list = []
    for i in range(0, len(tmp_kanji_bytecode_list), 3):
        kanji_bytecode_list.append(tmp_kanji_bytecode_list[i]+tmp_kanji_bytecode_list[i+1]+tmp_kanji_bytecode_list[i+2])
    
    l=len(kanji_bytecode_list)
    
    for s, e in itertools.combinations(range(l), 2):
        tmp = kanji_bytecode_list[s:e+1]
        for v in list(itertools.permutations(tmp, len(tmp))):
            tmp_kanji_list = []
            # v: ('\xe4\xb8\x8a',) や ('\xe8\xa5\xbf', '\xe4\xb8\xad', '\xe4\xb8\x8a')
            for k in range(len(v)):
                tmp_kanji_list.append(v[k])
            #print tmp_kanji_list # ['\xe6\x9d\xb1']
            kanji=''
            for k in tmp_kanji_list:
                kanji += k
            print kanji # 東
   
if __name__ == '__main__':
    # python maze_myoji.py 小田 中西
    args = sys.argv
    myoji1 = args[1]
    myoji2 = args[2]
    myoji = myoji1 + myoji2
    maze(myoji)
    
