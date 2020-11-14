
## 1. 프로젝트 구성
- data
    - train
        - knu
        - none-knu
    - test
        - knu
        - none-knu
- src
    - core
        - dataAdapter.py
        - network.py
        - model @Nullable
    - tool
        - train.py
        - predict.py

## 2. 요구 사항

### 2.1. dataAdapter.py
1. 사진 파일들을 읽는다.
2. 전처리를 한다
    1. 사이즈가 동일하다
    2. 컬러 스케일이 0~1 실수다
3. `train_X, train_y, test_x, test_y = loadMemory()`를 제공한다

### 2.2. network.py
1. 모델을 생성한다.
    1. 만약 학습된 파일이 없는 경우 새롭게 만든다
    2. 만약 학습된 파일이 있는 경우 불러온다.
2. 모델을 저장한다
3. `model = loadModel()`을 제공한다.
4. `saveModel(model: tensorflow.keras.Model)`을 제공한다.

### 2.3. train.py
1. 학습을 한다.
2. src/core/* 패키지의 요소를 사용한다.
3. 학습을 완료후 모델을 저장한다.

### 2.4. predict.py
1. 지정된 이미지를 예측한다.
2. src/core/* 패키지의 요소를 사용한다.


## 3. 깃 사용법

1. vscode  왼쪽 하단의 삼각형(현 분기 이름)을 클릭한다
2. create branch를 클릭한다
3. 작업할 제목을 입력한다 (feature/"제목" (한글, 띄어쓰기 안됨))
4. 작업한다
5. 왼쪽 가운데의 삼각형을 클릭한다
6. changes에서 작업한 파일을 + 을 클릭하여 stage에 올린다
7. MEssage항목에 메세지를 남긴다.
8. 상단의 체크박스(commit)을 클릭한다
9. ... 을 클릭해서 push를 한다
10. 끝
11. github들어가서 원격저장소에서 pull request를 들어간다
12. new pull request를 클릭한다
12. 상단의 콤보박스를 matser <- "자기가 작업한 분기"를 선택한다
13. 작업한 제목과 내용을 입력하고 create pull request를 클릭한다
14. 끝
15. (민영이) 깃허브 pull request 들어간다
16. (민영이) 요청이 있는 내용을 클릭해서 marge를 한다
17. 끝
