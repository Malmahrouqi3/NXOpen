
"""
## Wing
Airfoil ('Wing', 'Airfoil_w0', 'S8037 (16%).dat', 'MilliMeter')
Airfoil ('Wing', 'Airfoil_w1', 'S8037 (16%).dat', 'MilliMeter')
Airfoil ('Wing', 'Airfoil_w2', 'sd8040 (10%).dat', 'MilliMeter')
##--------------------------------------------------------
## Tail
## Hstab
Airfoil ('Hstab', 'Airfoil_h0', 'NACA0012.dat', 'MilliMeter')
Airfoil ('Hstab', 'Airfoil_h1', 'NACA0012.dat', 'MilliMeter')

## Vstab
Airfoil ('Vstab', 'Airfoil_v0', 'NACA0008.dat', 'MilliMeter')
Airfoil ('Vstab', 'Airfoil_v1', 'NACA0010.dat', 'MilliMeter')
Airfoil ('Vstab', 'Airfoil_v2', 'NACA0010.dat', 'MilliMeter')

Wing: 0 - S8037, 1 - S8037, 2 - SD8040 (inboard to outboard)
Vstab: 0 - NACA 0008, 1 - NACA 0010, 2 - NACA 0010 (bottom to top)
Hstab: All NACA 0012
"""
import os
# Get the current directory (where your Python code is)
dr = os.getcwd()

file1 = 'Wing_Airfoil_w0'
file2 = 'Wing_Airfoil_w1'
file3 = 'Wing_Airfoil_w2'

file4 = 'Hstab_Airfoil_h0'
file5 = 'Hstab_Airfoil_h1'

file6 = 'Vstab_Airfoil_v0'
file7 = 'Vstab_Airfoil_v1'
file8 = 'Vstab_Airfoil_v2'

filename = [dr+file1, dr+file2, dr+file3, dr+file4, dr+file5, dr+file6, dr+file7, dr+file8]  #List of all Airfoils
#filenames should include the directory without including the extension (.txt), yet they are a txt file
DG =    [3,3,3,3,3,3,3,3]          #Spline Degree
Upper = [25,25,25,25,25,25,25,25]    #Points on the Upper Limit
Lower = [25,25,25,25,25,25,25,25]    #Points on the Lower Limit

