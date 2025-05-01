from bs4 import BeautifulSoup
import re

class DocumentationParser:
    def __init__(self):
        self.stopwords = {'search', 'help', 'menu', 'footer', 'navigation'}
        self.min_desc_length = 30

    def parse(self, html_content, page_url):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove clutter
        for element in soup(['nav', 'footer', 'script', 'style', 'aside', 'header']):
            element.decompose()

        main_content = soup.find(['main', 'article']) or soup.find(id='content') or soup.body
        
        modules = []
        current_module = None
        
        for element in main_content.find_all(['h1', 'h2', 'h3', 'section']):
            if element.name in ['h1', 'h2']:
                if current_module:
                    modules.append(current_module)
                title = self._clean_text(element.get_text())
                if title and not any(w in title.lower() for w in self.stopwords):
                    current_module = {
                        'module': title,
                        'description': self._extract_description(element),
                        'submodules': {}
                    }
            elif element.name == 'h3' and current_module:
                sub_title = self._clean_text(element.get_text())
                if sub_title:
                    current_module['submodules'][sub_title] = self._extract_description(element)
        
        if current_module:
            modules.append(current_module)
            
        return {'modules': modules}

    def _extract_description(self, element):
        desc = []
        next_el = element.find_next_sibling()
        while next_el and next_el.name not in ['h1', 'h2', 'h3']:
            if next_el.name in ['p', 'div']:
                text = self._clean_text(next_el.get_text())
                if text and len(text) >= self.min_desc_length:
                    desc.append(text)
            next_el = next_el.find_next_sibling()
        return ' '.join(desc) if desc else "No description available"

    def _clean_text(self, text):
        return ' '.join(text.strip().split())
