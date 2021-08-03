import sys
import io

class ConsoleToStrConverter:

    def __init__(self):
        self.__stdout__ = sys.stdout

    def start(self):
        '''
        Starts the converter instance.
        Works by opening a StringIO buffer file and redirecting sys.stdout to the buffer file.

        Note: No outputs will be printed on the console window when the converter is running.
        '''
        self.consoleText = io.StringIO()
        sys.stdout = self.consoleText

    def stop(self):
        '''
        Stops the converter instance.
        Resets the value of sys.stdout to the default console, and closes the buffer file.

        Returns a <class 'str'> value which contains the data that was printed on the console.
        '''
        finalString = self.consoleText.getvalue()
        sys.stdout = self.__stdout__
        self.consoleText.close()
        return finalString

    def curr(self):
        ''' 
        Does not affect the converter instance.

        Returns a <class 'str'> value which contains the data that was printed on the console.
        '''
        currString = self.consoleText.getvalue()
        return currString
