from fastapi import APIRouter,Body
from controller.servico.getServico import consultarServico
from controller.servico.patchServico import patchServico
from controller.servico.postServico import cadastrarServico
from controller.servico.deleteServico import deletarServico

router = APIRouter()
@router.get("/servicos")
def get_servicos():
    return consultarServico()

@router.post("/servicos")
def post_servico(nome: str = Body(embed=True), preco: float = Body(embed=True)):
    return cadastrarServico(nome, preco)

@router.patch("/servicos")
def patch_servico(
    id: int = Body(embed=True), 
    novoNome: str = Body(embed=True), 
    novoPreco: float = Body(embed=True)
):
    return patchServico(novoNome, novoPreco, id)

@router.delete("/servicos")
def delete_servico(id: int = Body(embed=True)):
    return deletarServico(id)
