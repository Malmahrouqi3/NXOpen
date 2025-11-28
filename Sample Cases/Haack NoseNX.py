##----------------------------------------------------------------------
file1 = 'Haack'

import os
# Get the current directory (where your Python code is)
file_dir = os.getcwd()
file_path = os.path.join(file_dir, file1)

filename = file_path
#filenames should include the directory without including the extension (.txt), yet they are a txt file
DG = 3          #Spline Degree
n = 50    #how many datapoints are provided

def main(IN,DG, n): 
        import math
        import NXOpen
        import NXOpen.Features
        import NXOpen.GeometricUtilities#IN is the points name
        #VAL is an array with x,y,z values
        #DG is the spline degrees to control the path 
        Spline_Degress = DG
        theSession  = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work
        displayPart = theSession.Parts.Display
        # ----------------------------------------------
        #   Menu: Insert->Curve->Studio Spline...
        # ----------------------------------------------
        markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
        studioSplineBuilderEx1 = workPart.Features.CreateStudioSplineBuilderEx(NXOpen.NXObject.Null)
        origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
        normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
        plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
        studioSplineBuilderEx1.DrawingPlane = plane1
        unit1 = studioSplineBuilderEx1.Extender.StartValue.Units
        expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
        expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
        origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
        normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
        plane2 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
        studioSplineBuilderEx1.MovementPlane = plane2
        expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
        expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
        studioSplineBuilderEx1.OrientExpress.ReferenceOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Reference.WcsDisplayPart
        studioSplineBuilderEx1.MovementMethod = NXOpen.Features.StudioSplineBuilderEx.MovementMethodType.WCS
        studioSplineBuilderEx1.OrientExpress.AxisOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Axis.Passive
        studioSplineBuilderEx1.OrientExpress.PlaneOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Plane.Passive
        studioSplineBuilderEx1.OrientExpress.AxisOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Axis.X
        studioSplineBuilderEx1.Extender.StartValue.SetFormula("0")
        studioSplineBuilderEx1.Extender.EndValue.SetFormula("0")
        studioSplineBuilderEx1.InputCurveOption = NXOpen.Features.StudioSplineBuilderEx.InputCurveOptions.Hide
        theSession.SetUndoMarkName(markId1, "Studio Spline Dialog")
        studioSplineBuilderEx1.MatchKnotsType = NXOpen.Features.StudioSplineBuilderEx.MatchKnotsTypes.NotSet
        studioSplineBuilderEx1.OrientExpress.AxisOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Axis.Passive
        studioSplineBuilderEx1.OrientExpress.AxisOption = NXOpen.GeometricUtilities.OrientXpressBuilder.Axis.X
        markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        theSession.DeleteUndoMark(markId2, None)
        markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        studioSplineBuilderEx1.Degree = Spline_Degress
        theSession.SetUndoMarkName(markId3, "Studio Spline - Degree")
        theSession.SetUndoMarkVisibility(markId3, None, NXOpen.Session.MarkVisibility.Visible)
        theSession.SetUndoMarkVisibility(markId1, None, NXOpen.Session.MarkVisibility.Invisible)
        markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        studioSplineBuilderEx1.Degree = Spline_Degress
        theSession.SetUndoMarkName(markId4, "Studio Spline - Degree")
        theSession.SetUndoMarkVisibility(markId4, None, NXOpen.Session.MarkVisibility.Visible)
        theSession.SetUndoMarkVisibility(markId1, None, NXOpen.Session.MarkVisibility.Invisible)
        markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        theSession.DeleteUndoMark(markId5, None)
        markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        theSession.DeleteUndoMark(markId6, None)
        markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
        # ----------------------------------------------
        #   Dialog Begin Point
        # ----------------------------------------------
        #Upper Surface
        for i in IN[:n]:
            expression24 = workPart.Expressions.FindObject(i)
            point2 = workPart.Points.CreatePoint(expression24, NXOpen.SmartObject.UpdateOption.WithinModeling)
            workPart.MeasureManager.SetPartTransientModification()
            workPart.MeasureManager.ClearPartTransientModification()
            geometricConstraintData1 = studioSplineBuilderEx1.ConstraintManager.CreateGeometricConstraintData()
            geometricConstraintData1.Point = point2
            studioSplineBuilderEx1.ConstraintManager.Append(geometricConstraintData1)
            studioSplineBuilderEx1.Evaluate()
            theSession.SetUndoMarkName(markId7, "Studio Spline - Selection")
            theSession.SetUndoMarkVisibility(markId7, None, NXOpen.Session.MarkVisibility.Visible)
            theSession.SetUndoMarkVisibility(markId1, None, NXOpen.Session.MarkVisibility.Invisible)
            markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")            
            
        # ----------------------------------------------
        #   Closing spline
        # ----------------------------------------------
        studioSplineBuilderEx1.Evaluate()
        theSession.SetUndoMarkVisibility(markId1, None, NXOpen.Session.MarkVisibility.Invisible)
        markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        theSession.DeleteUndoMark(markId20, None)
        markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        nXObject1 = studioSplineBuilderEx1.Commit()
        theSession.DeleteUndoMark(markId21, None)
        theSession.SetUndoMarkName(markId1, "Studio Spline")
        studioSplineBuilderEx1.Destroy()
        try:
            # Expression is still in use.
            workPart.Expressions.Delete(expression2)
        except NXOpen.NXException as ex:
            ex.AssertErrorCode(1050029)
        try:
            # Expression is still in use.
            workPart.Expressions.Delete(expression4)
        except NXOpen.NXException as ex:
            ex.AssertErrorCode(1050029)
        try:
            # Expression is still in use.
            workPart.Expressions.Delete(expression1)
        except NXOpen.NXException as ex:
            ex.AssertErrorCode(1050029)
        try:
            # Expression is still in use.
            workPart.Expressions.Delete(expression3)
        except NXOpen.NXException as ex:
            ex.AssertErrorCode(1050029)
        theSession.SetUndoMarkVisibility(markId1, None, NXOpen.Session.MarkVisibility.Visible)
        theSession.DeleteUndoMark(markId11, None)
        theSession.DeleteUndoMark(markId7, None)
        theSession.DeleteUndoMark(markId4, None)
        theSession.DeleteUndoMark(markId3, None)
