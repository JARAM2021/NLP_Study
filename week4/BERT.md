## BERT
: Bidirectional Encoder Representations from Transformer
 
### tasks of BERT
1. Masked language model (MLM)
임의의 위치에 있는 단어 예측

2. Next sentence prediction (NSP)
다음에 등장했던 문장인지 판별


### architecture
멀티 레이어 양방향 transformer encoder
1. BERT base 모델
L = 12, H = 768, A = 12
Total params = 110M
2. BERT large 모델
L = 24, H = 1024, A = 16
Total params = 340M

### Input/ output Representation
token들을 word piece 개념을 사용해 집어넣음
1. Token embeding : 30000개 워드피스
2. Segment embeding : 첫번째 시퀀스인지 두번째 시퀀스인지 알려줌
3. Position embeding : transformer의 포지션 임베딩과 같음

### MLM 
전체 토큰 중 15%가 마스킹 됨
-> 모델이 가려진 단어들 잘 학습하도록 함
pretraning 과정에서만 등장

### NSP 
기존 문장단위 학습은 문장 간 관계 잘 알아내지 못함 
-> 50% 이어진 문장(1), 50% 안 이어진 문장(0)

Reference
https://www.youtube.com/watch?v=IwtexRHoWG0
