import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class SeleniumCrawler:
    def __init__(self):
        try:
            # 1. Configure Edge with automatic driver management
            edge_options = Options()
            edge_options.add_argument("--headless=new")
            edge_options.add_argument("--disable-gpu")
            
            # 2. Automatic driver setup (will install Edge if missing)
            self.driver = webdriver.Edge(
                service=Service(EdgeChromiumDriverManager().install()),
                options=edge_options
            )
            
        except Exception as e:
            print("\n" + "="*50)
            print("SETUP FAILED - REQUIRED ACTIONS:")
            print("1. Install Microsoft Edge from:")
            print("   https://www.microsoft.com/edge")
            print("2. Then run:")
            print("   pip install --upgrade selenium webdriver-manager")
            print("="*50)
            print(f"Technical details: {str(e)}")
            raise

    def get_page(self, url):
        try:
            self.driver.get(url)
            return self.driver.page_source
        except Exception as e:
            print(f"Page load error: {str(e)}")
            return None
        
    def close(self):
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
