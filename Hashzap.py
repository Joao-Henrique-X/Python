import flet as ft
#Evento = Clique do Botão

def main(pagina):
    

    def enviar_mensagem_tunel(mensagem):
         texto = ft.Text(mensagem)
         chat.controls.append(texto)
         pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
            nome_usuário = caixa_nome.value
            texto_campo_mensagem = campo_enviar_mensagem.value
            mensagem = f"{nome_usuário}: {texto_campo_mensagem}"
            pagina.pubsub.send_all(mensagem)
            campo_enviar_mensagem.value = ""
            pagina.update()

    

    def abrir_modal(evento):
        pagina.dialog = modal
        modal.open = True
        pagina.update()
        print("Clicou no Botão")



    def entrar_no_chat(evento):
        modal.open = False
        pagina.remove(titulo)
        pagina.remove(botão)

        pagina.add(chat)
        pagina.update()

        pagina.add(linha_enviar)
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    #Tela Inicial Sem Login

    titulo = ft.Text("Hashzap")
    pagina.add(titulo)    
    botão = ft.ElevatedButton("Iniciar Chat", on_click=abrir_modal)
    pagina.add(botão)

    #Função Enviar_Mensagem
    campo_enviar_mensagem = ft.TextField(label="Digite sua Mensagem", on_submit=enviar_mensagem)
    botão_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    chat = ft.Column()
    linha_enviar = ft.Row([campo_enviar_mensagem, botão_enviar]) 

    #Modal/Alert/Pop-up

    titulo_modal = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite seu Nome")
    botão_modal = ft.ElevatedButton("Entrar no Chat", on_click=entrar_no_chat)
    modal = ft.AlertDialog(title=titulo_modal, content=caixa_nome, actions=[botão_modal])

    

    
#Execução do App
ft.app(main, view=ft.WEB_BROWSER)
