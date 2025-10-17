#!/usr/bin/env python

# Todo
# Handle projets and env
# clean / refactor

import json
import os

stacks_filename = "matrix.stacks.json"

excludes = [
    "datadog", "core-services"
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
        if stack['env'] == env_name and stack['name'] != 'memory':
            env_stack.append(stack)
    return env_stack


def generate_stack_memory(env_name: str) -> list:
    env_stack = []
    for stack in stacks:
        if stack['name'] == 'memory':
            env_stack.append(stack)
    return env_stack


if __name__ == "__main__":
    dirs = list_leaf_dirs("stacks")
    transform(dirs)

    complete_stack = {}
    for envi in ['core-services',  'staging', 'development']:
        complete_stack[envi] = generate_stack_env(envi)


    complete_stack['memory'] = generate_stack_memory(envi)

    with open(stacks_filename, 'w') as f:
        f.write(json.dumps(complete_stack, indent=4))
    print(f"New {stacks_filename} written")

    #print(json.dumps(complete_stack, indent=4))
