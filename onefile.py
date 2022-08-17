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
        from_module = i.replace("from", "").strip().split("import")[0].strip()
        from_module = from_module.replace(".", os.sep)
        module_files.append(from_module)

        folder_import_file = i.replace("from", "").strip()
        folder=folder_import_file.split("import")[0].strip()
        file=folder_import_file.split("import")[1].strip()
        print(folder_import_file,folder,file)

project_modules = []
for i in module_files:
    if os.path.isfile(i):
        project_modules.append(i)

print(project_modules)
