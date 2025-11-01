class Atendimento():
    def __init__ (self, dataHoraInicio, dataHoraFim, status):
        self.dataHoraInicio = dataHoraInicio
        self.dataHoraFim = dataHoraFim
        self.status = status

    def getDataHoraInicio(self):
        return self.dataHoraInicio
    
    def setDataHoraInicio(self, novaDataHoraInicio):
        self.dataHoraInicio = novaDataHoraInicio

    def getDataHoraFim(self):
        return self.dataHoraFim
    
    def setDataHoraFim(self, novaDataHoraFim):
        self.dataHoraFim = novaDataHoraFim

    def getStatus(self):
        return self.status
    
    def setStatus(self, novoStatus):
        self.status = novoStatus