##---------------------------------------------------------------------------------------------------
def Revolve(run) : 
    import math
    import NXOpen
    import NXOpen.Features
    import NXOpen.GeometricUtilities
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    ## Revolve Feature
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    revolveBuilder1 = workPart.Features.CreateRevolveBuilder(NXOpen.Features.Feature.Null)
    revolveBuilder1.Limits.StartExtend.Value.SetFormula("0")
    revolveBuilder1.Limits.EndExtend.Value.SetFormula("360")
    revolveBuilder1.Limits.StartExtend.Value.SetFormula("0")
    revolveBuilder1.Limits.EndExtend.Value.SetFormula("360")
    revolveBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    revolveBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    revolveBuilder1.Offset.StartOffset.SetFormula("0")
    revolveBuilder1.Offset.EndOffset.SetFormula("5")
    revolveBuilder1.Tolerance = 0.01
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    revolveBuilder1.Section = section1
    smartVolumeProfileBuilder1 = revolveBuilder1.SmartVolumeProfile
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    theSession.SetUndoMarkName(markId1, "Revolve Dialog")
    section1.DistanceTolerance = 0.01
    section1.ChainingTolerance = 0.0094999999999999998
    starthelperpoint1 = [None] * 3 
    starthelperpoint1[0] = 0.0
    starthelperpoint1[1] = 0.0
    starthelperpoint1[2] = 0.0
    revolveBuilder1.SetStartLimitHelperPoint(starthelperpoint1)
    endhelperpoint1 = [None] * 3 
    endhelperpoint1[0] = 0.0
    endhelperpoint1[1] = 0.0
    endhelperpoint1[2] = 0.0
    revolveBuilder1.SetEndLimitHelperPoint(endhelperpoint1)
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    selectionIntentRuleOptions1 = workPart.ScRuleFactory.CreateRuleOptions()
    selectionIntentRuleOptions1.SetSelectedFromInactive(False)
    features1 = [NXOpen.Features.Feature.Null] * 1 
    studioSpline1 = workPart.Features.FindObject("SPLINE(1)")
    features1[0] = studioSpline1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1, NXOpen.DisplayableObject.Null, selectionIntentRuleOptions1)
    selectionIntentRuleOptions1.Dispose()
    section1.AllowSelfIntersection(False)
    section1.AllowDegenerateCurves(False)
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section1.AddToSection(rules1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    theSession.DeleteUndoMark(markId3, None)
    revolveBuilder1.Section = section1
    theSession.DeleteUndoMark(markId2, None)
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    selectionIntentRuleOptions2 = workPart.ScRuleFactory.CreateRuleOptions()
    selectionIntentRuleOptions2.SetSelectedFromInactive(False)
    features2 = [NXOpen.Features.Feature.Null] * 1 
    studioSpline2 = workPart.Features.FindObject("SPLINE(2)")
    features2[0] = studioSpline2
    curveFeatureRule2 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2, NXOpen.DisplayableObject.Null, selectionIntentRuleOptions2)
    selectionIntentRuleOptions2.Dispose()
    section1.AllowSelfIntersection(False)
    section1.AllowDegenerateCurves(False)
    rules2 = [None] * 1 
    rules2[0] = curveFeatureRule2
    helpPoint2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section1.AddToSection(rules2, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    theSession.DeleteUndoMark(markId5, None)
    revolveBuilder1.Section = section1
    theSession.DeleteUndoMark(markId4, None)
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    selectionIntentRuleOptions3 = workPart.ScRuleFactory.CreateRuleOptions()
    selectionIntentRuleOptions3.SetSelectedFromInactive(False)
    features3 = [NXOpen.Features.Feature.Null] * 1 
    studioSpline3 = workPart.Features.FindObject("SPLINE(3)")
    features3[0] = studioSpline3
    curveFeatureRule3 = workPart.ScRuleFactory.CreateRuleCurveFeature(features3, NXOpen.DisplayableObject.Null, selectionIntentRuleOptions3)
    selectionIntentRuleOptions3.Dispose()
    section1.AllowSelfIntersection(False)
    section1.AllowDegenerateCurves(False)
    rules3 = [None] * 1 
    rules3[0] = curveFeatureRule3
    helpPoint3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section1.AddToSection(rules3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint3, NXOpen.Section.Mode.Create, False)
    theSession.DeleteUndoMark(markId7, None)
    revolveBuilder1.Section = section1
    unit1 = revolveBuilder1.Offset.StartOffset.Units
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    theSession.DeleteUndoMark(markId6, None)
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    scalar1 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    spline1 = studioSpline3.FindObject("CURVE 1")
    point1 = workPart.Points.CreatePoint(spline1, scalar1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    scalar2 = workPart.Scalars.CreateScalar(6.6856915004945403, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    point2 = workPart.Points.CreatePoint(spline1, point1, scalar2, NXOpen.PointCollection.AlongCurveOption.Distance, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    direction1 = workPart.Directions.CreateDirection(spline1, point2, NXOpen.Direction.OnCurveOption.Tangent, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    axis1 = workPart.Axes.CreateAxis(NXOpen.Point.Null, direction1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    axis1.Point = NXOpen.Point.Null
    axis1.Evaluate()
    revolveBuilder1.Axis = axis1
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    theSession.DeleteUndoMark(markId8, None)
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    revolveBuilder1.ParentFeatureInternal = False
    feature1 = revolveBuilder1.CommitFeature()
    theSession.DeleteUndoMark(markId9, None)
    theSession.SetUndoMarkName(markId1, "Revolve")
    expression4 = revolveBuilder1.Limits.StartExtend.Value
    expression5 = revolveBuilder1.Limits.EndExtend.Value
    revolveBuilder1.Destroy()
    workPart.MeasureManager.SetPartTransientModification()
    workPart.Expressions.Delete(expression1)
    workPart.MeasureManager.ClearPartTransientModification()
    workPart.MeasureManager.SetPartTransientModification()
    workPart.Expressions.Delete(expression3)
    workPart.MeasureManager.ClearPartTransientModification()
    workPart.MeasureManager.SetPartTransientModification()
    workPart.Expressions.Delete(expression2)
    workPart.MeasureManager.ClearPartTransientModification()
    scaleAboutPoint1 = NXOpen.Point3d(-8.01916679397862, 12.156194162021137, 0.0)
    viewCenter1 = NXOpen.Point3d(8.0191667939782612, -12.156194162021084, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    scaleAboutPoint2 = NXOpen.Point3d(-6.4153334351829319, 9.7563261532608383, 0.0)
    viewCenter2 = NXOpen.Point3d(6.4153334351825704, -9.7563261532607868, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    scaleAboutPoint3 = NXOpen.Point3d(-5.1322667481463871, 7.8301575815238147, 0.0)
    viewCenter3 = NXOpen.Point3d(5.1322667481460158, -7.8301575815237623, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    scaleAboutPoint4 = NXOpen.Point3d(-4.8888291566695274, 5.8625795225768149, 0.0)
    viewCenter4 = NXOpen.Point3d(4.8888291566691553, -5.8625795225767581, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint4, viewCenter4)
    scaleAboutPoint5 = NXOpen.Point3d(-6.1612297636671425, 7.2780310853907313, 0.0)
    viewCenter5 = NXOpen.Point3d(6.1612297636667703, -7.2780310853906744, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint5, viewCenter5)
    rotMatrix1 = NXOpen.Matrix3x3()
    rotMatrix1.Xx = 0.987514461725571
    rotMatrix1.Xy = -0.044570401428514289
    rotMatrix1.Xz = -0.15109158546839743
    rotMatrix1.Yx = 0.1056523978265614
    rotMatrix1.Yy = -0.52403889255513125
    rotMatrix1.Yz = 0.84511585591745031
    rotMatrix1.Zx = -0.11684502007510052
    rotMatrix1.Zy = -0.85052731784822111
    rotMatrix1.Zz = -0.51278701512182934
    translation1 = NXOpen.Point3d(-12.701882506347586, 4.5598354410088664, 14.094394256782408)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 8.4340575923822296)
##---------------------------------------------------------------------------------------------------
def Nose_Spline (filename, DG, n):
        with open(filename + ".txt", "r") as file:
            # Create a list using list comprehension
            names = list () #empty list of names
            names = [line.strip() for line in file]
        main (names, DG, n)

def Nose_Line1 (filename, DG, n):
        with open(filename + ".txt", "r") as file:
            # Create a list using list comprehension
            names = list () #empty list of names
            names = [line.strip() for line in file]
        main (names[-2:], DG, n)

def Nose_Line2 (filename, DG, n):
        with open(filename + ".txt", "r") as file:
            # Create a list using list comprehension
            names = list () #empty list of names
            new_names = list ()
            names = [line.strip() for line in file]
            new_names = [names[0], names [-1]]
        main (new_names, DG, n)

Nose_Spline (filename, DG, n) #Create the nose line
Nose_Line1 (filename, DG, 2) #enclose it
Nose_Line2 (filename, DG, 2) #enclose it
Revolve ('run')
