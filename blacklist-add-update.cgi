#!/bin/bash
echo "Content-type: text/html"
echo ""

# LEE LOS PARAMETROS ENVIADOS POR EL NAVEGADOR
CMD=`echo "$QUERY_STRING" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
NUMERO=`echo "$QUERY_STRING" | sed -n 's/^.*numero=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
NOMBRE=`echo "$QUERY_STRING" | sed -n 's/^.*nombre=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`

# our html header
    echo "<html>"
    echo "<head><title>ASTERISK</title></head>"
    echo "<body>"

# VALIDA EL COMANDO QUE SE ESTA ENVIANDO
    if [ $CMD ] 
    then
      case "$CMD" in
    	blacklist-add-update)
            echo "<pre>"
            asterisk -rx "database put blacklist $NUMERO \"$NOMBRE\""
            echo "</pre>"
            ;;

# MUESTRA UN ERROR PA QUE CREAN QUE HAY SEGURIDAD
        *)
            echo "ERROR: 8990 --> $CMD"
            ;;
      esac
    fi

# CIERRA ETIQUETAS HTML    
    echo "</body>"
    echo "</html>"