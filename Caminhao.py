import ItemEntrega
import Local

class Caminhao:
  def __init__(self,placa: str, listaItens: list, listaLocal: list):
    self._placa = placa
    self._listaItens = listaItens
    self._listaLocal = listaLocal
  
  @property
  def placa(self) -> str:
    return self.placa
  
  @property
  def listaItens(self) -> list:
    return self.listaItens
  
  @property
  def listaLocal(self) -> list:
    return self.listaItens
