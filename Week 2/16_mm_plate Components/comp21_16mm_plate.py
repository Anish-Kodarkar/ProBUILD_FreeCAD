# -*- coding: utf-8 -*-

# Macro Begin: /Users/anish/ProBUILD_FreeCAD/comp21_16mm_plate.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
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
# Gui.runCommand('PartDesign_NewSketch',0)
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
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(47.222412, 0.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(47.222412, 0.000000, 0.000000),App.Vector(47.222412, 20.517746, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(47.222412, 20.517746, 0.000000),App.Vector(0.000000, 20.517746, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(0.000000, 20.517746, 0.000000),App.Vector(0.000000, 0.000000, 0.000000)))
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
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,1,2,2,47.222412)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',23.6112,20.5177,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',2,2,2,1,47.222412)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(9,App.Units.Quantity('520.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,3,2,20.517746)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',0,8.97566,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',3,2,3,1,20.517746)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(10,App.Units.Quantity('170.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(69.598839, 74.300781, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 44.125777))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(389.939789, 84.008110, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 45.476130))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',4,88.251554)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',113.324,80.2297,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(11,App.Units.Quantity('117.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_ConstrainEqual',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',125.673,90.9715,0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',348.672,64.9025,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',4,5))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,3,-1,1,398.886452)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex10',389.94,84.0081,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,5,3,84.008110)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,3,-1,1,398.886452)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,3,1,130.060211)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',520,85,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(13,App.Units.Quantity('90.930500 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,3,-1,1,437.216192)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex10',429.069,84.0081,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,3,0,84.008110)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',408.608,0,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(14,App.Units.Quantity('84.434000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,3,-1,1,101.806701)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex9',69.5988,74.3008,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,4,3,74.300781)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(15,App.Units.Quantity('74.820000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,3,-1,1,102.186255)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex9',69.5988,74.82,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,4,3,74.820000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,3,-1,1,102.186255)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',-1,1,4,3,69.598839)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,3,3,69.598839)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',0,85,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(16,App.Units.Quantity('75.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,3,-1,1,105.938814)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex9',75,74.82,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,3,5,3,354.200000)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex10',429.069,84.434,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',4,3,5,3,9.614000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,3,5,3,354.200000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',4,3,5,3,354.069500)) 
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,3,-1,1,102.186255)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex9',69.5988,74.82,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,4,3,74.820000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,3,-1,1,102.186255)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,4,3,74.820000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,3,3,69.598839)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',0,69.9882,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(16,App.Units.Quantity('75.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateFillets',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',0,15.6948,0)
App.getDocument('Unnamed').getObject('Sketch').fillet(3,0,App.Vector(0.000000,15.694780,0),App.Vector(29.717537,0.000000,0),15.694780,True,True,False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',520,22.2248,0)
App.getDocument('Unnamed').getObject('Sketch').fillet(1,0,App.Vector(520.000000,22.224752,0),App.Vector(469.091492,0.000000,0),22.224752,True,True,False)
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',6,15.694780)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',4.59689,4.59689,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(23,App.Units.Quantity('75.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',8,22.224729)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',513.491,6.50947,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(24,App.Units.Quantity('75.000000 mm'))
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
# Macro End: /Users/anish/ProBUILD_FreeCAD/comp21_16mm_plate.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