def main(IN,DG, Upper, Lower): 
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
           
        if Upper == 67:  # intended to flag out NACA 0012, as it has the first type of point distribution
            # ----------------------------------------------
            #   Dialog Begin Point    # First Distribution of Points (it forms enclosed area, yet it initially traces upper surface from origin, then lower surface from origin)
            # ----------------------------------------------
            # Upper Surface
            for i in IN[:Upper-1]:
                expression24 = workPart.Expressions.FindObject(i)
                markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
                point2 = workPart.Points.CreatePoint(expression24, NXOpen.SmartObject.UpdateOption.WithinModeling)
                workPart.MeasureManager.SetPartTransientModification()
                workPart.MeasureManager.ClearPartTransientModification()
                geometricConstraintData1 = studioSplineBuilderEx1.ConstraintManager.CreateGeometricConstraintData()
                geometricConstraintData1.Point = point2
                studioSplineBuilderEx1.ConstraintManager.Append(geometricConstraintData1)
                studioSplineBuilderEx1.Evaluate()
                theSession.SetUndoMarkName(markId7, "Studio Spline - Selection")
                markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
                markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
                markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
                markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
                
            for i in IN[Upper+Lower-1:Upper:-1]: 
                expression24 = workPart.Expressions.FindObject(i)
                markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
                point2 = workPart.Points.CreatePoint(expression24, NXOpen.SmartObject.UpdateOption.WithinModeling)
                workPart.MeasureManager.SetPartTransientModification()
                workPart.MeasureManager.ClearPartTransientModification()
                geometricConstraintData1 = studioSplineBuilderEx1.ConstraintManager.CreateGeometricConstraintData()
                geometricConstraintData1.Point = point2
                studioSplineBuilderEx1.ConstraintManager.Append(geometricConstraintData1)
                studioSplineBuilderEx1.Evaluate()
                markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
                markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
                markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
                markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
                
                
            expression24 = workPart.Expressions.FindObject(IN[0])
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
            markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
        else:
            # ----------------------------------------------
            #   Dialog Begin Point          # Second Distribution of Points (it forms enclosed area)
            # ----------------------------------------------
            markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
            markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")

            for i in IN:
                    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
                    expression24 = workPart.Expressions.FindObject(i)
                    point2 = workPart.Points.CreatePoint(expression24, NXOpen.SmartObject.UpdateOption.WithinModeling)
                    workPart.MeasureManager.SetPartTransientModification()
                    workPart.MeasureManager.ClearPartTransientModification()
                    geometricConstraintData1 = studioSplineBuilderEx1.ConstraintManager.CreateGeometricConstraintData()
                    geometricConstraintData1.Point = point2
                    studioSplineBuilderEx1.ConstraintManager.Append(geometricConstraintData1)
                    studioSplineBuilderEx1.Evaluate()
                    theSession.SetUndoMarkName(markId7, "Studio Spline - Selection")
                    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
                    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
                    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
                    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
        # ----------------------------------------------
        #   Closing spline
        # ----------------------------------------------
        studioSplineBuilderEx1.Evaluate()
        markId1 =  theSession.SetUndoMarkVisibility(markId1, None, NXOpen.Session.MarkVisibility.Invisible)
        markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        theSession.DeleteUndoMark(markId20, None)
        markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Studio Spline")
        nXObject1 = studioSplineBuilderEx1.Commit()
        theSession.DeleteUndoMark(markId21, None)
        #theSession.SetUndoMarkName(markId1, "Studio Spline")
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
        theSession.DeleteUndoMark(markId11, None)
        theSession.DeleteUndoMark(markId7, None)
        theSession.DeleteUndoMark(markId4, None)
        theSession.DeleteUndoMark(markId3, None)
