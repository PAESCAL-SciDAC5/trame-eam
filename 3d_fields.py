# state file generated using paraview version 5.11.0-RC1-245-g96ce6f3cec
from venv import create
import paraview

paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *

from trame.app import get_server
from trame.widgets import vuetify, paraview
from trame.ui.vuetify import SinglePageLayout

camera_config = [
    {
        "cameraPosition": [179.99999999999986, 0.0, -765.0709624885501],
        "cameraFocalPoint": [179.99999999999986, 0.0, 14.5],
        "cameraViewAngle": 17.676056338028168,
        "cameraParallelScale": 201.76781210093955,
    },
    {
        "cameraPosition": [179.99999999999986, 0.0, 794.0709624885501],
        "cameraFocalPoint": [179.99999999999986, 0.0, 14.5],
        "cameraViewAngle": 17.653972731546776,
        "cameraParallelScale": 201.76781210093955,
    },
    {
        "cameraPosition": [-599.5709624885502, 0.0, 14.5],
        "cameraFocalPoint": [179.99999999999986, 0.0, 14.5],
        "cameraViewUp": [0.0, 0.0, 1.0],
        "cameraViewAngle": 11.244131455399062,
        "cameraParallelScale": 201.76781210093955,
    },
    {
        "cameraPosition": [-513.7999767022803, -350.7482081356252, 72.36339406643907],
        "cameraFocalPoint": [179.99999999999986, 0.0, 14.5],
        "cameraViewUp": [-0.17659118226024734, 0.49012326212087765, 0.8535776135044297],
        "cameraViewAngle": 17.01927597555242,
        "cameraParallelScale": 201.76781210093955,
    },
]


def create_render_view():
    render_view = CreateView("RenderView")
    render_view.ViewSize = [1420, 857]
    render_view.AxesGrid = "GridAxes3DActor"
    render_view.CenterOfRotation = [179.99999999999986, 0.0, 14.5]
    render_view.StereoType = "Crystal Eyes"

    return render_view


def setup_camera(render_view, config):
    if "cameraPosition" in config:
        render_view.CameraPosition = config["cameraPosition"]

    if "cameraFocalPoint" in config:
        render_view.CameraFocalPoint = config["cameraFocalPoint"]

    if "cameraViewUp" in config:
        render_view.CameraViewUp = config["cameraViewUp"]

    if "cameraViewAngle" in config:
        render_view.CameraViewAngle = config["cameraViewAngle"]

    if "cameraParallelScale" in config:
        render_view.CameraParallelScale = config["cameraParallelScale"]


def create_layout(render_views):
    [render_view_1, render_view_2, render_view_3, render_view_4] = render_views
    # create new layout object 'Layout #1'
    layout = CreateLayout(name="Layout #1")
    layout.SplitHorizontal(0, 0.500000)
    layout.SplitVertical(1, 0.500000)
    layout.AssignView(3, render_view_1)
    layout.AssignView(4, render_view_2)
    layout.SplitVertical(2, 0.500000)
    layout.AssignView(5, render_view_3)
    layout.AssignView(6, render_view_4)
    layout.SetSize(2839, 1713)


