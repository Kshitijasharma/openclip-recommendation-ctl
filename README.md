# openclip-recommendation-system-ML
Implemented based on walmart case study about their "Complete the Look (CTL) model".

https://medium.com/walmartglobaltech/personalized-complete-the-look-model-ea093aba0b73

Dataset: https://huggingface.co/datasets/Marqo/polyvore

Building the complete application above this.

## Backstory

Every time I opened Amazon or Myntra, I noticed that after searching for a product and scrolling down, there were always a few recommended items displayed below it. I never really paid much attention to those recommendations until, while preparing, I came across a case study by Najmeh Forouzandehmehr explaining how Walmart built its Complete the Look (CTL) model. That sparked my curiosity, and I decided to try implementing a similar system myself.

## Goal:

## Tech Stack used:

## Concepts learned:
To convert fashion images into numerical vectors (embeddings), this project uses OpenCLIP.

### OPENCLIP: 
OpenCLIP is a library that lets you create different CLIP models.
For this project : ViT-B-32 + OpenAI weights are used.

#### 1. ViT-B-32 — The Model Architecture

- ViT stands for Vision Transformer, a deep learning model designed for image understanding.
- B (Base) represents the model size.
- 32 indicates that the input image is divided into 32×32 pixel patches before being processed.

#### 2. pretrained="openai"

- Loads the pretrained weights released by OpenAI.
- Instead of training the model from scratch, we use these learned weights so the model already understands visual patterns and can generate meaningful image embeddings.

Together, the architecture (ViT-B-32) and pretrained weights (openai) create a model capable of extracting semantic features from fashion images for retrieval and recommendation.

## Clone the repo:

## Results:

Home page:

<img width="997" height="307" alt="home" src="https://github.com/user-attachments/assets/2951db2b-8a78-4ee8-bbbc-b9db13bd8cbb" />

Case1:

<img width="1025" height="331" alt="6" src="https://github.com/user-attachments/assets/b1ff50ff-d8ca-4b20-8088-0d097d08efc2" />

Case2:

<img width="1025" height="359" alt="5" src="https://github.com/user-attachments/assets/83f7a95a-871d-41a1-8eeb-f7f5b770227f" />

Case3:

<img width="1022" height="353" alt="5 1" src="https://github.com/user-attachments/assets/79589093-9b36-48ac-a628-0fcff30cd6c8" />

#### Feel free to contribute or any feedbacks. :)







