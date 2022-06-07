## ========================================================================== ##

# if elif else
print()
print(">> if elif else")
# if 조건:
    # if 조건 만족시 실행 로직
# elif 조건:
    # elif 조건 만족시 실행 로직
# else:
    # if, elif 조건 불 만족시 실행 로직


condition = True

if condition:
    print("if loop") # <--
elif condition:
    print("elif loop")
else:
    print("else loop")

###############################################



# 조건문 안에 조건문 들여 쓰기
print()
print(">> inner if")
# if 조건:
    # if 조건:
        # if 조건 만족시 실행 로직
    # else 조건:
        # if 조건 불 만족시 실행 로직
# else:
    # if 조건 불 만족시 실행 로직

foo = True
bar = True

if foo:
    if bar:
        print("if foo bar") # <--
    else:
        print("if bar")
else:
    if bar:
        print("else if bar")
    else:
        print("else bar")

###############################################



# if in
print()
print(">> if in")
# if 검색할 데이터 in 대상 데이터:
    # if 조건 만족시 실행 로직
# else:
    # if 조건 불 만족시 실행 로직

fruit = ["apple", "banana", "kiwi"]
choice = "apple"
notChoice = "mango"

if choice in fruit:
    print("choice in fruit")
else:
    print("choice not in fruit")

###############################################


## ========================================================================== ##



# for in
print()
print(">> for in")
# for 순차적 묶음 데이터 in 데이터 묶음:
    # 순회 로직...

gugudan = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in gugudan:
    print("2 * ", i, " = ", 2 * i)

###############################################



# for in break
print()
print(">> for in break")
# for 순차적 묶음 데이터 in 데이터 묶음:
    # if 조건:
        # break <-- 멈추고 for문 탈출

for i in gugudan:
    if i == 5:
        print("for in break !!!")
        break #<-- 5번째에서 멈추고 for문 탈출
    print("3 * ", i, " = ", 3 * i)

###############################################



# for in continue
print()
print(">> for in continue")
# for 순차적 묶음 데이터 in 데이터 묶음:
    # if 조건문:
        # continue <-- 멈추고 다음 for문 진행

for i in gugudan:
    if i == 5:
        print("for in continue !!!")
        continue # <-- 5번째에서 멈추고 다음 for문 실행
    print("4 * ", i, " = ", 4 * i)

###############################################



# while
print()
print(">> while")
# while 조건:
    # 조건 만족할 때 까지 실행

count = 1
while count <= 10:
    print("count : ", count)
    count = count + 1

###############################################



# while break
print()
print(">> while break")
# while 조건:
    # if 조건:
        # break

count = 1
while True:
    if count >= 15:
        print("while break !!!")
        break
    print("count : ", count)
    count = count + 1

###############################################


# while continue
print()
print(">> while continue")
# while 조건:
    # if 조건:
        # break
count = 0
while True:
    count = count + 1
    if count == 5:
        print("while continue !!!")
        continue
    print("count : ", count)
    if count >= 15:
        break