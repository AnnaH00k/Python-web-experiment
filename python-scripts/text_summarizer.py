# python-scripts/text_summarizer.py

from gensim.summarization import summarize
import sys
import json

def get_summary(text):
    return summarize(text)

if __name__ == "__main__":
    text = sys.stdin.read()
    summary = get_summary(text)
    print(json.dumps({'summary': summary}))
