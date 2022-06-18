from multiprocessing.connection import answer_challenge
from tkinter.messagebox import showerror
from tkinter import messagebox
from tkinter import *

#창만들기
window = Tk()
window.geometry("270x65")
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
b = ""
error = ""
booltype = False

#입력칸 만들기
inputw = Entry(window)
inputw.place(x=5, y=29)

#함수 지정
def ent_p():
    
    global answer
    global expression
    global error
    global b
    global booltype

    try:
        answer = ""
        expression = ""
        error = ""
        b = ""
        a = str(inputw.get())
        if a.find("!") * -1 == int("-" + str(abs(a.find("!")))):
            a = str(a)
            
            error += str(a[a.find("!")+1:-1]) + a[-1]
            if error == "!":
                booltype = False
            elif len(error) > 0:
                booltype = True
            print(error)
            a = a[0:a.find("!")]
            b = a
            a = int(a)
            sums = 1
            count = 0

            for i in range(1, int(a)+1):
                sums *= i
                count += 1
                if a-count >= 1:
                    #print("{}x".format(i, sums), end="")
                    expression += "{}x".format(i, sums)
                else:
                    #print("{}=".format(i), end="")
                    expression += "{}=".format(i)

                answer = sums
            #print("{}\n".format(sums))
                
            if booltype == False:
                messagebox.showinfo(title="Answer and Expression", message='answer : {}\nexpression: {}{}'.format(sums,expression,answer))
                print("answer : {}".format(sums))
                print("expression :", str(expression), str(answer)+"\n")
            elif booltype == True:
                messagebox.showinfo(title="Answer and Expression", message='answer : {}\nexpression: {}{}\n    error : {}! "{}", {} <= error'.format(sums,expression,answer,b,error,error))
                print("answer : {}".format(sums))
                print("expression :", str(expression), str(answer))
                print('error : {}! "{}", {} <= error'.format(b, error, error) + "\n")
                
                """
                print("\n\n\n", expression) #여기 수정중, 완료(2022/06/18)
                label3.config(text="Expression: {}{}".format(expression, answer))
                label3.pack(side="bottom")
                """
            
        elif a.find("!") * -1 == abs(a.find("!")):
            showerror('ERROR code 1', 'Something is wrong. Check your number\nThe form sould be [ x! ]', parent = window)
        
    except:
        showerror('ERROR code 1', 'Something is wrong. Check your number\nThe form sould be [ x! ]', parent = window)
            

#확인 버튼 만들기
button1 = Button(window, text="CALCULATE")
button1.config(command = ent_p) 
button1.place(x=170, y=24)

window.mainloop()


"""
만들어야 할 것: RESET 버튼 만들기( 지금의 오류:
                    다른 식을 넣고 계산하면 label3가 이상하기 표현됨)
상태: 해결 완료

문제점2: 인풋박스에 숫자를 다음과 같은 형식으로 입력할 시 : x!y, 1!2, 6!2
!가 사라지며 xy, 12, 62등의 숫자로 바뀌게 된다

상태: 해결하지 못함 -> 해결 완료
해결방안: !뒤에있는 문자들을 모두 지우기

해야 할 일: 에러 만들기
상태: 해결 완료
                    """
