media2elp
=========

MediaWiki to elp (ExeLearning) Exporter
<p>
El programa consta de 3 arxius python, un Loader, un Saver i un runner i un servidor en php que genera l'arxiu de text entrada. 
<ol>
<li>Mediawiki envia al servidor php (elprenderer.php) la informació en JSON. Tenim un exemple en 666.txt. El servidor php llegirà un arxiu (id.txt) per tal de saver quin és el següent id a utilitzar. I executarà el controlador (run.py) passant-li com a paràmetre el id corresponent.
<li>El controlador (Run.py) carrega amb el loader les estructures de dades necessàries per crear el .elp 
<li>El controlador (Run.py) guarda les dades amb el saver
</ol>
</p>
Nota: Cal configurar en la mediawiki que agarre este servidor<br/>
Nota2: Cal les carpetes de l'exe learning per a poder executar el parser, ja que les utilitza


English Version
===============
The program consists of three python files, a loader, a Saver and a runner and a PHP server that generates the text file input. 
<p>
<ol>
<li>MediaWiki server sends php (elprenderer.php) information in JSON. One example 666.txt. PHP read a file server (id.txt) to what the next id saver to use. I run the driver (run.py) passing as parameter the corresponding id. 
<li>The controller (Run.py) loader loads the data structures necessary to create .elp 
<li>The controller (Run.py) saves the data
</ol>
Note: You must configure the grip that this server MediaWiki<br/>
Note 2: El folders of exelearning are needed to execute the parser
</p>
