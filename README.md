A simple Machine Learning web application that predicts a student's performance based on key factors like study hours, attendance, and internet usage.

🚀 Live App:
👉 https://student-performance-predictor-1lez.onrender.com

📌 Features
📊 Predicts student marks (regression)
✅ Predicts Pass/Fail (classification)
📈 Generates visual graphs dynamically
🌐 Fully deployed web app using Flask + Render
⚡ Real-time predictions via user input
🧠 Tech Stack
Frontend: HTML, CSS
Backend: Flask
ML Libraries: scikit-learn, pandas, numpy
Visualization: matplotlib, seaborn
Deployment: Render
⚙️ How It Works
User enters:
Study Hours
Attendance
Internet Usage
App processes input using trained ML models:
model1 → Predicts marks
model2 → Predicts pass/fail
Graphs are generated and displayed dynamically
📂 Project Structure
├── app.py
├── train_model.py
├── visualize.py
├── templates/
│   └── index.html
├── static/
│   └── plot.png
├── requirements.txt
└── README.md
▶️ Run Locally
pip install -r requirements.txt
python app.py

Then open:
👉 http://127.0.0.1:5000

☁️ Deployment

Deployed on Render using:

gunicorn app:app
⚠️ Notes
Models are trained at runtime if not found
Graphs are saved in the static/ folder
matplotlib uses non-GUI backend (Agg) for deployment
🙌 Author

Ashutosh
GitHub: https://github.com/ashutosh-codes45

⭐ If you like this project

Give it a star ⭐ on GitHub!
