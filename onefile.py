import sys
import os

start_file = sys.argv[-1]

with open(start_file, 'r', encoding="utf-8") as f:
    code = f.read()


def remove_comma_in_imports(code):
    new_code = []
    for line in code.splitlines():
        if line.startswith('import'):
            new_code.append(line.replace(',', '\nimport '))
        else:
            new_code.append(line)
    return '\n'.join(new_code)


code = remove_comma_in_imports(code)


def get_module_path(module_name):
    module_path = os.path.join(os.path.dirname(
        start_file), module_name.replace(".", os.sep))
    module_path = os.path.abspath(module_path)
    module_path = os.path.normpath(module_path)
    module_path += '.py'
    return module_path


def putcode(module_path, line, module_name, from_import=False):
    global code, added_module_names
    if module_name in added_module_names:
        code = code.replace(line, "")
        return
    with open(module_path, "r", encoding="utf-8") as f:
        module_code = f.read()

    code = code.replace(line, module_code)
    if from_import:
        code = code.replace(f"\n{module_name}.", "\n")
        code = code.replace(f" {module_name}.", " ")
        code = code.replace(f"={module_name}.", "=")
        code = code.replace(f"({module_name}.", "(")

    added_module_names.append(module_name)


def import_(line):
    module_name = line.replace("import", "").strip()
    if module_name.startswith('.'):
        module_name = module_name[1:]

    module_path = get_module_path(module_name)

    if os.path.isfile(module_path):
        project_modules.append(module_path)
        putcode(module_path, line, module_name, from_import=True)


def from_(line):
    module_name = line.replace("from", "").split("import")[0].strip()
    if module_name.startswith('.'):
        module_name = module_name[1:]

    module_path = get_module_path(module_name)

    if os.path.isfile(module_path):
        project_modules.append(module_path)
        putcode(module_path, line, module_name, from_import=False)


added_module_names = []

while True:
    project_modules = []

    for line in code.splitlines():
        if line.startswith('import'):
            import_(line)
        if line.startswith('from'):
            from_(line)

    if not project_modules:
        break


if "a" in sys.argv:
    print(code)
