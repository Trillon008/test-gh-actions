#!/usr/bin/env python

import json
import os

stacks_filename = "matrix.stacks.json"

def list_leaf_dirs(root_path: str) -> list:
    dirs = []
    for dirpath, dirnames, _ in os.walk(root_path):
        if not dirnames:
            dirs.append(dirpath)
    return dirs

def transform(dirs: list) -> list:
    stacks = []
    for dir in dirs:
        json_dict = {}
        splitter = dir.split('/')
        json_dict["name"] = splitter[1]
        json_dict["env"] = splitter[2]
        stacks.append(json_dict)

    return stacks


if __name__ == "__main__":
    dirs = list_leaf_dirs("stacks")
    stacks = transform(dirs)

    with open(stacks_filename, 'w') as f:
        f.write(json.dumps(stacks, indent=4))
    print(f"New {stacks_filename} written")
