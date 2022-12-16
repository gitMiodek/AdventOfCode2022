# Is tree visable? outside the edge
# 1. Its visable whent is on the edge
# 2. its visable from one side if there ar no trees higher from that sight
# 3. Count how many trees are visable, no matter from how many sides


#
with open('task8.txt', 'r') as f:
    # CREATE BOARD
    board = []
    for line in f:
        row = list(map(int, list(line.strip())))
        board.append(row)
    #print(board)

    n_cols = len(board[0])
    m_rows = len(board)

    n_trees_on_edges = 2 * m_rows + 2 * (n_cols - 2)
    #print(n_trees_on_edges)

    visible = set()
    # go right
    def find_right(value,x,y,board):
        score = 0
        for i in range(x + 1, len(board[0])):
            score += 1
            if board[i][y] >= value:
                return False, score
        return True, score


    def find_left(value, x, y, board):
        score = 0
        for i in range(x - 1, -1, -1):
            score +=1
            if board[i][y] >= value:
                return False, score
        return True, score


    def find_top(value, x, y, board):
        score = 0
        for i in range(y - 1, -1, -1):
            score += 1
            if board[x][i] >= value:
                return False, score
        return True,score


    def find_bot(value, x, y, board):
        score = 0
        for i in range(y + 1, len(board)):
            score += 1
            if board[x][i] >= value:
                return False, score
        return True, score



    inside_visible = 0
    score = 0
    for x in range(1, m_rows - 1):
        for y in range(1, n_cols - 1):
            value = board[x][y]

            b, score_bot = find_bot(value, x, y, board)
            l, score_left = find_left(value, x, y, board)
            r, score_right = find_right(value, x, y,board)
            t, score_top = find_top(value, x, y,board)
            if b or l or r or t:
                inside_visible += 1
            tmp = score_top * score_bot * score_left * score_right
            score = max(score, tmp)


    print(inside_visible + n_trees_on_edges)
    print(score)

