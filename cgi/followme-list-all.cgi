#!/bin/bash
echo "Content-type: text/html"
echo ""

# LEE LOS PARAMETROS ENVIADOS POR EL NAVEGADOR
CMD=`echo "$QUERY_STRING" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

# our html header
    echo "<html>"
    # echo "wget --save-cookies cookies.txt --keep-session-cookies --post-data=\"username=foo&password=bar\" \"http://some.site/login.php\""
    # echo "<meta http-equiv=\"refresh\" content=\"0; url=http://www.youtube.com/\"/>"
    echo "<head><title>ASTERISK</title></head>"
    echo "<body>"

# VALIDA EL COMANDO QUE SE ESTA ENVIANDO
    if [ $CMD ] 
    then
      case "$CMD" in
    	followme-list-all)
            echo "<pre>"
            
            #asterisk -rx "database show" | grep grplist | tr -d "[:blank:]" | jq -R -s -c 'split("\n")[:-1]' 
            
            asterisk -rx "database show" | grep grplist | tr -d "[:blank:]" | jq -R -s -c 'split("\n")[:-1]' | jq 'map(split(":"))' | jq '. | map( [{(.[0]): .[1]}] ) | add'
            
            #asterisk -rx "database show" | grep grplist | jq -R 'split (":")' | tr -d "[:blank:]"
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
