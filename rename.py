# import os

# directory = '/home/my/Desktop/download_file_prac'

# for filename in os.listdir(directory):
#     if filename.endswith('.pdf'):
#         new_filename = filename.replace(' ', '_')
#         os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

import os

directory = '/home/my/Desktop/download_file_prac'

for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        new_filename = filename.replace(' ', '_')
        os.system(f'git mv -f "{os.path.join(directory, filename)}" "{os.path.join(directory, new_filename)}"')
        
os.system(f'git add .')
os.system(f'git status')
