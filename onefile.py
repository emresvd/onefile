# This script converts multiple python files into one python file
import sys
import os

file_name = sys.argv[-1]

with open(file_name, "r", encoding="utf-8") as f:
    code = f.read()

module_files = []
for i in code.splitlines():
    i = i.strip()
    if i.startswith("import"):
        module_s = i.replace("import", "").strip()

        if len(module_s.split(",")) > 1:
            module_s = module_s.split(",")
        else:
            module_s = module_s.replace(".", os.sep)
            module_files.append(module_s+".py")

    if i.startswith("from"):
        packages = i.replace("from", "").strip().split("import")[0].strip()
        packages = packages.replace(".", os.sep)
        print(packages)

project_modules = []
for i in module_files:
    if os.path.isfile(i):
        project_modules.append(i)

print(project_modules)
