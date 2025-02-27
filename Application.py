# Loading the libraries
import os
import streamlit as st
from data_loader import DataLoader
from Agents import ResearchAgent

# Setting up the title

st.title('Smart Research Assistant Using Autogen')

# Loading the data

data_loader = DataLoader()

# laoding the enviroment variables

groq_api_key = os.getenv('GROQ_API_KEY')

if not groq_api_key:
    st.error('Please set the GROOQ_API_KEY environment variable.')
    
# Loading the agents

agents = ResearchAgent(groq_api_key)

query=st.text_input('Give me the research on this topic')

if st.button('Search'):
    st.spinner('Articles is now in process')

    arxiv_papers=data_loader.fetch_arxiv_papers(query)
    scholarly_papers=data_loader.fetch_scholarly_papers(query)
    all_papers=arxiv_papers + scholarly_papers
    
    if not all_papers:
        st.error('No articles found')
    else:
        processed_papers = []

            # Process each paper: generate summary and analyze advantages/disadvantages
        for paper in all_papers:
                summary = agents.summarize_research_papers(paper['summary'])  # Generate summary
                adv_dis = agents.analyze_paper_advantages_disadvantages(summary)  # Analyze pros/cons

                processed_papers.append({
                    "title": paper["title"],
                    "link": paper["link"],
                    "summary": summary,
                    "advantages_disadvantages": adv_dis,
                })
        st.subheader("Top Research Papers:")
        for i, paper in enumerate(processed_papers, 1):
                st.markdown(f"### {i}. {paper['title']}")  # Paper title
                st.markdown(f"🔗 [Read Paper]({paper['link']})")  # Paper link
                st.write(f"**Summary:** {paper['summary']}")  # Paper summary
                st.write(f"{paper['advantages_disadvantages']}")  # Pros/cons analysis
                st.markdown("---")  # Separator between papers