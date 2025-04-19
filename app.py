import streamlit as st
import os,sys
import torch
from torchvision import transforms
from PIL import Image
from io import BytesIO
import boto3
from dotenv import load_dotenv
from src.logger.custom_logging import logging
from src.exception.expection import CustomException
from src.constants import *
from src.model.arch import EfficientNetV2S


load_dotenv()

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

# DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
os.makedirs("images", exist_ok=True)


# ---------------- MODEL LOADER ---------------- #
class ModelLoader:
    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id or os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=aws_secret_access_key or os.getenv("AWS_SECRET_ACCESS_KEY")
        )

    def load_model(self, model_name, bucket_name, model_dir: str = None):
        try:
            model_key = f"{model_dir}/{model_name}" if model_dir else model_name
            logging.info(f"Downloading model from S3: s3://{bucket_name}/{model_key}")

            # Download model file into memory
            model_buffer = BytesIO()
            self.s3.download_fileobj(bucket_name, model_key, model_buffer)
            model_buffer.seek(0)

            # Create a new model instance and load weights
            model = EfficientNetV2S(num_classes=2)
            model.load_state_dict(torch.load(model_buffer, map_location=torch.device("cpu")))  # or DEVICE
            model.eval()

            logging.info("Model state_dict loaded successfully from S3.")
            return model

        except Exception as e:
            logging.error(f"Error loading model from S3: {e}")
            raise CustomException(e, sys)


# ---------------- IMAGE TRANSFORMATION ---------------- #
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
    ])

    image = Image.open(image_path).convert("RGB")
    tensor = transform(image)
    tensor = tensor.unsqueeze(0).to(DEVICE)  
    return tensor


# ---------------- PREDICTION ---------------- #
def predict(model, input_tensor):
    with torch.no_grad():
        output = model(input_tensor)
        prediction = int(torch.argmax(output, dim=1).item())
        return prediction


# ---------------- MAIN INFERENCE FUNCTION ---------------- #
def classify_image(uploaded_file):
    if uploaded_file is not None:
        save_path = os.path.join("images", "input.jpeg")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success("Image uploaded and saved.")
        logging.info("Image saved for prediction.")

        try:
            loader = ModelLoader(aws_access_key_id, aws_secret_access_key)
            model = loader.load_model(model_name=TRAINED_MODEL_NAME, bucket_name=AWS_BUCKET_NAME)
        except Exception as e:
            st.error("❌ Failed to load model.")
            logging.error(f"Model loading error: {e}")
            return

        input_tensor = preprocess_image(save_path)
        prediction = predict(model, input_tensor)

        result = "Normal" if prediction == 0 else "PNEUMONIA"
        st.success(f"Prediction: {result}")


# ---------------- STREAMLIT UI ---------------- #
if __name__ == "__main__":
    st.title("🩻 Lung X-ray Classifier")
    uploaded_file = st.file_uploader("📤 Upload an X-ray image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        classify_image(uploaded_file)
    