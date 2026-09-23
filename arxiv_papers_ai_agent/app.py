from agents.arxiv_paper_agent import analyseArxivPapers
import asyncio 
import sys 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(analyseArxivPapers(prompt=prompt))
