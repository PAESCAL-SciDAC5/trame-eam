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

from math import log

DEFAULT_ARRAY = "CLOUD"
Z_SCALARS = ["lev", "ilev", "Z3"]
# TODO We should be able to get these from teh NetCDF
Z_SCALARS_UNITS = {"lev": "hPa", "ilev": "hPa", "Z3": "m"}


class ProcessingPipeline:
    def __init__(self, reader):
        self.reader = reader
        self._z_ln = False

        self.reader.UpdatePipeline()
        names = [name for name in self.reader.PointData.keys() if name in Z_SCALARS]
        self._z_scalar = names[0]
        self.calculator = PythonCalculator(
            registrationName="PythonCalculator1", Input=reader
        )
        self.calculator.Expression = f"-(abs(points[:,2] + {self._z_scalar}))"

        self.warp_by_scalar = WarpByScalar(
            registrationName="WarpByScalar1", Input=self.calculator
        )
        self.warp_by_scalar.Scalars = ["POINTS", "result"]

    def get_output(self):
        return self.warp_by_scalar

    def get_reader(self):
        return self.reader

    def enable_ln(self, enable):
        self._z_ln = enable
        self.update()

    @property
    def z_scalar(self):
        return self._z_scalar

    @z_scalar.setter
    def z_scalar(self, array):
        self._z_scalar = array
        self.update()

    def update(self):
        if self._z_ln:
            self.calculator.Expression = (
                f"-(abs(points[:,2] + numpy.log({self._z_scalar})))"
            )
        else:
            self.calculator.Expression = f"-(abs(points[:,2] + {self._z_scalar}))"

    def z_axes_array_names(self):
        names = self.get_output().PointData.keys()

        return [name for name in names if name in Z_SCALARS]


