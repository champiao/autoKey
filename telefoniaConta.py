# Enter script code
retCode, conta = dialog.input_dialog(title='conta',
    message='digite a conta sip sem o domínio',
    default='')
    
retCode, senha = dialog.input_dialog(title='senha',
    message='digite a senha da conta sip',
    default='')

dialog.info_dialog(title='VOIP',message='acesse a página de VOIP Basic e clique em OK\n e depois na página já carregada',width='500')
mouse.wait_for_click(1)
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("sip.nipcable.com.br")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<ctrl>+a")
keyboard.send_keys("*xx|1x.S|[2-5]xxxxxxx|0[1-9][1-9]xxxxxx.S|[7-9]xxxxxxx.S|00xxxx.L|0300xxx.S|0800xxx.S|0500xxx.S")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("300")
keyboard.send_keys("<tab>")
keyboard.send_keys("<down><down>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<down><down>")
keyboard.send_keys("<tab>")
keyboard.send_keys("bra")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys(" ")
keyboard.send_keys("<tab>")
keyboard.send_keys(conta)
keyboard.send_keys("<tab>")
keyboard.send_keys(conta)
keyboard.send_keys("<tab>")
keyboard.send_keys("<tab>")
keyboard.send_keys(conta)
keyboard.send_keys("<tab>")
keyboard.send_keys(senha)
keyboard.send_keys("<tab>")
keyboard.send_keys(" ")