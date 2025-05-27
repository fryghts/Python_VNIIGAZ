import os
file_names = []
for curdir, dirs, files in os.walk('C:\\Users\\Администратор\\Desktop\\Python_2025\\14'):
    file_names.extend([os.path.join(curdir, name) for name in files])

print(*file_names, sep = '\n')
