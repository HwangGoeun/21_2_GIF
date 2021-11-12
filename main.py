
from tkinter import *
import serial
from time import sleep
import time

face_check = 'N'

################################################################################################
# 통신 관련 코드
################################################################################################
'''
UART 정의
'''

faceT = 0x00 #얼굴 인식 성공
faceF = 0x01 #얼굴 인식 실패

FACE = 0xf4 #얼굴 인식 part

uart_header = [0x55, 0x66] #유아트 header
# ser = serial.Serial ("/dev/ttyS0", 115200) # 여기서 막혔습니다 !!!!

################################################################################################
################################################################################################

################################################################################################
# 함수 코드
################################################################################################
'''
Frame 전환용 함수
'''

def dis_clockFrame() :
    clockBtn.pack_forget()
    btn.pack_forget()
    infoFrame.pack_forget()
    startFrame.pack_forget()
    motorFrame.pack_forget()
    clockFrame.pack()

    face_check = input("input face_check : ")
    if(face_check == 'Y') :
        go_startFrame()
    else :
        dis_clockFrame()

def go_startFrame() :
    clockBtn.pack_forget()
    clockFrame.pack_forget()
    infoFrame.pack_forget()
    motorFrame.pack_forget()
    btn.pack_forget()
    clockBtn.pack(side = BOTTOM)
    startFrame.pack()

def go_infoFrame() :
    clockBtn.pack_forget()
    clockFrame.pack_forget()
    startFrame.pack_forget()
    motorFrame.pack_forget()
    btn.pack(side = BOTTOM)
    infoFrame.pack()

def go_motorFrame() :
    clockBtn.pack_forget()
    clockFrame.pack_forget()
    startFrame.pack_forget()
    infoFrame.pack_forget()
    btn.pack(side = BOTTOM)
    motorFrame.pack()
################################################################################################
'''
clockFrame 관련 함수
'''

def clock() :
   live_T = time.strftime("%H:%M:%S")
   clock_width.config(text=live_T)
   clock_width.after(200, clock) # .after(지연시간{ms}, 실행함수)
################################################################################################
'''
infoFrame 관련 함수
'''

# 체크 박스 선택 여부 확인
def c11_check() :
    print("checkVar11 =", checkVar11.get())

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

################################################################################################
'''
motorFrame 관련 함수
'''

# Motor 상승
def motor_up() :
    '''
    send_data = uart_header
    send_data.append(FACE)
    send_data.append(faceT)
    ser.write(send_data)
    print(send_data)
    send_data = []
    '''
    print("모터 상승 버튼 시 작동되는 함수입니다. 아직 시리얼 통신은 안 해봤어요")

################################################################################################
################################################################################################

################################################################################################
# GUI 코드
################################################################################################
'''
GUI 화면 설정
'''

win = Tk() # GUI 생성 
win.title("21_2_GIF_moving2") #상단의 타이틀 지정
win.geometry("640x640") # 크기 설정 (640x640)
################################################################################################
'''
startFrame(시작 화면) 코드
'''

startFrame = Frame(win) #시작 화면 설정 화면 프레임

addBtn = Button(startFrame, text = "옷 정보 추가하기", command = go_infoFrame)
recBtn = Button(startFrame, text = "옷 추천 받기", command = go_motorFrame)
addBtn.config(width = 50, height = 5)
recBtn.config(width = 50, height = 5)

addBtn.grid(pady=100)
recBtn.grid(pady=10)

startFrame.pack()
################################################################################################
'''
infoFrame(옷 정보 설정 화면) 코드
'''

#프레임 설정
infoFrame = Frame(win) # 옷 정보 설정 화면 프레임


# 체크박스 상태 확인용 변수 설정
# 1 = 계절 / 2 = 날씨 (예: checkVar1n은 계절 관련, checkVar2n은 날씨 관련)
checkVar11 = IntVar() # 봄, 가을
checkVar12 = IntVar() # 여름
checkVar13 = IntVar() # 겨울

checkVar21 = IntVar() # 더울 때
checkVar22 = IntVar() # 추울 때
checkVar23 = IntVar() # 보통 때
checkVar24 = IntVar() # 비 올 때

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

################################################################################################
'''
motorFrame(모터 작동 스위치 화면) 코드 
'''

#프레임 설정
motorFrame = Frame(win) # 옷 정보 설정 화면 프레임

# 버튼 생성
mtBtn = Button(motorFrame, text = "UP", command = motor_up)
mtBtn.config(width=30, height=5)

mtBtn.grid(pady = 250)
'''
startFrame 가는 버튼
'''

btn = Button(win, text = "go to home", command = go_startFrame)
btn.config(width = 20, height = 3)
btn.pack(side = BOTTOM)

################################################################################################
'''
clockFrame 가는 버튼
'''

clockBtn = Button(win, text = "QUITE", command = dis_clockFrame)
clockBtn.config(width = 20, height = 3)

clockBtn.pack(side = BOTTOM)

################################################################################################
'''
clockFrame(시계 화면) 코드
'''

clockFrame = Frame(win)
clockFrame.pack()

txt_width = Label(clockFrame, text="현재 시간")
txt_width.pack()

clock_width = Label(clockFrame, font=("Times",60,"bold"), bd=8)
clock_width.config(width=20, height=3)
clock_width.pack()

clock()

clockFrame.pack()
dis_clockFrame()
################################################################################################

win.mainloop() # GUI가 보이고 종료될때까지 실행함

################################################################################################
################################################################################################