docker build . --tag shop

docker-compose -f stack.yml up -d --build
echo "initialize containers..."
sleep 30
docker exec -it shop-api sh -c "python manage.py migrate"
docker exec -it shop-api sh -c "echo \"from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@shop.com', 'admin_pass')\" | python manage.py shell"
