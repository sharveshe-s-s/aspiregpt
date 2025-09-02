AspireGPT 🌱

AspireGPT is an AI-powered career guidance and skill development assistant designed to help students, job seekers, and professionals discover career paths, explore required skills, and access personalized learning resources. It integrates speech-to-text transcription (Whisper AI), natural language understanding (LangChain + Transformers), and vector-based knowledge retrieval (FAISS) to deliver smart, multilingual, and context-aware answers.

🚀 Features

🎯 Career Guidance – Get tailored advice on career options based on your skills, interests, and aspirations.

📚 Skill Roadmap – Discover the essential skills, tools, and certifications needed for specific job roles.

🎙 Voice & Text Input – Ask questions through speech or text and receive instant, clear responses.

🌍 Multilingual Support – Works in multiple languages, ensuring inclusivity and accessibility.

⚡ Fast & Scalable – Powered by FastAPI backend, optimized with LangChain + FAISS for quick knowledge retrieval.

🤝 Hackathon-Ready Prototype – Lightweight yet impactful with 2–3 working core features.

🛠 Tech Stack

Backend: FastAPI, LangChain, FAISS, Hugging Face Transformers

AI Models: Whisper (speech-to-text), GPT-based transformers (text reasoning)

Frontend: HTML, CSS, JavaScript (single-page interface)

Other Tools: PyTorch, NumPy, Pandas, Scikit-learn

📂 Project Structure
AspireGPT/
│── backend/
│   ├── main.py          # FastAPI server
│   ├── build_vectorstore.py  # FAISS ingestion
│   ├── inference.py     # LangChain + GPT pipeline
│── frontend/
│   ├── index.html       # Simple UI with voice + text input
│   ├── script.js
│   ├── style.css
│── requirements.txt
│── README.md

⚡ Getting Started

Clone the repo

git clone https://github.com/your-username/AspireGPT.git
cd AspireGPT


Install dependencies

pip install -r requirements.txt


Run the backend

uvicorn backend.main:app --reload


Open frontend
Just open frontend/index.html in your browser.

📌 Roadmap

✅ Career Q&A prototype

✅ Skill roadmap suggestions

⏳ Personalized career planner with progress tracking

⏳ Integration with job portals & LinkedIn learning

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

📜 License

MIT License © 2025 AspireGPT Team

✨ AspireGPT – Guiding futures, building skills.
