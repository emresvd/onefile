import sys
import os

start_file = sys.argv[-1]

with open(start_file, 'r', encoding="utf-8") as f:
    code = f.read()


def strip(s):
    return s.strip()


def import_(line):
    module_s = list(map(strip, line.replace("import", "").split(",")))
    for module in module_s:
        if module.startswith('.'):
            module = module[1:]
        module = os.path.join(os.path.dirname(start_file), module)
        module = os.path.abspath(module)
        module = os.path.normpath(module)
        module += '.py'
        if os.path.isfile(module):
            print(module)


def from_(line):
    pass


for line in code.splitlines():
    if line.startswith('import'):
        import_(line)
    if line.startswith('from'):
        from_(line)
