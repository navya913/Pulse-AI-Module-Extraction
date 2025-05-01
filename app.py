from crawler import DocumentationCrawler
from custom_parser import DocumentationParser
from structure_builder import StructureBuilder
import streamlit as st
import json

def main():
    st.title("Documentation Module Extractor")
    
    url = st.text_input("Enter documentation URL:", "https://help.instagram.com/")
    
    if st.button("Extract Modules"):
        with st.spinner("Processing..."):
            try:
                # Initialize components
                crawler = DocumentationCrawler()
                parser = DocumentationParser()
                builder = StructureBuilder()
                
                # Process URL
                html = crawler.get_page(url)
                parsed = parser.parse(html, url)
                result = builder.build_structure([parsed])
                
                # Display
                st.subheader("Extracted Modules")
                st.json(result)
                
                # Download
                st.download_button(
                    "Download JSON",
                    json.dumps(result, indent=2),
                    "modules.json"
                )
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