##---------------------------------------------------------------------------------------------------
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def WingThroughCurves(WingCurves) : 
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: THrough Curves (Wing)
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    bodyType1 = theSession.Preferences.Modeling.BodyType
    throughCurvesBuilder1 = workPart.Features.CreateThroughCurvesBuilder(NXOpen.Features.Feature.Null)
    throughCurvesBuilder1.PreserveShape = False
    theSession.SetUndoMarkName(markId1, "Through Curves Dialog")
    throughCurvesBuilder1.Alignment.AlignCurve.DistanceTolerance = 0.01
    throughCurvesBuilder1.Alignment.AlignCurve.ChainingTolerance = 0.0094999999999999998
    throughCurvesBuilder1.SectionTemplateString.DistanceTolerance = 0.01
    throughCurvesBuilder1.SectionTemplateString.ChainingTolerance = 0.0094999999999999998
    throughCurvesBuilder1.Alignment.AlignCurve.AngleTolerance = 0.5
    throughCurvesBuilder1.SectionTemplateString.AngleTolerance = 0.5
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    throughCurvesBuilder1.SectionsList.Append(section1)
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.CurvesAndPoints)
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    selectionIntentRuleOptions1 = workPart.ScRuleFactory.CreateRuleOptions()
    selectionIntentRuleOptions1.SetSelectedFromInactive(False)
    features1 = [NXOpen.Features.Feature.Null] * 1 
    studioSpline1 = workPart.Features.FindObject("SPLINE("+str(WingCurves[0])+")")
    features1[0] = studioSpline1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1, NXOpen.DisplayableObject.Null, selectionIntentRuleOptions1)
    selectionIntentRuleOptions1.Dispose()
    section1.AllowSelfIntersection(False)
    section1.AllowDegenerateCurves(False)
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    spline1 = studioSpline1.FindObject("CURVE 1")
    helpPoint1 = NXOpen.Point3d(86.864766766910662, -17.951957472684555, 0.0)
    section1.AddToSection(rules1, spline1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    theSession.DeleteUndoMark(markId3, None)
    sections1 = [NXOpen.Section.Null] * 1 
    sections1[0] = section1
    throughCurvesBuilder1.Alignment.SetSections(sections1)
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    theSession.DeleteUndoMark(markId2, None)
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    throughCurvesBuilder1.SectionsList.Append(section2)
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.CurvesAndPoints)
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    selectionIntentRuleOptions2 = workPart.ScRuleFactory.CreateRuleOptions()
    selectionIntentRuleOptions2.SetSelectedFromInactive(False)
    features2 = [NXOpen.Features.Feature.Null] * 1 
    studioSpline2 = workPart.Features.FindObject("SPLINE("+str(WingCurves[1])+")")
    features2[0] = studioSpline2
    curveFeatureRule2 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2, NXOpen.DisplayableObject.Null, selectionIntentRuleOptions2)
    selectionIntentRuleOptions2.Dispose()
    section2.AllowSelfIntersection(False)
    section2.AllowDegenerateCurves(False)
    rules2 = [None] * 1 
    rules2[0] = curveFeatureRule2
    spline2 = studioSpline2.FindObject("CURVE 1")
    helpPoint2 = NXOpen.Point3d(55.165078649754648, -14.043660728500344, 275.0)
    section2.AddToSection(rules2, spline2, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    theSession.DeleteUndoMark(markId5, None)
    sections2 = [NXOpen.Section.Null] * 2 
    sections2[0] = section1
    sections2[1] = section2
    throughCurvesBuilder1.Alignment.SetSections(sections2)
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    theSession.DeleteUndoMark(markId4, None)
    section3 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    throughCurvesBuilder1.SectionsList.Append(section3)
    section3.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.CurvesAndPoints)
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    selectionIntentRuleOptions3 = workPart.ScRuleFactory.CreateRuleOptions()
    selectionIntentRuleOptions3.SetSelectedFromInactive(False)
    features3 = [NXOpen.Features.Feature.Null] * 1 
    studioSpline3 = workPart.Features.FindObject("SPLINE("+str(WingCurves[2])+")")
    features3[0] = studioSpline3
    curveFeatureRule3 = workPart.ScRuleFactory.CreateRuleCurveFeature(features3, NXOpen.DisplayableObject.Null, selectionIntentRuleOptions3)
    selectionIntentRuleOptions3.Dispose()
    section3.AllowSelfIntersection(False)
    section3.AllowDegenerateCurves(False)
    rules3 = [None] * 1 
    rules3[0] = curveFeatureRule3
    spline3 = studioSpline3.FindObject("CURVE 1")
    helpPoint3 = NXOpen.Point3d(54.871036650642793, -12.149674060616341, 675.0)
    section3.AddToSection(rules3, spline3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint3, NXOpen.Section.Mode.Create, False)
    theSession.DeleteUndoMark(markId7, None)
    sections3 = [NXOpen.Section.Null] * 3 
    sections3[0] = section1
    sections3[1] = section2
    sections3[2] = section3
    throughCurvesBuilder1.Alignment.SetSections(sections3)
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    theSession.DeleteUndoMark(markId6, None)
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Through Curves")
    theSession.DeleteUndoMark(markId8, None)
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Through Curves")
    feature1 = throughCurvesBuilder1.CommitFeature()
    displayModification1 = theSession.DisplayManager.NewDisplayModification()
    displayModification1.ApplyToAllFaces = False
    displayModification1.SetNewGrid(0, 0)
    displayModification1.PoleDisplayState = False
    displayModification1.KnotDisplayState = False
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    throughCurves1 = feature1
    face1 = throughCurves1.FindObject("FACE 10001 {(345.8671574768607,0.0729618058667,306.2499557959153) THRU_CURVE(9)}")
    objects1[0] = face1
    displayModification1.Apply(objects1)
    face1.Color = 32767
    displayModification1.SetNewGrid(0, 0)
    displayModification1.PoleDisplayState = False
    displayModification1.KnotDisplayState = False
    objects2 = [NXOpen.DisplayableObject.Null] * 1 
    face2 = throughCurves1.FindObject("FACE 1 {(199.9674431683013,4.2286863356171,0) THRU_CURVE(9)}")
    objects2[0] = face2
    displayModification1.Apply(objects2)
    face2.Color = 32767
    displayModification1.SetNewGrid(0, 0)
    displayModification1.PoleDisplayState = False
    displayModification1.KnotDisplayState = False
    objects3 = [NXOpen.DisplayableObject.Null] * 1 
    face3 = throughCurves1.FindObject("FACE 2 {(140.4673550508516,2.9705072246076,674.9999999999998) THRU_CURVE(9)}")
    objects3[0] = face3
    displayModification1.Apply(objects3)
    face3.Color = 32767
    theSession.DeleteUndoMark(markId9, None)
    theSession.SetUndoMarkName(markId1, "Through Curves")
    throughCurvesBuilder1.Destroy()
    workPart.MeasureManager.SetPartTransientModification()
    workPart.Expressions.Delete(expression1)
    workPart.MeasureManager.ClearPartTransientModification()
    workPart.MeasureManager.SetPartTransientModification()
    workPart.Expressions.Delete(expression2)
    workPart.MeasureManager.ClearPartTransientModification()
    workPart.MeasureManager.SetPartTransientModification()
    workPart.Expressions.Delete(expression3)
    workPart.MeasureManager.ClearPartTransientModification()
