# Engima
Quick Python Engima encoding and decoding

Uses: https://pypi.org/project/py-enigma/, https://py-enigma.readthedocs.io/en/latest/index.html


Suggested that you place all the files into a folder.
Use the example sheet, or spend some time creating your own. Both encoder and decoder need to have a copy of the same sheet. 
Using encrypt.py will print the output to console, as well as write it into message.txt
Using decrypt.py will take the text in message.txt and parse it as much as possible. Then it will return the Kenngrupen+garage for the user to compare to their give sheet and fill in the rest of the machine settings. 
Not all messages decode fully. Plug board limitations of current settings sheet, but will get the message close/readable. 
Message whitespace and unknowns should default to 'X' character. 
