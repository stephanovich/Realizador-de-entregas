class ItemEntrega:
  def __init__(self, identificador: int, nome: str):
    self._identificador = identificador
    self._nome = nome

  @property
  def identificador(self) -> int:
    return self.identificador

  @property
  def nome(self) -> str:
    return self.nome
  