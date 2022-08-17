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

codes = ""
for i in project_modules:
    with open(i, "r", encoding="utf-8") as f:
        for j in f.read().splitlines():
            if "if __name__ == '__main__':" == j.strip() or "if __name__=='__main__':" == j.strip() or 'if __name__ == "__main__":' == j.strip() or 'if __name__=="__main__":' == j.strip():
                pass
            else:
                codes += f.read()+"\n"
codes = code+codes

with open(file_name.split(".")[0]+"_one.py", "w", encoding="utf-8") as f:
    f.write(codes)
