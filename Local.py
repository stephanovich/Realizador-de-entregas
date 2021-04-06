import ItemEntrega

class Local:
  def __init__(self, identificador: int, nome: str, listaItens: list):
    self._identificador = identificador
    self._nome = nome
    self._listaItens = listaItens
    
  @property
  def identificador(self) -> int:
    return self.identificador

  @property
  def nome(self) -> str:
    return self.nome
  
  @property
  def listaItens(self) -> list:
    return self.listaItens
