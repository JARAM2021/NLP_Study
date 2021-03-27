# BERT
Pre-training of Deep Bidirectional Transformers for Language Understanding
- '사전 훈련 언어모델'
- 임베딩 과정에서 BERT 사용, 특정 과제 전 사전 훈련 Embedding을 통해 특정 과제의 성능 좋게 함.

## BERT 동작 과정
### 1. Input
Token Embedding + Segment Embedding + Position Embedding
#### Token Embedding
- Word Piece 임베딩 방식 사용
  - 단어를 표현할 수 있는 subwords units로 모든 단어를 표현
```
공연은 끝났어 -> ['공연-' + '-은' + '끝-' + '-났어']
공연을 끝냈어 -> ['공연-' + '-을' + '끝-' + '-냈어']
개막을 해냈어 -> ['개막-' + '-을' + '해-' + '-냈어']
```
개막공연 -> 개막 + 공연
```
개막공연을 끝냈어 -> ['개막-' + '공연-' + '-을' + '끝-' + '-냈어']
```
  - 모든 단어의 시작에는 underbar를 붙임 'Jet'은 '_Jet'이 됨
- 문자 단위로 임베딩
- 자주 등장하면서 가장 긴 길이의 sub-word를 하나의 단위로 만듦
- 자주 등장하지 않는 단어는 다시 sub-word로 만듦  -> OOV 문제 해결

#### Segment Embedding
- 토크나이징한 단어들을 다시 하나의 문장으로 만드는 작업
- 두 개의 문장을 `[SEP]`를 넣어 구분하고 두 문장을 하나의 Segment로 지정하여 입력.
  
#### Position Embedding
- Self-Attention 모델 사용
- Transformer의 인코더만 사용

### 2. Pre-Training

### 3. Tranfer Learning 
학습된 언어모델 전이학습 시켜 실제 NLP Task 수행 과정

## 한계점
- 일반 NLP모델에서 잘 작동
- Bio, Science, Finance 등 특정 분야의 언어모델에선 잘 적용 안 됨.

## BERT Tokenizer
- `[CLS]` : 모든 sequence의 첫 토근
- `[SEP]` : 문장 분리 토큰
- `[MASK]` : 학습시 MASK 처리 - fine-tuning 시 사용 안 함

## Reference
[BERT1](https://ebbnflow.tistory.com/151)
[BERT논문](https://arxiv.org/pdf/1810.04805.pdf)