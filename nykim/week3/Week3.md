# Attention Is All You Need

## Abstract
- Attention Mechanism에만 기반한 **Transformer**라는 간단한 모델 제안
- 병렬화와 학습시간 감소, 최고 수준의 품질
- BLEU state-of-the-art

**BLEU**
> Bilingual Evaluation Understudy
기계 번역 결과와 사람이 직접 번역한 결과가 얼마나 유사한지 비교하여 번역에 대한 성능 측정.    
측정 기준은 n-gram(연속적인 단어 나열)

## 1. Introduction
- 기존의 RNN, LSTM 등은 sequence모델링과 언어 모델 등에서 성과는 뛰어났지만 sequence가 길수록 병렬화가 힘듦
- Attention mechanism은 입/출력 sequence 거리에 상관 없이 의존성을 모델링하지만 대부분의 경우 recurrent 네트워크와 함께 사용됨.
- **Transformer** 는 recurrence를 제거하고 attention mechanism만을 사용한 모델. 병렬화를 비약적으로 달성

## 2. Background
- 연속적 계산을 줄이기 위해 여러 모델 탄생했지만 CNN을 기본으로 함. 
- 임의의 위치의 input-output 사이의 관련성 파악하기 위해서는 거리에 따라 계산량 증가 -> 장거리 의존성 학습이 어려움

## 3. Model Architecture
크게 encoder와 decoder로 나뉨.
- encoder는 input sentence(X 행렬)에 대해 다른 representation인 Z행렬로 바꿈
- decoder는 Z를 받아 output sequence(Y 행렬)을 하나씩 만들어 냄

### Encoder
- N개의 동일한 layer로 구성. input X가 첫 번째 layer에 들어가고 layer(x)가 다시 layer에 들어감

### Decoder
- N개의 동일한 layer로 구성
- encoder의 결과에 multi-head attention을 수행할 sub layer를 추가하고 residual connection을 사용한 뒤 layer normalization 해 줌
- 순차적으로 결과 만들어 내야 하기 때문에 self-attention 변형 : **masking**
- position i보다 이후에 있는 position에 attention을 못하게 함. : position i에 대한 예측은 미리 알고 있는 output들에만 의존을 하는 것

## 4. Why Self-Attention
X 행렬 -> Z 행렬에 self-attention이 적합한 이유 :
1. layer당 전체 계산량 적음
2. 계산의 병렬화 : 병렬적으로 한번에 많은 계산
3. 장거리 의존성

## Reference
[Attention Is All You Need(Attention 논문 설명)](https://greeksharifa.github.io/nlp(natural%20language%20processing)%20/%20rnns/2019/08/17/Attention-Is-All-You-Need/)
[Attention is all you need paper 뽀개기](https://pozalabs.github.io/transformer/)