#  arquivos com as constantes do projeto


################################################################
#  TODO : Tratar os diversos tipos de erro que podem acontecer #
################################################################


portNum = 465
userEmail = "python.email.smtp.modules@gmail.com"
userPassword = "testingPythonModules!"
serverURL = "smtp.gmail.com"
targetEmail = "targetEmail@gmail.com"

emailSubject = 'With love, from Papi'
fileName = 'iLoveYou.png'

textMsg ="""\
Oi, Mami. 

Como voce esta?
Passei so pra dizer que te amo.


Esta mensagem foi enviada com o Python."""

htmlMsg = """\
<!DOCTYPE html>
<html>
  <body>
    <h4><b>Oi, Mami.</b></h4>
    Passei so pra dizer que te amo.<br /><br /><br />
    <small>Esta mensagem foi enviada com o Python.</small>
  </body>
</html>
"""