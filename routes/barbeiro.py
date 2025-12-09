from fastapi import APIRouter,Body
from controller.barbeiro.getBarbeiro import consultarBarbeiro
from controller.barbeiro.patchBarbeiro import patchBarbeiro
from controller.barbeiro.postBarbeiro import cadastrarBarbeiro
from controller.barbeiro.deleteBarbeiro import deletarBarbeiro

router = APIRouter()
@router.get("/barbeiros")
def get_barbeiros():
    return consultarBarbeiro()

@router.post("/barbeiros")
def post_barbeiro(
    nome: str = Body(embed=True), 
    cpf: str = Body(embed=True),
    email: str = Body(embed=True),
    senha: str = Body(embed=True),
    telefone: str = Body(embed=True)
):
    return cadastrarBarbeiro(nome, cpf, email, senha, telefone)

@router.patch("/barbeiros")
def patch_barbeiro(
    id: int = Body(embed=True),
    nome: str = Body(embed=True), 
    cpf: str = Body(embed=True),
    email: str = Body(embed=True),
    senha: str = Body(embed=True),
    telefone: str = Body(embed=True)
):
    return patchBarbeiro(nome, cpf, email, senha, telefone, id)

@router.delete("/barbeiros/{id}")
def delete_barbeiro(id: int):
    return deletarBarbeiro(id)
