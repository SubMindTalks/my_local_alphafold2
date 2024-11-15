# Running AlphaFold

## Introduction

This guide will walk you through the process of predicting the structure of a protein using **AlphaFold** with the provided `AlphaFold.ipynb` notebook.

AlphaFold is a cutting-edge protein structure prediction tool developed by DeepMind. This notebook offers a simplified version of AlphaFold v2.3.2 that can be run on Google Colab.

## Step-by-Step Guide

### 1. Open the Notebook

First, locate and open the `AlphaFold.ipynb` notebook in the `notebooks/` directory.

### 2. Setup Environment

**Run the Setup Cells:**

- **Cell 1:** This cell ensures that the environment is appropriately set up by importing necessary modules and setting environment variables.

```python
import os
os.environ['TF_FORCE_UNIFIED_MEMORY'] = '1'
os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'] = '4.0'
```

- **Cell 2:** This cell handles the installation of third-party software including TensorFlow, py3Dmol, OpenMM, and more. Ensure you press the play button to execute the cell.

```python
from IPython.utils import io
import os
import subprocess
import tqdm.notebook

...
```

- **Cell 3:** This cell downloads AlphaFold and its dependencies, ensuring everything is installed correctly for running the model.

```python
GIT_REPO = 'https://github.com/deepmind/alphafold'
SOURCE_URL = 'https://storage.googleapis.com/alphafold/alphafold_params_colab_2022-12-06.tar'
...
```

### 3. Providing Input Sequences

**Enter the amino acid sequence(s) to fold:**

- **Cell 4:** This cell prompts you to enter the amino acid sequence(s) for the protein(s) you wish to predict. If you enter multiple sequences, it will run the multimer model.

```python
sequence_1 = 'MAAHKGAEHHHK...'
...
use_multimer_model_for_monomers = False  #@param {type:"boolean"}

...
```

### 4. Running the Prediction

**Search against genetic databases and run AlphaFold:**

- **Cell 5:** This cell performs the search against genetic databases to find multiple sequence alignments (MSAs) that will be used for the prediction.

```python
def get_msa(sequences):
    ...
```

- **Cell 6:** This cell runs the AlphaFold model to generate the protein structure prediction based on the input sequences and MSA data.

```python
run_relax = True  #@param {type:"boolean"}
relax_use_gpu = False  #@param {type:"boolean"}
...
files.download(f'{output_dir}.zip')
```

### 5. Interpret the Prediction

After the prediction is complete, the notebook will download a zip file containing the predicted structures to your computer. You can visualize the structures and assess the confidence levels using the provided visualizations and understanding how to interpret pLDDT and PAE values.

### FAQ & Troubleshooting

Some common questions and troubleshooting steps are provided at the end of the notebook to help you resolve any issues you might encounter during the run.

### Citing AlphaFold

If you use this notebook for any publication or research, make sure you cite the original AlphaFold paper as mentioned at the top of the notebook.

### License & Disclaimer

The notebook and the AlphaFold code are provided under the Apache 2.0 License, and the AlphaFold model parameters are licensed under the Creative Commons Attribution 4.0 International License. Please refer to the license section at the end of the notebook for complete details.

## Conclusion

Following these steps will allow you to run AlphaFold and predict protein structures using the provided Jupyter notebook. For any advanced usage or further customization, please refer to the official [AlphaFold GitHub repository](https://github.com/deepmind/alphafold).