media2elp
=========

MediaWiki to elp (ExeLearning) Exporter
<p>
El programa consta de 3 arxius python, un Loader, un Saver i un runner i un servidor en php que genera l'arxiu de text entrada. 
1. Mediawiki envia al servidor php (elprenderer.php) la informació en JSON. Tenim un exemple en 666.txt. El servidor php llegirà un arxiu (id.txt) per tal de saver quin és el següent id a utilitzar. I executarà el controlador (run.py) passant-li com a paràmetre el id corresponent.
2. El controlador (Run.py) carrega amb el loader les estructures de dades necessàries per crear el .elp 
3. El controlador (Rune.pyr) guarda les dades amb el saver
</p>
