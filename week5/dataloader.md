## Custom Dataset
파이토치에서 데이터셋을 좀 더 쉽게 다룰 수 있도록
torch.utils.data.Dataset과 torch.utils.data.DataLoader를 제공
이를 사용하면 미니 배치 학습, 데이터 셔플(shuffle), 병렬 처리까지 간단히 수행 가능

1.Dataset을 정의
2.이를 DataLoader에 전달

(torch.utils.data.Dataset을 상속받아 직접 커스텀 데이터셋(Custom Dataset)을 만드는 경우도 있음)

### 기본 뼈대
```
class CustomDataset(torch.utils.data.Dataset): 
  def __init__(self):
  # 데이터셋의 전처리를 해주는 부분

  def __len__(self):
  # 데이터셋의 길이. 즉, 총 샘플의 수를 적어주는 부분


  def __getitem__(self, idx): 
  # 데이터셋에서 특정 1개의 샘플을 가져오는 함수
```



## Reference 
https://wikidocs.net/57165
