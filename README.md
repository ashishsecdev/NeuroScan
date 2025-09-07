# NeuroScan: AI-Powered Local Code Analyzer

<img src="https://github.com/ashishsecdev/NeuroScan/blob/main/NeuroScan.png" alt="NeuroScan" width="500" height="800"/>

**NeuroScan** is a local code analysis tool that leverages a self-hosted LLM via Ollama to scan your code for potential vulnerabilities, unsafe practices, and logic flaws—all without sending your code to third-party APIs. It provides insights through an interactive Streamlit GUI and allows exporting reports in PDF format.

---

## Key Features

- **Local Analysis:** Your code never leaves your machine.  
- **AI-Powered:** Uses a locally hosted LLM (via Ollama) to analyze code intelligently.  
- **Interactive Chat:** Ask questions about your code, directory structure, or potential issues.  
- **Token Estimation:** See expected token usage to plan chunking, RAG, or RouteLLM integration.  
- **Report Generation:** Export findings to PDF for easy sharing with your team.  

---

## How NeuroScan Works

1. **Install Ollama & LLM Model**  
   Follow the setup guide: [Ollama API: Your Local Self-Hosted LLM](https://medium.com/@ashishsecdev/ollama-api-your-local-self-hosted-llm-08d2362598ad)

2. **Run NeuroScan**  
   ```bash
   streamlit run NeuroScan_LLM.py

3. **Provide Code Input** 

- Select the folder containing your project code.  
- Specify file extensions to analyze (e.g., `.xml`, `.py`).  

4. **Directory & Structure Parsing** 

- NeuroScan walks through every file, extracts content, and prepares it for the LLM.  
- Prompts are combined with code context (`final_prompt`) for analysis.  

5. **AI Analysis** 

- The local LLM scans code for vulnerabilities, unsafe practices, and logic flaws.  

6. **Interactive Chat** 

- Ask questions about your code, e.g., "What is the structure of the directory?"  
- Receive detailed responses from NeuroScan in the chat box.  

7. **Export Report** 

- Save findings as a PDF using the "Save PDF" option.  



### Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/ashishsecdev/NeuroScan.git
   cd NeuroScan
2. pip install -r requirements.txt
3. streamlit run NeuroScan_LLM.py

### Usage

- Select the project folder to analyze.
- Enter the file extensions to include.
- Use the chat box to interact with your code.
- Export the report as PDF for documentation.


**Why NeuroScan?**

NeuroScan transforms your local machine into a fully AI-powered code vulnerability scanner. It is simple to integrate, does not rely on third-party APIs, and opens up advanced possibilities for automated code auditing and analysis.

## License

MIT License

Copyright (c) 2025 [Ashish Bansal, AshishSecDev]

Permission is hereby granted, free of charge to anyone who wants to use NeuroScan.
