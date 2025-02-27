# Smart Research Assistant Using Autogen

## Overview
The **Smart Research Assistant** is a Streamlit-based application that utilizes **Autogen** and AI-powered agents to search, summarize, and analyze research papers from **ArXiv** and **Google Scholar**. The tool provides structured insights, including summaries and pros/cons analysis of retrieved papers.

## Features
- **Search Research Papers**: Fetches papers from **ArXiv** and **Google Scholar**.
- **Summarization**: Uses an AI agent to generate concise summaries of each research paper.
- **Analysis**: Identifies advantages and disadvantages of each paper.
- **User-Friendly Interface**: Built using **Streamlit** for seamless interaction.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/aky-ds/Smart_Research_Assistant_Using_Autogen
   cd smart-research-assistant
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file and add your **GROQ API key**:
   ```sh
   GROQ_API_KEY=your_api_key_here
   ```

## Usage
Run the Streamlit app:
```sh
streamlit run Application.py
```

## Project Structure
```
📂 Smart Research Assistant
│── 📜 Application.py  # Main Streamlit application
│── 📜 Agents.py       # AI research agents (summarization & analysis)
│── 📜 data_loader.py  # Fetches research papers from ArXiv & Google Scholar
│── 📜 requirements.txt # Dependencies
│── 📜 .env            # API Key (not included in repo)
```

## Dependencies
- **Python 3.8+**
- **Streamlit**
- **Autogen**
- **Requests**
- **Dotenv**

## Notes
- Ensure Docker is running or disable Docker in `code_execution_config` to avoid execution errors.
- If no papers are found for a query, the app will notify the user.

## Future Enhancements
- **Integration with IEEE Xplore** for broader research coverage.
- **Citation and reference generation**.
- **User authentication** to save research history.

---
### Author
**Ayaz**

For any issues, feel free to reach out!

