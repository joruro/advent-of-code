
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name


class Directory:
    def __init__(self, name, parent_directory=None):
        self.size = 0
        self.name = name
        self.directories = {}
        self.files = {}
        self.parent_directory = parent_directory

    def add_file(self, file):
        self.size += file.get_size()
        self.files[file.get_name()] = file

    def add_directory(self, directory):
        self.size += directory.get_size()
        self.directories[directory.get_name()] = directory

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def is_root(self):
        return self.parent_directory is None

    def get_parent(self):
        return self.parent_directory


def total_size(input):
    disk_space = 70000000
    update_size = 30000000

    current_dir = None

    dir_sizes = []

    for command in input:
        command = command.strip()
        if command.startswith('$ cd') and command != '$ cd ..':
            current_dir_name = command.split(' ')[2]
            current_dir = Directory(current_dir_name, current_dir)

        if command == '$ cd ..':
            parent_dir = current_dir.get_parent()
            parent_dir.add_directory(current_dir)
            dir_sizes.append(current_dir.get_size())
            current_dir = parent_dir

        if not command.startswith('$') and not command.startswith('dir'):
            file_size, file_name = command.split(" ")
            file_size = int(file_size)
            current_dir.add_file(File(file_name, file_size))

    while not current_dir.is_root():
        parent_dir = current_dir.get_parent()
        parent_dir.add_directory(current_dir)
        dir_sizes.append(current_dir.get_size())
        current_dir = parent_dir
    
    size_needed = (current_dir.get_size() + update_size) - disk_space
    dir_sizes = sorted(dir_sizes)
    for size in dir_sizes:
        if size_needed <= size:
            return size
    return 0


f = open('src_old/2022/days/07/input.txt', 'r')
lines = f.readlines()
r = total_size(lines)

print(r)
