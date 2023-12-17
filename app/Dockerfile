FROM python:3.8

WORKDIR /app
COPY requirements.txt /app/requirements.txt 
#copiando el archivo que esta en local y pasandolo asia el entono virtual

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt  
#Dejar listo la instalacion de la dependencias
#Hasta acá hemos copiado el archivo requirements.txt

#Acá copiamos todo el proyecto
COPY . /app 
#Los espacios son importantes

CMD bash -c 'while true; do sleep 1; done'
#Para que corra continuamente/ Mantiene encendido el contenedor