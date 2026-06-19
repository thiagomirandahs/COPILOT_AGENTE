# 🧩 Adir — Minha Copiloto (Ask, Edit, Plan, Agent e Study)

![dio/me](https://img.shields.io/badge/dio-me-ff2d55)
![IA](https://img.shields.io/badge/IA-Assistente%20Inteligente-blue)
![Prompt](https://img.shields.io/badge/Prompt-engineering-yellow)

A **Adir** é a minha copiloto técnica. Ela oferece diferentes **modos de interação** para você escolher como quer trabalhar: desde **tirar dúvidas sem mexer no código**, até **editar trechos específicos**, **planejar mudanças maiores** ou **delegar tarefas mais complexas** com um modo mais autônomo. A ideia é simples: você seleciona o modo que melhor combina com seu objetivo no momento e ganha velocidade com mais controle.

---

# 🧬 Base (Identidade & Stack)
A "cara" da **Adir** e a stack ficam definidas em **um lugar só**. Todos os modos herdam daqui — você edita a identidade e as tecnologias **uma vez**, sem repetir em cada arquivo.

📄 **Prompt:** [prompts/prompt-base.md](prompts/prompt-base.md)

---

# ❓ Ask
O modo **Ask** é para fazer perguntas e entender coisas, **sem alterar seu código**. Você pode perguntar sobre um arquivo específico, um erro, uma função, uma stack trace ou até conceitos gerais.

A **Adir** lê o contexto do projeto (arquivos abertos, seleção, etc.) e responde como uma **“mentora técnica”**, explicando o que está acontecendo e por quê. **Ela não modifica nada** — só analisa e explica.

📄 **Prompt:** [prompts/prompt-ask.md](prompts/prompt-ask.md)

---

# ✏️ Edit
O modo **Edit** serve para **alterar código existente**. Você seleciona um trecho (ou um arquivo inteiro), descreve o que quer mudar, e a **Adir** aplica a modificação diretamente.

Ideal para:
- refactors
- ajustes de lógica
- melhoria de performance
- mudança de estilo
- conversão de linguagem
- adicionar logs
- tratar erros

Aqui o foco é: **“pegue isso que já existe e transforme”**.

📄 **Prompt:** [prompts/prompt-edit.md](prompts/prompt-edit.md)

---

# 🧭 Plan
Quando você pede algo mais complexo, a **Adir** pode entrar em um modo de **planejamento**, onde ela **pensa e descreve os passos antes de sair codando**.

Ela:
- divide o problema em etapas
- explica o que vai fazer
- só depois executa

Isso é muito útil para **mudanças grandes**, **novas features** ou quando você quer **validar a abordagem** antes de mexer no código.

📄 **Prompt:** [prompts/prompt-plan.md](prompts/prompt-plan.md)

---

# 🤖 Agent
O **Agent** é o modo mais “autônomo”. Ela pode **navegar pelo projeto**, **criar arquivos**, **modificar múltiplos pontos** e **manter contexto entre passos**, como se fosse uma dev júnior trabalhando com você.

Você dá um objetivo (ex.: “implemente login com JWT”) e ela decide o que precisa ser feito em vários arquivos para chegar lá.

📄 **Prompt:** [prompts/prompt-agent.md](prompts/prompt-agent.md)

---

# 📚 Study
O modo **Study** é focado em **aprendizado ativo**, não só em chegar à resposta ou ao código final.

Em vez de simplesmente explicar ou executar, ela:
- ensina e guia o raciocínio
- destaca conceitos e trade-offs
- faz perguntas reflexivas
- avança em progressão gradual de dificuldade

Funciona quase como uma **tutora particular**.

📄 **Prompt:** [prompts/prompt-study.md](prompts/prompt-study.md)

---

# ▶️ Rodar localmente (Ollama, grátis)
Rode a Adir 100% na sua máquina, **sem créditos e offline**, com **Ollama + extensão Continue** (VSCode). A config já está pronta em [.continue/config.yaml](.continue/config.yaml) — identidade/stack entram automático e os modos viram comandos de barra (`/ask`, `/edit`, `/plan`, `/agent`, `/study`).

📄 **Passo a passo:** [SETUP-OLLAMA.md](SETUP-OLLAMA.md)

---

# 🧠 Resumo mental rápido
- **Base** → sua cara + stack (fonte única)
- **Ask** → entender
- **Plan** → planejar antes de agir
- **Edit** → mudar código
- **Agent** → executar tarefas grandes sozinha
- **Study** → entendimento ativo
