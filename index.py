from fastapi import FastAPI, Body, HTTPException

# ====================================================================
#  Imports dos Controllers (Organização)
# ====================================================================

# BARBEIRO
from controller.barbeiro.getBarbeiro import consultarBarbeiro
from controller.barbeiro.patchBarbeiro import patchBarbeiro
from controller.barbeiro.postBarbeiro import cadastrarBarbeiro
from controller.barbeiro.deleteBarbeiro import deletarBarbeiro

# CLIENTE
from controller.cliente.getCliente import consultarCliente
from controller.cliente.patchCliente import patchCliente
from controller.cliente.postCliente import cadastrarCliente
from controller.cliente.deleteCliente import deletarCliente

# SERVIÇO
from controller.servico.getServico import consultarServico
from controller.servico.patchServico import patchServico
from controller.servico.postServico import cadastrarServico
from controller.servico.deleteServico import deletarServico

# AGENDA
from controller.agenda.getAgenda import consultarAgenda
from controller.agenda.postAgenda import cadastrarAgenda
from controller.agenda.patchAgenda import patchAgenda
from controller.agenda.deleteAgenda import deletarAgenda

# ATENDIMENTO
from controller.atendimento.getAtendimento import consultarAtendimento
from controller.atendimento.postAtendimento import cadastrarAtendimento
from controller.atendimento.deleteAtendimento import deletarAtendimento
from controller.atendimento.patchAtendimento import patchAtendimento

# ATENDIMENTO SERVICO
from controller.atendimentoServico.getAtendimentoServico import consultarAtendimentoServico

# BARBEIRO SERVICO
from controller.barbeiroServico.getBarbeiroServico import consultarBarbeiroServico
from controller.barbeiroServico.postBarbeiroServico import cadastrarBarbeiroServico
#from controller.barbeiroServico.deleteBarbeiroServico import deletarBarbeiroServico
from controller.barbeiroServico.patchBarbeiroServico import patchBarbeiroServico

# ====================================================================
#  Inicialização do App
# ====================================================================

app = FastAPI()

# --------------------------------------------------------------------
## Rotas para BARBEIROS (/barbeiros)
# --------------------------------------------------------------------

@app.get("/barbeiros")
def get_barbeiros():
    return consultarBarbeiro()

@app.post("/barbeiros")
def post_barbeiro(
    nome: str = Body(embed=True), 
    cpf: str = Body(embed=True),
    email: str = Body(embed=True),
    senha: str = Body(embed=True),
    telefone: str = Body(embed=True)
):
    return cadastrarBarbeiro(nome, cpf, email, senha, telefone)

@app.patch("/barbeiros")
def patch_barbeiro(
    id: int = Body(embed=True),
    nome: str = Body(embed=True), 
    cpf: str = Body(embed=True),
    email: str = Body(embed=True),
    senha: str = Body(embed=True),
    telefone: str = Body(embed=True)
):
    return patchBarbeiro(nome, cpf, email, senha, telefone, id)

@app.delete("/barbeiros/{id}")
def delete_barbeiro(id: int):
    return deletarBarbeiro(id)

# --------------------------------------------------------------------
## Rotas para CLIENTES (/clientes)
# --------------------------------------------------------------------

@app.get("/clientes")
def get_clientes():
    return consultarCliente()

@app.post("/clientes")
def post_cliente(
    nome: str = Body(embed=True), 
    email: str = Body(embed=True),
    senha: str = Body(embed=True),
    telefone: str = Body(embed=True)
):
    return cadastrarCliente(nome, email, senha, telefone)

@app.patch("/clientes")
def patch_cliente(
    id: int = Body(embed=True),
    nome: str = Body(embed=True), 
    email: str = Body(embed=True),
    senha: str = Body(embed=True),
    telefone: str = Body(embed=True)
):
    return patchCliente(nome, email, telefone, senha, id) 

@app.delete("/clientes/{id}")
def delete_cliente(id: int):
    return deletarCliente(id)

