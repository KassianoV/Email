import imaplib

def insertEmailPass():
    email = input("<> email: ")
    while "@" not in email:
        email = input("Please, insert a valid email!\nPor favor, insira um email va'lido!\n<> email: ")
    pw = input("<> password/senha: ")
    return email, pw

def showMailBoxs(mail): 
    # get list of mailboxes
    old_mailboxsList = mail.list()[1]
    mailboxList = []

    # print("All your mailBoxs:\n")
    i = 0

    for mailbox in old_mailboxsList:
        mailboxList.append(mailbox.decode('UTF-8').split('"/" ')[1]) # criar nova lista transformando de bytes em str cada elemento da lista antiga
        print(f"{i} - {mailboxList[i]}")
        # print(mailbox.decode('UTF-8').split('"/" ')[1])
        i = i + 1
    return mailboxList

# inseting account credentials / inserção do email e da senha 
username, password = insertEmailPass()

# create an IMAP4 class with SSL, cria uma classe IMAP4 com SSL
imap = imaplib.IMAP4_SSL('Outlook.com', 993)

# authenticate, autentificação
imap.login(username, password)

# show all the option of the mailbox of the currently account
# mostra todas as opções de mailbox da conta atual
# return a list of it
# retorna uma lista destas opções
listaMailBox = showMailBoxs(imap)

num = int(input("Choose the mailbox by the id.\nEscolha um mailbox pelo id.\n> "))

imap.select(f'{listaMailBox[num]}')
# imap.select('"Python Tips"')

if int(input("Do you want to delete a email of a specific auth?\nDeseja deletar o email de um autor específico?\n< 0 > Yes/Sim\n< 1 > No/Não\n<> ")):
    tag = 'ALL'
else:
    tag = '(FROM "' + input("Insert the auth name/email.\nInsira o nome/email do autos.\n<> ") + '")'
    #'(FROM "newsletter@filipedeschamps.com.br")'

typ, data = imap.search(None, tag)

for num in data[0].split():
   imap.store(num, '+FLAGS', '\\Deleted')

# imap.expunge()
imap.close()
imap.logout()