# In how many assignment pairs does one range fully contain the other?


def camp_cleanup(filepath: str, second_task=False):
    with open(filepath, 'r') as f:
        if not second_task:
            score = 0

            for line in f:
                x = line.strip().split(',')
                # print(x)
                pair_1 = x[0].split('-')
                pair_2 = x[1].split('-')
                beg_1, end_1, beg_2, end_2 = int(pair_1[0]), int(pair_1[1]), int(pair_2[0]), int(pair_2[1])
                # print(beg_1)
                # print(beg_2)
                # print(end_1)
                # print(end_2)
                if beg_1 <= beg_2 and end_1 >= end_2 or beg_2 <= beg_1 and end_2 >= end_1:
                    score += 1
                # print(score)
        else:
            #in how many assigments overlaping happens
            score = 0
            for line in f:
                x = line.strip().split(',')
                # print(x)
                pair_1 = x[0].split('-')
                pair_2 = x[1].split('-')
                beg_1, end_1, beg_2, end_2 = int(pair_1[0]), int(pair_1[1]), int(pair_2[0]), int(pair_2[1])
                if (
                        (beg_1 >= beg_2 and beg_1 <= end_2)
                        or (end_1 >= beg_2 and end_1 <= end_2)
                        or (beg_2 >= beg_1 and beg_2 <= end_1)
                        or (end_2 >= beg_1 and end_2 <= end_1)
                ):
                    score += 1

    return score


def main():
    print(camp_cleanup('task4.txt'))
    print(camp_cleanup('task4.txt',second_task=True))


if __name__ == '__main__':
    main()
