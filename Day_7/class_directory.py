class Directory:
    def __init__(self, name, size, parent_directory, connected_directories):
        self.name = name
        self.size = size
        self.parent_directory = parent_directory
        self.connected_directories = connected_directories
    
    def toString(self):
        return [self.name, self.size, self.parent_directory.name]

    def display_directory(self, offset):
        string = f"{offset}Name:  {self.name} \n{offset}Size: {self.size}" 
        return string