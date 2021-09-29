score = []
sc = 0

print("점수를 입력하세요. 0을 입력하면 종료합니다.")

while True:
    sc = int(input("점수: "))
    if sc == 0:
        break
    score.append(sc)

print("현재 입력된 점수는")
print(score, "이고, 모두", len(score), "개 입니다.\n")

select = 0
i, v, c = 0, 0, 0

while True:
    print("리스트 연습")
    print("0. exit")
    print("1. insert")
    print("2. sort")
    print("3. reverse")
    print("4. index")
    print("5. remove")
    print("6. del")
    print("7. count")
    select = int(input("원하는 번호를 선택하세요: "))

    if select == 0:
        break

    elif select == 1:
        i = int(input("insert할 위치: "))
        v = int(input("insert할 값: "))
        score.insert(i, v)
        print(score)
    
    elif select == 2:
        score.sort()
        print(score)

    elif select == 3:
        score.reverse()
        print(score)

    elif select == 4:
        v = int(input("찾고 싶은 값: "))
        idx = score.index(v)
        print(score)
        print("%d는 %d번째 위치하고 있습니다." %(v, i))

    elif select == 5:
        v = int(input("삭제하고 싶은 값: "))
        score.remove(v)
        print(score)

    elif select == 6:
        i = int(input("삭제하고 싶은 위치: "))
        del(score[i])
        print(score)

    elif select == 7:
        v = int(input("갯수를 알고 싶은 값: "))
        c = score.count(v)
        print(score)
        print("%d는 %d번 나옵니다." %(v, c))

end = input("프로그램을 종료하려면 Enter을 눌러주세요...")