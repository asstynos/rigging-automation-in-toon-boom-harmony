class Properties:
    def __init__(self, ruta):
        self.properties_path = ruta

    def load_properties(self):
        properties = {}
        with open(self.properties_path, 'r') as properties_file:
            for line in properties_file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=')
                    properties[key.strip()] = value.strip()
        return properties

    def save_properties(self, properties):
        with open(self.properties_path, 'w') as properties_file:
            for key, value in properties.items():
                properties_file.write(f"{key}={value}\n")

    def get_property_value(self, property_key):
        properties = self.load_properties()
        return properties.get(property_key)

    def update_property_value(self, property_key, new_value):
        properties = self.load_properties()
        properties[property_key] = new_value
        self.save_properties(properties)
        return properties.get(property_key)
