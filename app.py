import pyautogui
import webbrowser
from time import sleep

# 1- navegar até o instagram https://www.instagram.com/
webbrowser.open_new('https://www.instagram.com/')
sleep(5)
# 2- fazer login
# colocar email/telefone
pyautogui.click(1472,392, duration=2)
pyautogui.typewrite('your email/phone', interval=0.2)
# senha
# obs: apenas por tratamento de erro, caso a senha estiver errada verificar se o caps lock não está ativo!
pyautogui.click(1458,449, duration=2)
pyautogui.typewrite('your password', interval=0.3)
# clicar em entrar
while True:
    try:
        botao_entrar = pyautogui.locateCenterOnScreen('botao_entrar.png')
        pyautogui.click(botao_entrar[0], botao_entrar[1], duration=1)
        break
    except:
        print('Botão Home não achado, tentando de novo.')
        continue

while True:
    ########## LOGADO ########
    # 3- ir a pagina inicial
    sleep(5)
    botao_home = pyautogui.locateCenterOnScreen('botao_home.png')
    pyautogui.click(botao_home[0], botao_home[1], duration=1)

    # 4- pesquisar pela página
    sleep(5)
    while True:
        try:
            sleep(2)
            barra_pesquisar = pyautogui.locateCenterOnScreen('barra_pesquisar.png')
            pyautogui.click(barra_pesquisar[0], barra_pesquisar[1], duration=2)
            break
        except:
            print('Barra de pesquisa não achada, tentando de novo.')
            continue
    pyautogui.typewrite('devaprender', interval=0.2)
    sleep(3)
    # 5- entrar na página
    pyautogui.click(1545,254, duration=2)
    # 6- Clicar na postagem mais recente
    sleep(4)
    pyautogui.scroll(-250)
    pyautogui.click(1271,638, duration=2)
    # 7- verificar se já curtir ou não aquela postagem
    sleep(3)
    try:
        # 9- Se não tiver curtido, curtir a foto
        botao_curtir = pyautogui.locateCenterOnScreen('botao_curtir.png')
        pyautogui.click(botao_curtir[0], botao_curtir[1], duration=2)
        # 10- se não tiver curtido, comentar na foto
        botao_coment = pyautogui.locateCenterOnScreen('botao_coment.png')
        pyautogui.click(botao_coment[0], botao_coment[1], duration=2)
        sleep(2)
        adicionar_comentario = pyautogui.locateCenterOnScreen('comentario.png')
        pyautogui.click(adicionar_comentario[0], adicionar_comentario[1], duration=2)
        pyautogui.typewrite('muito bom!')
        botao_publicar = pyautogui.locateCenterOnScreen('botao_publicar.png')
        pyautogui.click(botao_publicar[0], botao_publicar[1], duration=1)

    except: 
        # 8- Se já tiver curtido, fazer nada, e pausar o bot por 24 horas (86400 segundos)
        fechar_post = pyautogui.locateCenterOnScreen('botao_fechar_post.png')
        pyautogui.click(fechar_post[0], fechar_post[1], duration=2)
        print('post já curtido. Aguardando 24 horas...')
        sleep(86400)
