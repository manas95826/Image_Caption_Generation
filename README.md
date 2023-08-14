
# Image Caption Generation using Transformers and Streamlit

## Introduction
```markdown
Image captioning is the fascinating task of generating textual descriptions for images, enabling machines to understand and communicate the content of visual data. This project leverages the capabilities of the VisionEncoderDecoderModel, ViTFeatureExtractor, and AutoTokenizer from the Transformers library to automatically generate captions for images. The app is deployed on Streamlit Cloud for easy access and sharing.

## Prerequisites

Before you start, make sure you have the following prerequisites in place:

- Python 3.6 or higher installed.
- Streamlit and Transformers libraries. Install them using the command:
  ```bash
  pip install streamlit transformers
  ```
- Images you wish to caption in formats like jpg, jpeg, png or webp.

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/manas95826/Image_Caption_Generation.git
   cd your-app-repo
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app locally:
   ```bash
   streamlit run app.py
   ```

4. To deploy on Streamlit Cloud, follow these steps:

   - Create a free account on [Streamlit Cloud](https://streamlit.io/cloud).
   - Push your app repository to GitHub.
   - Connect your GitHub repository to Streamlit Cloud.
   - Configure environment variables, if needed.
   - Deploy the app on Streamlit Cloud.


## Project Structure

- `app.py`: The main Streamlit application script. It employs Transformers to automatically create captions for uploaded images.
- `requirements.txt`: Lists the necessary Python packages for the project.
- `Procfile`: Specifies the command to run the Streamlit app on Streamlit Cloud.
- `LICENSE`: This project is licensed under the MIT License.
- `README.md`: This document, providing an overview, usage instructions, and deployment guide.

## Acknowledgments

- This project harnesses the potential of the Transformers library, a remarkable tool for natural language and image processing.
- The pre-trained models used in this project, sourced from Hugging Face's Transformers library, offer cutting-edge capabilities in image captioning.
- Streamlit Cloud provides an accessible platform for deploying and sharing Streamlit apps.

## License

This project is open-source and distributed under the MIT License. For more details, consult the [LICENSE](LICENSE) file.

## Contact
```
Feel free to reach out with questions, suggestions, or feedback by opening an issue in the [GitHub repository](https://github.com/manas95826/Image_Caption_Generation).
```

