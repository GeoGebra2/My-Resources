from torchvision import datasets
import torch
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torch.nn as nn

data_transform = transforms.Compose([
	transforms.Resize((28, 28)),
	transforms.To()
])
train_data = datasets.ImageFolder(root = '', transform = data_transform)
test_data = datasets.ImageFolder(root = '', transform = data_transform)
#print(train_data.class_to_idx)

train_loader = DataLoader(train_data, batch_size = 4, shuffle = True)
test_loader = DataLoader(test_data, batch_size = 4, shuffle = False)

#定义model
class Net(nn.Module):
	def __init__(self):
		super(Net,self).__init__()
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

net = Net()
net.load_state_dict(torch.load('four.pth', map_location='cpu'))
net.eval()

with torch.no_grad():
	outputs = net(roi)
	predict = torch.max(outputs, dim=1)[1].numpy()
max_label=int(predict)

