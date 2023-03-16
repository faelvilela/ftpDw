from ftplib import FTP, error_perm
from datetime import date, timedelta, datetime
import os, shutil 
import schedule

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

def conecta():
    today = datetime.now().strftime("%Y%m%d")
    ftp = FTP('host.ftp.com.br')  
    ftp.login(user='User', passwd='Pass') 
    print('CONECTADO')

def dw_arquivo1():
    nome = 'AccountScore_'+today+'.csv'
    ftp.cwd('/Arquivo1/Outbound')  
    baixar(nome, 'C:/Arquivo1')
        
def dw_arquivo2():
    nome = 'AccountScore_'+today+'.csv'
    ftp.cwd('/Arquivo2/Outbound') 
    baixar(nome, 'C:/Arquivo2')

def job():
    conecta()
    dw_arquivo1()
    dw_arquivo2()
    ftp.quit()

schedule.every().day.at("08:30").do(job)

while True:
  schedule.run_pending()
