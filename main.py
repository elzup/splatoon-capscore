import cv2
import datetime
import time

# VideoCapture オブジェクトを取得
# キャプボの他にWebカメラなど接続している場合は他の数字を指定する必要があるかも
capture = cv2.VideoCapture(0)
print(capture.isOpened())
capture.set(3, 1920)
capture.set(4, 1080)

count = 0

while(True):
    ret, frame = capture.read()
    cv2.imshow('frame', frame)
    count += 1
    print(count)
    if count % 60 == 0:
        dt_now = datetime.datetime.now()
        # 1280 * 720のキャプチャ画像に変換、保存
        resized = cv2.resize(frame, (1280, 720))
        # 所定のフォルダにjpgで保存
        cv2.imwrite('./save.jpg', resized)

    time.sleep(1)
    # "q"キー または ctrl + C でキャプチャ停止
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()