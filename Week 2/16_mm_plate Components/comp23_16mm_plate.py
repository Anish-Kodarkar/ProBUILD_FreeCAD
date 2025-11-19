# -*- coding: utf-8 -*-

# Macro Begin: /Users/anish/ProBUILD_FreeCAD/comp23_16mm_plate.py.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD
import PartDesign
import PartDesignGui
import Sketcher

# Gui.runCommand('Std_DlgMacroRecord',0)
### Begin command Std_New
App.newDocument()
# App.setActiveDocument("Unnamed")
# App.ActiveDocument=App.getDocument("Unnamed")
# Gui.ActiveDocument=Gui.getDocument("Unnamed")
# Gui.activeDocument().activeView().viewDefaultOrientation()
### End command Std_New
### Begin command PartDesign_Body
App.activeDocument().addObject('PartDesign::Body','Body')
App.ActiveDocument.getObject('Body').Label = 'Body'
# Gui.activateView('Gui::View3DInventor', True)
# Gui.activeView().setActiveObject('pdbody', App.activeDocument().Body)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection(App.ActiveDocument.Body)
App.ActiveDocument.recompute()
### End command PartDesign_Body
# Gui.Selection.addSelection('Unnamed','Body')
# Gui.runCommand('PartDesign_CompSketches',0)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.')
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('XY_Plane'),[''])
App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch.')
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
# tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
# ActiveSketch.ViewObject.TempoVis = tv
# if ActiveSketch.ViewObject.EditingWorkbench:
#   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
# if ActiveSketch.ViewObject.HideDependent:
#   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
# if ActiveSketch.ViewObject.ShowSupport:
#   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not ref[0].isDerivedFrom("PartDesign::Plane")])
# if ActiveSketch.ViewObject.ShowLinks:
#   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
# tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
# tv.hide(ActiveSketch)
# del(tv)
# del(ActiveSketch)
# 
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
# if ActiveSketch.ViewObject.RestoreCamera:
#   ActiveSketch.ViewObject.TempoVis.saveCamera()
#   if ActiveSketch.ViewObject.ForceOrtho:
#     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
# 
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateRectangles',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(1590.179199, 0.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1590.179199, 0.000000, 0.000000),App.Vector(1590.179199, 326.549011, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1590.179199, 326.549011, 0.000000),App.Vector(0.000000, 326.549011, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(0.000000, 326.549011, 0.000000),App.Vector(0.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
constraintList.append(Sketcher.Constraint('Horizontal', 0))
constraintList.append(Sketcher.Constraint('Horizontal', 2))
constraintList.append(Sketcher.Constraint('Vertical', 1))
constraintList.append(Sketcher.Constraint('Vertical', 3))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))


# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,0,2,1590.179199)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',901.641,0,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',0,1,0,2,1590.179199)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(9,App.Units.Quantity('1598.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,3,2,326.549011)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',0,115.49,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',3,2,3,1,326.549011)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(10,App.Units.Quantity('170.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateRectangles',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(690.971558, 102.760742, 0.000000),App.Vector(690.971558, 21.109076, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(690.971558, 21.109076, 0.000000),App.Vector(769.901550, 21.109076, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(769.901550, 21.109076, 0.000000),App.Vector(769.901550, 102.760742, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(769.901550, 102.760742, 0.000000),App.Vector(690.971558, 102.760742, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 4, 2, 5, 1))
constraintList.append(Sketcher.Constraint('Coincident', 5, 2, 6, 1))
constraintList.append(Sketcher.Constraint('Coincident', 6, 2, 7, 1))
constraintList.append(Sketcher.Constraint('Coincident', 7, 2, 4, 1))
constraintList.append(Sketcher.Constraint('Vertical', 4))
constraintList.append(Sketcher.Constraint('Vertical', 6))
constraintList.append(Sketcher.Constraint('Horizontal', 5))
constraintList.append(Sketcher.Constraint('Horizontal', 7))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',7,1,7,2,78.929992)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',726.354,102.761,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',7,2,7,1,78.929992)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(19,App.Units.Quantity('60.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,1,6,2,81.651666)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',759.528,61.9349,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',6,1,6,2,81.651666)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(20,App.Units.Quantity('85.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,1,4,2,85.000000)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',699.528,61.18,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',4,2,4,1,85.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,1,4,2,85.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',4,2,4,1,85.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,4,699.527550)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',0,61.9348,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(21,App.Units.Quantity('769.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,1,5,2,60.000000)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',799,18.68,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',5,1,5,2,60.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,5,18.679981)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',799,0,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(22,App.Units.Quantity('15.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.getDocument('Unnamed').resetEdit()
App.ActiveDocument.recompute()
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
# tv = ActiveSketch.ViewObject.TempoVis
# if tv:
#   tv.restore()
# ActiveSketch.ViewObject.TempoVis = None
# del(tv)
# del(ActiveSketch)
# 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.')
App.getDocument('Unnamed').recompute()
### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = 10
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Pad').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pad').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pad').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pad').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pad').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pad').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pad.')
# Gui.Selection.clearSelection()
### End command PartDesign_Pad
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Pad').Length = 10.000000
App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad').Direction = (0, 0, 1)
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pad').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pad').Type = 0
App.getDocument('Unnamed').getObject('Pad').UpToFace = None
App.getDocument('Unnamed').getObject('Pad').Reversed = 0
App.getDocument('Unnamed').getObject('Pad').Midplane = 0
App.getDocument('Unnamed').getObject('Pad').Offset = 0
App.getDocument('Unnamed').recompute()
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
# Macro End: /Users/anish/ProBUILD_FreeCAD/comp23_16mm_plate.py.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
