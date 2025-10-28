def adicionar_contato(contatos, nome_contato, telefone_contato, favorito=False):
  contato = {"Nome:": nome_contato, "Telefone:": telefone_contato, "Favorito: ": favorito}
  contatos.append(contato)
  return

def ver_contatos(contatos):
  if not contatos:
    print("\nNenhum contato cadastrado.")
  
  print("\nLista de contatos:")
  for i, contato in enumerate(contatos, start=1):
    coracao = "❤️" if contato["Favorito: "] else ""
    print(f"{i}. {contato['Nome:']} - {contato['Telefone:']} {coracao}")

def editar_contato(contatos, i, nome_contato=None, telefone_contato=None):
  index_ajustado = i - 1
  if 0 <= index_ajustado < len(contatos):
    if nome_contato:
      contatos[index_ajustado]["Nome:"] = nome_contato
    if telefone_contato:
      contatos[index_ajustado]["Telefone:"] = telefone_contato
    print("\nContato atualizado com sucesso!")
  else:
    print("\nContato não encontrado.")

def favoritar_contato(contatos, i):
  index_ajustado = i - 1
  if 0 <= index_ajustado < len(contatos):
    contato = contatos[index_ajustado]
    contato["Favorito: "] = not contato["Favorito: "]
    status = "❤️ Favorito" if contato["Favorito: "] else "💔 Removido dos favoritos"
    print(f"\n{contato['Nome:']} agora está marcado como: {status}")
  else:
    print("\nContato não encontrado.")

def excluir_contato(contatos, i):
  index_ajustado = i - 1
  if 0 <= index_ajustado < len(contatos):
    contato_removido = contatos.pop(index_ajustado)
    print(f"\nContato '{contato_removido['Nome:']}' foi excluído com sucesso!")
  else:
    print("\nContato não encontrado.")


contatos = []

while True:
  print("\nAgenda de contatos")
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Editar contato")
  print("4. Favoritar contato")
  print("5. Excluir contato")
  print("6. Sair")

  opcao = input("O que deseja fazer: ")

  if opcao == "1":
    nome_contato = input("Digite o nome do contato: ")
    telefone_contato = input("Digite o telefone do contato: ")
    adicionar_contato(contatos, nome_contato, telefone_contato)
  elif opcao == "2":
    ver_contatos(contatos)
  elif opcao == "3":
    ver_contatos(contatos)
    if contatos:
      try:
        indice_contato = int(input("Digite o número do contato que deseja alterar: "))
        novo_nome = input("Novo nome (deixe em branco para manter): ")
        novo_telefone = input("Novo telefone (deixe em branco para manter): ")
        editar_contato(contatos, indice_contato, novo_nome if novo_nome else None, novo_telefone if novo_telefone else None)
      except ValueError:
        print("Entrada inválida. Digite um número válido.")
  elif opcao == "4":
    ver_contatos(contatos)
    if contatos:
      try:
        indice_contato = int(input("Digite o número do contato que deseja favoritar/desfavoritar: "))
        favoritar_contato(contatos, indice_contato)
      except ValueError:
        print("Entrada inválida. Digite um número válido.")
  elif opcao == "5":
    ver_contatos(contatos)
    if contatos:
      try:
        indice_contato = int(input("Digite o número do contato que deseja excluir: "))
        excluir_contato(contatos, indice_contato)
      except ValueError:
        print("Entrada inválida. Digite um número válido.")
  elif opcao == "6":
    break