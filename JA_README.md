# Selective ARC

[Abstraction and Reasoning Challenge(ARC)](https://github.com/fchollet/ARC)を選択式にしたデータセットです。

私の考えではARCは次の3つのステップに分かれています。

1. グリッド内のオブジェクトの認識。（赤の3x2ブロックがある、青の10x1区切り線がある,黄色のノイズがある等）
2. 認識された属性の関係性を導く。
3. 関係性から、回答グリッドを生成する。 

ARCでは最終の回答はグリッドの生成でしたが、3の生成は難易度が高く、本来の目的の人間的な抽象推論は1,2で計測できると感じたため、このデータセットを作成しました。  
このアイデアは主にraven's progressive matricesのようなものを機械学習に導入した[Procedurally Generated Matrices(PGM)](https://github.com/google-deepmind/abstract-reasoning-matrices)や[RAVEN](https://github.com/WellyZhang/RAVEN)を基にしています。
私はDeep LearningでARCを解くことを目的としており、PGMやRAVENはDeep Learningでよく研究されているようです。（参考論文）[Deep Learning Methods for Abstract Visual Reasoning: A Survey on Raven's Progressive Matrices](https://arxiv.org/abs/2201.12382)

# ディレクトリ構成

Selective ARCの実際のデータは☆にあります。

**original_arc**  
オリジナルのARCからコピーしたdataと同じです。
「data_for_editing」や「training」「evaluation」はidやname,desctiptionなどが
追加されていますが、ここでは追加されていません。

**data_for_editing**  
make_data_for_arc_editor.pyによってoriginal_arcからデータ編集作業をするために
タスクの延長とidやname,desctiptionなどが追加されたデータです。
タスクの延長とidやname,desctiptionの追加は[ARC Editor](https://arc-editor.lab42.global/editor)で編集するために必要でした。

**evaluation(☆)**  
延長されたevaluationタスク。データがどのように格納されているかは次の段落の例で説明されています。
 
**training(☆)**  
延長されたtrainingタスク。データがどのように格納されているかは次の段落の例で説明されています。

**pictures**  
-説明のための画像が入っています。

**make_data_for_arc_editor.py**  
[ARC Editor](https://arc-editor.lab42.global/editor)で編集をするためにoriginal_arcからdata_for_editingを生成するpythonコードです。

**revision_memo.md**  
編集中に誤りや不明瞭なtaskを見つけたので、どこがおかしいかをメモしています。
明確に誤っていると思ったものはevaluationでは編集しています。

**sanity_check.py**  
作成したtrainingとevaluationの健全性を確認します。元のdata_for_editingからコピーした部分を間違えて編集していないかと違いのない誤ったoutputを作成していないかをチェックします。


# 例
例を/training/239be575.jsonのtest pairで示します。

* pair1~6 trainのinputとoutputのpairです。元のARCデータセットと同様です。
![image](example_image/pair1.png)
![image](example_image/pair2.png)
![image](example_image/pair3.png)
![image](example_image/pair4.png)
![image](example_image/pair5.png)
![image](example_image/pair6.png)

* pair7 初めのtest pair。このoutputがtest inputに対する正しいoutputになります。 
![image](example_image/pair7.png)

* pair8~11 初めのtest pairの後の4つのpairに格納されるのは初めのinputに対する誤ったoutputです。これらは正しいoutputと似ていますが、一部違った部分があります。誤ったoutputは常に正しいpairの後に2x4=8つ格納されます。
![image](example_image/pair8.png)
![image](example_image/pair9.png)
![image](example_image/pair10.png)
![image](example_image/pair11.png)

* pair13 ２つ目の正しいtest pair。このようにtest pairが２つ以上ある場合は、一つ前の誤ったoutputセットの後に続いて格納されています。
![image](example_image/pair12.png)

* pair14~18 ２つ目のtest pairの誤ったoutput。誤ったoutputは常に正しいpairの後に2x4=8つ格納されます。
![image](example_image/pair13.png)
![image](example_image/pair14.png)
![image](example_image/pair15.png)
![image](example_image/pair16.png)
![image](example_image/pair17.png)

# 参考

[1] https://github.com/fchollet/ARC  
[2] https://github.com/google-deepmind/abstract-reasoning-matrices  
[3] https://github.com/WellyZhang/RAVEN  
[4] https://arxiv.org/abs/2201.12382

※README.mdはJA_README.mdから機械翻訳されたものです。