from fastapi import FastAPI, Body

from controller.barbeiro.getBarbeiro import consultarBarbeiro
from controller.barbeiro.patchBarbeiro import patchBarbeiro
from controller.barbeiro.postBarbeiro import cadastrarBarbeiro
from controller.barbeiro.deleteBarbeiro import deletarBarbeiro

from controller.cliente.getCliente import consultarCliente
from controller.cliente.patchCliente import patchCliente
from controller.cliente.postCliente import cadastrarCliente
from controller.cliente.deleteCliente import deletarCliente

from controller.agenda.getAgenda import consultarAgenda

app = FastAPI()

@app.get("/barbeiros")
def consultaBarbeiro():
	return consultarBarbeiro()

@app.patch("/barbeiros")
def updateBarbeiro(
	id: int = Body(embed=True),
	nome: str = Body(embed=True), 
 	cpf: str = Body(embed=True),
    email: str = Body(embed=True),
 	senha: str = Body(embed=True),
	telefone: str = Body(embed=True)
):
	return patchBarbeiro(nome, cpf, email, senha, telefone, id)

@app.post("/barbeiros")
def cadastroBarbeiro(
	nome: str = Body(embed=True), 
 	cpf: str = Body(embed=True),
    email: str = Body(embed=True),
 	senha: str = Body(embed=True),
	telefone: str = Body(embed=True)
):
	return cadastrarBarbeiro(nome, cpf, email, senha, telefone)

@app.delete("/barbeiros/{id}")
def deleteBarbeiro(id: int):
	return deletarBarbeiro(id)


@app.get("/clientes")
def consultaCliente():
	return consultarCliente()

@app.patch("/clientes")
def updateCliente(
	id: int = Body(embed=True),
	nome: str = Body(embed=True), 
    email: str = Body(embed=True),
 	senha: str = Body(embed=True),
	telefone: str = Body(embed=True)
):
	return patchCliente(nome, email,  telefone, senha, id)

@app.post("/clientes")
def cadastroCliente(
	nome: str = Body(embed=True), 
    email: str = Body(embed=True),
 	senha: str = Body(embed=True),
	telefone: str = Body(embed=True)
):
	return cadastrarCliente(nome, email, senha, telefone)

@app.delete("/clientes/{id}")
def deleteCliente(id: int):
	return deletarCliente(id)


@app.get("/agenda")
def consultaAgenda():
	return consultarAgenda()