CREATE TABLE IF NOT EXISTS mensagem (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    mensagens TEXT NOT NULL,
    tempo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- psycopg2-binary==2.9.1 usado para conectar aplicações Python a bancos de dados PostgreSQL. 
-- grpcio==1.41.0  é uma biblioteca Python para gRPC
-- protobuf==3.18.0 é utilizado para definir estruturas de dados em um formato serializável e é fundamental para o uso de mensagens e serviços definidos em arquivos 

-- requirements.txt é um arquivo fundamental em projetos Python que define e controla as dependências necessárias.

-- [localhost]
-- [localhost] é uma seção do inventário do Ansible. No inventário do Ansible, 
-- você pode definir diferentes grupos de hosts e atribuir variáveis a esses grupos ou hosts 
-- individuais. Neste caso específico, [localhost] está criando um grupo chamado localhost.
-- localhost ansible_connection=local
-- localhost é o nome do host dentro do grupo [localhost].
-- ansible_connection=local é uma variável atribuída ao host localhost. 
-- Ela define como o Ansible deve se conectar a esse host. local indica que o 
-- Ansible deve executar comandos diretamente no mesmo host onde o Ansible está sendo executado, 
-- sem a necessidade de usar SSH ou outra forma de conexão remota. Isso é útil quando você deseja executar 
-- tarefas localmente na máquina onde o playbook do Ansible está sendo executado.
-- localhost é o nome do host dentro do grupo [localhost].