
Los archivos en este directorio sirven para generar la *documentación* del repositorio
de GAPLEN que puede visitarse en [este enlace](http://gaplen.readthedocs.io/es/latest/).

Esta documentación se genera automáticamente y se publica online cada vez que se realiza un commit en la
rama `master` del repositorio; no obstante, las modificaciones pueden (y deben) probarse en local
antes de subirlas, para ello:

 1. Descarga el repositorio

    ```
    git clone https://github.com/lingwars/gaplen.git
    cd gaplen/docs
    ```

 1. Realizar las modificaciones oportunas. Recuerda que utilizamos
    [reStructuredText](http://docutils.sourceforge.net/rst.html), no es complicado,
    puedes encontrar una referencia de los comandos principales [aquí](http://docutils.sourceforge.net/docs/ref/rst/directives.html).

 1. Para ver tus cambios en local simplemente ejecuta (Windows o Linux, supongo que Mac también):

    ```
    make html
    ```
    (*Recuerda que necesitarás tener instalado `sphinx` para que funcione (simplemente `pip install sphinx`)*)

    Y abre el archivo que encontrarás en `_build/docs/html/index.html` utilizando el
    navegador web que quieras.

 1. Una vez que veas que todo está correcto, haz commit, pull-request,...
 


