from ftplib import FTP, error_perm
from datetime import date, timedelta, datetime
import os, shutil 
import schedule

global today
today = datetime.now().strftime("%Y%m%d")

def baixar(nome, local):
    path = os.path.join('./', nome)
    try:
        with open(nome, 'wb') as fp:
            ftp.retrbinary('RETR AccountScore_'+today+'.csv', fp.write)
        shutil.move(nome, local)
    except error_perm:
        print('Erro ao encontrar: '+nome+' em '+local)
        os.remove(path)

print('Comecando...')
ftp = FTP('host.ftp.com.br')  
def conecta():
    ftp.login(user='User', passwd='Pass') 
    print('CONECTADO')

def dw_ativos():
    local = 'C:/Ativos'
    nome = 'AccountScore_'+today+'.csv'
    path = os.path.join('./', nome)
    ftp.cwd('/Ativos_SA/Outbound')  
    baixar(nome, local)
        
def dw_digio():
    local = 'C:/Banco_Digio'
    nome = 'AccountScore_'+today+'.csv'
    path = os.path.join('./', nome)
    ftp.cwd('/Digio/Outbound') 
    baixar(nome, local)

def job():
    conecta()
    dw_ativos()
    dw_digio()
    ftp.quit()

schedule.every().day.at("08:30").do(job)

while True:
  schedule.run_pending()