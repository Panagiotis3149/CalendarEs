import sys
import os

def unicode_date_to_char(line):
    if not line.startswith('U+'):
        raise ValueError(f"Bruh, invalid line: {line}")
    parts = line[2:].strip().split('/')
    if len(parts) != 3:
        raise ValueError(f"Bruh, line not M/D/Y format: {line}")
    month, day, year = map(int, parts)
    codepoint = month + day + year
    if codepoint > 0x10FFFF:
        raise ValueError(f"Bruh, Unicode codepoint too big: {codepoint}")
    return chr(codepoint)

def compile_file(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chars = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('//'):
            continue
        if '#' in line:
            line = line.split('#', 1)[0].strip()
        if '//' in line:
            line = line.split('//', 1)[0].strip()
        if not line:
            continue
        chars.append(unicode_date_to_char(line))

    result = ''.join(chars)

    output_path = os.path.splitext(input_path)[0] + '.py'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result + '\n')

    print(f"Bruh, compiled {input_path} → {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py compile.py source.🗓Lang")
        sys.exit(1)
    compile_file(sys.argv[1])
