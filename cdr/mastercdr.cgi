#!/bin/bash
echo "Content-type: text/html"
echo ""

# LEE LOS PARAMETROS ENVIADOS POR EL NAVEGADOR
CMD=`echo "$QUERY_STRING" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
FECHA=`echo "$QUERY_STRING" | sed -n 's/^.*fecha=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`

# BASE DE CODIGO HTML
    echo "<html>"
    echo "<head><title>ASTERISK</title></head>"
    echo "<body>"
    
# VALIDA EL COMANDO QUE SE ESTA ENVIANDO
    if [ $CMD ] 
    then
      case "$CMD" in
    	master-cdr)
            echo "<pre>"
		jq -Rsn '
            	[inputs
                	| . / "\n"
                	| (.[] | select(length > 0) | . / ",") as $input
                	| {"CID": $input[0], "ORIGEN": $input[1], "DESTINO": $input[2], "CONTEXTO": $input[3], "CANAL ORIGEN": $input[4], "CANAL DESTINO": $input[5], "APP": $input[6],"LLAMADA INICIADA": $input[7], "LLAMADA CONTESTADA": $input[8], "LLAMADA TERMINADA": $input[9], "DURACION": $input[10], "TIEMPO AL AIRE": $input[11], "ESTADO LLAMADA": $input[12], "BANDERA": $input[13], "ID LLAMADA": $input[14] }]
            	' <"$FECHA.csv" | sed 's/\\"//g'
            echo "</pre>"
            ;;

# MUESTRA UN ERROR PA' QUE CREAN QUE HAY SEGURIDAD
        *)
            echo "ERROR: 8990 --> $CMD"
            ;;
      esac
    fi

# CIERRA ETIQUETAS HTML    
#    echo "</body>"
#    echo "</html>"
