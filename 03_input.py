#输入一个分数(score)
#及格/优秀（>=90），良好（>=80），及格（>=60）
#不及格

score=float(input("请输入你的分数："))
if score>=60:
    if score>=80:
        if score>=90:
            print("优秀")
        else:
            print("良好")
    else:
        print("及格")
else:
    print("不及格")