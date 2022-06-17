from multiprocessing.connection import answer_challenge
from tkinter import *

#창만들기
window = Tk()
window.geometry("260x70")
window.resizable(width=False, height=False)

"""
#window.geometry("500x400")
#window.geometry("260x70")
"""

#창 이름
window.title("Factorial")

#레이블 선언
label1 = Label(window, text="Factorial Calculator")
label1.pack()

label3 = Label(window, text="")
label3.pack(side= "bottom")
answer = ""
expression = ""


#입력칸 만들기
inputw = Entry(window)
inputw.place(x=5, y=29)

#함수 지정
def ent_p():
    
    global answer
    global expression
    global label3



    answer = ""
    expression = ""

    a = str(inputw.get())
    a = int(a.replace(a[a.find("!")], ""))
    sums = 1
    count = 0

    for i in range(1, a+1):
        sums *= i
        count += 1
        if a-count >= 1:
            print("{}x".format(i, sums), end="")
            expression += "{}x".format(i, sums)
        else:
            print("{}=".format(i), end="")
            expression += "{}=".format(i)

    answer = sums
    print("{}\n".format(sums))
    print("answer : {}".format(sums))
    print(expression, answer)
    label3.config(text="Expression: {}{}".format(expression, answer))
    label3.pack(side="bottom")


#확인 버튼 만들기
button1 = Button(window, text="CALCULATE")
button1.config(command = ent_p) 
button1.place(x=170, y=24)

window.mainloop()


"""
만들어야 할 것: RESET 버튼 만들기( 지금의 오류:
                    다른 식을 넣고 계산하면 label3가 이상하기 표현됨) ㅠㅠ
                    """
