#%%
#b7cb93ac.json 上下左右入れ替えても問題がなさそう
import json
import glob
import os
import numpy as np
import pyperclip
import pathlib


LEN_FALSE_OUTPUT = 5
#%%
def test_original_add_are_equal():

    original_dir = pathlib.Path("evaluation_expand")/"end"
    add_dir = pathlib.Path("evaluation_add")
    add_files = glob.glob(str(add_dir)+"/*.json")

    for file_idx, add in enumerate(add_files):
        add_path = pathlib.Path(str(add))
        with add_path.open() as f:
            add_task = dict(sorted(json.load(f).items()))

        with (original_dir/add_path.name).open() as f:
            original_task = dict(sorted(json.load(f).items()))


        original_task_json =  json.dumps(original_task["test"][::LEN_FALSE_OUTPUT])
        add_task_json =  json.dumps(add_task["test"][::LEN_FALSE_OUTPUT])


        if original_task_json != add_task_json:
            print(file_idx,  add)
            print(original_task_json)
            print(add_task_json)
            pyperclip.copy(add_path.name)

                
        # assert original_task_json == add_task_json 

test_original_add_are_equal()

#%%
def candidate_is_not_same():

    target_folder = pathlib.Path("training_add")
    target_folder = pathlib.Path("evaluation_add")
    hcl = 5
    files = sorted(glob.glob(str(target_folder/"*.json")))
    for file_num, file in enumerate(files):
        file_path = pathlib.Path(file)

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
                                print(file_path.name)
                            
                            assert not np.all(candidate == candidate2), "file num: {}\n{} candidate{} and candidata{} is same\n{}\n\n{}".format(file_num, file, i, j,candidate, candidate2)

candidate_is_not_same()
#%%
# def move_training_add_8():
#     target_folder = "training_add"
#     files = sorted(glob.glob(target_folder+"/*.json"))
#     for file in files:

#         with open(file, "r") as f:
#             task = json.load(f)

#         # print(len(task["test"]))
#         # print(len(task["test"][:5]))

#         original_task_len = int(len(task["test"])/5)
#         if original_task_len != 1:
#             print(original_task_len)
#         for i in range(original_task_len):
#             task["test"].pop((i+1)*5-i)

#         # print("training_add_8"+file.removeprefix(target_folder))
#         with open("training_add_8"+file.removeprefix(target_folder), 'w') as f:
#             json.dump(task, f, separators=(',', ':'))
    
        
#     #     test_tasks = [task["test"][idx*hcl:(idx+1)*hcl] for idx in range(int(len(task["test"])/hcl))] 
#     # print(original_files[0])

# move_training_add_8()

#%%
# def correction_add_task_len_more_than_two():
#     add_files = sorted(glob.glob("training_add/*.json"))
#     for file in add_files:
#         with open(file, "r") as f:
#             add_task = dict(sorted(json.load(f).items()))
#         if len(add_task["test"]) > 11:
            
#             print(len(add_task["test"]))
#             print(file)
#             for in_out in add_task["test"]:
#                 print(in_out["id"])
#             id_index = add_task["test"][0]["id"]
#             for i in range(len(add_task["test"])):
#                 add_task["test"][i]["id"] = id_index
#                 id_index += 1
#             print(add_task["test"])
#             # for in_out in add_task["test"]:
#             #     print(in_out["id"])

#             with open(file, "w") as f:
#                 json.dump(add_task, f, separators=(",", ":"))

# correction_add_task_len_more_than_two()