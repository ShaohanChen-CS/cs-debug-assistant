# 🧠 CS Debug Assistant

A lightweight web-based tool that helps beginner programmers understand and debug Python error messages in real time.

## 🚀 Features

- 🔍 Analyze Python error messages instantly
- 💡 Provide clear explanations of what went wrong
- 🛠️ Suggest actionable fixes for faster debugging
- ⚡ Simulate AI-like feedback with dynamic responses
- 🌐 Interactive web interface built with Streamlit

---

## 🖥️ Demo

Run locally:

pip install -r requirements.txt  
streamlit run app.py  

Then open in your browser (locally):  
http://localhost:8501

---

## 🧠 Example

Input:
[ IndexError: list index out of range ]

Output:
- Explanation: You are accessing an index that does not exist.  
- Fix: Check list length before accessing.

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Keyword-based error matching (NLP-inspired)

---

## 💡 Motivation

As a CS student and teaching intern, I noticed that many beginners struggle to interpret Python error messages.  
This project aims to make debugging more intuitive, faster, and less frustrating.

---

## 🔮 Future Improvements

- Integrate LLM APIs for smarter error analysis  
- Expand error database for broader coverage  
- Improve UI/UX for a more polished user experience