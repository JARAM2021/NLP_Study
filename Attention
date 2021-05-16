## Transformer : Attention Is All You Need

GPT : Transformer의 decoder architecture 활용
BERT : Transformer의 encoder architecture 활용

RNN -> LSTM -> Seq2Seq(고정된 크기의 context vector 사용) 
-> Attention(입력 시퀀스 전체에서 정보를 추출하는 방향으로 발전) -> transformer -> GPT-1 -> BERT -> GPT-3

### Seq2Seq with Attention 
Seq2Seq 문제점 :
하나의 문백 벡처가 소스 문장의 모든 정보를 가지고 있어야 하므로 성능이 저하됩니다.

해결방안 : 매번 소스 문장에서의 출력 전부를 입력으로 받는다 


### Transformer
- RNN, CNN 전혀 필요 X
- 대신 단어들 간 순서에 대한 정보를 알려주기 위해서 posirional Encoding 사용 (임베딩 끝나고 elementwise로 더해줌)
- 인코더와 디코더로 구성
- Attention 과정을 여러 레이어에서 반복
- 성능 향상을 위해 잔여 학습(residual learning) 사용
- 마지막 인코더 레이어의 출력이 모든 디코더 레이어에 입력됨

### Attention 
인코더와 디코더는 multi-head Attention을 사용
어텐션을 위한 3가지 입력 요소
-> 쿼리, 키, 값을 통해 가중치 구함
multi-head(Q, K, V)를 수행한 뒤에도 차원이 동일하게 유지됨


transformer에서는 세가지 종류의 어텐션 레이어가 사용됨
- encoder Self-Attention
- Mastked Decoder Self-Attention (앞쪽에 대한 정보만 참고!)
- Encoder-Decoder Attention

 

Reference
https://www.youtube.com/watch?v=AA621UofTUA
(Transformer : Attention Is All You Need 논문 리뷰)
