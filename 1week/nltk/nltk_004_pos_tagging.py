from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# 품사 태깅(POS tagging)
# NLTK에서는 펜 트리뱅크 태그세트(Penn Treebank Tagset)를 이용한
# 다.
# • NNP: 단수 고유명사
# • VB: 동사
# • VBP: 동사 현재형
# • TO: to 전치사
# • NN: 명사(단수형 혹은 집합형)
# • DT: 관형사


sentence = "Emma refused to permit us to obtain the refuse permit"
tagged_list = pos_tag(word_tokenize(sentence))
print(tagged_list)
# [('Emma', 'NNP'), ('refused', 'VBD'), ('to', 'TO'), ('permit', 'VB'), 
# ('us', 'PRP'), ('to', 'TO'), ('obtain', 'VB'), ('the', 'DT'), 
# ('refuse', 'NN'), ('permit', 'NN')]