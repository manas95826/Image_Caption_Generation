import streamlit as st
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
from PIL import Image

# Load the models and tokenizer
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# Define generation parameters
max_length = 20
num_beams = 7
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

# Define the Streamlit app
def main():
    st.title("Image Captioning App")
    st.write("Upload an image and get a caption!")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","webp"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)
        st.write("Generating caption...")

        # Preprocess the uploaded image
        image = Image.open(uploaded_image)
        if image.mode != "RGB":
            image = image.convert(mode="RGB")

        # Preprocess the image and generate caption
        pixel_values = feature_extractor(images=[image], return_tensors="pt").pixel_values
        output_ids = model.generate(pixel_values, **gen_kwargs)

        # Decode and display the caption
        caption = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        caption = caption[0].strip()
        st.write(f"Caption: {caption}")

if __name__ == "__main__":
    main()
