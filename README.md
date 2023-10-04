# 選択式のARC(!!作業中です!!)

[Abstraction and Reasoning Challenge(ARC)](https://github.com/fchollet/ARC)を選択式にしたデータセットを作成しています。!!
ただし、まだ作業中です!!
まだ作成されているのはtrainデータのみです。
11月末までにはevalationデータの回答候補も作成することを目標にしています。
結構、大変な作業なので、手伝っていただける方は大歓迎ですが、
同じタスクをしてしまうと無駄になってしまうので、
もし手伝っていただける方がいれば、ご連絡ください。

私の考えではARCは次の3つのステップに分かれています。

1. グリッド内のオブジェクトの認識。（赤の3x2ブロックがある、青の10x1区切り線がある,黄色のノイズがある等）
2. 認識された属性の関係性を導く。
3. 関係性から、回答グリッドを生成する。 

ARCでは最終の回答はグリッドの生成でしたが、3の生成は難易度が高く、本来の目的の人間的な抽象推論は1,2で計測できると感じたため、このデータセットを作成しました。  
このアイデアは主にraven's progressive matricesのようなものを機械学習に導入した[Procedurally Generated Matrices(PGM)](https://github.com/google-deepmind/abstract-reasoning-matrices)や[RAVEN](https://github.com/WellyZhang/RAVEN)を基にしています。
私はDeep LearningでARCを解くことを目的としており、PGMやRAVENはDeep Learningでよく研究されているようです。（参考論文）[Deep Learning Methods for Abstract Visual Reasoning: A Survey on Raven's Progressive Matrices](https://arxiv.org/abs/2201.12382)


# 形式

元のデータセットと同様のjsonですが、testデータのorignalのinput,outputの後にinput,outputセットが4つ、続いており、この4つが偽の回答候補となります。
以下はff28f65a.jsonでの例です。

![image](add_image_desc.png)

できれば良い説明をしたいですが、ダウンロードしたデータを[Arc Editer](https://arc-editor.lab42.global/editor)で見てもらう方が良いでしょう。

# 参考

[1] https://github.com/fchollet/ARC  
[2] https://github.com/google-deepmind/abstract-reasoning-matrices  
[3] https://github.com/WellyZhang/RAVEN  
[4] https://arxiv.org/abs/2201.12382

※en_read_me.mdでのこの文はchat GPTで翻訳されたものです。