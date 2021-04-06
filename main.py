from Caminhao import Caminhao
from ItemEntrega import ItemEntrega
from Local import Local

pontosEntrega = []
itensEntrega = []
caminhoes = []

def inserirPontoEntrega():
  id = int(input("Insira o identificador do local: "))
  nome = input("Insira o nome do local: ")
  listaItens = []
  escolha = input(f"Identificador: {id}\nNome: {nome}\nDeseja salvar esse ponto? (s/n): ").lower()
  if escolha == 's':
    pontoEntrega = Local(id,nome, listaItens)
    pontosEntrega.append(pontoEntrega)
    print('Ponto salvo com sucesso.')
  else:
    return

def inserirItemEntrega():
  id = int(input("Insira o identificador do item de entrega: "))
  nome = input("Insira o nome do item de entrega: ")
  escolha = input(f"Identificador: {id}\nNome: {nome}\nDeseja salvar esse item de entrega? (s/n): ")
  if escolha == 's':
    itemEntrega = ItemEntrega(id,nome)
    itensEntrega.append(itemEntrega)
    print('Item de entrega salvo com sucesso.')
  else:
    print('O item de entrega NAO FOI salvo!!')
    return

def inserirCaminhao():
  placa = input("Insira a placa do caminhao: ")
  listaPontos = []
  listaItens =[]
  escolha = input(f"Placa do caminhao: {placa}\n\nDeseja salvar esse caminhao? (s/n): ")
  if escolha == 's':
    c = Caminhao(placa, listaItens, listaPontos)
    caminhoes.append(c)
    print('Item de entrega salvo com sucesso.', len(caminhoes))
  else:
    print('O item de entrega NAO FOI salvo!!')
    return

def associarItemARota():
  for i in itensEntrega:
    if i not in itensAssociados:
      print('Numero: ',itensEntrega.index(i),' | Identificador: ',i._identificador,' | Nome: ',i._nome)
  
  idxItem = int(input('Escolha um dos itens acima pelo numero que o representa: '))
  item = itensEntrega[idxItem]

  for j in pontosEntrega:
    print('Numero: ',pontosEntrega.index(j),' | Identificador: ',j._identificador,' | Nome: ',j._nome)
  
  idxPonto = int(input('Escolha um dos pontos acima pelo numero que o representa: '))
  ponto = pontosEntrega[idxPonto]

  ler = input(f'Deseja associar o item {item._nome} ao ponto de entrega {ponto._nome}? (s/n): ').lower()
  if ler == 's':
    pontosEntrega[idxPonto]._listaItens.append(itensEntrega[idxItem])
    print('Item associado com sucesso!')

def associarRotaAoCaminhao():
  for j in pontosEntrega:
    if j not in rotasAssociadas:
      print('Numero: ',pontosEntrega.index(j),' | Identificador: ',j._identificador,' | Nome: ',j._nome)

  idxPonto = int(input('Escolha um dos pontos acima pelo numero que o representa: '))
  ponto = pontosEntrega[idxPonto]

  for i in caminhoes:
    print('Numero: ',caminhoes.index(i),' | Placa: ',i._placa)

  idxCam = int(input('Escolha um dos caminhões acima pelo numero que o representa: '))
  cam = caminhoes[idxCam]

  ler = input(f'Deseja associar o ponto {ponto._nome} ao caminhao {cam._placa}? (s/n): ').lower()
  if ler == 's':
    caminhoes[idxCam]._listaLocal.append(pontosEntrega[idxPonto])
    caminhoes[idxCam]._listaItens += pontosEntrega[idxPonto]._listaItens
    print('Item associado com sucesso!')

def realizarEntrega():
  for i in caminhoes:
    print('-' *40)
    print('Percurso do caminhão:',i._placa)
    for j in i._listaLocal:
      print(f'  Visitando o ponto de entrega "{j._nome}".\nForam entregues os itens:')
      for x in j._listaItens[::-1]:
        print("   ",x._nome)

def menu():
  print("-" * 40)
  print("----- Sistema de controle de frota -----")
  print("-" * 40)
  flag = True
  while(flag):
    print('-' * 40)
    print("[1] Inserir ponto de entrega")
    print("[2] Inserir item de entrega")
    print("[3] Inserir caminhão")
    print("[4] Associar item a ponto de entrega")
    print("[5] Associar ponto de entrega a caminhão")
    print("[6] Realizar entregas")
    print("[0] Sair")
    ler= int(input("Escolha uma opção: "))

    if ler == 1:
      inserirPontoEntrega()
    elif ler == 2:
      inserirItemEntrega()
    elif ler == 3:
      inserirCaminhao()
    elif ler == 4:
      associarItemARota()
    elif ler == 5:
      associarRotaAoCaminhao()
    elif ler == 6:
      realizarEntrega()
    elif ler == 0:
      print('O sistema será finalizado...')
      flag = False
    else:
      print('Opção inválida!')

menu()