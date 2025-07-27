# 🚀 SmartSDLC: AI-Powered Software Development Companion

SmartSDLC is an AI-powered web platform designed to enhance the software development lifecycle (SDLC) experience for developers, students, and teams. It provides intelligent code utilities, document analysis, and task classification tools – all accessible through a clean, Streamlit-based interface.

## 🔍 What You Can Do with SmartSDLC

### 🤖 AI Utilities for Developers:
- **Chat with AI Assistant**: Get instant help on any code or SDLC-related question.
- **Code Summarization**: Paste any code snippet and get an instant explanation.
- **Code Generator**: Generate code from prompts using AI.
- **Test Case Generator**: Automatically create test cases from code or requirements.
- **Bug Fixer**: Identify and fix bugs in pasted code.

### 📂 Document-Based Tools:
- **Task Classifier**: Upload your SRS document and classify tasks like Features Requirements, Bugs, Enhancements, etc.

### 📬 User & Feedback Storage:
- User registration and login is handled via Firebase Authentication.
- User data (email, name, password) is securely stored in Firebase Firestore.
- Feedbacks are stored in MongoDB.

## 🌐 Live Demo
👉 [https://smart-sdlc.streamlit.app/]

## 🛠️ Technology Stack

| Layer         | Technology                     |
|---------------|--------------------------------|
| Frontend      | Streamlit                      |
| Backend       | FastAPI                        |
| Authentication| Firebase Auth                  |
| Database      | Firebase Firestore (User Info), MongoDB (Feedback) |
| AI Features   | IBM Watsonx / OpenAI API       |
| Deployment    | Streamlit Cloud / Render       |

## 🧑‍💻 Local Setup Instructions

```bash
# 1. Clone the Repository
git clone https://github.com/gullipali-nagabhushan/Smart-SDLC.git
cd SmartSDLC

# 2. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install Backend Requirements
cd backend
pip install -r requirements.txt

# 4. Run FastAPI Server
uvicorn main:app --reload

# 5. Run Frontend (in new terminal)
cd ../frontend
streamlit run Home.py
```

## 📬 Feedback & Contributions
We welcome your feedback and contributions! Feel free to open issues or submit pull requests.

## 🔮 Future Enhancements (Open for Contribution)
- UML diagram generator
- SRS Document generator
- Full codebase analysis
- GitHub repo scanning
- CI/CD pipeline integration
- IDE and Code Suggesting

## 👨‍💻 Author
Developed by [Gullipalli Nagabhushan](https://github.com/gullipalli-nagabhushan)

---

> 🧠 _SmartSDLC simplifies software development by combining AI + code + documentation tools into a single distraction-free workspace._
