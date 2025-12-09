from fastapi import APIRouter,Body
from controller.atendimentoServico.getAtendimentoServico import consultarAtendimentoServico

router = APIRouter()
@router.get("/atendimentos_servicos/{id}")
def get_atendimento_servico(id: int):
	return consultarAtendimentoServico(id)