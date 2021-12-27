
def isValidChessBoard(dic):
    blackCount = 0
    whiteCount = 0
    whitePawns = 0
    blackPawns = 0
    blackKing = 0
    WhiteKing = 0
    for place,pieace in dic.items():
        if place[0] < '1' or place[0] > '9' or place[1] < 'a' or place[1] > 'h':
            print("not a valid board place" , place)
            break

        if pieace[0] == 'b':
            if pieace[1] == 'k':
                blackKing += 1
            if pieace[1] == 'p':
                blackPawns += 1
            blackCount += 1
        else:
            if pieace[1] == 'k':
                WhiteKing += 1
            if pieace[1] == 'p':
                whitePawns += 1
            whiteCount += 1

        if WhiteKing > 1 or blackKing > 1 or whitePawns > 8 or blackPawns > 8 or whiteCount > 16 or blackCount > 16 :
            print("not a valid pieace config")
            break
    else:
        print("Valid Board")

d = eval(input())
isValidChessBoard(d)


         