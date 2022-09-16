# EAM Trame Example


# Setup

* Install [pyenv](https://github.com/pyenv/pyenv)
* Install python 3.9.13
  * `pyenv install 3.9.13`
* Create a virtualenv using this python version
  * `pyenv virtualenv 3.9.13 eam`
* Activate the virtualenv
  * `pyenv virtualenv activate eam`
* Install trame
  * `pip install trame`
* Export environment variable so ParaView can find the virtualenv
  * `export PV_VENV=$PYENV_VIRTUAL_ENV`

# Run

* Single Layer
  * `<pvpython> <eam_repo>/single_layer.py -x <path_data_and_connectivity_file>`
* 3D Fields
  * `<pvpython> <eam_repo>/3d_fields.py -x <path_data_and_connectivity_file>`