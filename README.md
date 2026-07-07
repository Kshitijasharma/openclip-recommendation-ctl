# OpenCLIP Fashion Recommendation System

An AI-powered fashion recommendation system inspired by Walmart's **Complete the Look (CTL)** architecture. The system generates complete outfit recommendations from a single uploaded fashion image using **OpenCLIP**, **FAISS**, and a retrieval-based recommendation pipeline.

This project is an independent implementation created for learning and experimentation based on Walmart Global Tech's engineering case study.

**Reference:**  
https://medium.com/walmartglobaltech/personalized-complete-the-look-model-ea093aba0b73

---

## Dataset

**Polyvore Dataset (Hugging Face)**

https://huggingface.co/datasets/Marqo/polyvore

---

## Inspiration

While shopping on platforms like Amazon and Myntra, I often noticed the "Complete the Look" recommendations shown below product pages but never really thought about how they worked. During my preparation, I came across Walmart's engineering case study explaining their Complete the Look (CTL) recommendation system, which motivated me to build a similar retrieval-based recommendation engine from scratch.

Rather than reproducing the research notebook, the goal was to design a modular, production-style application implementing the complete recommendation pipeline.

---

## Goal

The objective of this project is to build an end-to-end AI fashion recommendation system that:

- Accepts a fashion image as input
- Generates a 512-dimensional image embedding using OpenCLIP
- Retrieves visually similar products using FAISS
- Generates complete outfit combinations
- Ranks and recommends the best outfit matches

---

## Tech Stack

**Backend**
- Python
- NumPy
- Pandas

**AI / Machine Learning**
- OpenCLIP
- PyTorch

**Vector Search**
- FAISS

**Frontend**
- Streamlit

---

## Recommendation Pipeline

```text
Uploaded Image
        │
        ▼
OpenCLIP Embedding
        │
        ▼
FAISS Similarity Search
        │
        ▼
Candidate Selection
        │
        ▼
Outfit Generation
        │
        ▼
Outfit Ranking
        │
        ▼
Top-2 Recommendations
```

---

## Concepts Learned

- Computer Vision
- Image Embeddings
- OpenCLIP
- Vision Transformers (ViT)
- Vector Similarity Search
- FAISS
- Cosine Similarity
- Retrieval-Based Recommendation Systems
- Candidate Selection
- Outfit Ranking
- Modular AI System Design

---

## OpenCLIP
OpenCLIP is used to convert fashion images into semantic feature vectors.

This project uses the **ViT-B-32** architecture with **OpenAI pretrained weights** to generate **512-dimensional image embeddings**. These embeddings capture high-level visual characteristics such as color, texture, shape, and clothing style, allowing visually similar products to be retrieved without relying on handcrafted features.

The embeddings are generated offline and reused during inference, enabling efficient real-time recommendations.

---
## FAISS

FAISS (Facebook AI Similarity Search) is a library for efficient similarity search over high-dimensional vectors.

Instead of comparing the uploaded image embedding against every fashion item manually, the application stores precomputed **512-dimensional OpenCLIP embeddings** in a FAISS index (`IndexFlatIP`). During inference, the uploaded image is converted into an embedding and the index retrieves the **Top-K most visually similar products** using cosine similarity.

This enables fast and scalable retrieval, making real-time outfit recommendation practical even for large fashion catalogs.

---

## Project Structure

```text
style-ai/
│
├── app/
├── backend/
├── data/
├── scripts/
├── requirements.txt
└── README.md
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/<your-username>/openclip-fashion-recommendation-system.git

cd openclip-fashion-recommendation-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app/main.py
```

---

## Results

The application accepts a single uploaded fashion image and recommends complementary outfit combinations using a retrieval-based recommendation pipeline.

### Home Page

<img width="997" height="307" alt="home" src="https://github.com/user-attachments/assets/2951db2b-8a78-4ee8-bbbc-b9db13bd8cbb" />

### Example 1

<img width="1025" height="331" alt="6" src="https://github.com/user-attachments/assets/b1ff50ff-d8ca-4b20-8088-0d097d08efc2" />

### Example 2

<img width="1025" height="359" alt="5" src="https://github.com/user-attachments/assets/83f7a95a-871d-41a1-8eeb-f7f5b770227f" />

### Example 3

<img width="1022" height="353" alt="5 1" src="https://github.com/user-attachments/assets/79589093-9b36-48ac-a628-0fcff30cd6c8" />

---

## Acknowledgements

- Walmart Global Tech — Complete the Look (CTL) Case Study
- OpenCLIP
- FAISS
- Hugging Face Datasets
- Polyvore Dataset

---

Contributions, suggestions, and feedback are always welcome.
