# Loading the libraries
from autogen import AssistantAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ResearchAgent:
    def __init__(self, api_key):
        self.groq_api_key = api_key
        self.llm_config = {
            "config_list": [
                {"model": "llama-3.3-70b-versatile", "api_key": self.groq_api_key, "api_type": "groq"}
            ]
        }

        self.summarizer = AssistantAgent(
            name="summarizer_agent",
            system_message="Summarize the retrieved research papers and present concise summaries to the user. JUST GIVE THE RELEVANT SUMMARIES OF THE RESEARCH PAPER AND NOT YOUR THOUGHT PROCESS.",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
            code_execution_config={"use_docker": False},  # Disables Docker usage
        )

        self.advantages_disadvantages = AssistantAgent(
            name="advantages_disadvantages_agent",
            system_message="Analyze the summaries of the research papers and provide a list of advantages and disadvantages for each paper in a pointwise format. JUST GIVE THE ADVANTAGES AND DISADVANTAGES, NOT YOUR THOUGHT PROCESS.",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
            code_execution_config={"use_docker": False},  # Disables Docker usage
        )


    def summarize_research_papers(self, paper_summary):
        response = self.summarizer.generate_reply(
            [{"role": "user", "content": f"Summarize this paper: {paper_summary}"}]
        )
        return response.get("content", "Did not succeed, try again")

    def analyze_paper_advantages_disadvantages(self, paper_summary):
        response = self.advantages_disadvantages.generate_reply(
            [{"role": "user", "content": f"Analyze the advantages and disadvantages of this paper: {paper_summary}"}]
        )
        return response.get("content", "Did not succeed, try again")
