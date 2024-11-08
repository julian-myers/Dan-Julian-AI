"""
VIBE AI v0.0.1 (test)
"""
import torch
import torch.nn as nn


# defining the neural network
class VibeAI(nn.Module):
    def __init__(self):
        super(VibeAI, self).__init__()
        self.fc1 = nn.Linear(9, 64)
        self.dropout1 = nn.Dropout(0.3)
        self.fc2 = nn.Linear(64, 32)
        self.dropout2 = nn.Dropout(0.3)
        self.fc3 = nn.Linear(32, 16)
        self.dropout3 = nn.Dropout(0.3)
        self.fcfinal = nn.Linear(16, 9)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout1(x)
        x = torch.relu(self.fc2(x))
        x = self.dropout2(x)
        x = torch.relu(self.fc3(x))
        x = self.dropout3(x)
        x = torch.relu(self.fcfinal(x))
        return x
