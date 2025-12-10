from fastapi import APIRouter,Body
from controller.login.postLogin import login

router =  APIRouter()

@router.post("/login")
def post_login(
    cpf: str = Body(embed=True), 
    senha: str = Body(embed=True)
    ):
    return login(cpf, senha)