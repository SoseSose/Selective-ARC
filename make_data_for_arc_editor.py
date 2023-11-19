# %%
from pathlib import Path
import glob
import json
import collections

EXPAND_LEN:int = 8

def rewrite_original_data(train_or_evaluation):

    original_dir = Path("original_arc")/train_or_evaluation
    for file in original_dir.glob("*.json"):
        with file.open() as f:
            task = json.load(f)

        # task = dict(sorted(task.items(), reverse=True))

        train_len = len(task["train"])

        for idx in range(train_len):
            task["train"][idx]["id"] = idx
            # id_index += 1
            task["train"][idx] = dict(sorted(task["train"][idx].items()))
        # print(task)
        # print(task["test"])

        test_set = []
        id_idx = train_len
        for i in range(len(task["test"])):
            input_output = dict(collections.OrderedDict(
                id=id_idx,
                input=task["test"][i]["input"],
                output=task["test"][i]["output"],
            ))#Use OrderedDict to order the id, input, and output in the correct order.
            test_set.append(input_output)
            id_idx += 1

            #Create a candidate for editing. copy test output and extend test by EXPAND_LEN.
            for j in range(int(EXPAND_LEN/2)): 
                # Divide by 2 since there is input and output.
                input_output = dict(collections.OrderedDict(
                    id=id_idx,
                    input=task["test"][i]["output"],
                    output=task["test"][i]["output"],
                ))
                id_idx += 1
                test_set.append(input_output)

        task["test"] = test_set
        task["name"] = file.stem
        task["description"] = ""#Without desc, it will not function in arc editor.
        
        json_text = json.dumps(task, separators=(",", ":"))
        make_path = Path("data_for_editing")/train_or_evaluation/file.name
        make_path.write_text(json_text)
        print("write {} {}".format(file.name, json_text))
        

rewrite_original_data("training")
rewrite_original_data("evaluation")