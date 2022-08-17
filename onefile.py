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
        if from_module.startswith("."):
            from_module = from_module.replace(".", "")
        from_module = from_module.replace(".", os.sep)
        module_files.append(from_module+".py")

        try:
            folder_import_file = i.replace("from", "").strip()
            folder = folder_import_file.split("import")[0].strip()
            file = folder_import_file.split("import")[1].strip()
            module_files.append(os.path.join(folder, file)+".py")
        except IndexError:
            continue

project_modules = []
for i in module_files:
    if os.path.isfile(i):
        if not i in project_modules:
            project_modules.append(i)

print(project_modules)

codes_of_all_modules = ""
for i in project_modules:
    with open(i, "r", encoding="utf-8") as f:
        module_code = f.read()

    module_code_without_name_main = ""
    name_main = False
    look_name_main_tab = False

    for j in module_code.splitlines():
        if not bool(j):
            continue

        tab = len(j.split(j.strip())[0])

        if j.strip() == 'if __name__ == "__main__":' or j.strip() == 'if __name__=="__main__":' or j.strip() == "if __name__ == '__main__':" or j.strip() == "if __name__=='__main__':":
            name_main = True
            look_name_main_tab = True
            continue

        if look_name_main_tab:
            name_main_tab = tab
            look_name_main_tab = False

        try:
            if tab < name_main_tab:
                name_main = False
            else:
                name_main = True
        except NameError:
            pass

        if not name_main:
            module_code_without_name_main += j+"\n"
        if name_main:
            print(j)

    codes_of_all_modules += module_code_without_name_main+"\n"

#print(codes_of_all_modules)

# with open(file_name.split(".")[0]+"_one.py", "w", encoding="utf-8") as f:
#     f.write(codes)
