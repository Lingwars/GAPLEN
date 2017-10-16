Recursos para empezar a programar en Python
===========================================

¿Te has apuntado al grupo de aprendizaje de NLTK, pero nunca has programado antes y no sabes por dónde empezar? No te preocupes, aquí vas a encontrar unos enlaces que te van a ayudar.   

Con este documento no pretendemos ofrecer una lista completa de recursos sobre programación en general y Python en particular, sino un pequeño "track" después del que tendrás conocimientos básicos de Python y sabrás crear y ejecutar un script.

En concreto, te recomendamos que sigas los siguientes pasos:

#. **Aprende Python a nivel básico**
	En teoría el libro oficial de NLTK está pensado para ser utilizado por gente que nunca ha programado en Python. En la práctica la lectura se te va a hacer más fácil si ya estás un poco familiarizado con este lenguaje. Para dar tus primeros pasos con Python, puedes seguir uno de los siguientes cursos online:

	- `Learn Python`_ de Codecademy
	- `Python 3 Tutorial`_ de SoloLearn

	Los dos cursos contienen ejercicios interactivos y cubren más o menos los mismos temas, así que puedes probar los dos y seguir con el que más te guste. No es necesario que completes un curso entero: después de los 3-4 primeros módulos de cualquiera de los dos cursos ya puedes pasar al siguiente paso de este "track".

	.. _Learn Python: https://www.codecademy.com/learn/learn-python
	.. _Python 3 Tutorial: https://www.sololearn.com/Course/Python/

#. **Familiarízate con la línea de comandos**

	En cuanto empieces a programar por tu cuenta, vas a tener que aprender a manejarte con la línea de comandos. Puedes empezar por este breve `tutorial de Django Girls`_ que explica cómo navegar por tus archivos usando la línea de comandos.

	.. _tutorial de Django Girls: https://tutorial.djangogirls.org/en/intro_to_command_line/


#. **Instala Python con Anaconda**

	Para poder utilizar Python lo tienes que tener instalado en tu ordenador. Hay diferentes maneras de hacerlo, pero te recomendamos que utilices `Anaconda`_, una distribución de Python que viene con muchos paquetes preinstalados, entre ellos NLTK. Simplemente elige la versión que corresponde a tu sistema operativo e instálala siguiendo las instrucciones. También, asegúrate de elegir la versión que viene con Python3 y no la de Python2.

	Si utilizas Windows, sigue las siguientes instrucciones para que la instalación se realice bien (en los otros sistemas operativos no suele haber problemas):

	  - Doble click en el ejecutable descargado. **MUY IMPORTANTE** No ejecutarlo como administrador. Elegir "Just me...". Lo instalará para el usuario actual. No hacen falta derechos administrativos.
	  - Dejar el directorio de instalación por defecto. Si se cambia no utilizar espacios ni caracteres como ñ o con tilde.
	  - **MUY IMPORTANTE** En el cuadro "Advanced Installation Options" **NO** marcar "Add Anaconda to my path..." **SÍ** marcar "Register Anaconda as my..."

	Una vez finalizada la instalación, en la consola de línea de comandos teclea ``python``. Si te aparece un mensaje de tipo ``Python 3.6.1 |Anaconda 4.4.0 (x86_64)| (default, May 11 2017, 13:04:09)``, es que todo se ha instalado bien y puedes empezar a utilizar Python desde la consola (por ejemplo, intenta escribir ``2 + 2`` y ver que pasa).

	Como puedes ver, instalar Python con Anaconda es muy fácil, pero por si acaso puedes echarle un vistazo al tutorial `Anaconda Installation and Using Conda`_. De momento solo hace falta que lo veas hasta el minuto 5:20.

	.. _Anaconda: https://www.anaconda.com/download/
	.. _Anaconda Installation and Using Conda: https://www.youtube.com/watch?v=YJC6ldI3hWk

#. **Aprende a crear y ejecutar un script de Python con Spyder**
 
	¿Qué programa hay que utilizar para escribir código en Python y luego ejectuarlo? Hay muchísimas formas de hacerlo, pero nosotros te recomendamos que utilices el IDE (entorno de desarrollo integrado) `Spyder`_ que viene incluido en Anaconda. Para lanzarlo solo tienes que escribir ``spyder`` en tu consola.

	Antes de empezar a trabajar en Spyder, te aconsejamos que hagas un pequeño cambio de configuración. En concreto, en el menu, tendrás que ir a *python > Preferences > Run* y seleccionar *Clear all variables before execution*.

	Para aprender a utilizar Spyder, puedes seguir `este tutorial`_. Ya verás que no es nada difícil.

	Si por lo que sea no te gusta Spyder, puedes utilizar otro IDE o incluso escribir tu código en un editor de texto avanzado, como puede ser `Sublime Text`_ o el `Notepad++`_, y luego ejecutarlo desde la consola. El tutorial `Creating Python Programs`_ te explica cómo hacerlo.


	.. _Spyder: https://pythonhosted.org/spyder/
	.. _este tutorial: https://www.youtube.com/watch?v=a1P_9fGrfnU
	.. _Sublime Text: https://www.sublimetext.com/3
	.. _Notepad++: https://notepad-plus-plus.org/download/v7.5.html
	.. _Creating Python Programs: https://en.wikibooks.org/wiki/Python_Programming/Creating_Python_Programs


#. **Aprende a utilizar Jupyter Notebook**

	Una herramienta a la que seguramente le daremos mucho uso en nuestro grupo de aprendizaje es `Jupyter Notebook`_.   

	Jupyter Notebook es una aplicación web que permite crear "cuadernos" con código Python, textos explicativos, gráficos y otros contenidos multimedia. Lo bueno de Jupyter es que el código se puede ejecutar directamente en el cuaderno. Jupyter viene incluido en Anaconda, así que si has realizado el paso 3, ya lo tienes en tu ordenador.    

	Para aprender a usar Jupyter te recomendamos el `Jupyter Notebook Tutorial`_.

	.. _Jupyter Notebook: http://jupyter.org/
	.. _Jupyter Notebook Tutorial: https://www.youtube.com/watch?v=HW29067qVWk
