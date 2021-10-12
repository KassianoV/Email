import imaplib
import email
from email.header import decode_header
import re


# account credentials
username = "juliamrz2@outlook.com"
password = "Santaluzia20113319freiasno"

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap-mail.outlook.com")
# authenticate
imap.login(username, password)

def showMailBoxs(): 
    # get list of mailboxes
    old_mailboxsList = imap.list()[1]
    mailboxList = []

    # print("All your mailBoxs:\n")
    i = 0

    for mailbox in old_mailboxsList:
        mailboxList.append(mailbox.decode('UTF-8').split('"/" ')[1]) # criar nova lista transformando de bytes em str cada elemento da lista antiga
        print(f"{i} - {mailboxList[i]}")
        # print(mailbox.decode('UTF-8').split('"/" ')[1])
        i = i + 1
    return mailboxList

listaMailBox = showMailBoxs()

'''
Sem o comando abaixo tem-se a mensagem de erro
"command SEARCH illegal in state AUTH, only allowed in states SELECTED"
consulta: https://stackoverflow.com/questions/39115141/imaplib-error-command-search-illegal-in-state-auth-only-allowed-in-states-sele
'''
# select the mailbox I want to delete in
# if you want SPAM, use imap.select("SPAM") instead
# select which mail box to process
# retorna a quantidade de emails lidos/não lidos que esse mailBox possui
imap.select(f'{listaMailBox[13]}')

resp, data = imap.uid('search',None, "ALL") # search and return Uids
# print(data)
""" data = [x.decode('UTF-8') for  x in data[0].split()]
print(data) """
# typ, data = box.search(None, 'ALL') mesma coisa do de cima

for num in data[0].split():
   imap.store(num, '+FLAGS', '\\Deleted')
imap.expunge()
imap.close()
imap.logout()
""" # make an IMAP search to search for mails we want to delete:

# search for specific mails by sender
status, messages = imap.search(None, 'FROM "info@realpython.com"')
print(messages)
 """