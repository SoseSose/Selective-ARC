#%%
import json
import glob
import os
import numpy as np
import pyperclip

#todo same original arc
#


def candidate_is_not_same():
    files = sorted(glob.glob("training_add/*.json"))
    for file_num, file in enumerate(files):

        # if os.path.exists(file.removesuffix(".json") + " (1).json"):
        #     print("exists")
        #     os.remove(file)
        #     os.rename(file.removesuffix(".json") + " (1).json", file)
        #     pass

        with open(file, "r") as f:
            task = json.load(f)
        
        hcl = 6 #half candidate length
        test_tasks = [task["test"][idx*hcl:(idx+1)*hcl] for idx in range(int(len(task["test"])/hcl))] 
        for test_task in test_tasks:
            #collect candidates
            candidates = []
            true_answer = test_task[0]["output"]
            candidates.append(true_answer)
            for i in range(1, len(test_task)):
                candidates.append(test_task[i]["input"])
                candidates.append(test_task[i]["output"])

            #Ensure that the candidates are not the same as each other.
            for i, candidate in enumerate(candidates):
                for j, candidate2 in enumerate(candidates):
                    if i != j:#i == j -> same candidate
                        candidate = np.array(candidate)
                        candidate2 = np.array(candidate2)
                        if candidate.shape == candidate2.shape:
                            # print(np.all(candidate == candidate2))
                            if np.all(candidate == candidate2):
                                # print(candidate, candidate2)
                                pyperclip.copy(file.removeprefix("training_add\\"))
                            
                            assert not np.all(candidate == candidate2), "file num: {}\n{} candidate{} and candidata{} is same\n{}\n\n{}".format(file_num, file, i, j,candidate, candidate2)



candidate_is_not_same()
#%%
a = [1, 2, 3]
b = a[:0] + a[0+1:]
print(b)
b[0]= 100
print(a)