##---------------------------------------------------------------------------------------------------
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def StabsThroughCurves(Curves) : 
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: THrough Curves
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    bodyType1 = theSession.Preferences.Modeling.BodyType
    throughCurvesBuilder1 = workPart.Features.CreateThroughCurvesBuilder(NXOpen.Features.Feature.Null)
    throughCurvesBuilder1.PreserveShape = False
    theSession.SetUndoMarkName(markId1, "Through Curves Dialog")
    throughCurvesBuilder1.Alignment.AlignCurve.DistanceTolerance = 0.01
    throughCurvesBuilder1.Alignment.AlignCurve.ChainingTolerance = 0.0094999999999999998
    throughCurvesBuilder1.SectionTemplateString.DistanceTolerance = 0.01
    throughCurvesBuilder1.SectionTemplateString.ChainingTolerance = 0.0094999999999999998
    throughCurvesBuilder1.Alignment.AlignCurve.AngleTolerance = 0.5
    throughCurvesBuilder1.SectionTemplateString.AngleTolerance = 0.5
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    throughCurvesBuilder1.SectionsList.Append(section1)
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.CurvesAndPoints)
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    selectionIntentRuleOptions1 = workPart.ScRuleFactory.CreateRuleOptions()
    selectionIntentRuleOptions1.SetSelectedFromInactive(False)
    features1 = [NXOpen.Features.Feature.Null] * 1 
    studioSpline1 = workPart.Features.FindObject("SPLINE("+str(Curves[0])+")")
    features1[0] = studioSpline1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1, NXOpen.DisplayableObject.Null, selectionIntentRuleOptions1)
    selectionIntentRuleOptions1.Dispose()
    section1.AllowSelfIntersection(False)
    section1.AllowDegenerateCurves(False)
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    spline1 = studioSpline1.FindObject("CURVE 1")
    helpPoint1 = NXOpen.Point3d(86.864766766910662, -17.951957472684555, 0.0)
    section1.AddToSection(rules1, spline1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    theSession.DeleteUndoMark(markId3, None)
    sections1 = [NXOpen.Section.Null] * 1 
    sections1[0] = section1
    throughCurvesBuilder1.Alignment.SetSections(sections1)
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    theSession.DeleteUndoMark(markId2, None)
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    throughCurvesBuilder1.SectionsList.Append(section2)
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.CurvesAndPoints)
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    selectionIntentRuleOptions2 = workPart.ScRuleFactory.CreateRuleOptions()
    selectionIntentRuleOptions2.SetSelectedFromInactive(False)
    features2 = [NXOpen.Features.Feature.Null] * 1 
    studioSpline2 = workPart.Features.FindObject("SPLINE("+str(Curves[1])+")")
    features2[0] = studioSpline2
    curveFeatureRule2 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2, NXOpen.DisplayableObject.Null, selectionIntentRuleOptions2)
    selectionIntentRuleOptions2.Dispose()
    section2.AllowSelfIntersection(False)
    section2.AllowDegenerateCurves(False)
    rules2 = [None] * 1 
    rules2[0] = curveFeatureRule2
    spline2 = studioSpline2.FindObject("CURVE 1")
    helpPoint2 = NXOpen.Point3d(55.165078649754648, -14.043660728500344, 275.0)
    section2.AddToSection(rules2, spline2, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    theSession.DeleteUndoMark(markId5, None)
    sections2 = [NXOpen.Section.Null] * 2 
    sections2[0] = section1
    sections2[1] = section2
    throughCurvesBuilder1.Alignment.SetSections(sections2)
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    theSession.DeleteUndoMark(markId4, None)
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Through Curves")
    theSession.DeleteUndoMark(markId8, None)
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Through Curves")
    feature1 = throughCurvesBuilder1.CommitFeature()
    displayModification1 = theSession.DisplayManager.NewDisplayModification()
    displayModification1.ApplyToAllFaces = False
    displayModification1.SetNewGrid(0, 0)
    displayModification1.PoleDisplayState = False
    displayModification1.KnotDisplayState = False
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    throughCurves1 = feature1
    face1 = throughCurves1.FindObject("FACE 10001 {(345.8671574768607,0.0729618058667,306.2499557959153) THRU_CURVE(9)}")
    objects1[0] = face1
    displayModification1.Apply(objects1)
    face1.Color = 32767
    displayModification1.SetNewGrid(0, 0)
    displayModification1.PoleDisplayState = False
    displayModification1.KnotDisplayState = False
    objects2 = [NXOpen.DisplayableObject.Null] * 1 
    face2 = throughCurves1.FindObject("FACE 1 {(199.9674431683013,4.2286863356171,0) THRU_CURVE(9)}")
    objects2[0] = face2
    displayModification1.Apply(objects2)
    face2.Color = 32767
    displayModification1.SetNewGrid(0, 0)
    displayModification1.PoleDisplayState = False
    displayModification1.KnotDisplayState = False
    theSession.DeleteUndoMark(markId9, None)
    theSession.SetUndoMarkName(markId1, "Through Curves")
    throughCurvesBuilder1.Destroy()
    workPart.MeasureManager.SetPartTransientModification()
    workPart.Expressions.Delete(expression1)
    workPart.MeasureManager.ClearPartTransientModification()
    workPart.MeasureManager.SetPartTransientModification()
    workPart.Expressions.Delete(expression2)
    workPart.MeasureManager.ClearPartTransientModification()
    workPart.MeasureManager.SetPartTransientModification()
    workPart.Expressions.Delete(expression3)
    workPart.MeasureManager.ClearPartTransientModification()
##---------------------------------------------------------------------------------------------------    
def Airfoil_Spline (filename, DG, Upper, Lower):
        with open(filename + ".txt", "r") as file:
            # Create a list using list comprehension
            names = list () #empty list of names
            names = [line.strip() for line in file]
        main (names, DG, Upper, Lower)

for i in range (0, len(filename)):
    Airfoil_Spline (filename[i], DG[i], Upper[i], Lower[i])

#Three Curves for the wing
#WingSplines = [1,2,3]  #the number for each spline of the wing
#WingThroughCurves (WingSplines)

#Two Curves for the Vstab and Hstab
#StabsSplines = [0,0]
#for i in range (0,6,2):
#    Spline_Names = [4,5,6,7,7,8]
#    j = i + 1
#    StabsSplines[0] = Spline_Names[i]
#    StabsSplines[1] = Spline_Names[j]
#    StabsThroughCurves (StabsSplines)
