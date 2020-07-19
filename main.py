import cv2

FPS = 30
FILE_PATH = './resource/splatoon_hoko.mp4'


def calc(file_path, fps):
    cap = cv2.VideoCapture(file_path)
    if not cap.isOpened():
        return

    frame_len = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(frame_len)
    for n in range(0, frame_len, fps):
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        if not ret:
            break
        count_frame = frame[79: 79 + 90, 309: 309 + 670]
        cv2.imwrite('dist/mov_%s.jpg' % (n), count_frame)


if __name__ == "__main__":
    calc(FILE_PATH, FPS * 10)
