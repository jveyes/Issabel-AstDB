#!/bin/bash
echo "Content-type: text/html"
echo ""

# read in our parameters
CMD=`echo "$QUERY_STRING" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
KEYS=`echo "$QUERY_STRING" | sed -n 's/^.*key=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`

# our html header
    echo "<html>"
    echo "<head><title>ASTERISK CGI</title></head>"
    echo "<body>"


# test if any parameters were passed
    if [ $CMD ]
    then
      case "$CMD" in
    	keys)
        echo "LISTA DE LLAVE "$KEYS" :<pre>"
	asterisk -rx "database showkey \"$KEYS\""
        echo "</pre>"
        ;;

	allkeys)
	echo "TODA LA BASE DE DATOS :<pre>"
        asterisk -rx "database show"
        echo "</pre>"
        ;;


    *)
        echo "COMANDO DESCONOCIDO --> $CMD<br>"
        ;;
      esac
    fi

    # print out the form
    # page header
    echo "<p>"
    echo "<center>"
    echo "<h2>ASTERISK</h2>"
    echo "</center>"
    echo "<p>"
    echo "<p>"
    echo "<form method=get>"
    echo "<br>ASTDB<br>"
    echo "##########<br>"
    echo "<input type=radio name=cmd value=keys> LLAVE A MOSTRAR <input type=text name=key><br>"
    echo "<input type=radio name=cmd value=allkeys> MOSTRAR TODA LA BASE DE DATOS<br>"    
    echo "<br><input type=submit>"
    echo "</form>"
    echo "</body>"
    echo "</html>"
