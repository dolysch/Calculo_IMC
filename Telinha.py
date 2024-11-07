import wx 

class IMCCalculator(wx.Frame):
    def __init__(self, parent, id, title):
        super(IMCCalculator, self).__init__(parent, id, title, size=(500, 300))


        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox_name = wx.BoxSizer(wx.HORIZONTAL)
        name_label = wx.StaticText(panel, label="Nome do Paciente:")
        self.name_text_ctrl = wx.TextCtrl(panel)
        hbox_name.Add(name_label, flag=wx.RIGHT, border=8)
        hbox_name.Add(self.name_text_ctrl, proportion=1)
        vbox.Add(hbox_name, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox_address = wx.BoxSizer(wx.HORIZONTAL)
        address_label = wx.StaticText(panel, label="Endereço Completo:")
        self.address_text_ctrl = wx.TextCtrl(panel)
        hbox_address.Add(address_label, flag=wx.RIGHT, border=8)
        hbox_address.Add(self.address_text_ctrl, proportion=1)
        vbox.Add(hbox_address, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        
        hbox_ap = wx.BoxSizer(wx.HORIZONTAL)
        height_label = wx.StaticText(panel, label="Altura (cm)")
        self.height_text_ctrl = wx.TextCtrl(panel, size=(100, -1))
        weight_label = wx.StaticText(panel, label="Peso (Kg)")
        self.weight_text_ctrl = wx.TextCtrl(panel, size=(100, -1))
        hbox_ap.Add(height_label, flag=wx.RIGHT | wx.TOP, border=8)
        hbox_ap.Add(self.height_text_ctrl, flag=wx.RIGHT, border=10)
        hbox_ap.Add(weight_label, flag=wx.RIGHT | wx.TOP, border=8)
        hbox_ap.Add(self.weight_text_ctrl, flag=wx.RIGHT, border=10)

        self.result_text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(200, 80))
        hbox_ap.Add(self.result_text_ctrl, proportion=1, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(hbox_ap, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox_buttons = wx.BoxSizer(wx.HORIZONTAL)
        calc_button = wx.Button(panel, label="Calcular")
        reset_button = wx.Button(panel, label="Reiniciar")
        exit_button = wx.Button(panel, label="Sair")

        hbox_buttons.Add(calc_button, flag=wx.RIGHT, border=10)
        hbox_buttons.Add(reset_button, flag=wx.RIGHT, border=10)
        hbox_buttons.Add(exit_button, flag=wx.RIGHT, border=10)
        vbox.Add(hbox_buttons, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.OnExit, exit_button)
        self.Bind(wx.EVT_BUTTON, self.OnCalculate, calc_button)
        self.Bind(wx.EVT_BUTTON, self.OnReset, reset_button)

        self.Show(True)

    def OnExit(self, event):
        self.Close()

    def OnCalculate(self, event):
        try:
            height = float(self.height_text_ctrl.GetValue()) / 100
            weight = float(self.weight_text_ctrl.GetValue())
            imc = weight / (height ** 2)
            self.result_text_ctrl.SetValue(f"IMC: {imc:.2f}")
        except ValueError:
            self.result_text_ctrl.SetValue("Por favor, insira valores válidos para altura e peso.")

    def OnReset(self, event):
        self.name_text_ctrl.SetValue("")
        self.address_text_ctrl.SetValue("")
        self.height_text_ctrl.SetValue("")
        self.weight_text_ctrl.SetValue("")
        self.result_text_ctrl.SetValue("")


if __name__ == '__main__':
    app = wx.App()
    frame = IMCCalculator(None, wx.ID_ANY, 'Cálculo do IMC - Índice de Massa Corporal')
    app.MainLoop()
