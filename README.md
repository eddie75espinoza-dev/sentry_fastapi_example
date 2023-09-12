# Ejemplo de **SENTRY** con *FastApi*
El middleware ASGI para [Sentry]('https://sentry.io/welcome/') requiere [Python]() 3.7+  o el paquete aiocontextvars. 

## Creación de *entorno virtual*

```bash
python3.8 -m venv venv
```
### Activación en Linux

```bash
source venv/bin/activate
```

## Instalación de dependencias

```bash
python -m pip install -r requirements.txt
```

## Instalación SENTRY 
Para usar con FastApi, ejecución realizada desde *requirements.txt*

```bash
pip install --upgrade 'sentry-sdk[fastapi]'
```


## Ejecución de script
Ejecute en la línea de comandos

```bash
python app.py
```

Esto permitirá levantar http://0.0.0.0:8050 asignado en app.py, una vez allí,
vaya a la dirección:

```html
http://0.0.0.0:8050/sentry-debug
```

Esto ejecutará la excepción del código y registrará en Sentry el issue.

