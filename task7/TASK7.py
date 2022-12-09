##### TASK GOALS #######
# 1. loop over input lines -> there are three main commands
#     a) cd (dir) -> change dir to a new one -> new current path, absolute_path +=current_path
#     b) cd .. -> come back to previous dir -> new current path, absolute_path.pop() -> it removes previous curr path
#     c) ls -> after ls file sizes can be gathered and d[curr_path] += item_size including the fact that it will be
# also added to parents directory size!!!
#
# 2. create dir.key = current path and its value as sum of files size
#     a) current path as a string
#     b) absolute path as a list of current paths
# 3. check sizes of directories

def not_in_dir(path, directory):
    if path not in directory.keys():
        directory[path] = 0


def parser(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        directories = {}
        current_path = ''
        absolute_path = []
        for i, line in enumerate(f):
            if line.startswith("$ cd /"):
                current_path = '/'
                absolute_path.append(current_path)
                not_in_dir(path=current_path, directory=directories)
                # print(
                #     f"Line {i}, absolute_path = {absolute_path}\ncurrent_path = {current_path}\n "
                #     f"directories = {directories}")

            elif line.startswith("$ cd") and ".." not in line and "/" not in line:
                if current_path == '/':
                    current_path += line.strip().split()[-1]
                else:
                    current_path += f'/{line.strip().split()[-1]}'
                absolute_path.append(current_path)
                not_in_dir(path=current_path, directory=directories)
                # print(
                #     f"Line {i}, absolute_path = {absolute_path}\ncurrent_path = {current_path}\n"
                #     f" directories = {directories}")
            elif line.startswith("$ cd .."):
                absolute_path.pop()
                current_path = current_path[:-2]
                # print(
                #     f"Line {i}, absolute_path = {absolute_path}\ncurrent_path = {current_path}\n "
                #     f"directories = {directories}")
            elif line[0].isdigit():
                for path in absolute_path:
                    directories[path] += int(line.split()[0])
        return directories


def first_task(filepath: str) -> int:
    d = parser(filepath)
    item_size = 0
    for value in d.values():
        if value < 100000:
            item_size += value
    return item_size


def second_task(filepath: str) -> int:
    d = parser(filepath)
    max_size = 70000000
    curr_size = d['/']
    required_free_space = 30000000
    possible_dirs_values = [value for value in d.values() if max_size - curr_size + value > required_free_space]
    return min(possible_dirs_values)


if __name__ == "__main__":
    # test 1st task
    assert first_task('test7.txt') == 95437
    print(first_task('task7.txt'))
    # test 2nd task
    assert second_task('test7.txt') == 24933642
    print(second_task('task7.txt'))
