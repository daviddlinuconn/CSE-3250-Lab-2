# nginx Load Balancer Lab 2 modified with PyJokes

This is a modified version of the NginxLoadBalancer demonstration from Phil Bradford all credit goes to him and his project: https://github.com/wonder-phil/nginxLoadBalancerPythonFlask/tree/main

TO get this working:

1. docker-compose up
2. python3 load_driver.py
3. curl -v -X GET "http://localhost:8080/"
4. curl -H "Content-Type: application/json" -d "{\\"heads\\":6 }" -X POST "http://localhost:8080/compute"

# NOTE clear docker containers from the cache
## docker-compose down --rmi all
