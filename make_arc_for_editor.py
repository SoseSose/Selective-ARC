#%%
from pathlib import Path
import glob
import json
import copy

base_path = "C:\\Users\\taeya\\Documents\\Optional ARC\\training_origin"
file_list = glob.glob(base_path +"\\*.json")

base_max = novel_max = num_upper_max_size = 0
for file in file_list:
    path = Path(file)
    with open(path, "r") as f:
        json_load = json.load(f)

    base_ind = novel_ind = 0
    images = {}
    id_index = 0
    json_load = dict(sorted(json_load.items(), reverse=True))

    for i in range(len(json_load["train"])):
        json_load["train"][i]["id"] = id_index
        id_index += 1
        json_load["train"][i] = dict(sorted(json_load["train"][i].items()))

    for i in range(len(json_load["test"])):

        json_load["test"][i]["id"] = id_index
        id_index += 1
        json_load["test"][i] = dict(sorted(json_load["test"][i].items()))
        
        for j  in range(4):
            one_train = copy.deepcopy(json_load["test"][4 * i + j])
            try:
                one_train["input"] = one_train["output"]
            except KeyError:
                print(path.stem)
            one_train["id"] = id_index
            id_index += 1

            one_train = dict(sorted(one_train.items()))
            json_load["test"].append(one_train)
    

    json_load["name"] = path.stem
    json_load["description"] = ""

    # del json_load["train"]
    # json_load["train"] = json_load["test"]

        

    json_load = dict(sorted(json_load.items(), reverse=True))
    

    # print(json_load)
    with open(base_path+"2\\"+path.stem+".json", 'w') as f:
        json.dump(json_load, f, separators=(',', ':'))
    
    # break

#%%

#%%
import os
add = glob.glob(base_path +"training_add\\*.json")
print(len(add))
for add_fn in add:
    add_fn = Path(add_fn)
    add_fn = add_fn.stem+".json"
    print(base_path+"training_origin\\"+add_fn)
    print(os.path.exists(base_path+"training_origin\\"+add_fn))
    os.remove(base_path+"training_origin\\"+add_fn)

origin = glob.glob(base_path +"training_origin\\*.json")
print(len(origin))