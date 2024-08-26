# Setup

Instalar python [3.12.5](https://www.python.org/downloads/)

## Entornos Virtuales

Para trabajar en un entorno seguro, y para no tener problemas de incompatibilidades con las dependencias que usamos, vamos a usar entornos virtuales. Para esto vamos install `pipenv`:

```shell
pip install pipenv
```

Cada vez que vayamos a trabajar en el proyecto, debemos activar el entorno virtual, para debemos correr el siguiente comando primero:

```shell
pipenv shell
```

### Dependencias

Las dependencias que usamos van a estar listasdas en el archivo `Pipfile` junto con otros datos para especifican un configuración estandar para el proyecto.
Para instalar las mismas, corremos este comando

```shell
pipenv install
```

Verificamos que se hayan instalado correctamente:

```shell
pipenv check
```

Para instalar otra dependencia:

```shell
pipenv install <dependencia>
```

## Migraciones

Lo siguiente que tenemos que hacer es migrar el mapeo de los objetos que hicimos hacia la base de datos. Para esto, vamos a crear una nueva conexión en mysql workbench con nombre de usario `root`.
> Es importante que el nombre de usuario sea root porque así está configurado en setting.py.

Una vez tenemos la conexión creada, tenemos que crear la base de datos. Para esto vamos a correr el siguiente comando en una query cualquiera en mysql workbench:

```sql
create database <nombre-que-quieran>
```

### .Env

Para que cada uno use contraseñas y creadencias que quiera, vamos a crear un archivo `.env` dentro de `recomendacion_de_donaciones/recomendacion_de_donaciones` y vamos a establecer las siguientes variables de entorno:

```env
DB_NAME=<nombre-de-la-base-de-datos>
PASSWORD=<contrasena-de-mysql>
PORT=<puerto>
```

De esta forma vamos a poder crear variables las cuales van a guardar las credenciales propias de cada uno.

Finalmente, vamos a realizar la migración. Para esto, nos paramos en `recomendacion_de_donaciones` y corremos el siguiente comando:

```python
python manage.py migrate
```

### Ejecutar el Proyecto

Para correr el proyecto, usamos este comando estando parados en `recomendacion_de_donaciones`:

```python
python manage.py runserver
```
