#!/bin/bash
set -e

echo "Step 1: Activate Python environment"
source alphafold/alphafold_env/bin/activate

echo "Step 2: Run AlphaFold test"
cd alphafold
python run_alphafold.py --fasta_paths=test_sequences/test.fasta --output_dir=test_output --max_template_date=2024-01-01 --db_preset=full_dbs --use_gpu_relax=True

echo "Test run complete!"
