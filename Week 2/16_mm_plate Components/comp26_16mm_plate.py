# -*- coding: utf-8 -*-

# Macro Begin: /Users/anish/ProBUILD_FreeCAD/comp26_16mm_plate.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
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
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 104.126869, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 27.928451))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject', 0, 3, -2))


# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-113.130363, 0.000000, 0.000000),App.Vector(-113.130363, 28.491650, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('PointOnObject', 1, 1, -1))
constraintList.append(Sketcher.Constraint('Vertical', 1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

# Gui.runCommand('Sketcher_CreatePolyline',0)
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(-113.130363,28.491650,0),App.Vector(-52.315926,113.415939,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',1,2,2,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(11.714777,67.563437,0),App.Vector(0,0,1),78.755208),1.720100,2.520142),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',2,2,3,2)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject',3,1,-2)) 
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',0,55.856902)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',26.4653,95.2057,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(6,App.Units.Quantity('55.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',3,78.755221)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',-23.4473,138.033,0)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex8',11.7148,67.5634,0.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.V_Axis',0,102.933,0.002,False)
### Begin command Sketcher_ConstrainCoincidentUnified
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject',3,3,-2))
### End command Sketcher_ConstrainCoincidentUnified
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.V_Axis',0,103.907,0.002,False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex1',0,104.127,0.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex8',11.7148,67.5634,0.014,False)
### Begin command Sketcher_ConstrainCoincidentUnified
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',0,3,3,3))
### End command Sketcher_ConstrainCoincidentUnified
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',3,60.415965)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',-30.2522,156.316,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(8,App.Units.Quantity('55.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,3,-1,1,104.042855)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex1',0,104.043,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,0,3,104.042855)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(9,App.Units.Quantity('62.910000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,-1,1,117.910000)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex6',3.36778e-15,117.91,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,3,1,117.910000)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(10,App.Units.Quantity('118.000000 mm'))
# Gui.Selection.clearSelection()
### Begin command Std_Delete
App.getDocument('Unnamed').getObject('Sketch').delConstraint(7)
App.getDocument('Unnamed').recompute()
### End command Std_Delete
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,-1,1,117.910000)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex6',3.36778e-15,117.91,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,3,1,117.910000)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(9,App.Units.Quantity('118.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,1,2,28.491644)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',-113.13,14.2458,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',1,1,1,2,28.491644)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',-2,1,1,113.130355)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.V_Axis',0,13.4187,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(10,App.Units.Quantity('95.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',-22.0351,112.466,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',-53.3243,81.5343,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',-95,21.933,0.008,False)
# Gui.runCommand('Sketcher_Symmetry',0)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',4.75027,117.613,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',-4.29969,117.665,0.008,False)
### Begin command Sketcher_ConstrainTangent
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',4,3))
### End command Sketcher_ConstrainTangent
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',56.2197,79.7457,0.008,False)
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,1,2,28.491657)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',-95,23.3537,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',1,1,1,2,28.491657)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,1,1,190.000000)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',95,14.2458,0)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',33.8593,106.28,0.008,False)
### Begin command Sketcher_ConstrainBlock
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',4))
### End command Sketcher_ConstrainBlock
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',59.4224,75.5129,0.008,False)
### Begin command Sketcher_ConstrainBlock
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',5))
### End command Sketcher_ConstrainBlock
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-95.000000, 0.000000, 0.000000),App.Vector(95.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 7, 1, 1, 1))
constraintList.append(Sketcher.Constraint('Coincident', 7, 2, 6, 1))
constraintList.append(Sketcher.Constraint('Horizontal', 7))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',-14.1039,116.182,0.008,False)
### Begin command Sketcher_ConstrainBlock
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',3))
### End command Sketcher_ConstrainBlock
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',-82.5828,44.9539,0.008,False)
### Begin command Sketcher_ConstrainBlock
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',2))
### End command Sketcher_ConstrainBlock
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').movePoint(1,2,App.Vector(-98.428703,33.100449,0),0)
App.getDocument('Unnamed').getObject('Sketch').movePoint(3,0,App.Vector(-44.820583,123.498451,0),0)
App.getDocument('Unnamed').getObject('Sketch').movePoint(4,0,App.Vector(18.598158,84.255905,0),0)
App.getDocument('Unnamed').getObject('Sketch').movePoint(4,1,App.Vector(70.103996,110.884773,0),0)
App.getDocument('Unnamed').getObject('Sketch').movePoint(6,0,App.Vector(1.732849,7.708363,0),1)
App.getDocument('Unnamed').getObject('Sketch').movePoint(4,0,App.Vector(18.814373,94.589684,0),0)
App.getDocument('Unnamed').getObject('Sketch').movePoint(0,3,App.Vector(4.247502,65.067474,0),0)
App.getDocument('Unnamed').getObject('Sketch').movePoint(0,3,App.Vector(1.334124,64.096359,0),0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',19.3411,114.455,0.008,False)
### Begin command Sketcher_ConstrainBlock
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',4))
### End command Sketcher_ConstrainBlock
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-95.000000, 0.000000, 0.000000),App.Vector(95.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 7, 1, 1, 1))
constraintList.append(Sketcher.Constraint('Coincident', 7, 2, 6, 1))
constraintList.append(Sketcher.Constraint('Horizontal', 7))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,1,5,2,84.887721)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',73.7497,56.5772,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',5,2,5,1,51.219363)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,1,5,2,84.887716)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Angle',5,1,7,2,0.923066)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',36.3309,0,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(19,App.Units.Quantity('54.000000 deg'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,1,2,2,87.149739)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',-79.0503,48.7916,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',2,1,2,2,53.842407)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Angle',-1,1,2,1,0.904836)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.H_Axis',-45.293,0,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(11,App.Units.Quantity('54.000000 deg'))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex8',-1.91986,63.0335,0.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.V_Axis',0,67.2412,0.002,False)
### Begin command Sketcher_ConstrainCoincidentUnified
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject',3,3,-2))
### End command Sketcher_ConstrainCoincidentUnified
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',-39.1345,101.646,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',-53.6889,82.6751,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',-95,11.727,0.008,False)
# Gui.runCommand('Sketcher_Symmetry',0)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',30.3405,108.874,0.008,False)
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_ConstrainBlock',0)
# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-95.000000, 0.000000, 0.000000),App.Vector(95.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 7, 1, 1, 1))
constraintList.append(Sketcher.Constraint('Coincident', 7, 2, 6, 1))
constraintList.append(Sketcher.Constraint('Horizontal', 7))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

# Gui.runCommand('Sketcher_ConstrainBlock',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',24.9695,112.005,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',4))
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',50.2498,87.4087,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',5))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',95,14.8151,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',6))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',-15.9922,115.624,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',3))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',-95,20.2047,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',1))
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',-86.1798,37.9553,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',2))
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',50.3181,87.3147,0)
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',35.2986,105.178,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',4))
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
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body')
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.')
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
### Begin command Std_SaveAs
# Gui.SendMsgToActiveView("SaveAs")
App.getDocument("Unnamed").saveAs(u"/Users/anish/ProBUILD_FreeCAD/comp26_16mm_plate.FCStd")
### End command Std_SaveAs
# Macro End: /Users/anish/ProBUILD_FreeCAD/comp26_16mm_plate.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
