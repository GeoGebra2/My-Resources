import torch
import torch.nn as nn
import torch.nn.functional as F
import os

from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from torchvision import datasets
from PIL import Image

import torch.optim as optim

class CustomDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.images = []
        for class_dir in os.listdir(root_dir):
            class_dir_path = os.path.join(root_dir, class_dir)
            for image_name in os.listdir(class_dir_path):
                self.images.append((os.path.join(class_dir_path, image_name), class_dir))

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        image_path, label = self.images[idx]
        image = Image.open(image_path).convert('L')  # 转换为灰度图
        if self.transform:
            image = self.transform(image)
        return image, torch.tensor(int(label), dtype=torch.long)

# 数据预处理
transform = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,)),
    transforms.Grayscale(num_output_channels=1)
])

train_dataset = datasets.ImageFolder(root='D:/SmartCar/raw_data/train', transform=transform)
test_dataset = datasets.ImageFolder(root='D:/SmartCar/raw_data/val', transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

class TrafficSignNet(nn.Module):
    def __init__(self):
        super(TrafficSignNet, self).__init__()
        self.conv = nn.Sequential(
			nn.Conv2d(1,16,3,padding=1),
			nn.Conv2d(16,16,5),
			nn.ReLU(),
			nn.MaxPool2d(2,stride=2),
			nn.Dropout(0.3),
			nn.Conv2d(16,32,5),
			nn.ReLU(),
			nn.MaxPool2d(2, stride=2),
			nn.Dropout(0.3)
		)
        self.fc = nn.Sequential(
			nn.Linear(32*4*4,100),
			nn.ReLU(),
			nn.Linear(100,4)
		)

    def forward(self, x):
        x= self.conv(x)
        x=x.view(-1,32*4*4)
        x= self.fc(x)
        #x= nn.functional.normalize(x)
        return x
    

# 实例化网络
net = TrafficSignNet()

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)

# 训练网络
'''
def train_network(train_loader, net, criterion, optimizer, epochs=10):
    for epoch in range(epochs):
        running_loss = 0.0
        for images, labels in train_loader:
            #print(images)
            optimizer.zero_grad()
            outputs = net(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f'Epoch {epoch+1}, Loss: {running_loss/len(train_loader)}')

train_network(train_loader, net, criterion, optimizer)

torch.save(net.state_dict(), 'D:/SmartCar/model2.pth')
'''
# 测试网络

net.load_state_dict(torch.load('D:/SmartCar/model2.pth', map_location='cpu', weights_only=True))
net.eval()
def test_network(test_loader, net):
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print(f'Accuracy: {100 * correct / total}%')

test_network(test_loader, net)