# --------------------------------------------------------------------
## Rotas para SERVIÇOS (/servicos)
# --------------------------------------------------------------------

@app.get("/servicos")
def get_servicos():
    return consultarServico()

@app.post("/servicos")
def post_servico(nome: str = Body(embed=True), preco: float = Body(embed=True)):
    return cadastrarServico(nome, preco)

@app.patch("/servicos")
def patch_servico(
    id: int = Body(embed=True), 
    novoNome: str = Body(embed=True), 
    novoPreco: float = Body(embed=True)
):
    return patchServico(novoNome, novoPreco, id)

@app.delete("/servicos")
def delete_servico(id: int = Body(embed=True)):
    return deletarServico(id)

# --------------------------------------------------------------------
##  Rotas para AGENDA (/agendas)
# --------------------------------------------------------------------

# Não existe rota GET para /agendas no seu código. Adicionando uma presumida.
@app.get("/agendas")
def get_agenda():
    return consultarAgenda()

@app.post("/agendas")
def post_agenda(dataHora: str = Body(embed=True), status: str = Body(embed=True), idBarbeiro: int = Body(embed=True)):
    return cadastrarAgenda(dataHora, status, idBarbeiro)

@app.patch("/agendas")
def patch_agenda(
    idAgenda: int = Body(embed=True),
    novaDataHora: str = Body(embed=True), 
    novoStatus: str = Body(embed=True), 
    novoIdBarbeiro: int = Body(embed=True)
):
    return patchAgenda(idAgenda, novaDataHora, novoStatus, novoIdBarbeiro)

@app.delete("/agendas/{id}")
def delete_agenda(id:int):
    return deletarAgenda(id)


# --------------------------------------------------------------------
## Rotas para ATENDIMENTO (/atendimentos)
# --------------------------------------------------------------------

@app.get("/atendimentos")
def get_atendimento():
    return consultarAtendimento()

@app.post("/atendimentos")
def post_atendimento(
    data_hora_inicio: str = Body(embed=True), 
    data_hora_fim: str = Body(embed=True),
    status: str = Body(embed=True),
    id_barbeiro: int = Body(embed=True),
    id_cliente: int = Body(embed=True),
    id_servico: int = Body(embed=True)
):
    return cadastrarAtendimento(data_hora_inicio, data_hora_fim, status, id_barbeiro, id_cliente, id_servico)

@app.patch("/atendimentos")
def patch_atendimento(
    id: int = Body(embed=True),
    data_hora_inicio: str = Body(embed=True), 
    data_hora_fim: str = Body(embed=True),
    status: str = Body(embed=True),
    id_barbeiro: int = Body(embed=True),
    id_cliente: int = Body(embed=True),
    id_servico: int = Body(embed=True)
):
    return patchAtendimento(data_hora_inicio, data_hora_fim, status, id_barbeiro, id_cliente, id_servico, id)

@app.delete("/atendimentos/{id}")
def delete_atendimento(id: int):
    return deletarAtendimento(id)

# --------------------------------------------------------------------
## Rotas para ATENDIMENTO_SERVICO (/atendimentos_servicos)
# --------------------------------------------------------------------

@app.get("/atendimentos_servicos/{id}")
def get_atendimento_servico(id: int):
	return consultarAtendimentoServico(id)

# --------------------------------------------------------------------
## Rotas para BARBEIRO_SERVICO (/barbeiros/{id}/servicos)
# --------------------------------------------------------------------

@app.get("/barbeiros/{id}/servicos")
def get_barbeiros_servico(id: int):
	return consultarBarbeiroServico(id)

@app.post("/barbeiros/{id_barbeiro}/servicos")
def post_barbeiros_servico(
    id_barbeiro: int,
    id_servico: int = Body(embed=True)
):
    return cadastrarBarbeiroServico(id_barbeiro, id_servico)

@app.patch("/barbeiros/{id_barbeiro}/servicos")
def patch_barbeiros_servico(
    id_barbeiro: int,
    id_servico: int = Body(embed=True)
):
    return patchBarbeiroServico(id_barbeiro, id_servico)