#!/bin/bash
echo "Content-type: text/html"
echo ""

# LEE LOS PARAMETROS ENVIADOS POR EL NAVEGADOR
CMD=`echo "$QUERY_STRING" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
EXT=`echo "$QUERY_STRING" | sed -n 's/^.*ext=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`

# our html header
    echo "<!DOCTYPE html>"
    echo "<html>"
    echo "<head><title>ASTERISK</title></head>"
    echo "<body>"

# VALIDA EL COMANDO QUE SE ESTA ENVIANDO
    if [ $CMD ] 
    then
      case "$CMD" in
        grptime-check)
            echo "<pre>"
            asterisk -rx "database get AMPUSER $EXT/followme/grptime" | tr -d "[:blank:]" | jq -R -s -c 'split("\n")[:-1]' | jq 'map(split(":"))' | jq '. | map( [{(.[0]): .[1]}] ) | add'
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