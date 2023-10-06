# Multiple Choice ARC (!!Under Construction!!)

I'm in the process of creating a dataset based on the [Abstraction and Reasoning Challenge (ARC)](https://github.com/fchollet/ARC) formatted as multiple choice. 
!!Please be informed it's still under construction!!
As of now, only the train data has been produced. 
I'm setting a goal to generate answer candidates for the evaluation data by the end of November. 
Creating this is quite challenging, so any help would be greatly appreciated. However, to avoid redundancy in tasks, if you are willing to assist, please get in touch first.

In my perspective, ARC can be segmented into the following three steps:

1. Recognizing objects within the grid (e.g., there's a red 3x2 block, a blue 10x1 dividing line, yellow noise, etc.).
2. Inferring the relationships of the recognized attributes.
3. Based on these relationships, produce the answer grid.

In ARC, the final response was in the form of a grid. Given that creating the grid in step 3 is challenging, I felt that the primary goal of human-like abstract reasoning could be gauged in steps 1 and 2. This inspired me to develop this dataset. 
This concept primarily draws from introducing ideas similar to raven's progressive matrices into machine learning via [Procedurally Generated Matrices (PGM)](https://github.com/google-deepmind/abstract-reasoning-matrices) and [RAVEN](https://github.com/WellyZhang/RAVEN). I am keen on solving ARC using Deep Learning, and it seems that PGM and RAVEN are being extensively explored in this field. (Refer to the paper: [Deep Learning Methods for Abstract Visual Reasoning: A Survey on Raven's Progressive Matrices](https://arxiv.org/abs/2201.12382)).

# Format

The dataset follows a similar json structure as the original. However, for test data, after the original input and output, four sets of input-output pairs are added. These four are intended as false answer candidates. 
An example from ff28f65a.json is provided below:

![image](add_image_desc.png)

While a detailed explanation is desired, it might be more insightful for users to view the downloaded data using the [Arc Editor](https://arc-editor.lab42.global/editor).

# References

[1] https://github.com/fchollet/ARC  
[2] https://github.com/google-deepmind/abstract-reasoning-matrices  
[3] https://github.com/WellyZhang/RAVEN  
[4] https://arxiv.org/abs/2201.12382

※ This text was translated.

