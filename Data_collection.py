import cv2
import mediapipe as mp
import numpy as np
import time
import csv

# 손 모델 로딩
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 반복할 시간 설정 (초)
duration = 5

# 프로그램 시작 시간 기록
start_time = time.time()

# 카운터 초기화
capture_count = 0

# 반복 실행
while (time.time() - start_time) < duration:
    # 프레임 캡처
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame from webcam.")
        exit()

    # OpenCV를 사용하여 BGR 이미지를 RGB로 변환
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Mediapipe를 사용하여 양손 감지
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 감지된 손의 landmark를 사용하여 bounding box 좌표 계산
            landmarks = hand_landmarks.landmark
            x_coords = [landmark.x for landmark in landmarks]
            y_coords = [landmark.y for landmark in landmarks]

            # Calculate bounding box size
            x_min, y_min = min(x_coords), min(y_coords)
            x_max, y_max = max(x_coords), max(y_coords)
            box_width = x_max - x_min
            box_height = y_max - y_min

            # Check if the hand is left or right
            if landmarks[mp_hands.HandLandmark.WRIST].x < 0.5:
                hand_type = "left"
            else:
                hand_type = "right"

            # Calculate bounding box size
            x_min, y_min = min(x_coords), min(y_coords)
            x_coords_shifted = [x - x_min for x in x_coords]
            y_coords_shifted = [y - y_min for y in y_coords]

            # Normalize coordinates by box width and height
            x_coords_normalized = [x * 100 / box_width for x in x_coords_shifted]
            y_coords_normalized = [y * 100 / box_height for y in y_coords_shifted]

            # Save the normalized coordinates to a CSV file
            csv_file_path = f"{hand_type}_hand_landmarks_0_{capture_count}.csv"
            with open(csv_file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['X', 'Y'])
                for x, y in zip(x_coords_normalized, y_coords_normalized):
                    csv_writer.writerow([x, y])

    # Display the frame
    cv2.imshow("Hand Detection", frame)

    # Increase the capture count
    capture_count += 1

    # Wait for 1 millisecond
    cv2.waitKey(1)

# 사용된 자원 해제
cap.release()
cv2.destroyAllWindows()