#!/bin/bash

# Check the health endpoints of each service
services=("5000" "5001" "5002" "5003")
for port in "${services[@]}"; do
  curl -f http://localhost:$port/health || { echo "Service on port $port health check failed"; exit 1; }
done

echo "All services are healthy"

# Run tests in each service container
services=("api-gateway" "account-management" "wallet" "trading")
for service in "${services[@]}"; do
  docker-compose exec $service pytest
done
