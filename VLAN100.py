retCode, gerencia = dialog.input_dialog(title='Configurar WAN',
	message='Digite o ip de gerencia', 
	default='192.168.')
	
retCode, gateway = dialog.input_dialog(title='Configurar WAN',
	message='Digite o ip de gateway', 
	default='192.168.')
	
mouse.wait_for_click(1)
keyboard.send_keys(userInput)

