# %%
from pathlib import Path
import glob
import json
import copy
import collections

base_path = "C:\\Users\\taeya\\Documents\\Optional ARC\\"
file_list = glob.glob(base_path + "original_evaluation\\*.json")

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

    test_set = []
    for i in range(len(json_load["test"])):
        input_output = collections.OrderedDict(
            id=id_index,
            input=json_load["test"][i]["input"],
            output=json_load["test"][i]["output"],
        )
        test_set.append(input_output)
        id_index += 1

        for j in range(4):
            input_output = collections.OrderedDict(
                id=id_index,
                input=json_load["test"][i]["output"],
                output=json_load["test"][i]["output"],
            )
            id_index += 1
            test_set.append(input_output)

    json_load["test"] = test_set

    if len(json_load["test"]) > 9:
        print(f)
        for tst in json_load["test"]:
            print(tst)

    json_load["name"] = path.stem
    json_load["description"] = ""

    # del json_load["train"]
    # json_load["train"] = json_load["test"]

    json_load = dict(sorted(json_load.items(), reverse=True))
    with open(base_path + "evaluation_expand\\" + path.stem + ".json", "w") as f:
        json.dump(json_load, f, separators=(",", ":"))

    # break

# %%

# %%
import os

add = glob.glob(base_path + "training_add\\*.json")
print(len(add))
for add_fn in add:
    add_fn = Path(add_fn)
    add_fn = add_fn.stem + ".json"
    print(base_path + "training_origin\\" + add_fn)
    print(os.path.exists(base_path + "training_origin\\" + add_fn))
    os.remove(base_path + "training_origin\\" + add_fn)

origin = glob.glob(base_path + "training_origin\\*.json")
print(len(origin))
