# 🎫 DropTicket Project

O **DropTicket** é um ecossistema para gestão e venda de ingressos focado em eventos de música eletrônica (Raves) e gestão de excursões.

## Status do Projeto
Atualmente, o projeto conta com:
- **Painel Administrativo:** Gestão completa de Eventos, Lotes e Excursões.
- **Home Page:** Vitrine de eventos com design responsivo.
- **Página de Detalhes:** Visualização de informações do evento, integração de lotes e lista de excursões disponíveis.

## Tecnologias Utilizadas
- **Python 3.13**
- **Django 6.0**
- **Bootstrap 5 (Front-end)**
- **SQLite (Banco de dados de desenvolvimento)**

## Regras de Negócio Implementadas
- **Cancelamento Inteligente:** Lógica para permissão de cancelamento baseada na data de pagamento e proximidade do evento.
- **Relacionamento de Dados:** Vínculo dinâmico entre Lotes/Excursões e seus respectivos Eventos.

## Como rodar o projeto
1. Clone o repositório: `git clone [link-do-repo]`
2. Instale o Django: `pip install django`
3. Execute as migrações: `py manage.py migrate`
4. Inicie o servidor: `py manage.py runserver`
