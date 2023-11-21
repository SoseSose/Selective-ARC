#%%
import json
import glob
import os
import numpy as np
import pyperclip
from pathlib import Path


LEN_FALSE_OUTPUT = 5
LEN_TASKS = 400

#%%
def test_original_add_are_equal(original_dir, training_or_evaluation):

    original_dir = Path(original_dir)/training_or_evaluation
    add_dir = Path(training_or_evaluation)
    original_files = original_dir.glob("*.json")


    for file_idx, original_file in enumerate(original_files):
        with original_file.open() as f:
            add_task = dict(sorted(json.load(f).items()))

        with (add_dir/original_file.name).open() as f:
            original_task = dict(sorted(json.load(f).items()))
        
        not_expanded_original_task = original_task["train"] + original_task["test"][::LEN_FALSE_OUTPUT]
        not_expanded_add_task = add_task["train"] + add_task["test"][::LEN_FALSE_OUTPUT]

        for original, add in zip(not_expanded_original_task, not_expanded_add_task):
            original_task_json =  json.dumps(original)
            add_task_json =  json.dumps(add)

            if original_task_json != add_task_json:
                print(training_or_evaluation, file_idx,  original_file.name)
                print(original_task_json)
                print(add_task_json)
                pyperclip.copy(original_file.name)

            # assert original_task_json == add_task_json 

    #test num of files
    assert len(list(original_dir.glob("*.json"))) == LEN_TASKS

                

test_original_add_are_equal("data_for_editing", "training")
test_original_add_are_equal("data_for_editing", "evaluation")

#%%
def candidate_is_not_same(target_folder_name):

    target_folder = Path(target_folder_name)
    hcl = 5
    files = sorted(glob.glob(str()))
    files = target_folder.glob("*.json")

    for file_num, file in enumerate(files):
        file_path = Path(file)

        with open(file, "r") as f:
            task = json.load(f)
        
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
                            if np.all(candidate == candidate2):
                                pyperclip.copy(file_path.name)
                            
                            assert not np.all(candidate == candidate2), "file num: {}\n{} candidate{} and candidata{} is same\n{}\n\n{}".format(file_num, file, i, j,candidate, candidate2)
    
    assert len(list(target_folder.glob("*.json"))) == LEN_TASKS

candidate_is_not_same("training")
candidate_is_not_same("evaluation")