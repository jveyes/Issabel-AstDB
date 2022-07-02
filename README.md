
<h1 align="center">Issabel-AstDB</h1>
<p align="center">
  <i>Issabel-AstDB te puede ayudar a crear, visualizar, actualizar o eliminar infomacion que se encuentre en la base de datos de asterisk (AstDB) que esta usando Issabel, todo esto es posible gracias a unos scripts basicos de cgi</i>
   <br/>
  <img width="120" src="https://i.ibb.co/LdRcFrW/Issabel-Ast-DB.webp" />
  <br/>
  <b><a href="https://www.issabel.org/">Issabel</a></b> | <b><a href="https://www.asterisk.org/">Asterisk</a></b> | <b><a href="https://www.wikiasterisk.com/index.php/AstDB">AstDB</a></b> | <b><a href="https://www.sqlite.org/index.html">SQLite</a></b> | <b><a href="https://stedolan.github.io/jq/">./jq</a></b>
  <br/><br/>
</p>

## Caracteristicas
- Crear la logica para hacer CRUD a la base de datos <a href="https://wiki.asterisk.org/wiki/display/AST/Asterisk+Internal+Database">AstDB</a> la cual se origina de <a href="https://es.wikipedia.org/wiki/Berkeley_DB">Berkeley DB</a>
- Configurar todo lo que necesites en <a href="https://en.wikipedia.org/wiki/Common_Gateway_Interface">CGI</a> web con <a href="https://en.wikipedia.org/wiki/Bash_(Unix_shell)">Bash scripts</a>
- Leer las solicitudes por medio de un navegador web
- Validacion de la peticion web en el servidor en la ruta <a href="https://es.wikipedia.org/wiki/Interfaz_de_entrada_com%C3%BAn">cgi-bin</a>
- Ejecuta una peticion a Asterisk por medio de <a href="https://wiki.asterisk.org/wiki/display/AST/Connecting+to+the+Asterisk+CLI">asterisk -rx</a>
- Muestra el resuldado con formato <a href="https://www.rfc-editor.org/info/rfc8259">json</a>

## Alcance de este ejercicio

<p>
  <i>El alcance de este ejercicio es modificar 2 opciones que usualmente podemos hacerlo por el GUI de issabel PBX, como lo son el <b>Blacklist</b> y  <b>Follow Me</b>.<br /></i>
   <br/>
  <p align="center">
	  <img src="https://i.ibb.co/rvtKvSG/bl-fm.webp" />
  </p>
  <br/>
  <i>Estas 2 opciones se encuentrar en la base de datos AstDB la cual almacena sus datos en agrupaciones llamadas <b>families</b>, con valores identificados por <b>keys</b>. Dentro de una familia, una clave solo se puede usar una vez. Por ejemplo, si tuviéramos una familia llamada test, podríamos almacenar solo un valor con una clave llamada count. Cada valor almacenado debe estar asociado a una familia.<br /><br />Existen 2 formas de modificar estas familias y llaves, por medio de las aplicaciones SET en el dialplan o por medio de la consola de Asterisk <b>CLI></b>, pero la ejecutaremos de forma forma remota con la ayuda de <b>asterisk -rx</b>, todo esto directamente desde la terminal de linux donde tenemos el Issabel instalado.</i>
  <br/>
  <br/>

```
CLI> help database
	database del                   -- Removes database key/value
	database deltree               -- Removes database keytree/values
	database get                   -- Gets database value
	database put                   -- Adds/updates database value
	database query                 -- Run a user-specified query on the astdb
	database show                  -- Shows database contents
	database showkey               -- Shows database contents
```


---

## Requisitos

---

## Instalacion jq (linux output --> formato json)

---
## Ejemplos Asterisk CLI>

---
## Ejemplos asterisk -rx (remoto*)

---
## Creacion de scripts CGI

---
## Ejemplos de modificacion de AstDB por medio del navegador web

---

<p align="center">
  <br>
  <a href="https://trackgit.com">
<img src="https://us-central1-trackgit-analytics.cloudfunctions.net/token/ping/l5385l9o46mbp449x6el" alt="trackgit-views" />
</a>
  <br><br>
  <a href="https://github.com/jveyes">
    <img width="40" src="https://avatars.githubusercontent.com/u/4891933?v=4" />
  </a>
  <br><br>
  <i>Gracias por visitar</i>
</p>
