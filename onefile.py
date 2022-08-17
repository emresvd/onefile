# This script converts multiple python files into one python file
import sys
import os

file_name = sys.argv[-1]

with open(file_name, "r", encoding="utf-8") as f:
    code = f.read()

for i in code.splitlines():
    i = i.strip()
    if i.startswith("import"):
        module_s = i.split("import")[1].strip()
        if len(module_s.split(",")) > 1:
            module_s = module_s.split(",")
        print(module_s)

        for i in module_s:
            if os.path.isdir(i+".py"):
                print(i)

    if i.startswith("from"):
        print(i)
