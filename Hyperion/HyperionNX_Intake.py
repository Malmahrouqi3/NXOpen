n = 50    # how many points allocated for each cross-section
DG = 1    # spline degree
dr = 'C:/Users/Mohammed/OneDrive - Georgia Institute of Technology/NXOpen/'    #directory of files
file1 = 'HyperionNX_Intake'
filename = dr+file1
#filenames should include the directory without including the extension (.txt), yet they are a txt file
def main(IN,DG): 
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
            #studioSplineBuilderEx1.Evaluate()
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
        #nXObject1 = studioSplineBuilderEx1.Commit()
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
        theSession.DeleteUndoMark(markId7, None)
        theSession.DeleteUndoMark(markId4, None)
        theSession.DeleteUndoMark(markId3, None)
##---------------------------------------------------------------------------------------------------
def Spline (filename, DG, n):
        with open(filename + ".txt", "r") as file:
            # Create a list using list comprehension
            names = list () #empty list of names
            names = [line.strip() for line in file]
        for i in range (0,11):
            main (names[i*n:n*(i+1)], DG)
Spline (filename, DG, n)
