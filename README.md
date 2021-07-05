# fullstack-interview-test
Prueba tecnica Nestor Medina.

# Levantar el proyecto.
1- clonar el repositorio.

2- crear el archivo .env dentro del directorio api y frontend basandose en el archivo
.env.skeleton ubicado en cado uno de los directorios antes especificados.

3-Se crearon 2 dockerFiles, uno para la api y otro para el frontend.
El proyecto se levanta ejecutando docker-compose
```
docker-compose build web
docker-compose up web
```

4- La API se levanta en http://0.0.0.0:8000/ y el frontend en http://0.0.0.0:3000/


# Posibles problemas.

1- El proyecto levanta una BD posgreSQL dockerizada en el puerto 5432 puede que tenga problemas 
en caos de que ya tenga algun servicio corrriendo en ese puerto. En tal caso pruebe detener el servicio
mientras realiza la prueba.

# Que no llegue a imnplementar.

1- Manejo de pull request de forma real

2- manejo de errores.

# Que podria mejorar

1- Agregar test en API.

2- Cacheo de endpoint no mutables como el detalle de los commits.

3- Loading en carga y llamados de APIs en componentes VUEJS.

4- El uso del wrapper para el manejo de git degrada la performance con el uso, se podria analizar otra tool mas performante.

5- Manejo de errores en fronted y backend mas robustos.
