from fastapi import APIRouter,Body
from controller.barbeiroServico.getBarbeiroServico import consultarBarbeiroServico
from controller.barbeiroServico.postBarbeiroServico import cadastrarBarbeiroServico
from controller.barbeiroServico.deleteBarbeiroServico import deletarBarbeiroServico
from controller.barbeiroServico.patchBarbeiroServico import patchBarbeiroServico

router = APIRouter()
@router.get("/barbeiros/{id}/servicos")
def get_barbeiros_servico(id: int):
	return consultarBarbeiroServico(id)

@router.post("/barbeiros/{id_barbeiro}/servicos")
def post_barbeiros_servico(
    id_barbeiro: int,
    id_servico: int = Body(embed=True)
):
    return cadastrarBarbeiroServico(id_barbeiro, id_servico)

@router.patch("/barbeiros/{id_barbeiro}/servicos")
def patch_barbeiros_servico(
    id_barbeiro: int,
    id_servico: int = Body(embed=True)
):
    return patchBarbeiroServico(id_barbeiro, id_servico)

@router.delete("/barbeiros/{id}/servicos")
def delete_barbeiro_servico(id: int):
    return deletarBarbeiroServico(id)