def create_source(args):
    # create a new 'NetCDF CAM reader'
    source = NetCDFCAMreader(
        registrationName="PD_1800_ad4fd8_ANN_climo_SE.nc",
        ConnectivityFileName=f"{args.data_dir}/ne30np4_latlon.nc",
        FileName=[f"{args.data_dir}/PD_1800_ad4fd8_ANN_climo_SE.nc"],
    )
    source.PointArrayStatus = [
        "AEROD_v [time,ncol]",
        "AODDUST1 [time,ncol]",
        "AODDUST3 [time,ncol]",
        "AODVIS [time,ncol]",
        "CDNUMC [time,ncol]",
        "CLDHGH [time,ncol]",
        "CLDLOW [time,ncol]",
        "CLDMED [time,ncol]",
        "CLDTOT [time,ncol]",
        "FLDS [time,ncol]",
        "FLNS [time,ncol]",
        "FLNSC [time,ncol]",
        "FLNT [time,ncol]",
        "FLNTC [time,ncol]",
        "FLUT [time,ncol]",
        "FLUTC [time,ncol]",
        "FSDS [time,ncol]",
        "FSDSC [time,ncol]",
        "FSNS [time,ncol]",
        "FSNSC [time,ncol]",
        "FSNT [time,ncol]",
        "FSNTC [time,ncol]",
        "FSNTOA [time,ncol]",
        "FSNTOAC [time,ncol]",
        "ICEFRAC [time,ncol]",
        "LANDFRAC [time,ncol]",
        "LHFLX [time,ncol]",
        "LWCF [time,ncol]",
        "OCNFRAC [time,ncol]",
        "PBLH [time,ncol]",
        "PHIS [time,ncol]",
        "PRECC [time,ncol]",
        "PRECL [time,ncol]",
        "PRECSC [time,ncol]",
        "PRECSL [time,ncol]",
        "PS [time,ncol]",
        "PSL [time,ncol]",
        "QFLX [time,ncol]",
        "SHFLX [time,ncol]",
        "SNOWHICE [time,ncol]",
        "SNOWHLND [time,ncol]",
        "SOLIN [time,ncol]",
        "SWCF [time,ncol]",
        "TAUX [time,ncol]",
        "TAUY [time,ncol]",
        "TGCLDIWP [time,ncol]",
        "TGCLDLWP [time,ncol]",
        "TMQ [time,ncol]",
        "TREFHT [time,ncol]",
        "TS [time,ncol]",
        "U10 [time,ncol]",
        "ANRAIN [time,lev, ncol]",
        "ANSNOW [time,lev, ncol]",
        "AQRAIN [time,lev, ncol]",
        "AQSNOW [time,lev, ncol]",
        "AREI [time,lev, ncol]",
        "AREL [time,lev, ncol]",
        "AWNC [time,lev, ncol]",
        "AWNI [time,lev, ncol]",
        "CCN3 [time,lev, ncol]",
        "CLDICE [time,lev, ncol]",
        "CLDLIQ [time,lev, ncol]",
        "CLOUD [time,lev, ncol]",
        "DCQ [time,lev, ncol]",
        "DTCOND [time,lev, ncol]",
        "DTV [time,lev, ncol]",
        "FICE [time,lev, ncol]",
        "FREQI [time,lev, ncol]",
        "FREQL [time,lev, ncol]",
        "FREQR [time,lev, ncol]",
        "FREQS [time,lev, ncol]",
        "ICIMR [time,lev, ncol]",
        "ICWMR [time,lev, ncol]",
        "IWC [time,lev, ncol]",
        "NUMICE [time,lev, ncol]",
        "NUMLIQ [time,lev, ncol]",
        "OMEGA [time,lev, ncol]",
        "OMEGAT [time,lev, ncol]",
        "Q [time,lev, ncol]",
        "QRL [time,lev, ncol]",
        "QRS [time,lev, ncol]",
        "RELHUM [time,lev, ncol]",
        "T [time,lev, ncol]",
        "U [time,lev, ncol]",
        "UU [time,lev, ncol]",
        "V [time,lev, ncol]",
        "VD01 [time,lev, ncol]",
        "VQ [time,lev, ncol]",
        "VT [time,lev, ncol]",
        "VU [time,lev, ncol]",
        "VV [time,lev, ncol]",
        "WSUB [time,lev, ncol]",
        "Z3 [time,lev, ncol]",
    ]

    return source


def setup_visualization(display, z_scale, render_view):
    # get 2D transfer function for 'U'
    uTF2D = GetTransferFunction2D("U")

    # get color transfer function/color map for 'U'
    uLUT = GetColorTransferFunction("U")
    uLUT.TransferFunction2D = uTF2D
    uLUT.RGBPoints = [
        -21.407419204711914,
        0.231373,
        0.298039,
        0.752941,
        15.344744682312012,
        0.865003,
        0.865003,
        0.865003,
        52.09690856933594,
        0.705882,
        0.0156863,
        0.14902,
    ]
    uLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'U'
    uPWF = GetOpacityTransferFunction("U")
    uPWF.Points = [-21.407419204711914, 0.0, 0.5, 0.0, 52.09690856933594, 1.0, 0.5, 0.0]
    uPWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    display.Representation = "Surface"
    display.ColorArrayName = ["POINTS", "U"]
    display.LookupTable = uLUT
    display.SelectTCoordArray = "None"
    display.SelectNormalArray = "None"
    display.SelectTangentArray = "None"
    display.Scale = [1.0, 1.0, z_scale]
    display.Texture = None
    display.BaseColorTexture = None
    display.NormalTexture = None
    display.CoatNormalTexture = None
    display.MaterialTexture = None
    display.AnisotropyTexture = None
    display.EmissiveTexture = None
    display.OSPRayScaleArray = "ANRAIN"
    display.OSPRayScaleFunction = "PiecewiseFunction"
    display.SelectOrientationVectors = "None"
    display.ScaleFactor = 36.00000000000003
    display.SelectScaleArray = "ANRAIN"
    display.GlyphType = "Arrow"
    display.GlyphTableIndexArray = "ANRAIN"
    display.GaussianRadius = 1.8000000000000014
    display.SetScaleArray = ["POINTS", "ANRAIN"]
    display.ScaleTransferFunction = "PiecewiseFunction"
    display.OpacityArray = ["POINTS", "ANRAIN"]
    display.OpacityTransferFunction = "PiecewiseFunction"
    display.DataAxesGrid = "GridAxesRepresentation"
    display.PolarAxes = "PolarAxesRepresentation"
    display.ScalarOpacityFunction = uPWF
    display.ScalarOpacityUnitDistance = 3.599181859937947
    display.OpacityArrayName = ["POINTS", "ANRAIN"]
    display.SelectInputVectors = ["POINTS", ""]
    display.WriteLog = ""
    display.PolarAxes.Scale = [1.0, 1.0, z_scale]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    display.ScaleTransferFunction.Points = [
        0.0,
        0.0,
        0.5,
        0.0,
        81995.0234375,
        1.0,
        0.5,
        0.0,
    ]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    display.OpacityTransferFunction.Points = [
        0.0,
        0.0,
        0.5,
        0.0,
        81995.0234375,
        1.0,
        0.5,
        0.0,
    ]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for uLUT in view render_view_1
    uLUTColorBar = GetScalarBar(uLUT, render_view)
    uLUTColorBar.Orientation = "Horizontal"
    uLUTColorBar.WindowLocation = "Any Location"
    uLUTColorBar.Position = [0.43910211267605626, 0.011074766355140209]
    uLUTColorBar.Title = "U"
    uLUTColorBar.ComponentTitle = ""
    uLUTColorBar.ScalarBarLength = 0.33000000000000007

    # set color bar visibility
    uLUTColorBar.Visibility = 1

    # show color legend
    display.SetScalarBarVisibility(render_view, True)


