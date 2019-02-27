import ssl
import smtplib

import constants
import helpers

secureContext = ssl.create_default_context()

# o with statement garante que a conexao sera encerrada apos o fim da execucao de seu bloco
with smtplib.SMTP_SSL(constants.serverURL, constants.portNum, context=secureContext) as server:
    server.login(constants.userEmail, constants.userPassword)

    newEmail = helpers.createNewEmail()
    mailComponents = helpers.generateMailComponents()
    newEmail = helpers.addPartsToMessage(mailComponents, newEmail)
    newEmail = helpers.attachFileToMessage(constants.fileName, newEmail)

    response = server.sendmail(constants.userEmail, constants.targetEmail, newEmail.as_string())

    print(response)
