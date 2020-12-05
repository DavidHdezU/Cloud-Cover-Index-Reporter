from ArgumentParser import ArgumentParser
class Main:
    """
    Main class to run the programm
    """
    def __init__(self):
        """
        Constructor that creates an instance of Argument Parser
        """
        self.argumentParser = ArgumentParser()
    
    def main(self):
        """
        Main function to run
        """
        self.argumentParser.main()

if __name__ == "__main__":
    programm = Main()
    programm.main()
    