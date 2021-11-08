from tkinter import *
import serial
from time import sleep

# UART 정의
faceT = 0x00 #얼굴 인식 성공
faceF = 0x01 #얼굴 인식 실패

FACE = 0xf4 #얼굴 인식 part

uart_header = [0x55, 0x66] #유아트 header
ser = serial.Serial ("/dev/ttyS0", 115200)

#모터 상승 버튼

# Motor 상승
def motor_up() :
    send_data = uart_header
    send_data.append(FACE)
    send_data.append(faceT)
    ser.write(send_data)
    print(send_data)
    send_data = []

###################################################

# GUI 화면 설정
win = Tk() # GUI 생성 
win.title("21_2_GIF_moving2") #상단의 타이틀 지정
win.geometry("640x640") # 크기 설정 (640x640)

# 버튼 생성
btn = Button(win, text = "UP", command = motor_up)
btn.config(width=20, height=2)
btn.pack(anchor = "center")

win.mainloop() # GUI가 보이고 종료될때까지 실행함