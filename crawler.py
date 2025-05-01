from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import WebDriverException
import time

class DocumentationCrawler:
    def __init__(self, max_depth=1, max_pages=5):
        self.max_depth = max_depth
        self.max_pages = max_pages
        self.visited_urls = set()
        self.driver = self._init_driver()

    def _init_driver(self):
        """Initialize Edge browser with automatic driver management"""
        try:
            options = Options()
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            
            service = Service(EdgeChromiumDriverManager().install())
            return webdriver.Edge(service=service, options=options)
            
        except WebDriverException as e:
            raise Exception(
                "Failed to initialize browser. Please:\n"
                "1. Install Microsoft Edge: https://www.microsoft.com/edge\n"
                f"2. Error details: {str(e)}"
            )

    def get_page(self, url):
        """Fetch and return page HTML"""
        try:
            if url in self.visited_urls:
                return None
                
            self.visited_urls.add(url)
            self.driver.get(url)
            time.sleep(2)  # Wait for page load
            return self.driver.page_source
            
        except Exception as e:
            print(f"Error fetching {url}: {str(e)}")
            return None

    def close(self):
        """Clean up resources"""
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
