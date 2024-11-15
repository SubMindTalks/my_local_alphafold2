import subprocess
import os
from typing import Optional


def run_command(command: str, env: Optional[dict] = None) -> subprocess.CompletedProcess:
    """
    Executes a shell command and returns the result.
    """
    print(f"Running command: {command}")
    return subprocess.run(command, shell=True, check=True, env=env)


def update_and_upgrade() -> None:
    """
    Updates and upgrades system packages.
    """
    print("Step 1: Updating and upgrading system packages...")
    run_command("sudo apt-get update -y")
    run_command("sudo apt-get upgrade -y")


def install_dependencies() -> None:
    """
    Installs essential system dependencies.
    """
    print("Step 2: Installing essential dependencies...")
    dependencies = [
        "build-essential",
        "cmake",
        "git",
        "wget",
        "curl",
        "aria2",
        "python3",
        "python3-pip",
        "python3-venv",
        "software-properties-common",
        "tree",
    ]
    run_command(f"sudo apt-get install -y {' '.join(dependencies)}")


def install_cuda() -> None:
    """
    Installs CUDA Toolkit 12.6 and configures environment variables.
    """
    print("Step 3: Installing CUDA Toolkit 12.6...")
    run_command("wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-ubuntu2404.pin")
    run_command("sudo mv cuda-ubuntu2404.pin /etc/apt/preferences.d/cuda-repository-pin-600")
    run_command(
        "sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/3bf863cc.pub"
    )
    run_command(
        'sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/ /"'
    )
    run_command("sudo apt-get update -y")
    run_command("sudo apt-get install -y cuda-toolkit-12-6")

    # Update environment variables
    cuda_bin_path = "/usr/local/cuda-12.6/bin"
    cuda_lib_path = "/usr/local/cuda-12.6/lib64"
    os.environ["PATH"] = f"{cuda_bin_path}:{os.environ.get('PATH', '')}"
    os.environ["LD_LIBRARY_PATH"] = f"{cuda_lib_path}:{os.environ.get('LD_LIBRARY_PATH', '')}"

    with open(os.path.expanduser("~/.bashrc"), "a") as bashrc:
        bashrc.write(f"\nexport PATH={cuda_bin_path}:$PATH\n")
        bashrc.write(f"export LD_LIBRARY_PATH={cuda_lib_path}:$LD_LIBRARY_PATH\n")
    print("CUDA Toolkit installed and environment variables configured.")


def install_anaconda() -> None:
    """
    Installs Anaconda for Python package management.
    """
    print("Step 4: Installing Anaconda...")
    anaconda_url = "https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh"
    run_command(f"wget {anaconda_url}")
    run_command("bash Anaconda3-2024.10-1-Linux-x86_64.sh -b -p ~/anaconda3")
    os.environ["PATH"] = f"~/anaconda3/bin:{os.environ.get('PATH', '')}"

    with open(os.path.expanduser("~/.bashrc"), "a") as bashrc:
        bashrc.write("\nexport PATH=~/anaconda3/bin:$PATH\n")
    print("Anaconda installed successfully.")


def clone_alphafold() -> None:
    """
    Clones the AlphaFold repository.
    """
    print("Cloning the AlphaFold repository...")
    run_command("git clone https://github.com/deepmind/alphafold.git")
    os.chdir("alphafold")


def setup_virtualenv() -> None:
    """
    Sets up a Python virtual environment.
    """
    print("Setting up Python virtual environment...")
    run_command("python3 -m venv alphafold_env")
    run_command("source alphafold_env/bin/activate")
    run_command("pip install --upgrade pip")


def install_python_dependencies() -> None:
    """
    Installs Python dependencies for AlphaFold.
    """
    print("Installing Python dependencies...")
    run_command("pip install -r requirements.txt")
    run_command("pip install absl-py==1.0.0")
    run_command(
        "pip install jax==0.4.26 jaxlib==0.4.26+cuda12.cudnn89 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html"
    )


def clone_and_build_pdbfixer() -> None:
    """
    Clones and builds PDBFixer.
    """
    print("Cloning and building PDBFixer...")
    run_command("git clone https://github.com/openmm/pdbfixer.git")
    os.chdir("pdbfixer")
    run_command("python setup.py install")
    os.chdir("..")


def verify_alphafold_installation() -> None:
    """
    Verifies the AlphaFold installation.
    """
    print("Verifying AlphaFold installation...")
    run_command("python3 -c 'import pdbfixer; print(\"PDBFixer installed successfully\")'")
    print("AlphaFold installation verified.")


def verify_data_directory_structure(data_dir: str) -> None:
    """
    Verifies and sets up the data directory for AlphaFold.
    """
    print("Verifying data directory structure...")
    os.makedirs(data_dir, exist_ok=True)
    run_command(f"bash scripts/download_all_data.sh {data_dir}")


def update_database_paths(data_dir: str) -> None:
    """
    Updates database paths in AlphaFold scripts.
    """
    print("Updating database paths in AlphaFold scripts...")
    replacements = {
        "--uniref90_database_path=None": f"--uniref90_database_path={data_dir}/uniref90/uniref90.fasta",
        "--mgnify_database_path=None": f"--mgnify_database_path={data_dir}/mgnify/mgy_clusters_2022_05.fa",
        "--template_mmcif_dir=None": f"--template_mmcif_dir={data_dir}/pdb_mmcif",
        "--obsolete_pdbs_path=None": f"--obsolete_pdbs_path={data_dir}/obsolete.dat",
    }

    with open("run_alphafold.py", "r") as file:
        content = file.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open("run_alphafold.py", "w") as file:
        file.write(content)
    print("Database paths updated.")


def run_alphafold_test() -> None:
    """
    Runs a test for AlphaFold.
    """
    print("Running AlphaFold test...")
    run_command(
        "python run_alphafold.py --fasta_paths=test_sequences/test.fasta --output_dir=test_output "
        "--max_template_date=2024-01-01 --db_preset=full_dbs --use_gpu_relax=True"
    )
    print("Test run complete!")


def main() -> None:
    update_and_upgrade()
    install_dependencies()
    install_cuda()
    install_anaconda()
    clone_alphafold()
    setup_virtualenv()
    install_python_dependencies()
    clone_and_build_pdbfixer()
    verify_alphafold_installation()
    data_dir = "/path/to/alphafold_data"  # Replace with actual path
    verify_data_directory_structure(data_dir)
    update_database_paths(data_dir)
    run_alphafold_test()


if __name__ == "__main__":
    main()
