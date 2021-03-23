# Enter script code
retCode, sn = dialog.input_dialog(title='SN huawei nova',
    message='digite cole o SN',
    default='')

retCode, pirulito = dialog.input_dialog(title='frame e slot',
    message='digite frame e slot',
    default='')

retCode, pon = dialog.input_dialog(title='pon',
    message='digite a PON',
    default='')

retCode, ont = dialog.input_dialog(title='ONTID',
    message='digite o ONTID',
    default='')

dialog.info_dialog(title='Acesse a OLT',message="Clique dentro do terminal\nAPÓS de clicar OK!",width='300')

mouse.wait_for_click(1)

keyboard.send_keys('interface gpon ' + pirulito)
keyboard.send_keys('<enter>')
keyboard.send_keys('ont modify ' + pon + ' ' + ont + ' sn ' + SN)
Keyboard.send_keys('<enter>')