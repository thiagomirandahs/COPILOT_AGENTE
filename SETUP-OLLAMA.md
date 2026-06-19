# ▶️ Rodar a Adir localmente com Ollama (grátis, sem créditos)

A Adir roda **100% na sua máquina** via **Ollama** + a extensão **Continue** no VSCode. Sem cota, sem chave de API, offline.

---

## 1. Instalar o Ollama
- Baixe em https://ollama.com/download (instalador Windows) — ou via winget: `winget install Ollama.Ollama`.
- Depois de instalar, o Ollama fica rodando em segundo plano (porta `11434`).
- **Abra um terminal novo** e teste: `ollama --version`

## 2. Baixar os modelos
```bash
ollama pull qwen2.5-coder:7b          # base da Adir (chat / edit / agent)
ollama pull qwen2.5-coder:1.5b-base   # autocomplete (FIM)
ollama pull nomic-embed-text          # busca no @codebase (opcional)
```

> **Hardware manda aqui.** O `7b` pede ~8 GB de RAM livre.
> - Máquina fraca? Troque por `qwen2.5-coder:3b` (ou `:1.5b`).
> - GPU forte / ≥16 GB? Suba pra `:14b` ou `:32b`.
>
> Se trocar a base, ajuste o `FROM` do `adir.Modelfile` e recrie (passo 3).

## 3. Criar a Adir (treinar a persona)
A identidade da Adir está no [adir.Modelfile](adir.Modelfile) (system prompt + parâmetros). Crie o modelo:

```bash
ollama create adir -f adir.Modelfile
ollama run adir        # testa — ela se apresenta; saia com /bye
```

## 4. Instalar a extensão Continue
- VSCode → **Extensions** → procure **Continue** → **Install**.

## 5. Carregar a config
- A config já está em **`.continue/config.yaml`** (o chat usa o modelo `adir`). **Abra a pasta `DIO` no VSCode** que o Continue carrega ela.
- Alternativa (config global): copie para `C:\Users\<você>\.continue\config.yaml` e troque a regra `file://prompts/prompt-base.md` por caminho absoluto.

## 6. Usar
- **No terminal:** `ollama run adir`
- **No VSCode (Continue):** abra o painel do Continue, escolha o modelo **Adir** e use os comandos `/ask`, `/edit`, `/plan`, `/agent`, `/study`. O autocomplete liga sozinho.

---

## Problemas comuns
- **`ollama` não reconhecido:** abra um terminal **novo** (o PATH só atualiza depois da instalação) ou use o caminho completo `%LOCALAPPDATA%\Programs\Ollama\ollama.exe`.
- **Primeira resposta lenta:** normal na CPU — carrega ~5 GB na RAM; as seguintes saem rápidas.
- **Está lento sempre:** modelo grande demais pro hardware — baixe o tamanho (`:3b` / `:1.5b`).
- **Continue não acha o Ollama:** confirme que está rodando com `ollama list`.
- **Sem `@codebase`:** verifique se o `nomic-embed-text` foi baixado.
