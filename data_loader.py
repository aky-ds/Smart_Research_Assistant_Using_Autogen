import requests
import xml.etree.ElementTree as ET
from scholarly import scholarly

# Creating the data loader class
class DataLoader:
    def __init__(self):
        print("Data Loading init")

    def fetch_arxiv_papers(self, query):
        """
        Returns the top 5 query results from the database. If fewer than 5 papers are found,
        it expands the search and passes it to the agents for summarization and important facts.
        """
        def search_query(query):
            url = f"https://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5"
            response = requests.get(url)

            if response.status_code == 200:
                root = ET.fromstring(response.content)
                return [
                    {
                        "title": entry.find("{http://www.w3.org/2005/Atom}title").text,
                        "summary": entry.find("{http://www.w3.org/2005/Atom}summary").text,
                        "link": entry.find("{http://www.w3.org/2005/Atom}id").text,
                    }
                    for entry in root.findall("{http://www.w3.org/2005/Atom}entry")
                ]
            else:
                return []

        papers = search_query(query)

        if len(papers) < 5 and hasattr(self, "search_agent"):
            related_topics_response = self.search_agent.generate_reply(
                messages=[{"role": "user", "content": f"Suggest 3 related research topics for '{query}'"}]
            )
            related_topics = related_topics_response.get("content", "Content not found").split("\n")

            for topic in related_topics:
                topic = topic.strip()
                if topic and len(papers) < 5:
                    new_papers = search_query(topic)
                    papers.extend(new_papers)
                    papers = papers[:5]  # Ensure we only keep the top 5 results

        return papers

    # Get data from scholarly
    def fetch_scholarly_papers(self, query):
        """
        Returns the top 5 papers from Scholarly.
        """
        papers = []
        search_results = scholarly.search_pubs(query)

        for i, pub in enumerate(search_results):
            if i >= 5:
                break
            papers.append({
                "title": pub["bib"]["title"],
                "summary": pub["bib"].get("abstract", "No summary available"),
                "link": pub.get("pub_url", "No link available"),
            })

        return papers
