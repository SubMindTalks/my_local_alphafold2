#!/bin/bash
set -e

echo "Step 1: Clone the AlphaFold repository"
git clone https://github.com/deepmind/alphafold.git
cd alphafold

echo "Step 2: Create and activate Python virtual environment"
python3 -m venv alphafold_env
source alphafold_env/bin/activate
pip install --upgrade pip

echo "Step 3: Install Python dependencies"
pip install -r requirements.txt
pip install absl-py==1.0.0
pip install jax==0.4.26 jaxlib==0.4.26+cuda12.cudnn89 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

echo "Step 4: Clone and build PDBFixer"
git clone https://github.com/openmm/pdbfixer.git
cd pdbfixer
python setup.py install
cd ..

echo "Step 5: Verify AlphaFold installation"
python3 -c "import pdbfixer; print('PDBFixer installed successfully')"
python3 -m alphafold

echo "Download and build complete!"
