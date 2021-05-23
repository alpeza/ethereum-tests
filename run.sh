echo 'Arrancando REMIX'
set -x
docker-compose up -d
set +x
echo 'Compartiendo '$(pwd)'/contracts con REMIX'
set -x
remixd -s $(pwd)"/contracts" --remix-ide http://localhost:8080
set +x