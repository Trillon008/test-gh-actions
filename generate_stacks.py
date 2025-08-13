#!/usr/bin/env python

import json
import os

stacks_filename = "matrix.stacks.json"

excludes = [
    "datadog", "memory-users", "core-services"
]

stacks = []

def list_leaf_dirs(root_path: str) -> list:
    dirs = []
    for dirpath, dirnames, _ in os.walk(root_path):
        if not dirnames:
            dirs.append(dirpath)
    return dirs

def transform(dirs: list):
    for dir in dirs:
        json_dict = {}
        splitter = dir.split('/')

        if splitter[1] in excludes:
            continue
        json_dict["name"] = splitter[1]
        json_dict["env"] = splitter[2]
        stacks.append(json_dict)


def generate_stack_env(env_name: str) -> list:
    env_stack = []
    for stack in stacks: 
        if stack['env'] == env_name:
            env_stack.append(stack)
    #return { env_name: env_stack }
    return env_stack

if __name__ == "__main__":
    dirs = list_leaf_dirs("stacks")
    transform(dirs)

    #for elt in stacks:
    #    print(elt)

    prod = generate_stack_env('production')
    staging = generate_stack_env('staging')
    final_stack = {"production": prod, "staging": staging}

    with open(stacks_filename, 'w') as f:
        f.write(json.dumps(final_stack, indent=4))
    print(f"New {stacks_filename} written")
