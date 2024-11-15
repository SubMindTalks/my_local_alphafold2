#!/bin/bash
set -e

DATA_DIR=$1

if [ -z "$DATA_DIR" ]; then
    echo "Usage: $0 <path_to_alphafold_data>"
    exit 1
fi

echo "Step 1: Verify data directory structure"
mkdir -p $DATA_DIR
bash scripts/download_all_data.sh $DATA_DIR

echo "Step 2: Update database paths in AlphaFold scripts"
cd alphafold
sed -i "s|--uniref90_database_path=None|--uniref90_database_path=$DATA_DIR/uniref90/uniref90.fasta|g" run_alphafold.py
sed -i "s|--mgnify_database_path=None|--mgnify_database_path=$DATA_DIR/mgnify/mgy_clusters_2022_05.fa|g" run_alphafold.py
sed -i "s|--template_mmcif_dir=None|--template_mmcif_dir=$DATA_DIR/pdb_mmcif|g" run_alphafold.py
sed -i "s|--obsolete_pdbs_path=None|--obsolete_pdbs_path=$DATA_DIR/obsolete.dat|g" run_alphafold.py

echo "Preparation for test run complete!"
