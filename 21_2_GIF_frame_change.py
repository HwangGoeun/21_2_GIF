#프레임 전환 테스트

from tkinter import *

# 체크 박스 선택했을 때의 함수
def c11_check() :
    print("checkVar11 =", checkVar11.get())
    #if(checkVar1 == 0)

def c12_check() :
    print("checkVar12 =",checkVar12.get())
    
def c13_check() :
    print("checkVar13 =",checkVar13.get())

def c21_check() :
    print("checkVar21 =",checkVar21.get())

def c22_check() :
    print("checkVar22 =",checkVar22.get())
    
def c23_check() :
    print("checkVar23 =",checkVar23.get())
    
def c24_check() :
    print("checkVar24 =",checkVar24.get())

# pack 테스트용 함수
def btnClick() :
    global btnVar
    if (btnVar == 0) :
        print("btnVar = ", btnVar)
        infoFrame.pack()
        btnVar += 1
    elif (btnVar == 1) :
        print("btnVar =", btnVar)
        infoFrame.pack_forget()
        btnVar += 1
    else :
        btnVar = 0
        btnClick()

###################################################

# GUI 화면 설정
win = Tk() # GUI 생성 
win.title("21_2_GIF_moving2") #상단의 타이틀 지정
win.geometry("640x640") # 크기 설정 (640x640)

#프레임 설정
infoFrame = Frame(win) # 옷 정보 설정 화면 프레임

# 체크박스 상태 확인용 변수 설정
# 1 = 계절 / 2 = 날씨
checkVar11 = IntVar()
checkVar12 = IntVar()
checkVar13 = IntVar()

checkVar21 = IntVar()
checkVar22 = IntVar()
checkVar23 = IntVar()
checkVar24 = IntVar()

# 체크 박스 출력
# 계절 설정 체크 박스
lab1 = Label(infoFrame, text = "무슨 계절에 입나요?")
c11 = Checkbutton(infoFrame, text = "봄, 가을", variable = checkVar11, command = c11_check)
c12 = Checkbutton(infoFrame, text = "여름", variable = checkVar12, command = c12_check)
c13 = Checkbutton(infoFrame, text = "겨울", variable = checkVar13, command = c13_check)

lab1.pack()
c11.pack()
c12.pack()
c13.pack()

# 계절 설정 체크 박스
lab2 = Label(infoFrame, text = "어떨 때 입고 싶은가요?")
c21 = Checkbutton(infoFrame, text = "더울 때", variable = checkVar21, command = c21_check)
c22 = Checkbutton(infoFrame, text = "추울 때", variable = checkVar22, command = c22_check)
c23 = Checkbutton(infoFrame, text = "보통 때", variable = checkVar23, command = c23_check)
c24 = Checkbutton(infoFrame, text = "비 올 때", variable = checkVar24, command = c24_check)

lab2.pack()
c21.pack()
c22.pack()
c23.pack()
c24.pack()

# 테스트용 버튼
btnVar = 0
btn = Button(win, text = "click", command = btnClick)
btn.pack()

win.mainloop() # GUI가 보이고 종료될때까지 실행함