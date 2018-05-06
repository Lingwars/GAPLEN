Kata 1: reescritura (fácil)
===========================

Problema
--------

Tenemos un fichero ``test.py`` con el siguiente contenido:

.. code :: python

	import pytest
	import kata_normalizacion

	testdata = [
		# 1 ejemplo
		('¿Dónde está el camino hacia las Puertas de Moria?',
		'donde esta el camino hacia las puertas de moria')
	]

	@pytest.mark.parametrize('entrada, salida', testdata)
	def test_funcion_normalizacion(entrada, salida):
		frase_normalizada = kata_normalizacion.funcion_normalizacion(entrada)
		assert frase_normalizada == salida
..

Lo que debemos hacer es crear un fichero ``kata_normalizacion.py`` en el que
debe definirse una función ``funcion_normalizacion`` que supere el test unitario
definido en ``test.py``.

Soluciones
----------

Hay muchas posibles soluciones a la kata.

1. Usando ``maketrans``:

- Una manera

.. code :: python

	def funcion_normalizacion(entrada):
		out_str = "aeiouAEIOU"
		in_str = "áéíóúÁÉÍÓÚ"
		transtab = entrada.maketrans(in_str,out_str)
		return entrada.translate(transtab).lower().replace("?","").replace("¿","")
..

- Otra manera

.. code :: python

	signos = "¿?"
	intab = "óáDPM"
	outtab = "oadpm"
	transform = str.maketrans(intab, outtab, signos)

	def funcion_normalizacion1(entrada):
		return entrada.translate(transform)
..

2. Usando un bucle:

.. code :: python
	
	signos = "¿?"

	def funcion_normalizacion2(entrada):
	lista = []
	for carácter in entrada:
		if carácter == "ó":
			lista.append("o")
		elif carácter == "á":
			lista.append("a")
		elif carácter == "D":
			lista.append("d")
		elif carácter == "P":
			lista.append("p")
		elif carácter == "M":
			lista.append("m")
		elif carácter not in signos:
			lista.append(carácter)
	return "".join(lista)
..

