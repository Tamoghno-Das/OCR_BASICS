import streamlit as st
from ocr_service import extract_text

st.set_page_config(
    page_title="OCR Text Extractor",
    page_icon="📄"
)

st.title("📄 Image to Text Extractor")

st.write("Upload an image and extract its text using OCR.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded Image"
    )

    if st.button("Extract Text"):

        try:
            with st.spinner("Extracting text..."):
                text = extract_text(uploaded_file)

            if text:

                st.success("Text extracted successfully!")

                st.subheader("Extracted Text")

                st.text_area(
                    "OCR Result",
                    text,
                    height=250
                )

                st.download_button(
                    label="Download Text",
                    data=text,
                    file_name="extracted_text.txt",
                    mime="text/plain"
                )

            else:
                st.warning("No text found in the image.")

        except Exception as e:
            st.error(f"Error: {e}")