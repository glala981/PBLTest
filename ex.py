import cv2

# 내장카메라 또는 외장 카메라에서 영상받아오기
# 0은 카메라의 장치 번호를 의미, 노트북을 이용할 경우 내장카메라가 존재하므로
# 카메라 번호는 0이됨 (카메라추가 연결의 경우 n까지 변화가능/0
capture = cv2.VideoCapture(0)

# capture.set(프레임의 너비와 높이 등의 속성, 너비와 높이의 값)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 얼굴 인식 캐스케이드 파일 읽는다
face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml')

# while로 영상 출력을 반복하는 구문
while (True):
    # capture.read()를 이용하여 카메라의 상태 및 프레임을 받아오기

    # ret은 카메라의 상태가 저장되며 정상 동작할 경우 true를 반환
    # 작동하지 않으면 false반환

    # frame은 현재 프레임에 저장
    # 한마디로 정리하면 frame별로 capture한다
    ret, frame = capture.read()

    # frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 인식된 얼굴 갯수를 출력
    print(len(faces))

    # 인식된 얼굴에 사각형을 출력한다
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # cv2.imshow("윈도우 창 제목", 이미지)로 윈도우 창에 이미지 띄우기
    # 키입력이 있을 때 까지 while문 반복
    cv2.imshow('frame', frame)
    # cvw.waitkey(time) time마다 키 입력 상태 받아옴
    # ord('q'):break는 q가 입력될때 while문 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 카메라 장치에서 받아온 메모리해제
capture.release()
# 모든 윈도우창 종료
cv2.destroyAllWindows()