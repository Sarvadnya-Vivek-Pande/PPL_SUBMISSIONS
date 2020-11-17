import gi.repository
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

screen=Gdk.Screen.get_default()
provider=Gtk.CssProvider()
provider.load_from_path("Calculator.css")
Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class Calculator(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(430,500)
        self.set_border_width(15)
        self.status=False

        header_bar=Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title= "Calculator"
        self.set_titlebar(header_bar)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)
        #box=Gtk.Box()
        #vbox.pack_start(box, False, False, 0)

        self.textarea=Gtk.Entry()
        self.textarea.set_property('editable', False)
        Gtk.Widget.set_size_request(self.textarea, 400, 100)
        self.textarea.set_text(" ")
        vbox.pack_start(self.textarea, True, True, 0)

        grid = Gtk.Grid()
        button1 = Gtk.Button(label="1")
        button2 = Gtk.Button(label="2")
        button3 = Gtk.Button(label="3")
        button4 = Gtk.Button(label="4")
        button5 = Gtk.Button(label="5")
        button6 = Gtk.Button(label="6")
        button7 = Gtk.Button(label="7")
        button8 = Gtk.Button(label="8")
        button9 = Gtk.Button(label="9")
        button0 = Gtk.Button(label="0")
        button_bracketopen=Gtk.Button(label="(")
        button_bracketclose=Gtk.Button(label=")")
        button_plus = Gtk.Button(label="+")
        button_minus=Gtk.Button(label="-")
        button_multiply=Gtk.Button(label="*")
        button_divide=Gtk.Button(label="/")
        button_equal=Gtk.Button(label="=")
        button_clear=Gtk.Button(label="AC")
        button_delete=Gtk.Button(label="DEL")
        button_dot=Gtk.Button(label=".")

        grid.add(button_clear)
        grid.add(button_bracketopen)
        grid.add(button_bracketclose)
        grid.add(button_divide)
        grid.attach(button7, 0, 1, 1, 1)
        grid.attach(button8, 1, 1, 1, 1)
        grid.attach(button9, 2, 1, 1, 1)
        grid.attach(button_multiply, 3, 1, 1, 1)
        grid.attach(button4, 0, 2, 1, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach(button6, 2, 2, 1, 1)
        grid.attach(button_plus, 3, 2, 1, 1)
        grid.attach(button1, 0, 3, 1, 1)
        grid.attach(button2, 1, 3, 1, 1)
        grid.attach(button3, 2, 3, 1, 1)
        grid.attach(button_minus, 3, 3, 1, 1)
        vbox.pack_start(grid, True, True, 0)
        grid.attach(button_delete, 0, 4, 1, 1)
        grid.attach(button0, 1, 4, 1, 1)
        grid.attach(button_dot, 2, 4, 1, 1)
        grid.attach(button_equal, 3, 4, 1, 1)

        Gtk.Widget.set_size_request(button_multiply, 100,70)
        Gtk.Widget.set_size_request(button_divide, 100,70)
        Gtk.Widget.set_size_request(button_clear, 100,70)
        Gtk.Widget.set_size_request(button_delete, 100,70)
        Gtk.Widget.set_size_request(button1, 100,70)
        Gtk.Widget.set_size_request(button2, 100,70)
        Gtk.Widget.set_size_request(button3, 100,70)
        Gtk.Widget.set_size_request(button4, 100,70)
        Gtk.Widget.set_size_request(button9, 100,70)
        Gtk.Widget.set_size_request(button0, 100,70)
        Gtk.Widget.set_size_request(button_plus, 100,70)
        Gtk.Widget.set_size_request(button_minus, 100,70)
        Gtk.Widget.set_size_request(button_bracketopen, 100,70)
        Gtk.Widget.set_size_request(button_bracketclose, 100,70)
        Gtk.Widget.set_size_request(button_dot, 100,70)
        Gtk.Widget.set_size_request(button_equal, 100,70)
        Gtk.Widget.set_size_request(button5, 100,70)
        Gtk.Widget.set_size_request(button6, 100,70)
        Gtk.Widget.set_size_request(button7, 100,70)
        Gtk.Widget.set_size_request(button8, 100,70)

        vbox.pack_start(grid, True, True, 0)
        
        button1.connect("clicked", self.set_text)
        button2.connect("clicked", self.set_text)
        button3.connect("clicked", self.set_text)
        button4.connect("clicked", self.set_text)
        button5.connect("clicked", self.set_text)
        button6.connect("clicked", self.set_text)
        button7.connect("clicked", self.set_text)
        button8.connect("clicked", self.set_text)
        button9.connect("clicked", self.set_text)
        button0.connect("clicked", self.set_text)
        button_bracketopen.connect("clicked", self.set_text)
        button_bracketclose.connect("clicked", self.set_text)
        button_plus.connect("clicked", self.set_text)
        button_minus.connect("clicked", self.set_text)
        button_divide.connect("clicked", self.set_text)
        button_multiply.connect("clicked", self.set_text)
        button_dot.connect("clicked", self.set_text)
        button_clear.connect("clicked", self.clear_all)
        button_delete.connect("clicked", self.delete)
        button_equal.connect("clicked", self.evaluate)

    def set_text(self, button):

        if (self.textarea.get_text() == "cannot divide by zero" or self.textarea.get_text() == "Enter a valid expression" ):
            self.textarea.set_text(" ")
        
        List=['1','2','3','4','5','6','7','8','9','0','.']
        if (self.status == True and button.get_label() in List):
            self.textarea.set_text(" ")
        if (self.textarea.get_text()[-1] in List and button.get_label() in List):
            self.textarea.set_text(self.textarea.get_text() + button.get_label())
        else:
            self.textarea.set_text(self.textarea.get_text()+ " " + button.get_label())
        
        self.status=False

    def clear_all(self, button_clear):
        self.textarea.set_text(" ")

    def delete(self, button_delete):
        buffer = self.textarea.get_text()
        try:
            check=buffer[-1]
            self.textarea.set_text(buffer[0:len(buffer)-1])
        except:
            self.textarea.set_text(" ")
            
    def evaluate(self, button_equal):
        to_solve=""
        expression = self.textarea.get_text()
        for i in expression:
            if(i !=" "):
                to_solve=to_solve+i
        try:
            self.textarea.set_text(str(eval(to_solve)))
        except ZeroDivisionError as e:
             self.textarea.set_text("cannot divide by zero")
        except Exception as e:
            self.textarea.set_text("Enter a valid expression")
        self.status=True
        

calsie=Calculator()
calsie.connect("destroy", Gtk.main_quit)
calsie.set_resizable(False)
calsie.show_all()
Gtk.main()

