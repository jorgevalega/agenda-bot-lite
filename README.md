# agenda-bot-lite

Agenda simples com integração futura para WhatsApp. Desenvolvida em Python e Flask com banco de dados MariaDB.

---

## Funcionalidades
- Registro de tarefas com data e hora.
- Verificação a cada 10 minutos com notificações.
- Painel web simples.
- Limite de 15 tarefas por usuário (modo gratuito).
- Área administrativa para controle de acesso.

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

