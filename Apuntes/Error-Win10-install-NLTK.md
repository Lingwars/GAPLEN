# Error al instalar NLTK en Windows 10

Hemos detectado un pequeño error que salta al intentar instalar NLTK en Windows 10: estás siguiendo al pie de la letra el libro de NLTK, te has instalado Python 3.6, te has descargado NLTK 3.4 y, cuando vas a ejecutar este último para instalarlo, ¡bam!, te sale este mensaje:

_Python version -32 required, which was not found in the registry_

y no te deja continuar.

La solución está en usar pip (ya explicamos en el blog [cómo instalar pip](http://lingwars.github.io/blog/instalar-python-en-windows-7.html)) para instalar NLTK, que consiste simplemente en abrir el cmd y teclear: `python -m pip install nltk`
