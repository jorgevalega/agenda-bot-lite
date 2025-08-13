# 🗓️ **agenda-bot-lite**

**Agenda Bot Lite** desenvolvida com **Python + Flask** e banco de dados MariaDB, é uma aplicação web integrada a um bot do Telegram, que permite a criação de lembretes de forma simples e rápida, diretamente do Telegram. É ideal para quem precisa de lembretes automatizados, utilizando uma interface leve e acessível.

---

## 🌐 Demonstração Online

Você pode acessar e testar a agenda diretamente em:

👉 [https://agenda.valega.dev](https://agenda.valega.dev)

---

## 🌍 Idiomas Disponíveis

- 🇧🇷 Português – *Você está aqui*
- 🇪🇸 [Versión en Español](https://github.com/jorgevalega/agendas)
- 🇺🇸 [English Version](https://github.com/jorgevalega/educational-game)

---

## 🚀 Funcionalidades
- Registro de tarefas com data e hora.
- Verificação a cada 10 minutos com notificações.
- Painel web simples.

---

## Como usar
1. Configure o banco MariaDB.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Execute o script `app/verificador_de_tarefas.py` a cada 10 minutos com cron.
4. Acesse `http://seusite.com/` para ver tarefas.

---

## 📁 Estrutura de Pastas

```bash
agenda-bot-lite/
├── app/
│   ├── core/
│   ├── services/
│   ├── database/
│   ├── web/
│   ├── verificador_de_tarefas.py
│   └── config.py
├── static/
├── templates/
├── requirements.txt
└── README.md
```

---

