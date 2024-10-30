# nginx Load Balancer Lab 2 modified with PyJokes

This is a modified version of the NginxLoadBalancer demonstration from Professor Bradford all credit goes to him and his project: https://github.com/wonder-phil/nginxLoadBalancerPythonFlask/

To get this running:

1. git clone this repository
2. pip install required components
4. docker-compose up
5. python3 load_driver.py
6. curl -H "Content-Type: application/json" -d "{}" -X POST "http://localhost:5000/compute"
7. gracefully shut down the system with docker-compose down
