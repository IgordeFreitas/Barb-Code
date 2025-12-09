from fastapi import APIRouter,Body
from controller.agenda.getAgenda import consultarAgenda
from controller.agenda.postAgenda import cadastrarAgenda
from controller.agenda.patchAgenda import patchAgenda
from controller.agenda.deleteAgenda import deletarAgenda

router = APIRouter()
@router.get("/agendas")
def get_agenda():
    return consultarAgenda()

@router.post("/agendas")
def post_agenda(dataHora: str = Body(embed=True), status: str = Body(embed=True), idBarbeiro: int = Body(embed=True)):
    return cadastrarAgenda(dataHora, status, idBarbeiro)

@router.patch("/agendas")
def patch_agenda(
    idAgenda: int = Body(embed=True),
    novaDataHora: str = Body(embed=True), 
    novoStatus: str = Body(embed=True), 
    novoIdBarbeiro: int = Body(embed=True)
):
    return patchAgenda(idAgenda, novaDataHora, novoStatus, novoIdBarbeiro)

@router.delete("/agendas/{id}")
def delete_agenda(id:int):
    return deletarAgenda(id)
