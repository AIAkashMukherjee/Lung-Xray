# Lung X-ray Classification: Normal vs. Pneumonia

## Overview

This project involves training a deep learning model to classify **lung X-ray images** into two categories: **Normal** and  **Pneumonia** . The model achieves **90% accuracy** and integrates with **MongoDB** to store metadata and **Amazon S3** to store the trained model for cloud access and deployment.

## Features

* **Model** : EfficientNetV2-S for image classification.
* **Accuracy Goal** : At least 88**%** accuracy on the validation set.
* **Data Source** : Public dataset of lung X-ray images (e.g., Kaggle's pneumonia detection dataset).
* **MongoDB** : Stores metadata such as model performance and training status.
* **Amazon S3** : Stores the trained model for cloud access.
* **Deep Learning Framework** : **PyTorch**

## Requirements

### Software Dependencies

Ensure you have the following installed:

* **Python 3.x** (preferably 3.7 or higher)
* **PyTorch** (>= 1.10)
* **MongoDB** (local or cloud-based)
* **Amazon S3** for cloud storage
* **Boto3** for interacting with AWS S3
* **pymongo** for MongoDB interactionConclusion

This project demonstrates how to build a **Lung X-ray Classification Model** to distinguish between **Normal** and **Pneumonia** cases. By utilizing  **EfficientNetV2-S** , the model is efficient yet accurate, achieving a target accuracy of  **90%** . Integration with **MongoDB** for metadata storage and **Amazon S3** for cloud-based deployment makes the model scalable and accessible for real-world applications.

### Key Takeaways:

* **Model** : EfficientNetV2-S for efficient classification.
* **Storage** : MongoDB for metadata and S3 for model storage.
* **Accuracy** : Achieves 90% accuracy, suitable for real-world deployment.
* **Deployment** : Trained model can be deployed and accessed via cloud services.
