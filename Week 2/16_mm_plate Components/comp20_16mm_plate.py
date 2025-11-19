# -*- coding: utf-8 -*-

# Macro Begin: /Users/anish/ProBUILD_FreeCAD/comp20_16mm_plate.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
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
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(2355.313232, 0.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(2355.313232, 0.000000, 0.000000),App.Vector(2355.313232, 519.210388, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(2355.313232, 519.210388, 0.000000),App.Vector(0.000000, 519.210388, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(0.000000, 519.210388, 0.000000),App.Vector(0.000000, 0.000000, 0.000000)))
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
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,1,2,2,2355.313232)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',1309.34,519.21,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',2,2,2,1,2355.313232)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(9,App.Units.Quantity('2038.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,1,2,519.210388)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',2038,121.893,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',1,1,1,2,519.210388)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(10,App.Units.Quantity('520.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateRectangles',2)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(203.857025, 350.800110, 0.000000),App.Vector(203.857025, 345.541351, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(247.679108, 301.719269, 0.000000),App.Vector(535.152405, 301.719269, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(578.974487, 345.541351, 0.000000),App.Vector(578.974487, 350.800110, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(535.152405, 394.622192, 0.000000),App.Vector(247.679108, 394.622192, 0.000000)))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(247.679108, 350.800110, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 43.822083), 1.570796, 3.141593))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(247.679108, 345.541351, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 43.822083), 3.141593, 4.712389))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(535.152405, 345.541351, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 43.822083), 4.712389, 6.283185))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(535.152405, 350.800110, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 43.822083), 0.000000, 1.570796))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(203.857025, 394.622192, 0.000000)))
constrGeoList.append(Part.Point(App.Vector(578.974487, 301.719269, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList.append(Sketcher.Constraint('Tangent', 4, 1, 8, 2))
constraintList.append(Sketcher.Constraint('Tangent', 4, 2, 9, 1))
constraintList.append(Sketcher.Constraint('Tangent', 5, 1, 9, 2))
constraintList.append(Sketcher.Constraint('Tangent', 5, 2, 10, 1))
constraintList.append(Sketcher.Constraint('Tangent', 6, 1, 10, 2))
constraintList.append(Sketcher.Constraint('Tangent', 6, 2, 11, 1))
constraintList.append(Sketcher.Constraint('Tangent', 7, 1, 11, 2))
constraintList.append(Sketcher.Constraint('Tangent', 7, 2, 8, 1))
constraintList.append(Sketcher.Constraint('Vertical', 4))
constraintList.append(Sketcher.Constraint('Vertical', 6))
constraintList.append(Sketcher.Constraint('Horizontal', 5))
constraintList.append(Sketcher.Constraint('Horizontal', 7))
constraintList.append(Sketcher.Constraint('Equal', 8, 9))
constraintList.append(Sketcher.Constraint('Equal', 9, 10))
constraintList.append(Sketcher.Constraint('Equal', 10, 11))
constraintList.append(Sketcher.Constraint('PointOnObject', 12, 1, 4))
constraintList.append(Sketcher.Constraint('PointOnObject', 12, 1, 7))
constraintList.append(Sketcher.Constraint('PointOnObject', 13, 1, 5))
constraintList.append(Sketcher.Constraint('PointOnObject', 13, 1, 6))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(209.115692, 151.068666, 0.000000),App.Vector(209.115692, 129.838965, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(249.334502, 89.620155, 0.000000),App.Vector(584.330751, 89.620155, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(624.549561, 129.838965, 0.000000),App.Vector(624.549561, 151.068666, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(584.330751, 191.287476, 0.000000),App.Vector(249.334502, 191.287476, 0.000000)))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(249.334502, 151.068666, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 40.218810), 1.570796, 3.141593))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(249.334502, 129.838965, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 40.218810), 3.141593, 4.712389))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(584.330751, 129.838965, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 40.218810), 4.712389, 6.283185))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(584.330751, 151.068666, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 40.218810), 0.000000, 1.570796))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(209.115692, 191.287476, 0.000000)))
constrGeoList.append(Part.Point(App.Vector(624.549561, 89.620155, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList.append(Sketcher.Constraint('Tangent', 14, 1, 18, 2))
constraintList.append(Sketcher.Constraint('Tangent', 14, 2, 19, 1))
constraintList.append(Sketcher.Constraint('Tangent', 15, 1, 19, 2))
constraintList.append(Sketcher.Constraint('Tangent', 15, 2, 20, 1))
constraintList.append(Sketcher.Constraint('Tangent', 16, 1, 20, 2))
constraintList.append(Sketcher.Constraint('Tangent', 16, 2, 21, 1))
constraintList.append(Sketcher.Constraint('Tangent', 17, 1, 21, 2))
constraintList.append(Sketcher.Constraint('Tangent', 17, 2, 18, 1))
constraintList.append(Sketcher.Constraint('Vertical', 14))
constraintList.append(Sketcher.Constraint('Vertical', 16))
constraintList.append(Sketcher.Constraint('Horizontal', 15))
constraintList.append(Sketcher.Constraint('Horizontal', 17))
constraintList.append(Sketcher.Constraint('Equal', 18, 19))
constraintList.append(Sketcher.Constraint('Equal', 19, 20))
constraintList.append(Sketcher.Constraint('Equal', 20, 21))
constraintList.append(Sketcher.Constraint('PointOnObject', 22, 1, 14))
constraintList.append(Sketcher.Constraint('PointOnObject', 22, 1, 17))
constraintList.append(Sketcher.Constraint('PointOnObject', 23, 1, 15))
constraintList.append(Sketcher.Constraint('PointOnObject', 23, 1, 16))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(1456.247070, 333.586301, 0.000000),App.Vector(1456.247070, 333.469149, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1514.764559, 274.951660, 0.000000),App.Vector(1847.593473, 274.951660, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1906.110962, 333.469149, 0.000000),App.Vector(1906.110962, 333.586301, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1847.593473, 392.103790, 0.000000),App.Vector(1514.764559, 392.103790, 0.000000)))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1514.764559, 333.586301, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 58.517489), 1.570796, 3.141593))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1514.764559, 333.469149, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 58.517489), 3.141593, 4.712389))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1847.593473, 333.469149, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 58.517489), 4.712389, 6.283185))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1847.593473, 333.586301, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 58.517489), 0.000000, 1.570796))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(1456.247070, 392.103790, 0.000000)))
constrGeoList.append(Part.Point(App.Vector(1906.110962, 274.951660, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList.append(Sketcher.Constraint('Tangent', 24, 1, 28, 2))
constraintList.append(Sketcher.Constraint('Tangent', 24, 2, 29, 1))
constraintList.append(Sketcher.Constraint('Tangent', 25, 1, 29, 2))
constraintList.append(Sketcher.Constraint('Tangent', 25, 2, 30, 1))
constraintList.append(Sketcher.Constraint('Tangent', 26, 1, 30, 2))
constraintList.append(Sketcher.Constraint('Tangent', 26, 2, 31, 1))
constraintList.append(Sketcher.Constraint('Tangent', 27, 1, 31, 2))
constraintList.append(Sketcher.Constraint('Tangent', 27, 2, 28, 1))
constraintList.append(Sketcher.Constraint('Vertical', 24))
constraintList.append(Sketcher.Constraint('Vertical', 26))
constraintList.append(Sketcher.Constraint('Horizontal', 25))
constraintList.append(Sketcher.Constraint('Horizontal', 27))
constraintList.append(Sketcher.Constraint('Equal', 28, 29))
constraintList.append(Sketcher.Constraint('Equal', 29, 30))
constraintList.append(Sketcher.Constraint('Equal', 30, 31))
constraintList.append(Sketcher.Constraint('PointOnObject', 32, 1, 24))
constraintList.append(Sketcher.Constraint('PointOnObject', 32, 1, 27))
constraintList.append(Sketcher.Constraint('PointOnObject', 33, 1, 25))
constraintList.append(Sketcher.Constraint('PointOnObject', 33, 1, 26))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(1456.247070, 92.245942, 0.000000),App.Vector(1456.247070, 92.142848, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1507.742431, 40.647488, 0.000000),App.Vector(1873.359986, 40.647488, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1924.855347, 92.142848, 0.000000),App.Vector(1924.855347, 92.245942, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1873.359986, 143.741302, 0.000000),App.Vector(1507.742431, 143.741302, 0.000000)))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1507.742431, 92.245942, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 51.495361), 1.570796, 3.141593))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1507.742431, 92.142848, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 51.495361), 3.141593, 4.712389))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1873.359986, 92.142848, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 51.495361), 4.712389, 6.283185))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1873.359986, 92.245942, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 51.495361), 0.000000, 1.570796))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(1456.247070, 143.741302, 0.000000)))
constrGeoList.append(Part.Point(App.Vector(1924.855347, 40.647488, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList.append(Sketcher.Constraint('Tangent', 34, 1, 38, 2))
constraintList.append(Sketcher.Constraint('Tangent', 34, 2, 39, 1))
constraintList.append(Sketcher.Constraint('Tangent', 35, 1, 39, 2))
constraintList.append(Sketcher.Constraint('Tangent', 35, 2, 40, 1))
constraintList.append(Sketcher.Constraint('Tangent', 36, 1, 40, 2))
constraintList.append(Sketcher.Constraint('Tangent', 36, 2, 41, 1))
constraintList.append(Sketcher.Constraint('Tangent', 37, 1, 41, 2))
constraintList.append(Sketcher.Constraint('Tangent', 37, 2, 38, 1))
constraintList.append(Sketcher.Constraint('Vertical', 34))
constraintList.append(Sketcher.Constraint('Vertical', 36))
constraintList.append(Sketcher.Constraint('Horizontal', 35))
constraintList.append(Sketcher.Constraint('Horizontal', 37))
constraintList.append(Sketcher.Constraint('Equal', 38, 39))
constraintList.append(Sketcher.Constraint('Equal', 39, 40))
constraintList.append(Sketcher.Constraint('Equal', 40, 41))
constraintList.append(Sketcher.Constraint('PointOnObject', 42, 1, 34))
constraintList.append(Sketcher.Constraint('PointOnObject', 42, 1, 37))
constraintList.append(Sketcher.Constraint('PointOnObject', 43, 1, 35))
constraintList.append(Sketcher.Constraint('PointOnObject', 43, 1, 36))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
# Gui.runCommand('Sketcher_CompCreateRectangles',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(793.762146, 252.807617, 0.000000),App.Vector(793.762146, 229.921860, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(793.762146, 229.921860, 0.000000),App.Vector(1331.577881, 229.921860, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1331.577881, 229.921860, 0.000000),App.Vector(1331.577881, 252.807617, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1331.577881, 252.807617, 0.000000),App.Vector(793.762146, 252.807617, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 44, 2, 45, 1))
constraintList.append(Sketcher.Constraint('Coincident', 45, 2, 46, 1))
constraintList.append(Sketcher.Constraint('Coincident', 46, 2, 47, 1))
constraintList.append(Sketcher.Constraint('Coincident', 47, 2, 44, 1))
constraintList.append(Sketcher.Constraint('Vertical', 44))
constraintList.append(Sketcher.Constraint('Vertical', 46))
constraintList.append(Sketcher.Constraint('Horizontal', 45))
constraintList.append(Sketcher.Constraint('Horizontal', 47))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',7,1,7,2,287.473297)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',358.71,394.622,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',7,2,7,1,287.473297)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(95,App.Units.Quantity('216.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',7,1,7,2,287.473297)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',391.416,394.622,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',7,2,7,1,287.473297)) 
# Gui.runCommand('Std_Undo',0)
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Sketcher_CompCreateRectangles',2)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(152.575027, 346.867795, 0.000000),App.Vector(152.575027, 346.761051, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(205.893726, 293.442352, 0.000000),App.Vector(557.860562, 293.442352, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(611.179260, 346.761051, 0.000000),App.Vector(611.179260, 346.867795, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(557.860562, 400.186493, 0.000000),App.Vector(205.893726, 400.186493, 0.000000)))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(205.893726, 346.867795, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 53.318698), 1.570796, 3.141593))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(205.893726, 346.761051, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 53.318698), 3.141593, 4.712389))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(557.860562, 346.761051, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 53.318698), 4.712389, 6.283185))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(557.860562, 346.867795, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 53.318698), 0.000000, 1.570796))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(152.575027, 400.186493, 0.000000)))
constrGeoList.append(Part.Point(App.Vector(611.179260, 293.442352, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList.append(Sketcher.Constraint('Tangent', 4, 1, 8, 2))
constraintList.append(Sketcher.Constraint('Tangent', 4, 2, 9, 1))
constraintList.append(Sketcher.Constraint('Tangent', 5, 1, 9, 2))
constraintList.append(Sketcher.Constraint('Tangent', 5, 2, 10, 1))
constraintList.append(Sketcher.Constraint('Tangent', 6, 1, 10, 2))
constraintList.append(Sketcher.Constraint('Tangent', 6, 2, 11, 1))
constraintList.append(Sketcher.Constraint('Tangent', 7, 1, 11, 2))
constraintList.append(Sketcher.Constraint('Tangent', 7, 2, 8, 1))
constraintList.append(Sketcher.Constraint('Vertical', 4))
constraintList.append(Sketcher.Constraint('Vertical', 6))
constraintList.append(Sketcher.Constraint('Horizontal', 5))
constraintList.append(Sketcher.Constraint('Horizontal', 7))
constraintList.append(Sketcher.Constraint('Equal', 8, 9))
constraintList.append(Sketcher.Constraint('Equal', 9, 10))
constraintList.append(Sketcher.Constraint('Equal', 10, 11))
constraintList.append(Sketcher.Constraint('PointOnObject', 12, 1, 4))
constraintList.append(Sketcher.Constraint('PointOnObject', 12, 1, 7))
constraintList.append(Sketcher.Constraint('PointOnObject', 13, 1, 5))
constraintList.append(Sketcher.Constraint('PointOnObject', 13, 1, 6))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
# Gui.runCommand('Sketcher_CompCreateRectangles',2)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(1406.346191, 361.096620, 0.000000),App.Vector(1406.346191, 360.995787, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1456.712340, 310.629639, 0.000000),App.Vector(1748.509462, 310.629639, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1798.875610, 360.995787, 0.000000),App.Vector(1798.875610, 361.096620, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1748.509462, 411.462769, 0.000000),App.Vector(1456.712340, 411.462769, 0.000000)))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1456.712340, 361.096620, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 50.366148), 1.570796, 3.141593))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1456.712340, 360.995787, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 50.366148), 3.141593, 4.712389))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1748.509462, 360.995787, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 50.366148), 4.712389, 6.283185))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1748.509462, 361.096620, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 50.366148), 0.000000, 1.570796))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(1406.346191, 411.462769, 0.000000)))
constrGeoList.append(Part.Point(App.Vector(1798.875610, 310.629639, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList.append(Sketcher.Constraint('Tangent', 14, 1, 18, 2))
constraintList.append(Sketcher.Constraint('Tangent', 14, 2, 19, 1))
constraintList.append(Sketcher.Constraint('Tangent', 15, 1, 19, 2))
constraintList.append(Sketcher.Constraint('Tangent', 15, 2, 20, 1))
constraintList.append(Sketcher.Constraint('Tangent', 16, 1, 20, 2))
constraintList.append(Sketcher.Constraint('Tangent', 16, 2, 21, 1))
constraintList.append(Sketcher.Constraint('Tangent', 17, 1, 21, 2))
constraintList.append(Sketcher.Constraint('Tangent', 17, 2, 18, 1))
constraintList.append(Sketcher.Constraint('Vertical', 14))
constraintList.append(Sketcher.Constraint('Vertical', 16))
constraintList.append(Sketcher.Constraint('Horizontal', 15))
constraintList.append(Sketcher.Constraint('Horizontal', 17))
constraintList.append(Sketcher.Constraint('Equal', 18, 19))
constraintList.append(Sketcher.Constraint('Equal', 19, 20))
constraintList.append(Sketcher.Constraint('Equal', 20, 21))
constraintList.append(Sketcher.Constraint('PointOnObject', 22, 1, 14))
constraintList.append(Sketcher.Constraint('PointOnObject', 22, 1, 17))
constraintList.append(Sketcher.Constraint('PointOnObject', 23, 1, 15))
constraintList.append(Sketcher.Constraint('PointOnObject', 23, 1, 16))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(1424.352051, 128.869991, 0.000000),App.Vector(1424.352051, 114.264302, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1465.665288, 72.951065, 0.000000),App.Vector(1775.568233, 72.951065, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1816.881470, 114.264302, 0.000000),App.Vector(1816.881470, 128.869991, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1775.568233, 170.183228, 0.000000),App.Vector(1465.665288, 170.183228, 0.000000)))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1465.665288, 128.869991, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 41.313237), 1.570796, 3.141593))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1465.665288, 114.264302, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 41.313237), 3.141593, 4.712389))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1775.568233, 114.264302, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 41.313237), 4.712389, 6.283185))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1775.568233, 128.869991, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 41.313237), 0.000000, 1.570796))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(1424.352051, 170.183228, 0.000000)))
constrGeoList.append(Part.Point(App.Vector(1816.881470, 72.951065, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList.append(Sketcher.Constraint('Tangent', 24, 1, 28, 2))
constraintList.append(Sketcher.Constraint('Tangent', 24, 2, 29, 1))
constraintList.append(Sketcher.Constraint('Tangent', 25, 1, 29, 2))
constraintList.append(Sketcher.Constraint('Tangent', 25, 2, 30, 1))
constraintList.append(Sketcher.Constraint('Tangent', 26, 1, 30, 2))
constraintList.append(Sketcher.Constraint('Tangent', 26, 2, 31, 1))
constraintList.append(Sketcher.Constraint('Tangent', 27, 1, 31, 2))
constraintList.append(Sketcher.Constraint('Tangent', 27, 2, 28, 1))
constraintList.append(Sketcher.Constraint('Vertical', 24))
constraintList.append(Sketcher.Constraint('Vertical', 26))
constraintList.append(Sketcher.Constraint('Horizontal', 25))
constraintList.append(Sketcher.Constraint('Horizontal', 27))
constraintList.append(Sketcher.Constraint('Equal', 28, 29))
constraintList.append(Sketcher.Constraint('Equal', 29, 30))
constraintList.append(Sketcher.Constraint('Equal', 30, 31))
constraintList.append(Sketcher.Constraint('PointOnObject', 32, 1, 24))
constraintList.append(Sketcher.Constraint('PointOnObject', 32, 1, 27))
constraintList.append(Sketcher.Constraint('PointOnObject', 33, 1, 25))
constraintList.append(Sketcher.Constraint('PointOnObject', 33, 1, 26))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(189.144150, 105.412204, 0.000000),App.Vector(189.144150, 105.311371, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(239.510388, 54.945133, 0.000000),App.Vector(635.741977, 54.945133, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(686.108215, 105.311371, 0.000000),App.Vector(686.108215, 105.412204, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(635.741977, 155.778442, 0.000000),App.Vector(239.510388, 155.778442, 0.000000)))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(239.510388, 105.412204, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 50.366238), 1.570796, 3.141593))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(239.510388, 105.311371, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 50.366238), 3.141593, 4.712389))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(635.741977, 105.311371, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 50.366238), 4.712389, 6.283185))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(635.741977, 105.412204, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 50.366238), 0.000000, 1.570796))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(189.144150, 155.778442, 0.000000)))
constrGeoList.append(Part.Point(App.Vector(686.108215, 54.945133, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList.append(Sketcher.Constraint('Tangent', 34, 1, 38, 2))
constraintList.append(Sketcher.Constraint('Tangent', 34, 2, 39, 1))
constraintList.append(Sketcher.Constraint('Tangent', 35, 1, 39, 2))
constraintList.append(Sketcher.Constraint('Tangent', 35, 2, 40, 1))
constraintList.append(Sketcher.Constraint('Tangent', 36, 1, 40, 2))
constraintList.append(Sketcher.Constraint('Tangent', 36, 2, 41, 1))
constraintList.append(Sketcher.Constraint('Tangent', 37, 1, 41, 2))
constraintList.append(Sketcher.Constraint('Tangent', 37, 2, 38, 1))
constraintList.append(Sketcher.Constraint('Vertical', 34))
constraintList.append(Sketcher.Constraint('Vertical', 36))
constraintList.append(Sketcher.Constraint('Horizontal', 35))
constraintList.append(Sketcher.Constraint('Horizontal', 37))
constraintList.append(Sketcher.Constraint('Equal', 38, 39))
constraintList.append(Sketcher.Constraint('Equal', 39, 40))
constraintList.append(Sketcher.Constraint('Equal', 40, 41))
constraintList.append(Sketcher.Constraint('PointOnObject', 42, 1, 34))
constraintList.append(Sketcher.Constraint('PointOnObject', 42, 1, 37))
constraintList.append(Sketcher.Constraint('PointOnObject', 43, 1, 35))
constraintList.append(Sketcher.Constraint('PointOnObject', 43, 1, 36))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',7,1,7,2,351.966819)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',318.787,400.186,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',7,2,7,1,351.966819)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(87,App.Units.Quantity('216.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',8,69.698111)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',197.518,373.453,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(88,App.Units.Quantity('50.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,1,-1,1,612.023666)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex13',514.018,332.202,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,6,1,332.202460)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,1,-1,1,612.023666)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,6,1,332.202460)) 
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,1,6,2,2.882369)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',514.018,333.258,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',6,1,6,2,2.882369)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(89,App.Units.Quantity('27.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex9',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex10',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge5',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex11',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex12',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex13',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex14',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex15',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex16',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex17',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex18',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex19',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex20',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex21',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex22',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge10',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex23',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex24',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex25',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge11',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex26',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex27',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex28',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge12',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex29',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex30',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex31',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex32',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge15',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex33',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex34',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge16',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex35',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex36',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge17',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex37',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex38',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge18',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex39',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex40',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex41',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge19',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex42',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex43',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex44',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge20',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex45',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex46',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex47',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge21',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex48',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex49',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex50',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge22',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex51',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex52',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex53',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex54',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge25',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex55',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex56',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge26',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex57',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex58',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge27',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex59',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex60',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge28',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex61',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex62',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex63',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge29',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex64',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex65',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex66',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge30',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex67',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex68',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex69',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge31',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex70',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex71',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex72',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge32',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex73',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex74',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex75',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex76',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge35',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex77',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex78',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge36',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex79',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex80',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge37',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex81',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex82',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge38',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex83',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex84',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex85',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge39',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex86',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex87',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex88',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge40',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex89',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex90',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex91',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge41',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex92',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex93',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex94',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge42',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex95',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex96',0,0,0,False)
# Gui.runCommand('Sketcher_ConstrainEqual',0)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',394.441,396.662,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge38',373.003,155.778,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge18',1661.65,411.463,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge28',1554.46,170.183,0.008,False)
### Begin command Sketcher_ConstrainEqual
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',7,37))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',37,17))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',17,27))
### End command Sketcher_ConstrainEqual
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',224.617,390.478,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge19',1439.56,409.172,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge30',1337.01,166.749,0.008,False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge9',228.847,392.55,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge39',295.437,204.741,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge19',1448.26,413.433,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge30',1317.17,126.563,0.008,False)
### Begin command Sketcher_ConstrainEqual
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',8,38))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',38,18))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',18,29))
### End command Sketcher_ConstrainEqual
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',514.724,332.795,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge15',1420.98,351.025,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge37',623.099,80.0942,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge25',1420.32,97.012,0.008,False)
### Begin command Sketcher_ConstrainEqual
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',6,14))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',14,36))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',36,24))
### End command Sketcher_ConstrainEqual
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex53',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex54',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge25',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex55',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex56',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge26',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex57',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex58',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge27',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex59',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex60',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge28',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex61',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex62',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex63',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge29',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex64',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex65',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex66',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge30',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex67',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex68',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex69',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge31',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex70',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex71',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex72',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge32',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex73',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex74',0,0,0,False)
### Begin command Std_Delete
App.getDocument('Unnamed').getObject('Sketch').delGeometries([24,25,26,27,28,29,30,31,32,33])
App.getDocument('Unnamed').recompute()
### End command Std_Delete
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateRectangles',2)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(1439.325317, 118.437858, 0.000000),App.Vector(1439.325317, 101.224209, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1503.097573, 37.451954, 0.000000),App.Vector(1711.765465, 37.451954, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1775.537720, 101.224209, 0.000000),App.Vector(1775.537720, 118.437858, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1711.765465, 182.210114, 0.000000),App.Vector(1503.097573, 182.210114, 0.000000)))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1503.097573, 118.437858, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 63.772255), 1.570796, 3.141593))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1503.097573, 101.224209, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 63.772255), 3.141593, 4.712389))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1711.765465, 101.224209, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 63.772255), 4.712389, 6.283185))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(1711.765465, 118.437858, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 63.772255), 0.000000, 1.570796))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(1439.325317, 182.210114, 0.000000)))
constrGeoList.append(Part.Point(App.Vector(1775.537720, 37.451954, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList.append(Sketcher.Constraint('Tangent', 34, 1, 38, 2))
constraintList.append(Sketcher.Constraint('Tangent', 34, 2, 39, 1))
constraintList.append(Sketcher.Constraint('Tangent', 35, 1, 39, 2))
constraintList.append(Sketcher.Constraint('Tangent', 35, 2, 40, 1))
constraintList.append(Sketcher.Constraint('Tangent', 36, 1, 40, 2))
constraintList.append(Sketcher.Constraint('Tangent', 36, 2, 41, 1))
constraintList.append(Sketcher.Constraint('Tangent', 37, 1, 41, 2))
constraintList.append(Sketcher.Constraint('Tangent', 37, 2, 38, 1))
constraintList.append(Sketcher.Constraint('Vertical', 34))
constraintList.append(Sketcher.Constraint('Vertical', 36))
constraintList.append(Sketcher.Constraint('Horizontal', 35))
constraintList.append(Sketcher.Constraint('Horizontal', 37))
constraintList.append(Sketcher.Constraint('Equal', 38, 39))
constraintList.append(Sketcher.Constraint('Equal', 39, 40))
constraintList.append(Sketcher.Constraint('Equal', 40, 41))
constraintList.append(Sketcher.Constraint('PointOnObject', 42, 1, 34))
constraintList.append(Sketcher.Constraint('PointOnObject', 42, 1, 37))
constraintList.append(Sketcher.Constraint('PointOnObject', 43, 1, 35))
constraintList.append(Sketcher.Constraint('PointOnObject', 43, 1, 36))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',320.952,396.454,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge38',1619.11,182.21,0.008,False)
### Begin command Sketcher_ConstrainEqual
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',7,37))
### End command Sketcher_ConstrainEqual
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',514.724,329.238,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge35',1439.32,108.452,0.008,False)
### Begin command Sketcher_ConstrainEqual
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',6,34))
### End command Sketcher_ConstrainEqual
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge12',495.369,385.994,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge39',1468.92,176.075,0.008,False)
### Begin command Sketcher_ConstrainEqual
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',11,38))
### End command Sketcher_ConstrainEqual
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',29,3,-1,1,366.030494)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex66',357.109,80.3197,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',-1,1,29,3,357.109324)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',29,3,-1,1,366.030494)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',29,3,3,357.109324)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',0,79.8089,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(99,App.Units.Quantity('409.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',29,3,-1,1,416.812016)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex66',409,80.3197,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,29,3,80.319713)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',29,3,-1,1,416.812016)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',29,3,0,80.319713)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',440.608,0,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(100,App.Units.Quantity('25.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',16,2,-1,1,1775.323878)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex36',1736.98,366.987,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',-1,1,16,2,366.987473)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',16,2,-1,1,1775.323878)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',16,2,1,301.021282)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',2038,380.912,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(100,App.Units.Quantity('359.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',16,2,-1,1,1718.638304)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex36',1679,366.983,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',16,2,2,153.016868)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',1696.02,520,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(101,App.Units.Quantity('125.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',14,1,14,2,27.000000)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge15',1363,378.595,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',14,2,14,1,27.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',14,1,14,2,27.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,1,14,848.276880)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',514.723,332.99,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(102,App.Units.Quantity('688.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',7,1,7,2,216.000000)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge8',492.505,396.486,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',7,2,7,1,216.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,1,7,127.000000)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',475.719,269.486,0)
# Gui.Selection.clearSelection()
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,2,-1,1,758.734309)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex14',675,346.486,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,2,2,173.513706)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',690.755,520,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(103,App.Units.Quantity('125.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex25',625,368,0.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex72',625,107.32,0.014,False)
### Begin command Sketcher_ConstrainVertical
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',10,3,31,3))
### End command Sketcher_ConstrainVertical
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex74',675,30.3199,0.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex30',675,318,0.014,False)
### Begin command Sketcher_ConstrainVertical
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',33,1,13,1))
### End command Sketcher_ConstrainVertical
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',34,2,-1,1,1452.152978)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex76',1449.03,95.2404,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',34,2,0,95.240446)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',1373.86,0,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(104,App.Units.Quantity('129.014600 mm'))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex73',359,157.32,0.014,False)
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_ConstrainHorizontal',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex73',359,157.32,0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex95',1449.02,206.015,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',32,1,42,1))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_ConstrainVertical',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex52',1679,318,0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex96',1765.02,79.0146,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',23,1,43,1))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateRegularPolygon',0)
# Gui.runCommand('Sketcher_CompCreateRectangles',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(823.814514, 286.582977, 0.000000),App.Vector(823.814514, 261.241241, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(823.814514, 261.241241, 0.000000),App.Vector(1173.772339, 261.241241, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1173.772339, 261.241241, 0.000000),App.Vector(1173.772339, 286.582977, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(1173.772339, 286.582977, 0.000000),App.Vector(823.814514, 286.582977, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 44, 2, 45, 1))
constraintList.append(Sketcher.Constraint('Coincident', 45, 2, 46, 1))
constraintList.append(Sketcher.Constraint('Coincident', 46, 2, 47, 1))
constraintList.append(Sketcher.Constraint('Coincident', 47, 2, 44, 1))
constraintList.append(Sketcher.Constraint('Vertical', 44))
constraintList.append(Sketcher.Constraint('Vertical', 46))
constraintList.append(Sketcher.Constraint('Horizontal', 45))
constraintList.append(Sketcher.Constraint('Horizontal', 47))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',44,1,44,2,25.341736)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge45',823.815,272.102,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',44,2,44,1,25.341736)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',44,1,44,2,25.341736)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(115,App.Units.Quantity('24.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',47,1,47,2,349.957825)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge48',960.177,285.524,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',47,2,47,1,349.957825)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(116,App.Units.Quantity('216.000000 mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',44,1,44,2,24.000000)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge45',921.72,273.524,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',44,2,44,1,24.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',44,1,44,2,24.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,44,921.719933)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',0,229.914,0)
App.getDocument('Unnamed').getObject('Sketch').setDatum(117,App.Units.Quantity('911.000000 mm'))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_ConstrainSymmetric',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex97',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex98',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge45',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex99',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex100',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge46',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex101',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex102',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge47',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex103',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex104',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge48',0,0,0,False)
# Gui.runCommand('Sketcher_ConstrainSymmetric',0)
App.ActiveDocument.recompute()
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.')
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
# tv = ActiveSketch.ViewObject.TempoVis
# if tv:
#   tv.restore()
# ActiveSketch.ViewObject.TempoVis = None
# del(tv)
# del(ActiveSketch)
# 
# Gui.Selection.clearSelection()
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
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex97',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex98',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge45',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex99',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex100',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge46',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex101',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex102',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge47',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex103',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex104',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge48',0,0,0,False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex97',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex98',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge45',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex99',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex100',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge46',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex101',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex102',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge47',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex103',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex104',0,0,0,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge48',0,0,0,False)
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(1019.000000, 520.000000, 0.000000),App.Vector(1019.000000, 285.524084, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Symmetric', 2, 1, 2, 2, 48, 1))
constraintList.append(Sketcher.Constraint('Symmetric', 47, 1, 47, 2, 48, 2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(1019.000000, 261.524084, 0.000000),App.Vector(1019.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Symmetric', 45, 1, 45, 2, 49, 1))
constraintList.append(Sketcher.Constraint('Symmetric', 0, 1, 0, 2, 49, 2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge49',1019,351.001,0.008,False)
### Begin command Sketcher_ToggleConstruction
App.getDocument('Unnamed').getObject('Sketch').toggleConstruction(48) 
### End command Sketcher_ToggleConstruction
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge50',1019,118.204,0.008,False)
### Begin command Sketcher_ToggleConstruction
App.getDocument('Unnamed').getObject('Sketch').toggleConstruction(49) 
### End command Sketcher_ToggleConstruction
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_ConstrainEqual',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge49',1019,446.169,0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge50',1019,200.195,0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',48,49))
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
# Macro End: /Users/anish/ProBUILD_FreeCAD/comp20_16mm_plate.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
