from fastapi import FastAPI
from routes import (
    agenda, 
    atendimento,
    atendimentoServico,
    barbeiro,
    barbeiroServico,
    cliente,
    servico,
    login
)
# ====================================================================
#  Inicialização do App
# ====================================================================

app = FastAPI()

app.include_router (agenda.router)
app.include_router (atendimento.router)
app.include_router (atendimentoServico.router)
app.include_router (barbeiro.router)
app.include_router (barbeiroServico.router)
app.include_router (cliente.router)
app.include_router (servico.router)
app.include_router (login.router)