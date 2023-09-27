#%%
import json
import glob
import os
import numpy as np
import pyperclip

#todo same original arc
#todo check candidate length


def candidate_is_not_same():

    def check_func(target_folder, hcl):
        """_summary_

        Args:
            target_file_name (str):
            hcl (int):half candidate length 
        """
        files = sorted(glob.glob(target_folder+"/*.json"))
        for file_num, file in enumerate(files):

            # if os.path.exists(file.removesuffix(".json") + " (1).json"):
            #     print("exists")
            #     os.remove(file)
            #     os.rename(file.removesuffix(".json") + " (1).json", file)
            #     pass

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
                                # print(np.all(candidate == candidate2))
                                if np.all(candidate == candidate2):
                                    # print(candidate, candidate2)
                                    pyperclip.copy(file.removeprefix(target_folder+"\\"))
                                
                                assert not np.all(candidate == candidate2), "file num: {}\n{} candidate{} and candidata{} is same\n{}\n\n{}".format(file_num, file, i, j,candidate, candidate2)

    check_func(target_folder= "training_add", hcl=6)
    check_func(target_folder= "training_add_8", hcl=5)



candidate_is_not_same()

#%%
def move_training_add_8():
    target_folder = "training_add"
    files = sorted(glob.glob(target_folder+"/*.json"))
    for file in files:

        with open(file, "r") as f:
            task = json.load(f)
        print(len(task["test"]))
        print(len(task["test"][:5]))
        task["test"] = task["test"][:5]
        # break
        print("training_add_8"+file.removeprefix(target_folder))
        with open("training_add_8"+file.removeprefix(target_folder), 'w') as f:
            json.dump(task, f, separators=(',', ':'))
    
        
    #     test_tasks = [task["test"][idx*hcl:(idx+1)*hcl] for idx in range(int(len(task["test"])/hcl))] 
    # print(original_files[0])

move_training_add_8()
#%%
def check_original_n_add_are_equal():
    def check_func(original_dir, add_dir):
        original_files = sorted(glob.glob(original_dir+"/*.json"))
        add_files = sorted(glob.glob(original_dir+"/*.json"))
        # for file_num, file in enumerate(files):


    check_func(original_dir="training_origin", add_dir="training_add")
    check_func(original_dir="training_origin", add_dir="training_add")


candidate_is_not_same()