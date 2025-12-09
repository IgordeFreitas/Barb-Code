from fastapi import APIRouter,Body
from controller.cliente.getCliente import consultarCliente
from controller.cliente.patchCliente import patchCliente
from controller.cliente.postCliente import cadastrarCliente
from controller.cliente.deleteCliente import deletarCliente

router = APIRouter()
@router.get("/clientes")
def get_clientes():
    return consultarCliente()

@router.post("/clientes")
def post_cliente(
    nome: str = Body(embed=True), 
    email: str = Body(embed=True),
    senha: str = Body(embed=True),
    telefone: str = Body(embed=True)
):
    return cadastrarCliente(nome, email, senha, telefone)

@router.patch("/clientes")
def patch_cliente(
    id: int = Body(embed=True),
    nome: str = Body(embed=True), 
    email: str = Body(embed=True),
    senha: str = Body(embed=True),
    telefone: str = Body(embed=True)
):
    return patchCliente(nome, email, telefone, senha, id) 

@router.delete("/clientes/{id}")
def delete_cliente(id: int):
    return deletarCliente(id)
