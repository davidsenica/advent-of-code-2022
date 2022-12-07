FILE = 'data/day7.txt'


class Dir:
    def __init__(self, name):
        self.parent_dir = None
        self.dir_name = name
        self.dir_size = 0
        self.children = []
        self.files = []

    def add_files(self, file, size):
        self.dir_size += size
        self.files.append((file, size))
        self._add_to_parent(size)

    def _add_to_parent(self, size):
        if self.parent_dir is not None:
            self.parent_dir.dir_size += size
            self.parent_dir._add_to_parent(size)

    def add_child(self, name):
        child = Dir(name)
        child.parent_dir = self
        self.children.append(child)

    def flatten_structure(self):
        flatten_structure = [(self.dir_name, self.dir_size)]
        for child in self.children:
            flatten_structure += child.flatten_structure()
        return flatten_structure


def build_directory_structure():
    with open(FILE) as f:
        f.readline()
        root = Dir('/')
        current_dir = root
        line = f.readline().rstrip()
        while line != '':
            params = line.split(' ')
            if params[0] == '$':
                if params[1] == 'cd':
                    if params[2] == '..':
                        current_dir = current_dir.parent_dir
                    else:
                        for child in current_dir.children:
                            if child.dir_name == params[2]:
                                current_dir = child
            else:
                file_dir = line.rstrip().strip().split(' ')
                if file_dir[0] == 'dir':
                    current_dir.add_child(file_dir[1])
                else:
                    current_dir.add_files(file_dir[1], int(file_dir[0]))
            line = f.readline().rstrip()
    return root


def first_problem_solution():
    structure = build_directory_structure()
    return sum(d[1] for d in filter(lambda x: x[1] <= 100000, structure.flatten_structure()))


def second_problem_solution():
    structure = build_directory_structure()
    need_to_delete = 30000000 - (70000000 - structure.dir_size)
    for s in sorted(structure.flatten_structure(), key=lambda x: x[1]):
        if s[1] > need_to_delete:
            return s[1]
    return None


def main():
    print(f'Solution to first problem is {first_problem_solution()}')
    print(f'Solution to second problem is {second_problem_solution()}')
