#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools

# referred https://teratail.com/questions/44502, but it seems I don't have to use this

def maze(myoji):
    ans = []
    for i in range(1, len(myoji)+1):
        # 漢字をi個だけ選んで並べ替える
        tmp_ans = list(itertools.combinations(myoji, i))
        # ['東', '東', '東']の場合
        # [('\xe6\x9d\xb1',), ('\xe6\x9d\xb1',), ('\xe6\x9d\xb1',)]
        kanji_list = []
        for j in range(len(tmp_ans)):
            s = tmp_ans[j] # ('\xe6\x9d\xb1',)
            tmp_kanji_list = []
            for k in range(len(s)):
                tmp_kanji_list.append(s[k])
            #print tmp_kanji_list # ['\xe6\x9d\xb1']
            kanji=''
            for k in tmp_kanji_list:
                kanji += k
            # print kanji # 東
            
            kanji_list.append(kanji)
        ans += kanji_list
        for k in ans:
            print k
   
if __name__ == '__main__':
    args = sys.argv
    print args
    myoji1 = args[1]
    myoji2 = args[2]
    # 3つずつに分割
    #print str(myoji1)
    myoji1 = list(myoji1)
    myoji2 = list(myoji2)
    tmp1=[]
    for i in range(0, len(myoji1), 3):
        tmp1.append(myoji1[i]+myoji1[i+1]+myoji1[i+2])
    tmp2=[]
    for i in range(0, len(myoji2), 3):
        tmp2.append(myoji2[i]+myoji2[i+1]+myoji2[i+2])
    #print tmp1
    #['\xe6\x9d\xb1']

    #print tmp2
    #['\xe6\x9d\xb1', '\xe6\x9d\xb1']

    kanji = tmp1 + tmp2
    #['\xe6\x9d\xb1', '\xe6\x9d\xb1', '\xe6\x9d\xb1']

    maze(kanji)
    
