# Dataset
- Data를 관리하기 쉽게 객체화 시켜 놓은것
- Data 와 Lable을 tensor로 input 한다.
## Dataset의 구성
- __init__(self): 필요한 변수들을 선언한다. 전체 x_data와 y_data를 load하거나 파일목록을 load한다.
- __get_item__(self, index): index번째 data(tensor)를 return하게 method를 구성해야한다.
- __len__(self): 데이터의 length를 return 한다. x_data와 y_data는 길이가 같으니 아무 length나 return하면 된다.
```python
import torch
import torch.utils.data as data


class BasicDataset(data.Dataset):
    def __init__(self, x_tensor, y_tensor):
        super(BasicDataset, self).__init__()

        self.x = x_tensor
        self.y = y_tensor
        
    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return len(self.x)
```

# Dataloader
- 많은 양의 데이터를 로드하려 해도 RAM용량의 한계가 있다.
- 그래서 데이터를 Batch(epoch 1회분)라는 단위로 나눠 묶어서 처리한다.
- Dataset을 input으로 넣어 주면 여러 옵션(데이터 묶기, 섞기, 알아서 병렬처리)을 통해 batch를 만들어준다.
- input의 길이가 변하는 등의 상황에서는 Custom Dataloader도 구성할 수 있다.
