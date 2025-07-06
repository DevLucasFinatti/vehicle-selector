# Projeto Anti Bucha - Gerenciamento de Veículos

## Descrição

Este projeto é uma aplicação Django voltada para gerenciamento de veículos, com funcionalidades para buscar veículos por marca, nome, perfil do usuário, e um quiz para definição de perfil do usuário. Inclui scripts para inicializar e popular o banco de dados automaticamente a partir de um arquivo JSON.

O sistema possui uma interface simples baseada em terminal para interação, com menus, quiz para definição de perfil e resultados customizados para perfis de usuários.

---

## Funcionalidades

- Inicialização automática do banco de dados e migração.
- População inicial do banco com veículos a partir de arquivo JSON (`vehicles_test.json`).
- Quiz interativo para definir o perfil do usuário (Conan, Pai de Família, Garotão, Fino).
- Busca de veículos por:
  - Marca ou nome
  - Busca geral (qualquer campo)
  - Perfil do usuário
- Interface em terminal com menus interativos.
- Formatação amigável da resposta para o usuário.
- Tratamento básico de erros durante carregamento e buscas.

---

## Tecnologias Utilizadas

- Python 3.x
- Django
- SQLite (padrão do Django para desenvolvimento)
- Terminal/Console para interface de usuário
- JSON para armazenamento inicial de dados

---

## Como Rodar Localmente

1. **Clone o repositório**

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

2. **Configure o ambiente**

Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente**

Certifique-se que o `DJANGO_SETTINGS_MODULE` está apontando para o arquivo correto de configurações (`cs2test.settings`).

4. **Prepare o banco e popule os dados**

O script principal executa a migração e carrega os dados do arquivo `vehicles_test.json` automaticamente se o banco estiver vazio.

Execute:

```bash
python main.py
```

5. **Utilização**

- Será exibida uma tela inicial perguntando se deseja buscar um carro de qualidade.
- Você pode escolher fazer buscas por marca/nome, busca geral ou busca baseada no perfil.
- O perfil é definido via quiz interativo no terminal.

---

## Como Adicionar Veículos

- Atualize o arquivo `vehicles_test.json` com os veículos desejados, seguindo o formato esperado (com campos como `name`, `wheels`, `brand`, `model`, `manufacture_date`, `weight_kg`, `fuel`, etc).
- Execute o script principal para que o banco seja populado.

---

## Endpoints e Serviços

Embora o projeto tenha serviços que poderiam ser usados via API, a interface atual é toda em terminal.

As principais funcionalidades de busca são:

- `search_vehicle_by_brand_name(texto)`
- `search_vehicle(texto)` (busca geral)
- `search_vehicle_by_profile(perfil)`

---

## Detalhes Técnicos

- A classe `Services` é responsável pelo CRUD de veículos, buscas e carregamento dos dados JSON.
- A classe `Page` lida com a interface, exibindo menus, formulários, mensagens de saída e quiz.
- O script `main.py` controla o fluxo principal, interagindo com o usuário e os serviços.

---