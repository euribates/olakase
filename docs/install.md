## Instalación del proyecto

### Paso 1: Clonar el repositorio del proyecto

El primer paso sera descargar el código fuente desde el repositorio:

```shell
git clone https://github.com/euribates/olakase
```

Esto nos creá la carpeta `olakease`, a la que tenemos que entrar
con:

```shell
cd olakease
```

### Paso 2: Crear un entorno virtual

El segundo paso es crear el entorno virtual para el proyecto

Si usamos `uv`:
        
```
uv venv
```

Si no queremos usar `uv`, podemos usar el módulo `venv`, que
está disponible desde la versión 3.3 de Python.

```
python -m venv .venv
```

De cualquiera de las dos maneras, tenemos que tener un entorno
virtual en la carpeta `.venv`, que podemos activar
con:

```
source .venv/bin/activate
```

### Paso 3: Instalar Django y el resto de dependencias

Los requerimientos están en
`[requirements.txt](../requirements.txt)`.

De nuevo, podemos hacerlo usando `uv`:

```
uv pip install -r requirements.txt
```

O si no queremos usarlo:

```
python -m pip install -r requirements.txt
```

### Paso 4: Comprobar que todo está correctamente instalado

Primero, nos pasamos al directorio `web`, que es donde está
el servidor web del proyecto:

```
cd web
```

Una vez aquí, podemos realizar una serie de comprobaciones
para ver que todo esté correctamente instalado:

```
python manage.py check
```

Debería imprimir algo como esto:

```
System check identified no issues (0 silenced).
```

Si tenemos `just`, podemos hacer:

```
just check
```

### Paso 5: Ejecutar migraciones iniciales

Si todo ha ido bien,  podemos ejecutar:

```
python manage.py migrate
```

Para crear la base de datos y realizar las migraciones iniciales, seguido de:

```
python manage.py loaddata tasks/fixtures/tasks.json
```

Para tener en la base de datos algunas tareas con las que podamos jugar.

Si usamos `just`, los pasos 3, 4, 5 podemos realizarlos con la orden:

```
just startup
```

### Paso 6: Ejecutar el servidor de desarrollo

Por  último, arrancar el servidor en modo desarrollo, y
comprobar que podemos acceder con un navegador
a <http://localhost:8000/>, haremos:

Si usas `just`:

```
just rundev
```

Si no:

```
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000
```
