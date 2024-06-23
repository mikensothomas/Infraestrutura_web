REDE_WEB="rede_web"

docker network create --driver bridge $REDE_WEB

# Exibir redes criadas
echo "Redes Docker criadas:"
docker network ls

echo "Redes configuradas com sucesso."

# Manter o container em execução
exec "$@"
