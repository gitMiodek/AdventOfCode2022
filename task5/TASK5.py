def parser(filepath: str) -> tuple:
    stack = [[] for i in range(9)]
    instructions = []
    with open(filepath, 'r') as f:

        for i, line in enumerate(f):
            # first parse stacks
            if i < 8:
                for idx in range(0, len(line), 4):

                    if line[idx + 1] != ' ' and line[idx + 1] not in ['[', ']']:
                        # print(line[idx + 1])
                        # print(idx // 4)

                        stack[idx // 4].append(line[idx + 1])
            if i > 9:
                instr = line.strip().split(' ')
                instructions.append(list(map(int, [instr[1], instr[3], instr[5]])))

    # print(stack)
    # print(instructions)
    return stack, instructions


def first_task(stack, instructions):
    # print('#######')
    # print(stack)
    # print('#######')

    for instruction in instructions:
        # print(instruction)
        how_many = instruction[0]
        from_ = instruction[1] - 1
        to = instruction[2] - 1
        for i in range(how_many):
            stack[to].insert(0, stack[from_].pop(0))
        # print(stack)
        # if i > 5:
        #     break

    res = [i[0] for i in stack]
    res = "".join(res)
    print(res)


def second_task(stack, instructions):
    for instruction in instructions:
        # print('####')
        # print(stack)
        # print('#####')
        print(instruction)
        how_many = instruction[0]
        from_ = instruction[1] - 1
        to = instruction[2] - 1
        slice = stack[from_][:how_many]
        slice.reverse()
        stack[to].reverse()
        stack[to] += slice
        stack[to].reverse()
        del stack[from_][:how_many]
        # print('####')
        # print(stack)
        # print('#####')

    res = [i[0] for i in stack]
    res = "".join(res)
    print(res)


if __name__ == '__main__':
    stack, instructions = parser('task5.txt')
    first_task(stack, instructions)
    stack, instructions = parser('task5.txt')
    second_task(stack, instructions)
