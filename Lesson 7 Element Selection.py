
import Autodesk

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
#from Autodesk.Revit.UI.Selection import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
#path=os.path.dirname(os.path.abspath(__file__))

class Single_Category(Selection.ISelectionFilter):
	def __init__(self, nom_categorie):
		self.nom_categorie = nom_categorie
	def AllowElement(self, e):
		if e.Category.Name == self.nom_categorie:
			return True
		else:
			return False
	def AllowReference(self, ref, point):
		return true

class Mult_Category(Selection.ISelectionFilter):
	def __init__(self, nom_categorie_1, nom_categorie_2):
		self.nom_categorie_1 = nom_categorie_1
		self.nom_categorie_2 = nom_categorie_2
	def AllowElement(self, e):
		if e.Category.Name == self.nom_categorie_1 or e.Category.Name == self.nom_categorie_2:
			return True
		else:
			return False
	def AllowReference(self, ref, point):
		return true

#Element
#PointOnElement
#Edge
#Face
#LinkedElement

# Num_1 -------------------------------------------Select One Element
sel = uidoc.Selection.PickObject(Selection.ObjectType.Element, 'Choose element')
el = doc.GetElement(sel)

t = Transaction(doc, 'selection')
t.Start()
par1 = el.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
par1.Set('Text_1')
t.Commit()

# Num_2 --------------------------------------Select Elements
sel = uidoc.Selection.PickObjects(Selection.ObjectType.Element, 'Choose elements')


"""els = []
for i sel:
	el = doc.GetElement(i)
	els.append(el)"""
els = [doc.GetElement( elId ) for elId in sel]
t = Transaction(doc, 'selection')
t.Start()
for i in els:
	par1 = i.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
	par1.Set('Text_1')
t.Commit()

# Num_3 ------------------------------ Single Category Selection
sel = uidoc.Selection.PickObjects(Selection.ObjectType.Element,  Single_Selection('Structural Columns'))
els = [doc.GetElement( elId ) for elId in sel]
t = Transaction(doc, 'selection')
t.Start()
for i in els:
	par1 = i.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
	par1.Set('Text_1')
t.Commit()



# Num_4 ------------------------------ Multiple Category Selection

sel = uidoc.Selection.PickObjects(Selection.ObjectType.Element,  Mult_Category('Structural Columns', 'Floors'))
els = [doc.GetElement( elId ) for elId in sel]

t = Transaction(doc, 'selection')
t.Start()
for i in els:
	par1 = i.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
	par1.Set('Text_1')
t.Commit()

# Num_5 ------------------------------ Mouse Selection
els = [ doc.GetElement( elId ) for elId in uidoc.Selection.GetElementIds() ]

"""els = []
selection = uidoc.Selection.GetElementIds()
for i in selection:
	el = doc.GetElement(i)
	els.append(el)"""

t = Transaction(doc, 'selection')
t.Start()
for i in els:
	par1 = i.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
	par1.Set('Text_1')
t.Commit()
