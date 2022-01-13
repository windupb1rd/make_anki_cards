# Card Maker for Anki
In the base of this module are [**anki-connect**](https://github.com/FooSoft/anki-connect) 
and [**reverso_context_api**](https://github.com/flagist0/reverso_context_api) modules. As its core functionality,
Card Maker searches an english word on https://dictionaryapi.dev/ then gets the word's data
(translation, transcription, several definitions, link to an audio file with pronunciation sample). Translations
and usage examples are taken from https://context.reverso.net/translation/.  
  
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
to be contunued...


## Card template
In order to work properly, Card Maker needs...

Just **make sure that your cards have the next fields**:  
1. Term
2. Transcription
3. Translation
4. Definition
5. Context
6. Audio

Just copy-paste the code below into a card's tabs respectively. The template isn't pretty, but it does its work. You are totally free to change the styling as you like. 


####Front template
```html
<div id="term">{{Term}}<br></div>

<div id="transcription">{{Transcription}}<br>
{{Audio}}</div>
```
####Back template
```html
{{FrontSide}}

<h1 class="one"><span>TRANSLATION</span></h1>
<div id="translation"> {{edit:Translation}} </div>

<h1 class="one"><span>MEANING</span></h1>
<div id="definition"> {{edit:Definition}} </div>

{{#Context}}
<h1 class="one"><span>CONTEXT</span></h1>
<div class="context" id="context">{{edit:Context}}</div>
{{/Context}}
```
####Styling
```html
.card {
 	font-family: Segoe UI;
 	font-size: 22px;
 	text-align: left;
 	color: black;
}

#term {
	font-family: Segoe UI;
	font-size: 28px;
	font-weight: bold;
	text-align: center;
	color: blue;
}

#transcription {
	font-family: helvetica;
	font-size: 18px;
	text-align: center;
}

#translation {
	font-family: Segoe UI;
	font-size: 18px;
	text-align: left;
	color: ;
}

#definition {
	font-family: verdana;
	font-size: 20px;
	margin-top: 12px;
}

#context {
	font-family: verdana;
	font-size: 21px;
	font-style: ;
	padding: 8px;
	margin-bottom: 0px;
	border-radius: 6px;
	line-height: 90%;
	position: absolute;
}

h1 {
	position: relative;
	margin-bottom: 10px;
	margin-top: 16px;
	color: #839496; 
}

h1.one {
	font-size: 14px;
}

h1.one:before {
	content: "";
	display: block;
	color: #999;
	border-top: solid 1px #93a1a1;
	width: 100%;
	height: 1px;
	position: absolute;
	top: 50%;
	z-index: 1; 
}

h1.one span {
	background: ivory;
	color: #999;
	padding: 0 20px;
	position: relative;
	z-index: 5;
}

.extra {
	font-size: 16px;
}
```

