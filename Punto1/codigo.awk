#!/usr/bin/awk -f

BEGIN {
    print "Analizador Léxico - Reconocimiento de Números Decimales"
}

# Analizador léxico en AWK
{
    while (match($0, /[0-9]+\.[0-9]+/)) {
        print "TOKEN: NUMERO_DECIMAL -> " substr($0, RSTART, RLENGTH);
        $0 = substr($0, RSTART + RLENGTH); # Avanzar en la línea
    }
}

