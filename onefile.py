import sys
import os

start_file = sys.argv[-1]

with open(start_file, 'r', encoding="utf-8") as f:
    code = f.read()


def strip(s):
    return s.strip()


def get_module_path(module_name):
    module_path = os.path.join(os.path.dirname(
        start_file), module_name.replace(".", os.sep))
    module_path = os.path.abspath(module_path)
    module_path = os.path.normpath(module_path)
    module_path += '.py'
    return module_path


def putcode(module_path, line, module_name, from_import=False):
    global code
    with open(module_path, "r", encoding="utf-8") as f:
        module_code = f.read()
    code = code.replace(line, module_code)
    if from_import:
        # if code != code.replace(f" {module_name}.", ""):
        #     code = code.replace(f" {module_name}.", " ")
        # if code != code.replace(f"={module_name}.", ""):
        #     code = code.replace(f"={module_name}.", "=")
        # if code != code.replace(f"({module_name}.", ""):
        #     code = code.replace(f"({module_name}.", "(")
        code = code.replace(f" {module_name}.", " ")
        code = code.replace(f"={module_name}.", "=")
        code = code.replace(f"({module_name}.", "(")


def import_(line):
    module_s_name = list(map(strip, line.replace("import", "").split(",")))

    for module_name in module_s_name:
        if module_name.startswith('.'):
            module_name = module_name[1:]
        # module_path = os.path.join(os.path.dirname(
        #     start_file), module_name.replace(".", os.sep))
        # module_path = os.path.abspath(module_path)
        # module_path = os.path.normpath(module_path)
        # module_path += '.py'

        module_path = get_module_path(module_name)

        if os.path.isfile(module_path):
            project_modules.append(module_path)
            print(os.path.dirname(module_path))
            putcode(module_path, line, module_name, from_import=True)


def from_(line):
    pass


for i in range(3):
    project_modules = []

    for line in code.splitlines():
        if line.startswith('import'):
            import_(line)
        if line.startswith('from'):
            from_(line)
    print(project_modules)


# print(code)
