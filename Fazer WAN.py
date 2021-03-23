retCode, vlan = dialog.input_dialog(title='Configurar WAN',
	message='Digite a VLAN', 
	default='')

retCode, usuario = dialog.input_dialog(title='Configurar WAN',
	message='Digite o pppoe', 
	default='')
		
retCode, senha = dialog.input_dialog(title='Configurar WAN',
	message='Digite a senha', 
	default='')
	
dialog.info_dialog(title='Acesse a pagina de WAN',message="Clique dentro da pagina carregada\nAPÓS de clicar OK!",width='300')
	
mouse.wait_for_click(1)

keyboard.send_keys("<tab>")
keyboard.send_keys(" ")
keyboard.send_keys("<tab><tab><tab><tab>")
keyboard.send_keys("<left>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<down>")
keyboard.send_keys("<down>")
keyboard.send_keys("<tab><tab><tab><tab>")
keyboard.send_keys(vlan)
keyboard.send_keys("<tab><tab><tab><tab>")
keyboard.send_keys(usuario)
keyboard.send_keys("<tab>")
keyboard.send_keys(senha)
