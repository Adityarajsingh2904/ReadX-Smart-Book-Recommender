# 📚 ReadX – Smart Book Recommender

> **Empowering readers with intelligent book recommendations**

ReadX is a powerful and lightweight book recommender system designed to help readers discover new books based on their interests, reading patterns, and similarity to past preferences. Built using collaborative filtering and powered by Python and Streamlit, it offers an interactive web experience for book lovers.

---

## ✨ Features

- ✅ Personalized book recommendations using user ratings
- 🔍 Search by book title, author, or genre
- 📈 Visual stats and feedback from dataset insights
- 🧠 Collaborative filtering via user-item matrix
- ⚡ Fast, responsive interface using Streamlit
- 🗂️ Clean, modular project structure

---

## 🛠️ Tech Stack

| Layer      | Technologies                     |
|------------|----------------------------------|
| Frontend   | Streamlit                        |
| Backend    | Python, Pandas, Numpy            |
| Recommender| Cosine Similarity, Sklearn       |
| Data       | Book-Crossing Dataset (CSV files)|
| Misc       | Matplotlib (optional), GitHub    |

---

## 📁 Project Structure

```
ReadX/
├── app.py                         # Main Streamlit app
├── template.py                   # Layout and modular UI code
├── requirements.txt              # Dependencies list
├── data/
│   ├── BX-Books.csv              # Book metadata
│   ├── BX-Users.csv              # User data
│   └── BX-Book-Ratings-Subset.csv # Filtered ratings
└── README.md                     # You're reading it!
```

---

## 🚀 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/Adityarajsingh2904/ReadX-Smart-Book-Recommender.git
cd ReadX-Smart-Book-Recommender
pip install -r requirements.txt
```

---

### ▶️ Run the App

```bash
streamlit run app.py
```

Then open the local Streamlit link in your browser (usually http://localhost:8501)

---

## 🧪 Sample Use-Cases

- College project submission for AI/Data Science
- Portfolio app to showcase ML/Streamlit integration
- Prototype for personalized e-library systems

---

## 🖼️ Screenshots

> Add screenshots of your app UI here using:
> `![App Screenshot](relative/path/to/screenshot.png)`

---

## 🧑‍💻 Author

Made with ❤️ by [Aditya Raj Singh](mailto:thisis.adityarajsingh@gmail.com)

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

## 📌 Tips

- Use smaller subsets of the dataset to test locally
- You can extend this with a login system, rating tracker, or NLP book search!
