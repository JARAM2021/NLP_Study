import nltk
from nltk.tokenize import sent_tokenize

emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt")
# 해당 파일 읽어와서 변수에 저장
# print(emma_raw)
# ->본문 출력됨

print(sent_tokenize(emma_raw[:1000])[2])
# 1000번째 글자까지 문장 단위로 분리, 배열로 저장



# 형대소 분석의 예(morphological analysis)
# • 어간 추출(stemming)
# • 원형 복원(lemmatizing)
# • 품사 태깅(Part-Of-Speech tagging)