#PATRONES DE DISEÑO DECORATOR Y SINGLETON:

**DECORATOR:** El patrón Decorator responde a la necesidad de añadir dinámicamente funcionalidad a un Objeto. Esto nos permite no tener que crear sucesivas clases que hereden de la primera incorporando la nueva funcionalidad, sino otras que la implementan y se asocian a la primera. 

**SINGLETON:** singleton o instancia única es un patrón de diseño que permite restringir la creación de objetos pertenecientes a una clase o el valor de un tipo a un único objeto. Su intención consiste en garantizar que una clase solo tenga una instancia y proporcionar un punto de acceso global a ella.

#CÓDIGO:

- En el fichero singleton.py se podrán observar 3 secciones de código.
La primera corresponde al código del patrón de diseño decorator en el que agregamos la funcionalidad de crear una sola instancia de las clases que implementen este decorador que he llamado singleton.

- El segundo bloque de código corresponde a la creación de una clase Contact en la que utilizo el decorador (singleton) creado en la primera sección. Adicionalmente se crean varias instancias de la misma clase y como resultado obtendremos la implementación del patrón de diseño singleton.

- El tercer bloque de código lo que hicimos fue crear el patrón de diseño singleton de cero, sin utilizar el decorados. En otras palabras tomamos como referencia la forma como se codifica la creación del patrón singleton en Java y lo adaptamos al código en Python

#PRE-REQUISITOS:
`1.	Instalar Python (se recomienda la última versión) https://www.python.org/downloads/`

`2.	Un IDE para python que puede ser VSCode o PyCharm`

#PUESTA EN MARCHA:

`1. git clone git@github.com:Adrian-Vergara/decorator_singleton_python.git`

`2. Abrir una terminal y en la ubicación donde se encuentra el código clonado`

`3. ejecutar en consola el comando: python singleton.py`