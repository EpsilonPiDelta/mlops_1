import torch
import wget
from torch.utils.data import Dataset
import numpy as np
import os

def mnist():
    # exchange with the corrupted mnist dataset
    train = torch.randn(50000, 784)
    test = torch.randn(10000, 784) 
    return train, test



class CorruptMnist(Dataset):
    def __init__(self, train):
        self.download_data(train)
        if train:
            content = [ ]
            for i in range(5):
                content.append(np.load(f"/data/corruptmnist/train_{i}.npz", allow_pickle=True))
            data = torch.tensor(np.concatenate([c['images'] for c in content])).reshape(-1, 1, 28, 28)
            targets = torch.tensor(np.concatenate([c['labels'] for c in content]))
        else:
            content = np.load("/data/corruptmnist/test.npz", allow_pickle=True)
            data = torch.tensor(content['images']).reshape(-1, 1, 28, 28)
            targets = torch.tensor(content['labels'])
            
        self.data = data
        self.targets = targets
    
    def download_data(self, train):
        files = os.listdir()
        if train:
            for file_idx in range(5):
                if f'/data/corruptmnist/train_{file_idx}.npy' not in files:
                    wget.download(f"https://raw.githubusercontent.com/SkafteNicki/dtu_mlops/main/data/corruptmnist/train_{file_idx}.npz")
        else:
            if "/data/corruptmnist/test.npy" not in files:    
                wget.download("https://raw.githubusercontent.com/SkafteNicki/dtu_mlops/main/data/corruptmnist/test.npz")
    
    def __len__(self):
        return self.targets.numel()
    
    def __getitem__(self, idx):
        return self.data[idx].float(), self.targets[idx]


if __name__ == "__main__":
    dataset_train = CorruptMnist(train=True)
    dataset_test = CorruptMnist(train=False)
    print(dataset_train.data.shape)
    print(dataset_train.targets.shape)
    print(dataset_test.data.shape)
    print(dataset_test.targets.shape)