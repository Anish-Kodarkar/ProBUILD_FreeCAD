# -*- coding: utf-8 -*-

# Macro Begin: /Users/anish/ProBUILD_FreeCAD/comp25_16mm_plate.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
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
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(7.089358, 14.873554, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 1.632394))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(10.955741, 17.550280, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 1.745724))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
# Gui.runCommand('Sketcher_CreateLine',0)
# Gui.runCommand('Sketcher_CreatePolyline',0)
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(10.137853,20.115477,0),App.Vector(4.970284,16.397800,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(6.402698,14.406745,0),App.Vector(0,0,1),2.452776),2.194440,3.587326),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',2,2,3,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(4.189571,13.349305,0),App.Vector(11.359404,-1.656512,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',3,2,4,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(11.359404,-1.656512,0),App.Vector(13.669643,-0.889389,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',4,2,5,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(13.669643,-0.889389,0),App.Vector(20.547346,12.828834,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',5,2,6,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(20.547346,12.828834,0),App.Vector(13.409407,19.557825,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',6,2,7,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(11.354557,17.378094,0),App.Vector(0,0,1),2.995603),0.814881,1.989048),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',7,2,8,1)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',8,2,2,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(14.784946,11.118702,0),App.Vector(11.699276,13.163424,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(11.174673,12.371751,0),App.Vector(0,0,1),0.949713),0.985579,3.754978),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',9,2,10,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(10.398089,11.825059,0),App.Vector(13.620274,7.247896,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',10,2,11,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(14.502311,7.868824,0),App.Vector(0,0,1),1.078676),-2.528207,-0.410657),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',11,2,12,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(15.491305,7.438204,0),App.Vector(16.327482,9.358629,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',12,2,13,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(15.141357,9.875083,0),App.Vector(0,0,1),1.293684),-0.410657,1.849907),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',13,2,14,1)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',14,2,9,1)) 
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,1,4,2,16.630726)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',7.03613,7.39171,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',4,2,4,1,15.005817)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,1,4,2,16.630726)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',4,2,4,1,15.005817)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,1,4,2,16.630726)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',4,2,4,1,15.005817)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,1,4,2,16.630726)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(13,App.Units.Quantity('1077.346300 mm'))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex1',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex2',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex3',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex4',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex5',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex6',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex7',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex8',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex9',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex10',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex11',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex12',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex13',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex14',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex15',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex16',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex17',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex18',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex19',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex20',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge10',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex21',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex22',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex23',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge11',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex24',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex25',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge12',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex26',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex27',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex28',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge13',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex29',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex30',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge14',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex31',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex32',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex33',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge15',0,0,0,False)
### Begin command Std_Delete
App.getDocument('Unnamed').getObject('Sketch').delConstraintOnPoint(14,2)
App.getDocument('Unnamed').getObject('Sketch').delConstraintOnPoint(8,2)
App.getDocument('Unnamed').getObject('Sketch').delConstraintOnPoint(7,1)
App.getDocument('Unnamed').getObject('Sketch').delConstraintOnPoint(6,1)
App.getDocument('Unnamed').getObject('Sketch').delConstraintOnPoint(5,1)
App.getDocument('Unnamed').getObject('Sketch').delGeometries([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
App.getDocument('Unnamed').recompute()
### End command Std_Delete
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(17.109982, 66.643311, 0.000000),App.Vector(957.673950, -702.857849, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
App.getDocument('Unnamed').getObject('Sketch').movePoint(0,0,App.Vector(-410.351627,744.663925,0),1)
# Gui.runCommand('Sketcher_CreatePolyline',0)
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(547.322323,41.806076,0),App.Vector(628.268738,132.753876,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',0,2,1,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(628.268738,132.753876,0),App.Vector(681.385559,688.065796,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',1,2,2,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(681.385559,688.065796,0),App.Vector(-178.140244,982.622437,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',2,2,3,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-225.133848,845.493582,0),App.Vector(0,0,1),144.957655),1.240643,1.991794),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',3,2,4,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(-284.373869,977.793777,0),App.Vector(-366.463440,886.046509,0)),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',4,2,5,1)) 
App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-287.859685,815.716911,0),App.Vector(0,0,1),105.474180),2.411694,3.183413),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',5,2,6,1)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',6,2,0,1)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',-383.341,803.208,0.008,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,0,2,1215.233563)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',0,2,0,1,769.501160)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,0,2,1215.233563)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(7,App.Units.Quantity('1077.346300 mm'))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,1,2,280.071296)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',522.822,96.7182,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',1,1,1,2,265.022863)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,1,2,280.071296)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',1,1,1,2,265.022863)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,1,2,280.071296)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(8,App.Units.Quantity('111.363800 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,1,2,2,574.800765)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',625.4,461.866,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',2,1,2,2,557.964628)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,1,2,2,574.800765)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(9,App.Units.Quantity('550.384600 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,3,2,914.665639)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',411.757,764.439,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(10,App.Units.Quantity('833.934700 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,1,5,2,122.842074)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',-331.273,925.118,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',5,2,5,1,91.747243)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,1,5,2,122.842074)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(11,App.Units.Quantity('133.262500 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',4,176.079999)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',-194.981,1019.52,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(12,App.Units.Quantity('81.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',6,101.042490)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',-373.474,864.104,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(13,App.Units.Quantity('78.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',-229.915,956.962,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',-207.595,1005.44,0.008,False)
### Begin command Sketcher_ConstrainTangent
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',4,2,5,1))
App.getDocument('Unnamed').getObject('Sketch').delConstraintOnPoint(4,2)
### End command Sketcher_ConstrainTangent
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-199.274963, 953.552246, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 56.850915))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
# Gui.runCommand('Sketcher_CompDimensionTools',0)
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',7,113.701830)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',-142.446,955.136,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(14,App.Units.Quantity('117.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',7,3,-1,1,974.152142)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex17',-199.275,953.552,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,7,3,953.552246)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',7,3,4,3,5.166874)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex11',-204.428,953.171,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',4,3,7,3,5.152783)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(15,App.Units.Quantity('7.390500 mm'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-298.928833, 864.808411, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 59.992021))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',8,119.984042)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',-340.204,821.272,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(16,App.Units.Quantity('118.300000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,3,-1,1,909.655569)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex16',-298.909,859.143,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',6,3,-1,1,298.908745)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,3,-1,1,909.655569)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,3,8,3,5.665376)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex18',-298.929,864.808,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',6,3,8,3,5.665340)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,3,8,3,5.665376)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',6,3,8,3,5.665340)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,3,8,3,5.665376)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(17,App.Units.Quantity('5.359200 mm'))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',-373.213,835.418,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',-349.567,803.999,0.008,False)
### Begin command Sketcher_ConstrainTangent
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',6,2,0,1))
App.getDocument('Unnamed').getObject('Sketch').delConstraintOnPoint(6,2)
### End command Sketcher_ConstrainTangent
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,1,2,111.363800)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',490.082,107.641,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',1,1,1,2,35.536390)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,1,2,111.363800)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',1,1,1,2,35.536390)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Angle',1,1,0,2,2.100477)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',420.668,130.997,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(18,App.Units.Quantity('102.000000 deg'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,3,2,833.934700)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',477.833,731.001,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',3,2,3,1,757.406119)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Angle',3,1,2,2,1.895902)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',576.702,579.913,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(19,App.Units.Quantity('103.000000 deg'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').movePoint(4,3,App.Vector(-210.404068,950.015076,0),0)
# Gui.runCommand('Sketcher_ConstrainBlock',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',-145.474,964.111,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',7))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',-292.924,833.669,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',8))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').movePoint(5,0,App.Vector(6.056657,-4.111341,0),1)
# Gui.runCommand('Sketcher_ConstrainBlock',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',-404.277,912.302,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',6))
# Gui.Selection.clearSelection()
### Begin command Std_Delete
App.getDocument('Unnamed').getObject('Sketch').delConstraint(22)
App.getDocument('Unnamed').recompute()
### End command Std_Delete
# Gui.Selection.clearSelection()
### Begin command Std_Delete
App.getDocument('Unnamed').getObject('Sketch').delConstraint(20)
App.getDocument('Unnamed').recompute()
### End command Std_Delete
# Gui.Selection.clearSelection()
### Begin command Std_Delete
App.getDocument('Unnamed').getObject('Sketch').delConstraint(20)
App.getDocument('Unnamed').recompute()
### End command Std_Delete
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').movePoint(8,0,App.Vector(-284.420624,847.156738,0),0)
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-57.759956, 756.639343, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 17.322472))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(56.152020, 560.141174, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 25.133171))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(129.245544, 664.560486, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 25.822889))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-69.033283, 743.487152, 0.000000),App.Vector(34.683307, 547.073250, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('PointOnObject', 12, 1, 9))
constraintList.append(Sketcher.Constraint('Tangent', 12, 2, 10))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(78.789780, 550.884011, 0.000000),App.Vector(151.726004, 651.854168, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('PointOnObject', 13, 1, 10))
constraintList.append(Sketcher.Constraint('Tangent', 13, 2, 11))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-47.365707, 770.498418, 0.000000),App.Vector(147.132166, 689.064890, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('PointOnObject', 14, 1, 9))
constraintList.append(Sketcher.Constraint('Tangent', 14, 2, 11))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge13',-62.2738,730.771,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge10',-61.2651,739.685,0.008,False)
### Begin command Sketcher_ConstrainTangent
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',12,1,9))
App.getDocument('Unnamed').getObject('Sketch').delConstraint(20)
### End command Sketcher_ConstrainTangent
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge15',-27.9088,761.985,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge10',-61.7076,768.76,0.008,False)
### Begin command Sketcher_ConstrainTangent
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',14,1,9))
App.getDocument('Unnamed').getObject('Sketch').delConstraint(23)
### End command Sketcher_ConstrainTangent
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',12,1,12,2,222.434430)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge13',-45.4609,695.069,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',12,2,12,1,195.223159)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',12,1,12,2,222.434430)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(26,App.Units.Quantity('462.969800 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',10,261.606888)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge11',338.821,442.944,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(27,App.Units.Quantity('100.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',11,133.108797)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge12',185.805,603.579,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(28,App.Units.Quantity('100.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',9,84.201796)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge10',-75.8428,821.333,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(29,App.Units.Quantity('60.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').movePoint(11,3,App.Vector(289.374115,632.551880,0),0)
App.getDocument('Unnamed').getObject('Sketch').movePoint(10,0,App.Vector(217.234863,503.889008,0),0)
App.getDocument('Unnamed').getObject('Sketch').movePoint(13,1,App.Vector(224.561005,431.789551,0),0)
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',14,1,14,2,414.639578)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge15',155.329,759.587,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(30,App.Units.Quantity('412.955500 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',13,1,13,2,199.442612)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge14',276.912,516.899,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',13,1,13,2,170.219550)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',13,1,13,2,199.442612)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(31,App.Units.Quantity('124.431800 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').movePoint(13,1,App.Vector(239.605255,421.140808,0),0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge14',249.435,439.27,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge11',222.824,403.449,0.008,False)
### Begin command Sketcher_ConstrainTangent
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Tangent',13,1,10))
App.getDocument('Unnamed').getObject('Sketch').delConstraint(21)
### End command Sketcher_ConstrainTangent
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').movePoint(11,3,App.Vector(252.642868,604.948608,0),0)
App.getDocument('Unnamed').getObject('Sketch').movePoint(9,3,App.Vector(-87.561523,813.989868,0),0)
# Gui.runCommand('Sketcher_CompCurveEdition',0)
App.getDocument('Unnamed').getObject('Sketch').trim(9,App.Vector(-63.506153,795.462463,0))
App.getDocument('Unnamed').getObject('Sketch').trim(10,App.Vector(200.315475,515.203369,0))
App.getDocument('Unnamed').getObject('Sketch').trim(11,App.Vector(229.081024,549.722046,0))
App.getDocument('Unnamed').getObject('Sketch').movePoint(14,0,App.Vector(51.786646,-92.633956,0),1)
# Gui.runCommand('Sketcher_ConstrainBlock',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge15',80.8329,688.432,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',14))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').movePoint(12,0,App.Vector(-22.074639,-14.372369,0),1)
App.getDocument('Unnamed').getObject('Sketch').movePoint(0,0,App.Vector(-27.913521,16.173983,0),1)
App.getDocument('Unnamed').getObject('Sketch').movePoint(7,3,App.Vector(-239.936096,970.063171,0),0)
App.getDocument('Unnamed').getObject('Sketch').movePoint(8,0,App.Vector(-358.548309,872.208130,0),0)
# Gui.runCommand('Sketcher_ConstrainBlock',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',-262.842,916.686,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',7))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',-327.574,888.677,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',8))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',-355.116,798.663,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Block',0))
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
# Macro End: /Users/anish/ProBUILD_FreeCAD/comp25_16mm_plate.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
