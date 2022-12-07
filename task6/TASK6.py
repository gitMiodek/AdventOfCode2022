# how to be sure that 4 consequences differ from each other
def first_task(filename: str) -> int:
    with open(filename, 'r') as f:
        line = f.readlines()
        i, j = 0, 4
        while j <= len(line[0]):
            tmp = line[0][i:j]
            d = {}
            for letter in tmp:
                try:
                    d[letter] += d[letter]
                except KeyError:
                    d[letter] = 1
            if max(d.values()) == 1:
                # print('found consequence')
                break

            i += 1
            j += 1
        return j


def second_task(filename: str) -> int:
    with open(filename, 'r') as f:
        line = f.readlines()
        i, j = 0, 14
        while j <= len(line[0]):
            tmp = line[0][i:j]
            d = {}
            for letter in tmp:
                try:
                    d[letter] += d[letter]
                except KeyError:
                    d[letter] = 1
            if max(d.values()) == 1:
                # print('found consequence')
                break

            i += 1
            j += 1
        return j


if __name__ == '__main__':
    # Test 1st task
    assert first_task('test6.txt') == 11
    # run with 1st task input
    print(first_task('task6.txt'))
    # test 2nd task
    assert second_task('test6.txt') == 26
    # run with 2nd task input
    print(second_task('task6.txt'))
