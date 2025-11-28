# Airfoil_Spline.py plots airfoils from DAT files unparameterized.
# Check the Dat file point distribution
# 1) The points are consecutive and continuous regardless of airfoil surface
# 2) the points are split into origin through upper surface then origin through lower surface
# For one, put False in PD. For two, put True in PD.


filename = ['C:/Users/96879/GitHub/NXOpen/n64212.dat', 'C:/Users/96879/GitHub/NXOpen/n64212.dat', 'C:/Users/96879/GitHub/NXOpen/n64212.dat']  #List of all Airfoils
DG = [3,5,7]          #Spline Degree
Upper = [26,26,26]    #Points on the Upper Limit
Lower = [26,26,26]    #Points on the Lower Limit
PD = [False, False, False]

def main(IN,DG, Upper, Lower, PD): 
        import math
        import NXOpen
        import NXOpen.Features
        import NXOpen.GeometricUtilities#IN is the points name
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
        if PD:
                #Upper Surface
                for i in IN[:Upper-1]:
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
                    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
                #Lower Surface
                for i in IN[Upper+Lower-1:Upper:-1]:
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
                for i in IN[:Upper-1]:
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
                    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
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
      
    #if __name__ == '__main__':
    #    main()
        
def Airfoil_Spline (filename, DG, Upper, Lower, PD):
        with open(filename + ".txt", "r") as file:
            # Create a list using list comprehension
            names = list () #empty list of names
            names = [line.strip() for line in file]
        main (names, DG, Upper, Lower, PD)

for i in range (0, len(filename)):
    Airfoil_Spline (filename[i], DG[i], Upper[i], Lower[i], PD[i])
