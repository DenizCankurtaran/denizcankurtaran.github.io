import os

dirs = []
for dir in os.listdir():
    if os.path.isdir(dir) and not dir.startswith('.'):
        dirs.append(dir)

with open('index.md', 'w') as index_file:
    index_file.write('# Notizen von Deniz Cankurtaran\n')
    index_file.write('## Module:')
    for dir in dirs:
        index_file.write(f' - [{dir}]({dir}/index.md)\n')

    
