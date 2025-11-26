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
from controller.agenda.postAgenda import cadastrarAgenda



from controller.servico.getServico import consultarServico
from controller.servico.patchServico import patchServico
from controller.servico.postServico import cadastrarServico
from controller.servico.deleteServico import deletarServico

from controller.atendimento.getAtendimento import consultarAtendimento
from controller.atendimento.postAtendimento import cadastrarAtendimento
from controller.atendimento.deleteAtendimento import deletarAtendimento
from controller.atendimento.patchAtendimento import patchAtendimento


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

@app.get("/servicos")
def consultaServico():
	return consultarServico()

@app.post("/agenda")
def cadastraAgenda(dataHora: str = Body(embed=True), status: str = Body(embed=True)):
	return cadastrarAgenda(dataHora, status)

@app.post("/servicos")
def cadastrarServico(nome: str = Body(embed=True), preco: float = Body(embed=True)):
	return cadastrarServico(nome, preco)

@app.patch("/servicos/{id}")
def updateServico(novoNome: str = Body(embed=True), novoPreco: float = Body(embed=True), id: int = Body(embed=True)):
	return patchServico(novoNome, novoPreco, id)

app.delete("/servicos")
def deleteServico(id: int = Body(embed=True)):
	return deletarServico(id)

























































































































@app.get("/atendimento")
def consultaAtendimento():
	return consultarAtendimento()

@app.post("/atendimento")
def cadastroAtendimento(
	data_hora_inicio: str = Body(embed=True), 
	data_hora_fim: str = Body(embed=True),
    status: str = Body(embed=True),
	id_barbeiro: int = Body(embed=True),
	id_cliente: int = Body(embed=True),
	id_servico: int = Body(embed=True)
):
	return cadastrarAtendimento(data_hora_inicio, data_hora_fim, status, id_barbeiro, id_cliente, id_servico)

@app.delete("/atendimento/{id}")
def deleteAtendimento(id: int):
	return deletarAtendimento(id)

@app.patch("/atendimento")
def updateAtendimento(
	id: int = Body(embed=True),
	data_hora_inicio: str = Body(embed=True), 
	data_hora_fim: str = Body(embed=True),
    status: str = Body(embed=True),
	id_barbeiro: int = Body(embed=True),
	id_cliente: int = Body(embed=True),
	id_servico: int = Body(embed=True)
):
	return patchAtendimento(data_hora_inicio, data_hora_fim, status, id_barbeiro, id_cliente, id_servico, id)


# @app.get("/clientes/{id_cliente}")
# def getCliente(id_cliente):
# 	return ({"cliente_id": id_cliente})

# @app.get("/produtos")
# def todosOsProdutos():
# 	return ({"Produtos": "Lista de Produtos"})

#@app.delete("/produtos/{id_produto}")
#def deletarProduto(id_produto):
#	return({"Ação": "deletar produto", "produto": {id_produto}})


# @app.post("/produtos")
# def cadastrarProduto(
#     nome_produto: str = Body(embed=True), 
# 	categoria: str = Body(embed=True),
#     preco: float = Body(embed=True),
# 	especialidade: str = Body(embed=True)
# ):
#     return({"Ação": "Cadastrar Produto", "nome" : nome_produto, "categoria" : categoria, "preco" : str(preco), "especialidade":especialidade} )

#CRUD - C -> Create / R -> Read / U -> Update / D -> Delete

## HTTP ==> POST / GET / PUT ou PATCH / DELETE

##MVC ==> M -> Model / V -> View / C -> Controller

# Model ===> Responsável pela comunicação com o Banco de dados

# View ===> Responsável pela parte de renderização e apresentação dos dados (onde o usuário interage)

# Controller ===> Responsável pela integração da view e da model e a responsável pela regra de negócio

#usuário -> View (Frontend) -> Fez o pedido -> Backend -> Chegar o pedido no backend na rota /pedido -> controller processa e verifica os dados -> controller aciona a model para cadastar no banco de dados o novo pedido -> model comunica com o banco de dados e obtém uma resposta (ok! inseriu com sucesso!) -> a model responde a controller que foi tudo ok! -> a controller solicita a view um objeto para uma mensagem de cadastro de pedido com sucesso -> a controller a recebe a resposta da view -> agora a controller retorna a resposta pela mesma rota que foi acionada -> o frontend recebe a resposta renderiza na tela