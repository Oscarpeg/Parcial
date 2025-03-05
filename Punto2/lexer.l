%{
#include <stdio.h>

int valid = 1; // Bandera para saber si la entrada es válida
%}

%%
[a-zA-Z_][a-zA-Z0-9_]*[ \t]*=[ \t]*lambda[ \t]*[a-zA-Z_][a-zA-Z0-9_]*[ \t]*:[ \t]*[a-zA-Z0-9_ \t]+(\*\*[ \t]*[0-9]+)? {
    printf("TOKEN: LAMBDA_ASSIGN -> %s\n", yytext);
}

print[ \t]*\([ \t]*[a-zA-Z_][a-zA-Z0-9_]*[ \t]*\([ \t]*[0-9]+[ \t]*\)[ \t]*\) {
    printf("TOKEN: FUNCTION_CALL -> %s\n", yytext);
}

.|\n { valid = 0; } // Si hay un caracter inesperado, la entrada es inválida
%%

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Uso: %s archivo.txt\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    yyin = file;
    yylex();
    fclose(file);

    if (valid)
        printf("ACEPTA\n");
    else
        printf("NO ACEPTA\n");

    return 0;
}

int yywrap() {
    return 1;
}
