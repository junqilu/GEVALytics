# GEVALytics
This repository includes a data analysis pipeline that standardizes the 
processing of microscopy images from the GTP biosensor (GEVAL). It also features a machine learning model that uses image features, extracted by the ImageJ plugin [GEVALIris](https://github.com/junqilu/GEVALIris), to screen out suboptimal images.

You can read [here](GEVALIris_GEVALytics_presentation.pdf)  for 
more information on the importance of measuring unbound GTP concentrations in live cells and how these measurements reveal the influence of GTP concentration on protrusions and the invasiveness of melanoma.
* GEVAL was developed by the Nikiforov Lab in the Biomedical Engineering 
  Department at Duke University and was featured in a [Nature publication](https://www.nature.com/articles/s41467-021-26324-6).

# Workflow
## Wet lab operations
![wet_lab_workflow.png](readme_images/wet_lab_workflow.png)

## GEVALIris
For more details regarding how the ImageJ plugin GEVALIris extracts image 
features, please 
refer to this GitHub repository [GEVALIris](https://github.com/junqilu/GEVALIris).
![GEVALIris_ImageJ_plugin.png](readme_images/GEVALIris_ImageJ_plugin.png)

## Heatmap data analysis pipeline
![heatmap_data_analysis_pipeline.png](readme_images/heatmap_data_analysis_pipeline.png)

## Machine learning model
![ML_model.png](readme_images/ML_model.png)

The combination of the ImageJ plugin ***GEVALIris*** and the machine learning 
model ***GEVALytics*** enables automatic image screening with expert-level 
accuracy and strong generalization. This system effectively identifies 
suboptimal images, providing GEVAL users with a reliable solution that can 
be utilized __anytime__ and __anywhere__.
