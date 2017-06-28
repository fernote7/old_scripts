__author__ = 'fernando.ormonde'

import urllib2 as url, csv


download_data = url.urlopen('http://nupei.iag.puc-rio.br/publicacoes/')
download_data2 = url.urlopen('http://nupei.iag.puc-rio.br/publicacoes/page/2/')
download_data3 = url.urlopen('http://nupei.iag.puc-rio.br/publicacoes/page/3/')

csv_data = csv.reader(download_data)



for row in csv_data:
    print row

