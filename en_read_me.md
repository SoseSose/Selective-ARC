# Multiple Choice ARC (!!Under Construction!!)

I'm creating a dataset based on the [Abstraction and Reasoning Challenge (ARC)](https://github.com/fchollet/ARC) formatted as multiple choice. 
!!Please note, it's still under construction!!
Currently, only the train data has been created. 
I aim to also generate answer candidates for the validation data by the end of October.

In my perspective, ARC can be divided into the following three steps:

1. Recognizing objects within the grid (e.g., there's a red 3x2 block, a blue 10x1 dividing line, yellow noise, etc.).
2. Inferring the relationships of the recognized attributes.
3. Based on these relationships, generate the answer grid.

While in ARC the final answer was given in the form of a grid, I found creating the grid in step 3 to be challenging. I felt that the primary objective of human-like abstract reasoning could be assessed in steps 1 and 2, prompting me to create this dataset.
This idea is mainly built upon the [Procedurally Generated Matrices (PGM)](https://github.com/google-deepmind/abstract-reasoning-matrices) and [RAVEN](https://github.com/WellyZhang/RAVEN), which introduce concepts akin to raven's progressive matrices into machine learning. I am aiming to solve ARC using Deep Learning, and it seems that PGM and RAVEN have been extensively studied in the Deep Learning context. (Refer to the paper: [Deep Learning Methods for Abstract Visual Reasoning: A Survey on Raven's Progressive Matrices](https://arxiv.org/abs/2201.12382)).

# References

[1] https://github.com/fchollet/ARC  
[2] https://github.com/google-deepmind/abstract-reasoning-matrices  
[3] https://github.com/WellyZhang/RAVEN  
[4] https://arxiv.org/abs/2201.12382

