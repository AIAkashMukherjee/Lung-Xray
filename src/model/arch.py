import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models

class EfficientNetB7(nn.Module):
    def __init__(self, num_classes=2):
        super(EfficientNetB7, self).__init__()
        
        self.model = models.efficientnet_b7(pretrained=True)

        # Get input features from the last Linear layer inside the Sequential classifier
        in_features = self.model.classifier[1].in_features

        # Replace the classifier with a new Linear layer
        self.model.classifier = nn.Sequential(
            nn.Dropout(p=0.5, inplace=True),  # Optional dropout for regularization
            nn.Linear(in_features, num_classes)
        )

    def forward(self, x):
        x = self.model(x)
        return F.log_softmax(x, dim=-1)
