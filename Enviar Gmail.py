import smtplib
import email.message
from credenciais import emailuser,senha
def enviar_email():  
    corpo_email = """
    <p>Olá Gabriel,</p>
    <p>Email automático com python enviado com sucesso!!</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Email automático com python"
    msg['From'] = emailuser
    msg['To'] =  emailuser
    password = senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Utiliza as credenciais pra realizar o envio do email
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado!')

enviar_email()