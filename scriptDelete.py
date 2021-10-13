import imaplib
from os import system as sys

def escolhe():
    opcs= ['Outlook.com', 'imap.gmail.com']
    return opcs[int(input("<0> outlook\n<1> gmail\n<> "))]

# login no email
def insertEmailPass():
    email = input("<> email: ")
    while "@" not in email:
        email = input("Insira um email va'lido!\n<> email: ")
    pw = input("<> password/senha: ")

    sys("cls") # limpar tela

    return email, pw
    
# retorna lista de mailBoxes
def getMailBox(mail):
    old_mailboxesList = mail.list()[1]
    mailboxList = []
    
    for mailbox in old_mailboxesList:
        mailboxList.append(mailbox.decode('UTF-8').split('"/" ')[1]) # criar nova lista transformando de bytes em str cada elemento da lista antiga

    return mailboxList 

# mostra mailboxes da conta atual
def showMailBoxes(mailBox): 

    print("MailBoxes:\n")
    i = 0
    for mail in mailBox:
        print(f"{i} - {mail}")
        i = i + 1

'''
Função para deletar emails:
    Deleta todas as mensagens da mailbox selecionada ou de um autor específico.
    Não há opção de selecionar por data.

'''
def deleteEmail(imap, mailBox):
    showMailBoxes(mailBox)
    num = int(input("Escolha o mailbox pelo id.\n<> "))

    sys("cls")

    imap.select(f'{mailBox[num]}')
    
    if int(input("Deseja deletar o email de um autor específico?\n< 0 > Sim\n< 1 > Não\n<> ")):
        tag = 'ALL'
    else:
        tag = '(FROM "' + input("Insira o nome/email do autos.\n<> ") + '")'

    sys("cls")
    typ, data = imap.search(None, tag)

    for n in data[0].split():
        imap.store(n, '+FLAGS', '\\Deleted')

    imap.expunge()
    imap.close()

def main():
    continuar = 0
    mudar_email = 0
    # cria uma classe IMAP4 com SSL
    imap = imaplib.IMAP4_SSL(escolhe(), 993)

    # inserção do email e da senha 
    username, password = insertEmailPass()

    # autenticação
    imap.login(username, password)
    while not continuar:
        if mudar_email:
            # cria uma classe IMAP4 com SSL
            imap = imaplib.IMAP4_SSL(escolhe(), 993)

            # inserção do email e da senha 
            username, password = insertEmailPass()

            # autenticação
            imap.login(username, password)

        listaMailBox = getMailBox(imap)

        deleteEmail(imap, listaMailBox)

        sys("cls")

        continuar = int(input("Deletar novamente?\n<0> Sim\n<1> Não\n<> "))
        if not continuar:
            mudar_email = int(input("Deletar no mesmo email?\n<0> Sim\n<1> Não\n<> "))
            if mudar_email:
                imap.logout()
        if continuar:
            imap.logout()
        sys("cls")  

main()