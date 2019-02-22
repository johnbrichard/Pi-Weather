from ftplib import FTP
ftp=FTP('ftp.jamesbraman.com')
ftp.login(user='weather2', passwd='123!weatherR')

filename='Mike_log.txt'
ftp.storbinary('STOR '+filename, open(filename, 'rb'))
