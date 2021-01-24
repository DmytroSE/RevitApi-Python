# pylint: skip-file
from pyrevit import forms
from pyrevit.framework import Input
from pyrevit import framework
from pyrevit import script, revit
from pyrevit import DB, UI
from pyrevit import HOST_APP, EXEC_PARAMS

from Autodesk.Revit.UI import TaskDialog
from pyrevit.forms import WPFWindow

__persistentengine__ = True
import os

class NonModalWindow(WPFWindow):

    def __init__(self, xaml_file_name):

    	WPFWindow.__init__(self, xaml_file_name)
        self.Show()

    @revit.events.handle('doc-changed', 'doc-closed', 'doc-opened', 'view-activated')
    def uiupdator_eventhandler(sender, args):
        ui.update_ui()

    def update_ui(self):
        if revit.doc:
            print('ok')

    def window_moving(self, sender, args):
        if args.ChangedButton == Input.MouseButton.Left:
            self.DragMove()

    def window_closing(self, sender, args): #pylint: disable=unused-argument
        revit.events.stop_events()

def open_script_2(sender, args):
    try:
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        file = os.path.realpath(os.path.join(location + '/interface.xaml'))
        ui = Form(file)
    except Exception,e: TaskDialog.Show('1', str(e))

def __selfinit__(script_cmp, ui_button_cmp, __rvt__):
    try:
    	HOST_APP.app.DocumentOpened += \
    	    framework.EventHandler[DB.Events.DocumentOpenedEventArgs](
    	        open_script_2
    	        )
    	return True
    except Exception:
    	return False

if __name__ == '__main__':
    ui = NonModalWindow('interface.xaml')
