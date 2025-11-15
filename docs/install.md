## Instalación del proyecto

El primer paso sera descargar el código fuente desde el repositorio:

```shell
git clone https://github.com/euribates/olakase
```

Esto nos creara la carpeta olakease, a la que tenemos que entrar
con:

```shell
cd olakease
```

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
