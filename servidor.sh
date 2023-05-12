cd /home/ubuntu/proyecto/
sudo docker-compose -f docker-compose-nginx.yml down
sudo docker-compose -f docker-compose-nginx.yml pull
sudo docker-compose -f docker-compose-nginx.yml up -d --build
sudo docker-compose -f docker-compose-nginx.yml exec web python manage.py collectstatic