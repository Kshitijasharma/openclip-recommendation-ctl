# openclip-recommendation-system-ML

AI recommendation system inspired by Walmart's Complete the Look (CTL) architecture.
Generates complete outfit recommendations from a single uploaded fashion image using OpenCLIP, FAISS, and retrieval-based recommendation.
Implemented based on walmart case study about their "Complete the Look (CTL) model".

https://medium.com/walmartglobaltech/personalized-complete-the-look-model-ea093aba0b73

[Dataset][https://huggingface.co/datasets/Marqo/polyvore]

Building the complete application above this.

## Inspiration
This project is implemented based on Walmart's engineering case study:
Personalized Complete the Look (CTL) Model

https://medium.com/walmartglobaltech/personalized-complete-the-look-model-ea093aba0b73

Although this project follows the same high-level idea of retrieval-based outfit recommendation, it is an independent implementation built for learning and experimentation.

## Dataset

Polyvore Dataset (Hugging Face)

https://huggingface.co/datasets/Marqo/polyvore

## Backstory

Every time I opened Amazon or Myntra, I noticed that after searching for a product and scrolling down, there were always a few recommended items displayed below it. I never really paid much attention to those recommendations until, while preparing, I came across Walmart's engineering case study explaining how they built their Complete the Look (CTL) recommendation model.

This project is my attempt to recreate the core idea using modern computer vision and vector search techniques while designing it as a modular, production-style application.

## Goal:

The objective of this project is to build an end-to-end AI fashion recommendation system that:

- Accepts a single uploaded fashion image
- Converts the image into a semantic embedding using OpenCLIP
- Retrieves visually similar products using FAISS vector search
- Generates complete outfit combinations
- Ranks and recommends the best matching outfits

The focus was not only on recommendation quality but also on building a clean, modular architecture suitable for production environments.

## Tech Stack used:

Backend : Python, NumPy, Pandas
AI : OpenCLIP, PyTorch
Vector Search: FAISS
Frontend: Streamlit



## Concepts learned:

- Computer Vision
- Image Embeddings
- OpenCLIP
- FAISS Similarity Search
- Retrieval-Based Recommendation Systems
- Cnadidate Generation
- Outfit Ranking

## OpenCLIP:

To convert fashion images into numerical representations, this project uses OpenCLIP.
For this implementation:

Model: ViT-B-32
Pretrained Weights: OpenAI

## Clone the repo:

git clone https://github.com/<your-username>/openclip-fashion-recommendation-system.git

cd openclip-fashion-recommendation-system

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app/main.py

## Results:

The system accepts a single fashion image as input and recommends complementary outfit combinations using retrieval-based AI.

Home page:

<img width="997" height="307" alt="home" src="https://github.com/user-attachments/assets/2951db2b-8a78-4ee8-bbbc-b9db13bd8cbb" />

Case1:

<img width="1025" height="331" alt="6" src="https://github.com/user-attachments/assets/b1ff50ff-d8ca-4b20-8088-0d097d08efc2" />

Case2:

<img width="1025" height="359" alt="5" src="https://github.com/user-attachments/assets/83f7a95a-871d-41a1-8eeb-f7f5b770227f" />

Case3:

<img width="1022" height="353" alt="5 1" src="https://github.com/user-attachments/assets/79589093-9b36-48ac-a628-0fcff30cd6c8" />

## Acknowledgements:
Walmart Global Tech – Complete the Look (CTL) engineering case study
OpenCLIP
FAISS
Hugging Face Datasets
Polyvore Dataset

#### Feel free to contribute or any feedbacks. :)







