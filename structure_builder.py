class StructureBuilder:
    def build_structure(self, parsed_pages):
        final_output = []
        
        for page in parsed_pages:
            for module in page['modules']:
                if module['module']:
                    formatted_module = {
                        'module': module['module'],
                        'Description': module['description'],
                        'submodules': module['submodules']
                    }
                    final_output.append(formatted_module)
        
        return final_output
