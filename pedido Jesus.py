# Enter script code
#window.activate("WhatsDesk", switchDesktop=True)
retCode, prato = dialog.input_dialog(title='Prato',
	message='Digite o prato desejado:', 
	default='')
#----------------------------------------------
window.activate("Whatsdesk", switchDesktop=True)
keyboard.send_keys("Bom dia... gostaria de pedir " + prato + " tamanho mini..... eu busco ai as 11:30, sem nada para beber, com salada, precisarei de talher pagamento alelo refeiçao, em nome de Champião por favor<enter>")