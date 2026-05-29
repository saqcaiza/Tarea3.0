#paso 1 crear una iamgen

FROM python:3.12-alpine

#paso 2 crear el direfctorio de trabajo

WORKDIR /app

#paso 3 copiar el archivo de dependencias

COPY requirements.txt /app

#paso 4 instalar las dependencias

RUN pip install --no--cache-dir -r requirements.txt

#paso 5  copiar nuestro codigo fuente 

COPY app.py /app

#paso 6 exponer el puerto 5000

EXPOSE 5000

#PASO 7 Ejecutar la aplicacion

CMD ["python","app.py"]