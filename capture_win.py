import os
from io import BytesIO
from PIL import Image
import keyboard
from pynput.mouse import Listener as mouse
import pyautogui as pag
import time
import shutil

dir_path='./save_file/'
temp_path=dir_path+'temp.png'
def settings():
    if not os.path.isdir(dir_path):
        print("저장 디렉토리가 없습니다. 새로 생성합니다...")
        os.makedirs(dir_path)
def mouse_capture():
    return pag.position()

settings()
i=1
print("프로그램 실행 완료!")
while True:
    t=0
    fail=0
    while True:
        if t==0:
            print(i,"/ 첫 번째 포인트 대기 중")
            t+=1
        if keyboard.is_pressed("\\"):
            print("종료합니다.")
            exit()
        if keyboard.is_pressed("["):
            print("자동 입력 값 1 감소 :",end=" ")
            if i<=1:
                print("1")
                continue
            i-=1
            print(i)
            time.sleep(0.2)
        if keyboard.is_pressed("]"):
            i+=1
            print("자동 입력 값 1 증가 :",i)
            time.sleep(0.2)
        if keyboard.is_pressed("="):
            i=1
            print("자동 입력 값 초기화 :",i)
            time.sleep(0.2)
        if keyboard.is_pressed("`"):
            temp_scr=pag.screenshot()
            temp_scr.save(temp_path)
            start=mouse_capture()
            print("첫 번째 포인트 포착 완료",start[0],start[1])
            time.sleep(0.2)
            break
    while True:
        if t==1:
            print("두 번째 포인트 대기 중")
            t=0
        if keyboard.is_pressed("`"):
            fail=1
            break
        if keyboard.is_pressed("\\"):
            end=pag.position()
            print("두 번째 포인트 포착 완료",end[0],end[1])
            time.sleep(0.2)
            break
        
    if fail==0:
        print("파일 저장 중...")
        file_path=dir_path+str(i).zfill(2)+".png"

        img=Image.open(temp_path)
        if (start[0]<end[0]) and (start[1]<end[1]):
            # pag.screenshot(temp_path,region=(start[0],start[1],end[0]-start[0],end[1]-start[1]))
            result=img.crop((start[0],start[1],end[0],end[1]))
        else:
            # pag.screenshot(temp_path,region=(end[0],end[1],start[0]-end[0],start[1]-end[1]))
            print("캡처 실패")
            continue

        output=BytesIO()
        result.convert("RGB").save(output,"PNG")
        result.save(file_path)
        # data=output.getvalue()[14:]
        # output.close()
        # shutil.copyfile(temp_path,file_path)

        print("파일 저장 완료! :",file_path)
        i+=1