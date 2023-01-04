# Be careful ! Analyze the code first!
import os
import shutil
from time import time


KB = 1024
MB = 1024 * KB
GB = 1024 * MB

# If run in root of disk
disk = os.fspath(os.path.abspath(os.getcwd()))

# create folder(bin-free-bin) for junk if it is not available
os.makedirs(os.fspath('bin-free-bin'), exist_ok=True)

# path for junk
ballast_files_path = os.fspath(os.path.join(disk, 'bin-free-bin'))

print('All freespace will be filled on the disk:')
print(f'{disk=}')
print(f'{ballast_files_path=}')
print(f'Free space on disk \"{disk}\", Kb: ', shutil.disk_usage('/').free / KB)

# free space on disk
free_size = shutil.disk_usage('/').free  # bytes

block = '0'

big_files_count = free_size // (2 * GB)

small_file_size = free_size % (2 * GB)

print(f'Amount of 2GB files: {big_files_count},')

print(f'And 1 file {small_file_size} byte. (~{small_file_size // MB} MB)')

if input('Press Enter to continue or type something to exit.'):
    exit()

def drop_file(cx: int, file_s_number: int) -> bool:
    """Write 0 blocks to file with file's number in file name."""
    file = os.fspath(os.path.join(ballast_files_path, f'F{file_s_number}.data'))
    
    start = time()

    try:

        with open(file, 'wb') as fh:

            fh.write(bytes(block*cx, 'utf-8'))

    except Exception as err_:

        print(f'Oops, exception =) : {repr(err_)}') 

        #  input('Press Enter to exit...')

        return False   

    print(f'Done in {int((time() - start)//60)} m {int((time() - start)%60)} s\n:')

    return True


file_number = 0  # number for filename (counter)

# Recording files ...
while drop_file(len(block)*2*GB, file_number):
    
    # if not file_number % 2:
    #     print(f'{file_number=}')

    print(f'{file_number=} created.\n')
    file_number += 1

    if file_number == big_files_count:
        break

print(new_free_size := shutil.disk_usage('/').free)  # bytes

drop_file(new_free_size, file_number)

input(f'''Free space on disk \"{disk}\", Kb: {shutil.disk_usage('/').free / KB}''')
