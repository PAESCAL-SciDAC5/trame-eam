# EAM Trame Example


# Setup

* Create conda environment containing ParaView
  * `conda create -n eam -c cjh1 -c conda-forge paraview`
  * `conda activate eam`

# Run

* Single Layer
  * `python <eam_repo>/single_layer.py -x <path_containing_data_and_connectivity_file>`
* 3D Fields
  * `python <eam_repo>/3d_fields.py -x <path_to_data_file> -o <path_to_connectivity_file>`