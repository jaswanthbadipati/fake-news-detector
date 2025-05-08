# 📰 Real-Time Fake News Detector using BERT

A Streamlit-powered web application that predicts whether **real-time news content** is **Fake** or **Real** using a fine-tuned BERT transformer model. Just paste any piece of news or article, and let AI handle the rest!

---

## 🚀 Features

- ✅ Real-time prediction on any text or news snippet  
- 🧠 Powered by fine-tuned BERT transformer (`jy46604790/Fake-News-Bert-Detect`)
- 📊 Shows prediction confidence for better transparency
- 🖥️ Interactive UI built with [Streamlit](https://streamlit.io)
- 🌐 Clean and modern interface for quick use

---

## 📸 Demo Preview

| Input Example                            | Output     | Confidence |
|------------------------------------------|------------|------------|
| _"NASA confirms alien life on Mars."_    | ❌ Fake     | 96.2%      |
| _"WHO launches new malaria vaccine."_    | ✅ Real     | 98.7%      |

![App Screenshot](https://i.imgur.com/sA7DDgu.png)

---

## 🏗️ Project Structure

fake_news_detector/
│
├── app/
│ ├── streamlit_app.py # Main Streamlit UI
│ └── utils/
│ └── news_fetcher.py # Model loading + Prediction logic
│
├── fake_news_model/ # Directory for the downloaded BERT model
│ ├── config.json
│ ├── pytorch_model.bin
│ ├── tokenizer_config.json
│ ├── vocab.txt
│ └── special_tokens_map.json
│
├── requirements.txt # Python dependencies
└── README.md # You're reading it!


---

## 🧠 Model Info

We use the [jy46604790/Fake-News-Bert-Detect](https://huggingface.co/jy46604790/Fake-News-Bert-Detect) model fine-tuned on a fake news classification dataset.  
It is based on **DistilBERT** for faster inference while preserving strong performance.

---

## 🛠️ Installation & Setup

### 1. Clone the repository:
```bash
git clone https://github.com/jaswanthbadipati/fake_news_detector.git
cd fake_news_detector

2. (Optional) Create a virtual environment:
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

3. Install the dependencies:
pip install -r requirements.txt

4. Download the pre-trained model:

from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "jy46604790/Fake-News-Bert-Detect"
AutoModelForSequenceClassification.from_pretrained(model_name).save_pretrained("fake_news_model")
AutoTokenizer.from_pretrained(model_name).save_pretrained("fake_news_model")

5. Run the app:
streamlit run app/streamlit_app.py
Open the app in your browser: http://localhost:8501

🎯 Usage
Paste or type any news content or article into the input box.

Click "🔍 Predict".

Instantly see if the news is Real ✅ or Fake ❌, with a confidence score.

🌟 Sample Interactions
🔎 Input:
"The Government of India has declared 2025 as the National AI Year."

✅ Output:
Prediction: ✅ Real
Confidence: 97.3%

📌 Future Enhancements
🌍 Add multilingual support

📱 Mobile-responsive layout

📦 REST API for integration

📈 Historical prediction analytics

🤝 Contributing
We welcome all contributions! Please open an issue or submit a pull request.

If you like this project, ⭐ Star this repo to support it!

🧑‍💻 Author
Made with ❤️ by Jaswanth Badipati
📫 Reach me at: jaswanthbadipati@gmail.com
www.linkedin.com/in/jaswanthbadipati
