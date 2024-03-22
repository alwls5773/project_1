## Hand exercise services for preventing alzheimer

#### 목적: 치매 예방을 도와주는 손 운동 서비스 제작
#### 사용툴: numpy, opencv2, tensorflow, pymysql, requests, FastAPI, Amason RDS, MediaPipe

### 시스템 아키텍처
![image](https://github.com/alwls5773/project_1/assets/66359601/f19871a7-d928-41ac-9653-1ff8d1e873f0)

### 서버 구축: main.py 
라이브러리: 
![image](https://github.com/alwls5773/project_1/assets/66359601/abc8211f-8fd0-4439-a75d-c5ad3e4ee665)

#### 데이터 전처리: hand_tracking.py
라이브러리:

#### camera, LED 구동: rasberry_pi.py
라이브러리:

#### 웹: static, templates
라이브러리: 
![image](https://github.com/alwls5773/project_1/assets/66359601/fe64ed18-e9ce-48c6-9d79-9b0df04df1da)

### 데이터베이스 구성: Database.ipynb
라이브러리: 
![image](https://github.com/alwls5773/project_1/assets/66359601/ae8d3021-f2d2-4619-963b-05934646406f)

### 모델 선정: best_model.ipynb
라이브러리: 
1. CNN
- epochs =100, batch_size=40, learning_rate=0.0001
- 테스트 세트 손실: 0.015 | 테스트 세트 정확도: 0.99
- 총 파라미터 개수: 13440

![image](https://github.com/alwls5773/project_1/assets/66359601/a778a0f7-90ff-49bf-83e2-1319568bcc76)


2. LSTM
- epochs=100, batch_size=40, learning_rate=0.0001
- 테스트 세트 손실: 0.020678449422121048
- 테스트 세트 정확도: 0.9963924884796143
- 총 파라미터 개수: 29799

![image](https://github.com/alwls5773/project_1/assets/66359601/a4f6d393-2fbb-438a-8a58-998016721fd9)


3. DNN(MLP)
- epochs=100, batch_size=40, learning_rate=0.0001
- 테스트 세트 손실: 0.010606429539620876
- 테스트 세트 정확도: 0.9992784857749939
- 총 파라미터 개수: 16071

![image](https://github.com/alwls5773/project_1/assets/66359601/15e326a4-48cf-4a37-b08b-9056f5cca002)

4. GRU
- epochs=100, batch_size=40, learning_rate=0.0001
- 테스트 세트 손실: 0.01709848828613758
- 테스트 세트 정확도: 0.9978355169296265
- 총 파라미터 개수: 22695

![image](https://github.com/alwls5773/project_1/assets/66359601/f55078a2-d854-4e77-b8ff-cf91d042d067)

![image](https://github.com/alwls5773/project_1/assets/66359601/57cd6f73-372c-41d4-bf36-1dcf4cf2b340)

- 네 가지 모델 모두 정확도가 0.99 이상으로 높음.
- DNN이 타 모델에 비하여 정확도 및 손실도의 측면에서 빠른 수렴이 일어남. 즉, 짧은 시간에 최적의 솔루션으로 수렴이 가능하다는 뜻임.
- DNN의 총 파라미터 개수는 16071으로, LSTM과 GRU에 비하여 모델이 가벼움.
- DNN이 타 모델에 비하여 진동이 덜 한 편임.

#### 높은 정확도, 빠른 수렴, 적은 파라미터 수, 적은 진동폭을 고려했을 때, DNN모델이 가장 적합하다고 판단함.
