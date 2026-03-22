# education-tutor
This project builds a low-cost AI tutor that answers questions from state-board textbooks. It ingests large PDF textbooks, retrieves relevant sections using a RAG pipeline, and applies context pruning to remove unnecessary content before generating answers. This reduces data transfer, latency, and API costs while providing concise.

📚 Low-Cost AI Tutor for Rural Education
Context-Pruned Retrieval for Efficient Textbook Question Answering

An AI tutoring system that ingests entire textbooks and answers questions with minimal cost, low latency, and reduced data transfer, designed for rural and low-resource environments.

🚀 Problem

Personalized AI tutors are transforming education, but they are expensive and resource-intensive.

In rural India, students often face:

📶 Poor internet connectivity
💻 Low computing power
💰 High cost of LLM API queries

Traditional AI tutoring systems send large textbook contexts to models like GPT-4, which increases latency, bandwidth usage, and cost.

💡 Our Solution

We built a Context-Pruned AI Tutor that:

1️⃣ Ingests entire state-board textbooks (PDFs)
2️⃣ Retrieves only the most relevant sections
3️⃣ Prunes irrelevant context before answer generation
4️⃣ Produces concise curriculum-aligned answers

This drastically reduces:

API costs
token usage
response time
bandwidth consumption
✨ Key Features

✅ Textbook AI Tutor
Ask questions directly from textbooks.

✅ Context Pruning (Core Innovation)
Only relevant textbook sections are used for answering.

✅ Cost-Efficient RAG Pipeline
Reduces token usage compared to baseline RAG systems.

✅ Source-Aware Answers
Each response includes textbook chapter references.

✅ Fast Responses
Low-latency question answering.

✅ Clean Chat Interface
Simple UI designed for students.

🧠 How It Works

The system follows a Retrieval-Augmented Generation (RAG) pipeline with context pruning.

Workflow
Textbook PDF
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
Vector Database
      ↓
Student Question
      ↓
Similarity Search
      ↓
Context Pruning
      ↓
Answer Generation
      ↓
Final Answer + Sources

Instead of sending the entire textbook to the model, we send only the most relevant paragraphs, drastically reducing computation and cost.

🧩 System Architecture
Frontend (Chat UI)
        ↓
FastAPI Backend
        ↓
RAG Retrieval Engine
        ↓
Vector Database
        ↓
Context Pruning
        ↓
Answer Generation
🛠 Tech Stack
Backend
Python
FastAPI
AI / Retrieval
Sentence Transformers
Retrieval Augmented Generation (RAG)
Data Processing
PDF text extraction
Text chunking
Frontend
HTML
CSS
JavaScript
Storage
Vector embeddings database
💰 Cost Optimization Strategy

Baseline RAG systems often send large chunks of text to the LLM.

Our system reduces cost by:

retrieving only top relevant chunks
pruning irrelevant context
generating answers from minimal text

Result:

✔ Lower token usage
✔ Faster response time
✔ Reduced API costs

🎓 Example
Question
What happened when the hailstorm came?
Answer
The hailstorm lasted for about an hour and covered the fields with ice.
The crops were completely destroyed by the storm.
Lencho realized that all his hard work had been ruined.
This made him worried about how his family would survive.

Sources

english.pdf - Chapter 1
📦 Project Structure
project/
│
├── api.py
├── rag_engine.py
├── embeddings/
├── textbooks/
├── index.html
└── README.md
▶️ Running the Project
1️⃣ Install Dependencies
pip install fastapi uvicorn sentence-transformers
2️⃣ Start the Server
uvicorn api:app --reload

Server runs at:

http://127.0.0.1:8000
3️⃣ Open the UI

Open:

index.html

Ask questions from the textbook.

📊 Impact

This system makes AI tutoring accessible and affordable for rural students by:

minimizing computational cost
reducing internet data usage
enabling fast textbook Q&A

It demonstrates how AI systems can be optimized for low-resource environments rather than high-end infrastructure.

🔮 Future Improvements
🌐 Multi-language support
🎤 Voice-based questions
📱 Mobile-first UI
🧠 Better semantic ranking
📚 Multiple textbook support
🏆 Why This Matters

AI tutoring should not be limited to high-bandwidth, high-cost environments.

By combining RAG + Context Pruning, this project shows how we can build efficient, scalable AI education tools for rural communities.

⭐ Built to make AI tutoring accessible everywhere.
