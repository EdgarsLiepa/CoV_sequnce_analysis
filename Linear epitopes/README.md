# Predict epitope structures Using ESM fold

## Dependecies.

Hugging face Transformers

[Installation](https://huggingface.co/docs/transformers/installation)

Transformers are standertized API that combines open source Inference models.

For this task ESMFold model is used.

[ESM Github](https://github.com/facebookresearch/esm#quickstart)


## Files

[generate-3D-struct-combinations.ipynb](./generate-3D-struct-combinations.ipynb) - generate vaccine insert sequences from multiple epitopes and defined linkers starting and end linkers.
Then distances between N and C ends are calculated.

[show_best_models.ipynb](./show_best_models.ipynb) - display calculated 3D structures and calculate distance between N and C ends. 

