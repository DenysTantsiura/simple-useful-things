# Be careful ! Analyze the code first!
import os
import shutil


KB = 1024
MB = 1024 * KB
GB = 1024 * MB

# If run in root of disk

disk = os.fspath(os.path.abspath(os.getcwd()))

os.makedirs(os.fspath('bin-free-bin'), exist_ok=True)

ballast_file = os.fspath(os.path.join(disk, 'bin-free-bin'))

print(disk)

print(ballast_file)

print(f'Free space on disk \"{disk}\", Kb: ', shutil.disk_usage('/').free / KB)

free_size = shutil.disk_usage('/').free  # bytes

block = '0'

big_files_count = free_size // (2 * GB)

small_file_size = free_size % (2 * GB)

input(f'2 GB Files: {big_files_count}')

print(f'And 1 file {small_file_size} byte')


def drop_file(cx, file_s_number):

    file = os.fspath(os.path.join(ballast_file, f'F{file_s_number}.data'))

    try:

        with open(file, 'wb') as fh:

            fh.write(bytes(block*cx, 'utf-8'))

    except Exception as err_:

        print(f'Oops, exception =) : {repr(err_)}') 

        input('Press Enter to exit...')

        return False   

    return True


file_number = 0

while drop_file(len(block)*2*GB, file_number):
    
    if not file_number % 2:
        
        print(file_number)
        
    file_number += 1

print(new_free_size := shutil.disk_usage('/').free)  # bytes

drop_file(new_free_size, file_number)

input(f'''Free space on disk \"{disk}\", Kb: {shutil.disk_usage('/').free / KB}''')
