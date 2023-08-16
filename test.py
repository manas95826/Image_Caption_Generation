import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer
from PIL import Image
import torch

# Load the model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

# Define generation parameters
max_length = 20
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams, "no_repeat_ngram_size": 2}

# Define the Streamlit app
def main():
    st.title("Image Captioning App")
    st.write("Upload an image and get a caption!")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)
        st.write("Generating caption...")

        # Preprocess the uploaded image
        image = Image.open(uploaded_image)
        if image.mode != "RGB":
            image = image.convert(mode="RGB")

        # Convert image to bytes
        image_bytes = image.tobytes()

        # Generate caption
        input_ids = tokenizer(image_bytes, return_tensors="pt").input_ids
        with torch.no_grad():
            output_ids = model.generate(input_ids, **gen_kwargs)

        # Decode and display the caption
        caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        st.write(f"Caption: {caption}")

if __name__ == "__main__":
    st.set_option('deprecation.showfileUploaderEncoding', False)  # Disable file uploader encoding warning
    main()
