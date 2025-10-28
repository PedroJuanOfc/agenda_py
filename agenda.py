def adicionar_contato(contatos, nome_contato, telefone_contato, favorito=False):
  contato = {"Nome:": nome_contato, "Telefone:": telefone_contato, "Favorito: ": favorito}
  contatos.append(contato)
  return

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
  elif opcao == "6":
    break