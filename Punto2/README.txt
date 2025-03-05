Descripción

Este proyecto es un analizador léxico desarrollado en LEX que permite identificar tokens en un archivo de entrada. El programa procesa expresiones específicas y devuelve los tokens reconocidos según las reglas definidas en el archivo de especificación de LEX.

Requisitos

Antes de ejecutar el programa, es necesario instalar LEX y las herramientas necesarias para compilar y ejecutar el analizador.

Instalación de LEX

Dependiendo del sistema operativo, los pasos pueden variar:

Linux (Ubuntu/Debian):

Abrir una terminal.

Ejecutar el siguiente comando para instalar flex:

sudo apt-get install flex

MacOS:

Abrir una terminal.

Instalar Homebrew si no está instalado:

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Instalar flex con Homebrew:

brew install flex

Windows:

Instalar Cygwin o WSL con soporte para flex.

En Cygwin, asegurarse de incluir flex durante la instalación.

Archivos del Proyecto

analizador.l: Archivo de especificación de LEX que define las reglas de reconocimiento de tokens.

lex.yy.c: Archivo generado por flex al compilar analizador.l.

analizador: Archivo ejecutable generado después de la compilación.

input.txt: Archivo de entrada con las expresiones a analizar.

Compilación y Ejecución

Compilar el analizador

Para generar el código C a partir del archivo LEX:

flex analizador.l

Compilar el archivo generado:

gcc lex.yy.c -o analizador -lfl

Ejecutar el analizador

Ejecutar el programa con un archivo de entrada:

./analizador < input.txt

Ejemplo de Entrada

Si input.txt contiene:

square = lambda x: x ** 2
print(square(3))

El analizador identificará y mostrará los tokens correspondientes.
