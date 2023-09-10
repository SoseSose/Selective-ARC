# 選択式のARC(!!作業中です!!)

[Abstraction and Reasoning Challenge(ARC)](https://github.com/fchollet/ARC)を簡易にしたデータセットを作成しています。!!作業中です。!!

私の考えではARCは次の3つのステップに分かれています。

1. グリッド内のオブジェクトの認識。（赤の3x2ブロックがある、青の10x1区切り線がある,黄色のノイズがある等）
2. 認識された属性の関係性を導く。
3. 関係性から、回答グリッドを生成する。 

ARCでは最終の回答はグリッドの生成でしたが、3の生成は難易度が高く
本来の目的の人間的な抽象推論は1,2で計測できると感じたため、このデータセットを作成しました。
このアイデアは主にraven's progressive matricesのようなものを機械学習に導入した[Procedurally Generated Matrices](https://github.com/google-deepmind/abstract-reasoning-matrices)や[RAVEN](https://github.com/WellyZhang/RAVEN)を基にしています。

# References

[1] https://github.com/fchollet/ARC  
[2] https://github.com/google-deepmind/abstract-reasoning-matrices  
[3] https://github.com/WellyZhang/RAVEN  
