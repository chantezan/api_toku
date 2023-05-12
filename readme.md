# Nombre del Proyecto

Descripción breve del proyecto.

## Tecnologías utilizadas

- Django
- Django REST Framework

## Instalación

1. Clona el repositorio:
2. Ve al directorio del proyecto

## Configuración

1. Asegúrate de que la base de datos tenga el mismo nombre que se especifica en el archivo `.env`.


## Docker

El proyecto incluye archivos de configuración Docker para entornos de desarrollo y producción.

### Desarrollo

1. Asegúrate de tener Docker instalado en tu máquina.

2. Ejecuta el siguiente comando para iniciar el contenedor de desarrollo: docker-compose up -d

3. Y ejecuta las migraciones dentro del docker

### Como se hizo

El proyecto esta consultando cada 15m con un celery task a la data y actualiza los registros de los heroes, despues
con resframework se crearon endpoint y filtros para los heroes, y la documentacion fue generada por swagger