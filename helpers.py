from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


import constants



#######################################################
#  TODO : Alterar paradigma para orientado a objetos  #
#   Ideia inicial - Singleton que segura a mensagem   #
#######################################################


#  criando o objeto email, configurando os parametros sujeito, remetente e destinatario
#  o identificador alternative permite a criacao de uma mensagem com conteudo plain text e html
#  ao mesmo tempo.
def createNewEmail():
    message = MIMEMultipart("alternative")
    message['From'] = constants.userEmail
    message['To'] = constants.targetEmail if constants.targetEmail != "" else input("Enter the target email address: ")
    message['Subject'] = constants.emailSubject
    return message


#  gerando os componentes html e plain text e adicionando-os ao email
def generateMailComponents():
    mailParts = list()
    mailParts.append(MIMEText(constants.textMsg, "plain"))
    mailParts.append(MIMEText(constants.htmlMsg, "html"))
    return mailParts


def addPartsToMessage(parts, message):
    for mailPart in parts:
        message.attach(mailPart)
        message.attach(mailPart)
    return message


def attachFileToMessage(fileName, message):
    with open(fileName, "rb") as messageAttachment:
        newPart = MIMEBase("application", "octet-stream")
        newPart.set_payload(messageAttachment.read())

    encoders.encode_base64(newPart)

    newPart.add_header("Content-Disposition",
                        f"attachment; filename= {fileName}",)

    message.attach(newPart)
    return message
