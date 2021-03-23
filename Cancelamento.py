retCode, interface1 = dialog.input_dialog(title='Cancelamento',
    message='Digite a interface X/X:', 
    default='')
	
retCode, interface2 = dialog.input_dialog(title='Cancelamento',
    message='Digite a interface X:', 
    default='')
	
retCode, ontid = dialog.input_dialog(title='Cancelamento',
    message='Digite a ONTID:', 
    default='')

retCode, profile = dialog.input_dialog(title='Cancelamento',
	message='Digite nome do profile:', 
	default='')
dialog.info_dialog(title='Acesse a OLT',message="Clique dentro da OLT")
	
mouse.wait_for_click(1)
keyboard.send_keys("undo service-port port " + interface1 + "/" + interface2 + " ont " + ontid + "<enter><enter>y<enter>")
keyboard.send_keys("interface gpon " + interface1 + "<enter>")
keyboard.send_keys("ont delete " + interface2 + " " + ontid + "<enter>quit<enter>")
keyboard.send_keys("undo ont-lineprofile gpon profile-name " + profile + "<enter>save<enter><enter>")

dialog.info_dialog(title='OK',message="Removido. Clique nas obs do Nipranet")

mouse.wait_for_click(1)

keyboard.send_keys("Removidas as configurações da OLT e dalloradius.<enter>")
hoje = system.exec_command("date +%d/%m/%Y-%H:%M")
keyboard.send_keys("Isaque Silva - " + hoje)
keyboard.send_keys("<enter>========================")