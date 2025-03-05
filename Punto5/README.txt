Descargar ANTLR:

1. Ir a la página oficial de ANTLR y descargar la versión más reciente del archivo JAR.
Guardarlo en una carpeta accesible, por ejemplo, en el escritorio dentro de una carpeta llamada "antlr".

2.Configurar ANTLR en la terminal:
Abrir la terminal y agregar la siguiente línea al archivo de configuración de la terminal (por ejemplo, .zshrc o .bashrc) con nano.
export CLASSPATH=".:/ruta/a/antlr-4.13.2-complete.jar:$CLASSPATH"
Guardar y cerrar el archivo, luego ejecutar source  .bashrc para aplicar los cambios.

3. Crear los archivos del proyecto:
Crear una carpeta para el proyecto, por ejemplo, "Complex".
Dentro de esta carpeta, crear los archivos necesarios:
Complex.g4 (definición de la gramática)
ComplexEvalVisitor.java (implementación del visitor)
ComplexMain.java (archivo principal para ejecutar la Complex)

4. Escribir la gramática en Complex.g4:
Definir la estructura de la Complex en este archivo.
Asegurar que la regla inicial se llame prog y que incluya operaciones matemáticas básicas.

5. Generar los archivos de ANTLR:
Navegar a la carpeta del proyecto en la terminal.
Ejecutar el siguiente comando para generar los archivos Java de ANTLR:
java -jar /ruta/a/antlr-4.13.2-complete.jar -Dlanguage=Java -visitor Complex.g4

6.Compilar los archivos generados y los archivos Java del proyecto:
Ejecutar el siguiente comando para compilar todo el código:
javac -cp .:/ruta/a/antlr-4.13.2-complete.jar *.java

7.Ejecutar la Complex:
Iniciar la Complex con el siguiente comando:
java -cp .:/ruta/a/antlr-4.13.2-complete.jar ComplexMain

8.Probar la Complex:


