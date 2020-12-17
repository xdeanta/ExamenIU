import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 15-12-2018")
        self.set_border_width(10)

        BoxTop = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        BoxBottom = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 6)
        SubBoxTop = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 6)
        SubBoxTopImage =Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        self.add(BoxTop)

        imaxe = Gtk.Image()
        imaxe.set_from_icon_name ("media-optical", Gtk.IconSize.DIALOG)
        chkAnimado= Gtk.CheckButton(label = "Animado")
        SubBoxTopImage.pack_start(imaxe, False, True, 1)
        SubBoxTopImage.pack_start(chkAnimado,False, True, 1)

        SubBoxTop.pack_start(SubBoxTopImage, False, False, 1)

        self.txvAreatexto = Gtk.TextView()
        self.txvAreatexto.set_size_request(420, 100)
        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.ALWAYS)
        scroll.add(self.txvAreatexto)
        SubBoxTop.pack_start(scroll, False, True, 5)

        SubBoxTopButtons = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        btnReproducir = Gtk.Button(label = "Engadir a pista a reproducir")
        btnPausa = Gtk.Button(label = "Subir na lista")
        btnParar = Gtk.Button(label = "Baixar na lista")
        btnSaltar= Gtk.Button(label = "Saltar")
        SubBoxTopButtons.pack_start(btnReproducir, False, False, 1)
        SubBoxTopButtons.pack_start(btnPausa, False, False, 1)
        SubBoxTopButtons.pack_start(btnParar, False, False, 1)

        SubBoxTopBtnCombo = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        self.cmbPosicionSaltar =Gtk.ComboBoxText()
        self.cmbPosicionSaltar.set_size_request(140,10)
        self.cmbPosicionSaltar.append_text("Inicio")
        self.cmbPosicionSaltar.append_text("Fin")
        self.cmbPosicionSaltar.append_text("Anterior")
        self.cmbPosicionSaltar.append_text("Siguiente")
        self.cmbPosicionSaltar.connect("changed", self.on_cmbPosicionSaltar_changed)
        SubBoxTopBtnCombo.pack_start(btnSaltar, False, False, 1)
        SubBoxTopBtnCombo.pack_start(self.cmbPosicionSaltar,True, False, 1)

        SubBoxTopButtons.pack_start(SubBoxTopBtnCombo, False, False, 1)

        SubBoxTopButtons2 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)

        btnAbrirFicheiro = Gtk.Button(label = "Abrir ficheiro...")
        btnFalarFicheiro = Gtk.Button (label = "Reproducir ficheiro...")
        btnGardarComo = Gtk.Button (label = "Gardar como...")
        btnEliminar = Gtk.Button (label = "Eliminar pista")

        SubBoxTopButtons2.pack_start(btnAbrirFicheiro, False, False, 1)
        SubBoxTopButtons2.pack_start(btnFalarFicheiro, False, False, 1)
        SubBoxTopButtons2.pack_start(btnGardarComo, False, False, 1)
        SubBoxTopButtons2.pack_start(btnEliminar, False, False, 1)

        SubBoxTopButtons.pack_start(SubBoxTopButtons2, False, False, 1)

        SubBoxTop.pack_start(SubBoxTopButtons, False, False, 1)

        BoxTop.pack_start(SubBoxTop, False, False, 1)

        builder = Gtk.Builder()
        builder.add_from_file("cadroSonGlade.glade")

        grid = builder.get_object("grid2")

        BoxBottom.pack_start(grid, False, False, 1)

        contedorH2 = Gtk.Frame()
        contedorH2.set_label("Opcións de reproducción")

        grid2 = Gtk.Grid()
        contedorH2.add(grid2)

        self.chkAsincrono= Gtk.CheckButton(label = "Asíncrono")
        chkENomeFicheiro= Gtk.CheckButton(label = "É nome de ficheiro")
        chkXmlPersistente= Gtk.CheckButton(label = "XML persistente")
        chkFiltrarAntesReproducir= Gtk.CheckButton(label = "Filtrar antes de reproducir")
        chkExml= Gtk.CheckButton(label = "É XML")
        chkReproduccionNpl= Gtk.CheckButton(label = "Reproducción NPL")

        self.chkAsincrono.connect("toggled", self.on_chkAsincrono_toggled)

        grid2.attach(self.chkAsincrono, 0, 0, 1, 1)
        grid2.attach(chkENomeFicheiro, 0, 1, 1, 1)
        grid2.attach(chkXmlPersistente, 0, 2, 1, 1)
        grid2.attach(chkFiltrarAntesReproducir, 1, 0, 1, 1)
        grid2.attach(chkExml, 1, 1, 1, 1)
        grid2.attach(chkReproduccionNpl, 1, 2, 1, 1)

        BoxBottom.pack_start(contedorH2, False, False, 1)

        BoxTop.pack_start(BoxBottom, False, False, 1)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_cmbPosicionSaltar_changed(self, comboBox):
        opcion = self.cmbPosicionSaltar.get_active()
        if opcion == 0:
            print("Inicio")
        if opcion == 1:
            print("Fin")
        if opcion == 2:
            print("Anterior")
        if opcion == 3:
            print("Siguiente")

    def on_chkAsincrono_toggled(self, chkbutton):
        txtbuffer = Gtk.TextBuffer()
        txtbuffer.set_text("Modo de Reproduccion Asíncrono seleccionado")
        if self.chkAsincrono.get_active() == 1:
            self.txvAreatexto.set_buffer(txtbuffer)
        else:
            txtbuffer.set_text("")
            self.txvAreatexto.set_buffer(txtbuffer)


if __name__=="__main__":

    Exame()
    Gtk.main()