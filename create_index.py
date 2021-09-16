import os
from datetime import datetime

now = datetime.now().strftime('%A %d-%m-%Y, %H:%M:%S')

dirs = []
for dir in os.listdir():
    if os.path.isdir(dir) and not dir.startswith('.'):
        dirs.append(dir)

with open('index.md', 'w') as index_file:
    index_file.write('# Notizen von Deniz Cankurtaran\n')
    index_file.write(f'### last update: {now} \n')
    index_file.write('## Module:\n')
    for dir in dirs:
        index_file.write(f' - [{dir}]({dir}/index.md)\n')
