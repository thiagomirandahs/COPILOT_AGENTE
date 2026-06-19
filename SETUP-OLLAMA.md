# ▶️ Rodar a Adir localmente com Ollama (grátis, sem créditos)

A Adir roda **100% na sua máquina** via **Ollama** + a extensão **Continue** no VSCode. Sem cota, sem chave de API, offline.

---

## 1. Instalar o Ollama
- Baixe em https://ollama.com/download (tem instalador Windows).
- Depois de instalar, o Ollama fica rodando em segundo plano (porta `11434`).
- Teste no terminal: `ollama --version`

## 2. Baixar os modelos
No terminal:

```bash
ollama pull qwen2.5-coder:7b          # chat / edit / agent
ollama pull qwen2.5-coder:1.5b-base   # autocomplete (FIM)
ollama pull nomic-embed-text          # busca no @codebase (opcional)
```

> **Hardware manda aqui.** O `7b` pede ~8 GB de RAM livre.
> - Máquina fraca? Troque por `qwen2.5-coder:3b` (ou `:1.5b`).
> - GPU forte / ≥16 GB? Suba pra `:14b` ou `:32b`.
>
> É só trocar o valor de `model:` no `.continue/config.yaml`.

## 3. Instalar a extensão Continue
- VSCode → **Extensions** → procure **Continue** → **Install**.

## 4. Carregar a config
- A config já está em **`.continue/config.yaml`** deste repositório. **Abra a pasta `DIO` no VSCode** que o Continue carrega ela automaticamente.
- Alternativa (config global): copie o conteúdo para `C:\Users\<você>\.continue\config.yaml`. Nesse caso, troque a regra `file://prompts/prompt-base.md` por um **caminho absoluto** (ex.: `file://C:/Users/<você>/Documents/DIO/prompts/prompt-base.md`).

## 5. Usar
- Abra o painel do **Continue** (ícone na barra lateral).
- A **identidade + stack da Adir** entram sozinhas (regra `prompt-base.md`).
- Os **modos** são comandos de barra no chat: `/ask`, `/edit`, `/plan`, `/agent`, `/study`.
- O **autocomplete** liga sozinho enquanto você digita.

---

## Problemas comuns
- **A regra não carregou:** confirme que abriu a pasta `DIO` como workspace; senão use caminho absoluto no `file://`.
- **Está lento:** o modelo é grande demais pro seu hardware — baixe o tamanho (`:3b` ou `:1.5b`).
- **Continue não acha o Ollama:** confirme que ele está rodando com `ollama list` no terminal.
- **Sem `@codebase`:** verifique se o `nomic-embed-text` foi baixado (é o modelo de embeddings).
