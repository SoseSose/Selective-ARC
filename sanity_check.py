#%%
import json
import glob
import os
import numpy as np

def candidate_is_not_same():
    files = glob.glob("training_add/*.json")
    for file in files:
        candidates = []
        with open(file, "r") as f:
            task = json.load(f)
        true_answer = task["test"][0]["output"]
        candidates.append(true_answer)
        for i in range(1, len(task["test"])):
            candidates.append(task["test"][i]["input"])
            candidates.append(task["test"][i]["output"])
        for i, candidate in enumerate(candidates):
            for j, candidate2 in enumerate(candidates):
                if i != j:
                    candidate = np.array(candidate)
                    candidate2 = np.array(candidate2)
                    if candidate.shape == candidate2.shape:
                        # print(np.all(candidate == candidate2))
                        if np.all(candidate == candidate2):
                            print(candidate, candidate2)
                        
                        assert not np.all(candidate == candidate2), "{} candidate{} and candidata{} is same".format(file, i, j)


        # break

candidate_is_not_same()