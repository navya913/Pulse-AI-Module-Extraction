import re
from transformers import pipeline

# Load an NLP model for summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_modules(crawled_data):
    structured_data = []
    for base_url, pages in crawled_data.items():
        modules = _infer_modules(pages)
        structured_data.extend(modules)
    return structured_data

def _infer_modules(pages):
    modules = []
    for url, content in pages.items():
        # Infer modules and submodules from the content hierarchy
        module = _extract_main_topic(content)
        submodules = _extract_subtopics(content)
        if module:
            modules.append({
                "module": module,
                "Description": _generate_description(content),
                "Submodules": submodules
            })
    return modules

def _extract_main_topic(content):
    # Extract main topic from the content (e.g., first-level heading)
    match = re.search(r"^[A-Za-z].*?$", content, re.MULTILINE)
    return match.group(0) if match else None

def _extract_subtopics(content):
    # Extract subtopics based on the content structure
    subtopics = {}
    matches = re.findall(r"^\s*-\s*(.*?):\s*(.*?)$", content, re.MULTILINE)
    for subtopic, description in matches:
        subtopics[subtopic] = _generate_description(description)
    return subtopics

def _generate_description(text):
    # Generate a detailed description using summarization
    summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
    return summary[0]['summary_text']
