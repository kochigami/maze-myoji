# maze-myoji (まぜ名字)

## 説明

今は結婚して名前を変える時にどちらか片方の名字に合わせる必要がある．  

今後名字を混ぜても良くなったら面白いのではないか．

来たる将来に備えてまぜ名字の候補を表示するプログラムを作ってみた．

## サンプル

ハロプロの推しメンの２人に登場して頂く．

```
cd scripts
python maze_myoji.py 小田 中西 # 名前の間は半角スペースを空ける
```

結果
```
Maze Myoji...

小田
田小
小中
中小
小西
西小
田中
中田
田西
西田
中西
西中
小田中
小中田
田小中
田中小
中小田
中田小
小田西
小西田
田小西
田西小
西小田
西田小
小中西
小西中
中小西
中西小
西小中
西中小
田中西
田西中
中田西
中西田
西田中
西中田
小田中西
小田西中
小中田西
小中西田
小西田中
小西中田
田小中西
田小西中
田中小西
田中西小
田西小中
田西中小
中小田西
中小西田
中田小西
中田西小
中西小田
中西田小
西小田中
西小中田
西田小中
西田中小
西中小田
西中田小
The number of maze-myoji candidates is ... 60
```

この中から好きなまぜ名字を選ぶことができる．

## 今後の課題

双方の漢字に重複がある場合のことを考える．