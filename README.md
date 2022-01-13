# Card Maker for Anki
In the base of this module are [**anki-connect**](https://github.com/FooSoft/anki-connect) 
and [**reverso_context_api**](https://github.com/flagist0/reverso_context_api) modules. As its core functionality,
Card Maker searches an english word on https://dictionaryapi.dev/ then gets the word's data
(translation, transcription, several definitions, link to an audio file with pronunciation sample). Translations
and usage examples are taken from https://context.reverso.net/translation/. 
After that the new word can be automatically added to your Anki.
  
## Installation
First of all, you'll need the desktop version of Anki installed on your computer. 
Then install the [**anki-connect**](https://github.com/FooSoft/anki-connect) add-on:  
>The installation process is similar to other Anki plugins and can be accomplished in three steps:
>
>1.  Open the `Install Add-on` dialog by selecting `Tools` | `Add-ons` | `Get Add-ons...` in Anki.
>2.  Input [2055492159](https://ankiweb.net/shared/info/2055492159) into the text box labeled `Code` and press the `OK` button to proceed.
>3.  Restart Anki when prompted to do so in order to complete the installation of Anki-Connect.

Install requirements from the file:  
>pip install -r requirements.txt

## How to use 
To begin with, it's worth mentioning that you can change some basic settings, 
such as the language of translations and context examples, number of definitions and examples to be shown. 
In order to set these options, edit `config.py` file.  
#####
To start the program run `start.bat` or `start.sh` depending on your operation system. 
It will be opened in terminal.
You can use the program as it is, a learner's dictionary/agregator, which may prove useful, 
since the program combines the best traits of two sources 
(although Reverso Context is a very powerful tool, it still lacks transcriptions and dictionary definitions,
in my humble opinion).
#####
After the search is done you will be asked if you prefer add a card with the word to your Anki. 
**Anki must be started by the moment**.
The program will create a new deck with all the needed card fields and styling.
You don't have to do anything in Anki beforehand, however, you may if needed.
## Customization
You are free to edit several deck settings in `config.py`.  
  
If you want to use your existing decks, make sure they have the required fields in the order given:
1. Term
2. Transcription
3. Translation
4. Definition
5. Context
6. Audio

The absence of any of the fields will cause an error. Therefore, if you want a custom deck name, 
I advise you not to enter your own decks names, but enter
a non-existing name to `config.py` and let the program initialize a new deck with given name.
Your decks won't be affected in any way, and you won't lose or ruin you data.
There's also a variable to apply existing schedule settings from your own deck in `config.py`.

#####-------------
This program was written for personal use. There is no any warranty or responsibility 
If you have any thoughts or suggestions on Anki Card Maker, please feel free to contact me.  
`sheyan44@gmail.com`


