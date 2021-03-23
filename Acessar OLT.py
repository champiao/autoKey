optionShapes = ['Taubate', 'Cacapava', 'Helbor', 'Century', 'Aquarius', 'Alphaville', 'Mansao']

retCode, choices = dialog.list_menu_multi(options=optionShapes, 
	title='Selecione a OLT', 
	message='OLT:',
	defaults='', 
	height='280')
	
if retCode:
	myMessage = 'Dialog exit code was: ' + str(retCode)

	dialog.info_dialog(title='You cancelled the dialog', 
	message=myMessage, 
	width='200')  # width is extra zenity parameter. See the zenity manpage for details.


for item in choices:
    system.exec_command("gnome-terminal")

    window.wait_for_exist("oem@suporte-isaque: ~",timeOut=10)

    window.activate('oem@suporte-isaque: ~', switchDesktop=True)

    keyboard.send_keys("ssh " + item + "<enter>")