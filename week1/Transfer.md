# nlp_study
2021 NLP Study

# Transfer Learning
이미 개발된 모델을 새로운 작업에서 재사용하는 머신러닝 방법

# fine tuning
Fine Tuning 이란?
기존에 학습되어져 있는 모델을 기반으로 아키텍쳐를 새로운 목적(나의 이미지 데이터에 맞게)변형하고 이미 학습된 모델 Weights로 부터 학습을 업데이트하는 방법

# pre training
MLM(Masked Language Model), NSP(Next Sentence Prediction)

MLM
: 입력 문장에서 임의로 토큰을 버리고(Mask), 그 토큰을 맞추는 방식으로 학습을 진행합니다.

NSP
: 두 문장이 주어졌을 때, 두 문장의 순서를 예측하는 방식입니다. 두 문장 간 관련이 고려되야 하는 NLI와 QA의 파인 튜닝을 위해 두 문장의 연관을 맞추는 학습을 진행합니다.

출처: https://ebbnflow.tistory.com/151 [Dev Log : 삶은 확률의 구름]
