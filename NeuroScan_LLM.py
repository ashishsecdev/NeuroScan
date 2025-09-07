# AshishSecDev
import os
import requests
import streamlit as st 
from transformers import AutoTokenizer # Helps you converting text length to Tokens used.
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


MODEL_NAME = "llama3.1:8b" # Change as required
OLLAMA_URL = "http://localhost:11434/api/generate"
CONTEXT_LIMIT = 8192  


def read_all_files(folder_path, extensions=None):
    all_content = ""
    for root, _, files in os.walk(folder_path):
        for file in files:
            if extensions is None or file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        all_content += f"\n\n# File: {file_path}\n"
                        all_content += f.read()
                except Exception as e:
                    st.warning(f"Skipping {file_path}: {e}")
    return all_content

def count_tokens(text):
    try:
        tokenizer = AutoTokenizer.from_pretrained("hf-internal-testing/llama-tokenizer")
        tokens = tokenizer.encode(text)
        return len(tokens)
    except Exception as e:
        st.error(f"Tokenizer error: {e}")
        return None

def ask_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data.get("response", "").strip()
    else:
        return f"Error {response.status_code}: {response.text}"

def save_pdf(chat_history, filename="analysis_report.pdf"):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(filename)
    story = []

    for entry in chat_history:
        story.append(Paragraph(f"<b>User:</b> {entry['user']}", styles["Normal"]))
        story.append(Paragraph(f"<b>Model:</b> {entry['model']}", styles["Normal"]))
        story.append(Spacer(1, 12))

    doc.build(story)
    return filename

st.title("NeuroScan: Code Analyzer") # UI Formatting

code_folder = st.text_input("Folder Path", value="")
exts = st.text_input("📝 File extensions (comma separated)", value=".py,.php,.js,.ts,.java,.cpp,.c,.html,.css") # Hardcode file extensions as required.
exts = [e.strip() for e in exts.split(",")]

if st.button("Run Initial Analysis"):
    file_content = read_all_files(code_folder, exts)
    final_prompt = "Analyze the following code for any potential vulnerabilities, security issues, or unsafe practices.\n" + file_content

    token_count = count_tokens(final_prompt)
    if token_count:
        st.write(f"**Estimated token count:** {token_count} / {CONTEXT_LIMIT}")
        if token_count > CONTEXT_LIMIT:
            st.warning("Exceeds model context window, may be truncated.")
        elif token_count > CONTEXT_LIMIT * 0.9:
            st.warning("Very close to context limit.")

    analysis = ask_ollama(final_prompt)
    st.session_state["file_content"] = file_content
    st.session_state["chat_history"] = [{"user": "Initial Analysis", "model": analysis}]
    st.subheader("Initial Vulnerability Analysis")
    st.write(analysis)


if "chat_history" in st.session_state:
    st.subheader("Ask here, chat with you code!") # Chat with your code

    user_q = st.text_input("Your question:")
    if st.button("Ask"):
        file_content = st.session_state.get("file_content", "")
        followup_prompt = file_content + "\n\nUser question: " + user_q
        answer = ask_ollama(followup_prompt)

        st.session_state["chat_history"].append({"user": user_q, "model": answer})


    for entry in st.session_state["chat_history"]: # Keeping Chat history in view window
        st.markdown(f"**User:** {entry['user']}")
        st.markdown(f"**Model:** {entry['model']}")
        st.markdown("---")

    if st.button("Save the report as PDF"):
        pdf_path = save_pdf(st.session_state["chat_history"])
        st.success(f"Report saved as {pdf_path}")
