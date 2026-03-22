from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rag_engine import RAG
import re

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Loading RAG engine...")
rag = RAG()
print("RAG loaded")


def generate_answer(question, context):
    """
    Generate a cleaner 4–5 line answer using keyword relevance
    """

    # Split context into sentences
    sentences = re.split(r'[.!?]', context)

    # Extract keywords from question
    keywords = question.lower().split()

    scored_sentences = []

    for sentence in sentences:
        sentence = sentence.strip()

        # ignore very short sentences
        if len(sentence.split()) < 5:
            continue

        # score sentence based on keyword overlap
        score = sum(1 for word in keywords if word in sentence.lower())

        if score > 0:
            scored_sentences.append((score, sentence))

    # sort by highest relevance
    scored_sentences.sort(reverse=True)

    # take best 4 sentences
    best_sentences = [s for _, s in scored_sentences[:4]]

    # fallback if no matches
    if not best_sentences:
        best_sentences = sentences[:4]

    answer = ". ".join(best_sentences).strip()

    if not answer.endswith("."):
        answer += "."

    return answer


@app.get("/ask")
def ask(q: str):

    results = rag.retrieve(q)

    if not results:
        return {
            "answer": "Sorry, I could not find the answer in the textbook.",
            "sources": []
        }

    # combine top chunks for context
    context = " ".join([r["text"] for r in results[:3]])

    # generate answer
    answer = generate_answer(q, context)

    # collect sources
    sources = list(set([
        f'{r["source"]} - {r["chapter"]}'
        for r in results
    ]))

    return {
        "answer": answer,
        "sources": sources
    }