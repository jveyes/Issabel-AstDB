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
        grptime-delete)
            echo "<pre>"
            asterisk -rx "database put AMPUSER $EXT/followme/grptime 30" | sed 's/Updated database successfully/[ { "query": grptime, "id": 1002, "status": Database entry removed-updated successfully } ]/g'
            # ELIMINA UNA EXTENCION QUE ESTE CREADA
            # asterisk -rx "database del AMPUSER $EXT/followme/grptime"
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