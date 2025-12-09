from fastapi import APIRouter,Body
from controller.atendimento.getAtendimento import consultarAtendimento
from controller.atendimento.postAtendimento import cadastrarAtendimento
from controller.atendimento.deleteAtendimento import deletarAtendimento
from controller.atendimento.patchAtendimento import patchAtendimento

router = APIRouter()
@router.get("/atendimentos")
def get_atendimento():
    return consultarAtendimento()

@router.post("/atendimentos")
def post_atendimento(
    data_hora_inicio: str = Body(embed=True), 
    data_hora_fim: str = Body(embed=True),
    status: str = Body(embed=True),
    id_barbeiro: int = Body(embed=True),
    id_cliente: int = Body(embed=True),
    id_servico: int = Body(embed=True)
):
    return cadastrarAtendimento(data_hora_inicio, data_hora_fim, status, id_barbeiro, id_cliente, id_servico)

@router.patch("/atendimentos")
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

@router.delete("/atendimentos/{id}")
def delete_atendimento(id: int):
    return deletarAtendimento(id)