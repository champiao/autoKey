retCode, ssid = dialog.input_dialog(title='Configurar WIFI',
	message='Digite o SSID:', 
	default='')
#----------------------------
retCode, senha = dialog.input_dialog(title='Configurar WIF',
	message='Digite a senha:', 
	default='')
	
dialog.info_dialog(title='Acesse a pagina de Wifi',message="Clique dentro da pagina carregada\nAPÓS de clicar OK!",width='300')
	
mouse.wait_for_click(1)

keyboard.send_keys("<tab>")
keyboard.send_keys(ssid)
keyboard.send_keys("<tab>")
keyboard.send_keys(senha)
keyboard.send_keys("<tab><tab>")
keyboard.send_keys(ssid + " - 5G")
keyboard.send_keys("<tab>")
keyboard.send_keys(senha)
keyboard.send_keys("<tab><tab>")
keyboard.send_keys(" ")