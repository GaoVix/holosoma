
import argparse
import os
import sys
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple
import yaml
from tqdm import tqdm
import time, csv

project_root = Path(__file__).resolve().parent.parent

def smpl_to_smplx(key_name):
    key_name = key_name.replace("SSM_synced", "SSM")
    key_name = key_name.replace("MPI_HDM05", "HDM05")
    key_name = key_name.replace("MPI_mosh", "MoSh")
    key_name = key_name.replace("MPI_Limits", "PosePrior")
    key_name = key_name.replace("TCD_handMocap", "TCDHands")
    key_name = key_name.replace("Transitions_mocap", "Transitions")
    key_name = key_name.replace("DFaust_67", "DFaust")
    key_name = key_name.replace("BioMotionLab_NTroje", "BMLrub")
    key_name = key_name.replace("EyesJapanDataset","Eyes_Japan_Dataset")

    return key_name

def load_motion_list(txt_path: Path) -> List[str]:
    """Load motion identifiers from txt file."""
    entries = []
    with open(txt_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(line)
    return entries

def run_command(cmd: List[str], cwd: Path, description: str = "Running command") -> int:
    """Run a shell command and return the exit code."""
    print(f"\n{'='*60}")
    print(f"{description}")
    print(f"{'='*60}")
    print(f"Command: {' '.join(cmd)}")
    print(f"CWD: {cwd}")

    env = os.environ.copy()
    env["PYTHONPATH"] = str(get_project_root()) + os.pathsep + env.get("PYTHONPATH", "")
    result = subprocess.run(cmd, cwd=cwd, env=env, check=False)
    return result.returncode

def run_shell_command(cmd: List[str], cwd: Path, description: str = "Running command") -> int:
    """Run a shell command and return the exit code."""
    print(f"\n{'='*60}")
    print(f"{description}")
    print(f"{'='*60}")
    print(f"Command: {' '.join(cmd)}")
    print(f"CWD: {cwd}")

    result = subprocess.run(cmd, cwd=cwd, shell=False, check=False)
    return result.returncode

def get_project_root() -> Path:
    """Get the project root directory (where protomotions/ and scripts/ folders are located)."""
    # Script is at data/scripts/prepare_rollout_data.py
    # Go up 3 levels: data/scripts -> data -> project_root (/workspace)
    return Path(__file__).resolve().parent.parent.parent

def create_parser():
    """Create and configure the argument parser for inference."""
    parser = argparse.ArgumentParser(
        description="Test trained reinforcement learning agent",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--output-path",
        type=str,
        default='/mnt/Exp_ziqian/projects/holosoma/retargeted',
        help="Path to save the results",
    )
    parser.add_argument(
        "--processed-data-dir",
        type=str,
        default='/mnt/Exp_ziqian/projects/spider/gmr/',
    )
    parser.add_argument(
        "--motion-list",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--time-file",
        type=str,
        required=True,
    )
    return parser

def process_data(args, motion_list):

    # script = project_root / "src" / "holosoma_retargeting" / "holosoma_retargeting" / "examples" / "robot_retarget.py"
    script = project_root / "examples" / "robot_retarget.py"

    processed = 0
    for motion_path in tqdm(motion_list, desc="Retargeting files"):
        motion_path = smpl_to_smplx(motion_path).replace('_poses.', '_stageii.').replace(".npy", ".pkl").replace(".pkl", ".npz").replace(' ', '_')

        motion_path_rel = Path(*Path(motion_path).parts[-3:])
        motion_path_abs = Path(args.processed_data_dir) / motion_path_rel

        output = Path(args.output_path) / motion_path_rel
        if output.exists():
            print(f'Found retargeted data at {output}, continue ...')
            continue

        cmd = [
            sys.executable, str(script),
            "--data_path", f"{motion_path_abs}",
            f"--task-type", 'robot_only',
            "--data_format", 'smplx',
            "--task-config.ground-range", "-10", "10",
            f"--save_dir", f"{args.output_path}"
        ]

        run_command(cmd, project_root, "Retargeting")
        processed += 1


def retarget(args, motion_list):

    # script = project_root / "src" / "holosoma_retargeting" / "holosoma_retargeting" / "examples" / "robot_retarget.py"
    script = project_root / "examples" / "robot_retarget.py"
    times = []
    processed = 0
    try:
        for motion_path in tqdm(motion_list, desc="Retargeting files"):
            motion_path = smpl_to_smplx(motion_path).replace('_poses.', '_stageii.').replace(".npy", ".pkl").replace(".pkl", ".npz").replace(' ', '_')

            motion_path_rel = Path(*Path(motion_path).parts[-3:])
            motion_path_abs = Path(args.processed_data_dir) / motion_path_rel

            output = Path(args.output_path) / motion_path_rel
            if output.exists():
                print(f'Found retargeted data at {output}, continue ...')
                continue

            cmd = [
                sys.executable, str(script),
                "--data_path", f"{motion_path_abs}",
                f"--task-type", 'robot_only',
                "--data_format", 'smplx',
                "--task-config.ground-range", "-10", "10",
                f"--save_dir", f"{args.output_path}"
            ]
            s_time = time.time()
            run_command(cmd, project_root, "Retargeting")
            e_time = time.time()
            processed += 1

            rtgt_time =  e_time - s_time
            info = [motion_path, rtgt_time]
            times.append(info)
            print(info)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        file_path = args.time_file
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)

            header = ['Motion', 'Processing Time']
            writer.writerow(header)

            for row in times:
                writer.writerow(row)


        print(f'Finished, file saved to {file_path}')

def load_motion_list(txt_path: Path) -> List[str]:
    """Load motion identifiers from txt file."""
    entries = []
    with open(txt_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(line)
    return entries

def main():
    parser = create_parser()
    args = parser.parse_args()
    motion_list = load_motion_list(args.motion_list)
    retarget(args, motion_list)

if __name__ == "__main__":
    main()
