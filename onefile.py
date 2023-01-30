import sys

start_file = sys.argv[-1]

with open(start_file, 'r', encoding="utf-8") as f:
    code = f.read()


def strip(s):
    return s.strip()


def import_(line):
    module_s = list(map(strip, line.replace("import", "").split(",")))
    print(module_s)


def from_(line):
    print(line)


for line in code.splitlines():
    if line.startswith('import'):
        import_(line)
    if line.startswith('from'):
        from_(line)