def create_single_page(render_views):
    server = get_server()
    state, ctrl = server.state, server.controller

    [render_view_1, render_view_2, render_view_3, render_view_4] = render_views
    views = []

    def update_views(**kwargs):
        for v in views:
            v.update()

    ctrl.on_server_ready.add(ctrl.view_update)
    ctrl.view_update = update_views

    with SinglePageLayout(server) as layout:
        with layout.content:
            layout.title.set_text("EAM Application")
            with vuetify.VContainer(fluid=True, classes="pa-0 fill-height"):
                with vuetify.VRow(dense=True, style="height: 50%;"):
                    with vuetify.VCol():
                        views.append(paraview.VtkRemoteView(render_view_1, ref="view1"))
                    with vuetify.VCol():
                        views.append(paraview.VtkRemoteView(render_view_2, ref="view2"))
                with vuetify.VRow(dense=True, style="height: 50%;"):
                    with vuetify.VCol():
                        views.append(paraview.VtkRemoteView(render_view_3, ref="view3"))
                    with vuetify.VCol():
                        views.append(paraview.VtkRemoteView(render_view_4, ref="view4"))
    server.start()


def z_axes_array_names(source):
    names = source.PointData.keys()
    return [name for name in names if name in ["lev", "ilev"]]


def z_axes_scale(source):
    bounds = source.GetDataInformation().GetBounds()
    y_bounds = bounds[2:4]
    y_delta = abs(y_bounds[0] - y_bounds[1])
    z_bounds = bounds[4:6]
    z_delta = abs(z_bounds[0] - z_bounds[1])

    return z_delta / y_delta


def setup_axes(source, render_view, z_scale):
    names = z_axes_array_names(source)
    name = names[0]

    if name in ["lev", "ilev"]:
        render_view.AxesGrid.ZTitle = f"{name} (hPa)"

    render_view.AxesGrid.Visibility = 1
    render_view.AxesGrid.DataScale = [1.0, 1.0, z_scale]


def setup_pipeline(source):
    calculator = PythonCalculator(registrationName="PythonCalculator1", Input=source)
    calculator.Expression = "-points[:,2] + lev"

    warp_by_scalar = WarpByScalar(registrationName="WarpByScalar1", Input=calculator)
    warp_by_scalar.Scalars = ["POINTS", "result"]

    return warp_by_scalar


def main():
    server = get_server()
    server.cli.add_argument(
        "-x",
        "--data-dir",
        help="Directory containing data",
        dest="data_dir",
        required=True,
    )
    args = server.cli.parse_args()
    reader = create_source(args)
    source = setup_pipeline(reader)
    source.UpdatePipeline()
    z_scale = z_axes_scale(reader)

    render_views = []
    for i in range(0, 4):
        render_view = create_render_view()
        display = Show(source, render_view, "UnstructuredGridRepresentation")
        setup_visualization(display, z_scale, render_view)
        setup_camera(render_view, camera_config[i])
        setup_axes(source, render_view, z_scale)
        render_views.append(render_view)

    create_layout(render_views)

    SetActiveView(render_views[0])
    SetActiveSource(source)

    create_single_page(render_views)


main()
