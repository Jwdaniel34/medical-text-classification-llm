# Medical Text Classification + LLM

**“HuggingFace text classifier for medical descriptions”**  

Web scraped ~1,220 medical descriptions from `drugs.com`, cleaned the data, and built a BERT‑based text classification model. Also included a small web application for inference.  

---

## 🚀 Project Overview

This project aims to classify medical text descriptions (e.g. drug side effects, conditions) into categories using a fine‑tuned transformer. The goals include:

- Demonstrating full pipeline: data collection → cleaning → modeling → deployment  
- Showing experience with NLP, transformers, fine-tuning, and web serving  
- Producing a usable interface for inference  

---

## 🗂️ Repository Structure

Here’s an overview of the files and what they do:

| File / Folder | Purpose |
|----------------|---------|
| `webscraper.ipynb` | Notebook which scrapes medical descriptions data from `drugs.com` |
| `onemed.csv` | The cleaned dataset of medical descriptions (labels + text) |
| `model_learning.ipynb` | Notebook for model training, evaluation, experiments |
| `webapp.py` | Flask / API code for serving model predictions via a web interface |
| `.gitignore` | Files / folders to ignore when pushing (e.g. data, temp files) |
| `.idea/` | IDE config files |

---

## 🛠️ Tech Stack & Tools

- **Python** (pandas, numpy, scikit-learn)  
- **Transformers / Hugging Face** (for fine-tuning BERT)  
- **Flask** (or other) for web app / inference interface  
- **Jupyter Notebooks** for exploration, modeling  
- **Web scraping tools** (requests, BeautifulSoup, etc.)  

---

## 📊 Methodology & Results

### Data Collection & Cleaning  
- Scraped ~1,220 entries from `drugs.com`  
- Removed HTML tags, normalized text, handled missing data  
- Possibly created label categories (e.g. “side effect”, “usage”, “contraindication”)  

### Modeling & Experiments  
- Fine‑tuned a **BERT** (or other transformer) model  
- Tried baseline vs advanced architectures  
- Evaluated using **accuracy**, **F1 score**, **confusion matrix**, and perhaps **precision/recall**

### Results  
- (Here you’d insert your model’s metrics — e.g. “F1 = 0.89”, “Accuracy = 92%”)  
- Visualizations of error analysis, confusion matrix, etc.  
- Insights observed — what kinds of classes are harder, what features are important  

---

## 📱 Demo / Web App Usage

You can run the web app locally (assuming dependencies installed):

```bash
pip install -r requirements.txt
python webapp.py