class View:
    def __init__(self, reader):
        self._view = None
        self._scale = None
        self._render_view = self._create_render_view()
        self._pipeline = ProcessingPipeline(reader)
        self._z_log_scale = False
        self._lut_color_bar = None

        # self._pipelines.append(pipeline)

        # z_scale = self._z_axes_scale()
        self._setup_display()
        # displays.append(display)
        ResetCamera(view=self.render_view)
        self._setup_axes()
        # render_views.append(render_view)

    def _z_axes_scale(self):
        bounds = self._pipeline.get_output().GetDataInformation().GetBounds()
        y_bounds = bounds[2:4]
        y_delta = abs(y_bounds[0] - y_bounds[1])
        z_range = (
            self._pipeline.get_output()
            .PointData.GetArray(self._pipeline.z_scalar)
            .GetRange()
        )
        if self._z_log_scale:
            z_range = [log(z_range[0]), log(z_range[1])]

        z_delta = abs(z_range[0] - z_range[1])

        return y_delta / z_delta

    def _create_render_view(self):
        render_view = CreateView("RenderView")
        render_view.ViewSize = [1420, 857]
        render_view.AxesGrid = "GridAxes3DActor"
        render_view.CenterOfRotation = [179.99999999999986, 0.0, 14.5]
        render_view.StereoType = "Crystal Eyes"

        return render_view

    def _setup_axes(self):
        name = self._pipeline.z_scalar
        units = Z_SCALARS_UNITS[name]
        title = f"{name} ({units})"
        if self._z_log_scale:
            title = f"ln({name})"

        self.render_view.AxesGrid.ZTitle = title

        self.render_view.AxesGrid.Visibility = 1

        z_axes_scale = self._z_axes_scale()

        self._display.Scale = [1.0, 1.0, z_axes_scale]
        self._display.PolarAxes.Scale = [1.0, 1.0, z_axes_scale]

        self.render_view.AxesGrid.DataScale = [1.0, 1.0, -z_axes_scale]

        self.render_view.AxesGrid.Modified()

    def _setup_display(self):
        self._pipeline.get_output().UpdatePipeline
        self._display = Show(
            self._pipeline.get_output(),
            self._render_view,
            "UnstructuredGridRepresentation",
        )

        self.color_by(DEFAULT_ARRAY)

    def color_by(self, array):
        # get 2D transfer function for 'U'
        tf2D = GetTransferFunction2D(array)

        # get color transfer function/color map for 'U'
        lut = GetColorTransferFunction(array)
        lut.TransferFunction2D = tf2D
        lut.ScalarRangeInitialized = 1.0

        # get opacity transfer function/opacity map for 'U'
        pwf = GetOpacityTransferFunction(array)
        pwf.Points = [
            -21.407419204711914,
            0.0,
            0.5,
            0.0,
            52.09690856933594,
            1.0,
            0.5,
            0.0,
        ]
        pwf.ScalarRangeInitialized = 1

        # trace defaults for the display properties.
        self._display.Representation = "Surface"
        self._display.ColorArrayName = ["POINTS", array]
        self._display.LookupTable = lut
        self._display.SelectTCoordArray = "None"
        self._display.SelectNormalArray = "None"
        self._display.SelectTangentArray = "None"
        self._display.Scale = [1.0, 1.0, self._z_axes_scale()]
        self._display.Texture = None
        self._display.BaseColorTexture = None
        self._display.NormalTexture = None
        self._display.CoatNormalTexture = None
        self._display.MaterialTexture = None
        self._display.AnisotropyTexture = None
        self._display.EmissiveTexture = None
        self._display.OSPRayScaleArray = "ANRAIN"
        self._display.OSPRayScaleFunction = "PiecewiseFunction"
        self._display.SelectOrientationVectors = "None"
        self._display.ScaleFactor = 36.00000000000003
        self._display.SelectScaleArray = "ANRAIN"
        self._display.GlyphType = "Arrow"
        self._display.GlyphTableIndexArray = "ANRAIN"
        self._display.GaussianRadius = 1.8000000000000014
        self._display.SetScaleArray = ["POINTS", "ANRAIN"]
        self._display.ScaleTransferFunction = "PiecewiseFunction"
        self._display.OpacityArray = ["POINTS", "ANRAIN"]
        self._display.OpacityTransferFunction = "PiecewiseFunction"
        self._display.DataAxesGrid = "GridAxesRepresentation"
        self._display.PolarAxes = "PolarAxesRepresentation"
        self._display.ScalarOpacityFunction = pwf
        self._display.ScalarOpacityUnitDistance = 3.599181859937947
        self._display.OpacityArrayName = ["POINTS", "ANRAIN"]
        self._display.SelectInputVectors = ["POINTS", ""]
        self._display.WriteLog = ""
        self._display.PolarAxes.Scale = [1.0, 1.0, self._z_axes_scale()]

        # Hide the previous one
        if self._lut_color_bar is not None:
            self._lut_color_bar.Visibility = 0

        # Get the new one
        self._lut_color_bar = GetScalarBar(lut, self._render_view)
        self._lut_color_bar.Orientation = "Horizontal"
        self._lut_color_bar.WindowLocation = "Any Location"
        self._lut_color_bar.Position = [0.43910211267605626, 0.011074766355140209]
        self._lut_color_bar.Title = array
        self._lut_color_bar.ComponentTitle = ""
        self._lut_color_bar.ScalarBarLength = 0.33000000000000007

        # set color bar visibility
        self._lut_color_bar.Visibility = 1

        # show color legend
        self._display.SetScalarBarVisibility(self._render_view, True)

    @property
    def render_view(self):
        return self._render_view

    def _update_axes_actor(self):
        # Hack to ensure AxesGrid is updated in trame!
        self.render_view.AxesGrid.Visibility = False
        Render(view=self.render_view)
        self.render_view.AxesGrid.Visibility = True
        Render(view=self.render_view)

    def create_component(self):
        server = get_server()
        state, _ = server.state, server.controller
        ln_z_axis_key = f"view_{id(self)}_ln_z_axis"

        @state.change(ln_z_axis_key)
        def on_ln_z_axis_change(*parg, **kwargs):
            value = kwargs[ln_z_axis_key]
            self._pipeline.enable_ln(value)
            self._pipeline.get_output().UpdatePipeline()
            self._z_log_scale = value

            z_scale = self._z_axes_scale()
            self._display.Scale = [1.0, 1.0, -z_scale]
            self._setup_axes()
            self._update_axes_actor()
            self.update()

        variables = self._pipeline.get_output().PointData.keys()
        color_by_state_key = f"view_{id(self)}_color_by"
        z_axis_scalar_state_key = f"view_{id(self)}_z_axis_scalar"

        @state.change(color_by_state_key)
        def on_color_by_changed(*pargs, **kwargs):
            array = kwargs[color_by_state_key]
            self.color_by(array)
            self.update()

        @state.change(z_axis_scalar_state_key)
        def on_z_axis_scalar_changed(*pargs, **kwargs):
            array = kwargs[z_axis_scalar_state_key]
            self._pipeline.z_scalar = array
            self._setup_axes()
            self._update_axes_actor()
            self.update()

        with vuetify.VContainer(fluid=True, classes="pa-0 fill-height"):
            with vuetify.VRow(dense=True, style="height: 90%;"):
                with vuetify.VCol():
                    self._view = paraview.VtkRemoteView(
                        self._render_view, ref=f"view{id(self)}"
                    )
            with vuetify.VRow(dense=True, style="height: 10%;"):
                with vuetify.VContainer(fluid=True, classes="pa-0 fill-height"):
                    with vuetify.VRow(
                        dense=True, style="height: 100%;", classes="justify-end"
                    ):
                        with vuetify.VCol():
                            vuetify.VSelect(
                                # Color By
                                label="Color by",
                                v_model=(color_by_state_key, DEFAULT_ARRAY),
                                items=("array_list", variables),
                                dense=True,
                                outlined=True,
                            )
                        with vuetify.VCol():
                            vuetify.VSelect(
                                # Color By
                                label="Z Axis",
                                v_model=(
                                    z_axis_scalar_state_key,
                                    self._pipeline.z_axes_array_names()[0],
                                ),
                                items=(
                                    "z_axes_array_list",
                                    self._pipeline.z_axes_array_names(),
                                ),
                                dense=True,
                                outlined=True,
                            )
                        with vuetify.VCol():
                            vuetify.VCheckbox(
                                v_model=(ln_z_axis_key, False),
                                label="Apply ln to Z",
                                dense=True,
                                classes="mx-2",
                            )

    def update(self):
        self._view.update()


