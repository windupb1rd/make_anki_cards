front = """<div id="term">{{Term}}<br></div>

<div id="transcription">{{Transcription}}<br>
{{Audio}}</div>"""


back = """{{FrontSide}}

<h1 class="one"><span>TRANSLATION</span></h1>
<div id="translation"> {{edit:Translation}} </div>

<h1 class="one"><span>MEANING</span></h1>
<div id="definition"> {{edit:Definition}} </div>

{{#Context}}
<h1 class="one"><span>CONTEXT</span></h1>
<div class="context" id="context">{{edit:Context}}</div>
{{/Context}}"""


style = """.card {
 	font-family: Segoe UI;
 	font-size: 22px;
 	text-align: left;
 	color: black;
	background: DarkSlateGrey;
}

#term {
	font-family: Segoe UI, sans-serif;
	font-size: 28px;
	font-weight: bold;
	text-align: center;
	color: Lavender;
	background: 	#264040;
}

#transcription {
	font-family: helvetica, sans-serif;
	font-size: 18px;
	text-align: center;
	color: azure;
	background: DarkSlateGrey;
}

#translation {
	font-family: verdana, sans-serif;
	font-size: 18px;
	text-align: left;
	color: Lavender;
	background: #264040;
}

#definition {
	font-family: verdana, sans-serif;
	font-size: 18px;
	margin-top: 12px;
	background: #264040;
	color: Lavender;
}

#context {
	font-family: Lucida Console, sans-serif;
	font-size: 18px;
	font-style: ;
	padding: ;
	margin-bottom: 0px;
	border-radius: 6px;
	line-height: 120%;
	position: absolute;
	color: Lavender;
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
	background: SlateGrey;
	color: lavender;
	padding: 0 20px;
	position: relative;
	z-index: 5;
}

.extra {
	font-size: 16px;
}"""


style1 = """.card {
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
}"""

deck_conf = {'id': 1641449709710,
 'mod': 1641974383, 
 'name': 'AnkiCardMakerSchedule',
 'usn': 46, 
 'maxTaken': 60, 
 'autoplay': True, 'timer': 0, 
 'replayq': True, 
 'new': {'bury': False, 'delays': [5.0, 10.0, 240.0, 480.0, 1440.0],
        'initialFactor': 2500, 'ints': [2, 4, 0],
         'order': 1, 'perDay': 10},
 'rev': {'bury': False, 'ease4': 1.3, 'ivlFct': 1.0, 'maxIvl': 36500, 'perDay': 1000, 'hardFactor': 1.2},
 'lapse': {'delays': [10.0], 'leechAction': 1, 'leechFails': 8, 'minInt': 1, 'mult': 0.5}, 'dyn': False}
