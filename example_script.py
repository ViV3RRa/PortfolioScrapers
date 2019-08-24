from platforms.mintos import Mintos
from platforms.nordnet import Nordnet
from platforms.peerberry import Peerberry
from platforms.grupeer import Grupeer
from platforms.fastinvest import Fastinvest


nordnet = Nordnet()
nordnet.login()
print('Nordnet:	' + str(nordnet.get_account_value()) + ' kr')
nordnet.quit()

mintos = Mintos()
mintos.login()
print('Mintos:		' + str(mintos.get_account_value()) + ' €')
mintos.quit()

peerberry = Peerberry()
peerberry.login()
print('Peerberry:	' + str(peerberry.get_account_value()) + ' €')
peerberry.quit()

grupeer = Grupeer()
grupeer.login()
print('Grupeer:	' + str(grupeer.get_account_value()) + ' €')
grupeer.quit()

fastinvest = Fastinvest()
fastinvest.login()
print('Fastinvest:	' + str(fastinvest.get_account_value()) + ' €')
fastinvest.quit()

