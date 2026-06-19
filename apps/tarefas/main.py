# App de Tarefas — backend FastAPI + SQLite (full-stack pra estudar).
# Um servidor so: a API fica em /api/tarefas e a pagina em /.
import sqlite3
from pathlib import Path
from contextlib import closing
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

DB = Path(__file__).parent / "tarefas.db"
app = FastAPI(title="Tarefas da Adir")


def db():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    with closing(db()) as con:
        con.execute(
            "CREATE TABLE IF NOT EXISTS tarefas ("
            " id INTEGER PRIMARY KEY AUTOINCREMENT,"
            " titulo TEXT NOT NULL,"
            " feita INTEGER NOT NULL DEFAULT 0)"
        )
        con.commit()


init_db()


class TarefaIn(BaseModel):
    titulo: str


class TarefaUpdate(BaseModel):
    feita: bool


@app.get("/api/tarefas")
def listar():
    with closing(db()) as con:
        rows = con.execute("SELECT id, titulo, feita FROM tarefas ORDER BY id DESC").fetchall()
        return [dict(r) for r in rows]


@app.post("/api/tarefas")
def criar(t: TarefaIn):
    titulo = t.titulo.strip()
    if not titulo:
        raise HTTPException(status_code=400, detail="Titulo vazio")
    with closing(db()) as con:
        cur = con.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
        con.commit()
        return {"id": cur.lastrowid, "titulo": titulo, "feita": 0}


@app.put("/api/tarefas/{tid}")
def atualizar(tid: int, t: TarefaUpdate):
    with closing(db()) as con:
        cur = con.execute("UPDATE tarefas SET feita=? WHERE id=?", (1 if t.feita else 0, tid))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
        return {"ok": True}


@app.delete("/api/tarefas/{tid}")
def remover(tid: int):
    with closing(db()) as con:
        con.execute("DELETE FROM tarefas WHERE id=?", (tid,))
        con.commit()
        return {"ok": True}


# Serve o frontend (a pagina HTML)
@app.get("/")
def home():
    return FileResponse(Path(__file__).parent / "index.html")