views = []


class App:
    def __init__(self, data_dir):
        self._server = get_server()
        self._reader = self._create_source(data_dir)
        SetActiveSource(self._reader)

        self._views = []

        for i in range(0, 4):
            view = View(self._reader)
            self._views.append(view)

        # self._create_layout()
        self._create_single_page()

    def _create_source(self, data_dir):
        # create a new 'NetCDF CAM reader'
        source = NetCDFCAMreader(
            registrationName="PD_1800_ad4fd8_ANN_climo_SE.nc",
            ConnectivityFileName=f"{data_dir}/ne30np4_latlon.nc",
            FileName=[f"{data_dir}/PD_1800_ad4fd8_ANN_climo_SE.nc"],
        )

        return source

    def _render_views(self):
        return [v.render_view for v in self._views]

    def _create_single_page(self):
        server = get_server()
        _, ctrl = server.state, server.controller

        def update_views(**kwargs):
            for v in self._views:
                v.update()

        ctrl.on_server_ready.add(ctrl.view_update)
        ctrl.view_update = update_views

        [view1, view2, view3, view4] = self._views

        with SinglePageLayout(server) as layout:
            with layout.content:
                layout.title.set_text("EAM Application")
                with vuetify.VContainer(fluid=True, classes="pa-0 fill-height"):
                    with vuetify.VRow(dense=True, style="height: 50%;"):
                        with vuetify.VCol():
                            view1.create_component()
                        with vuetify.VCol():
                            view2.create_component()
                    with vuetify.VRow(dense=True, style="height: 50%;"):
                        with vuetify.VCol():
                            view3.create_component()
                        with vuetify.VCol():
                            view4.create_component()

    def start(self):
        self._server.start()


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

    app = App(args.data_dir)
    app.start()


main()
