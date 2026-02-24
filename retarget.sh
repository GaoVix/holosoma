#!/bin/bash
set -euo pipefail

# PROCESSED_DATA_DIR="/mnt/Exp_ziqian/projects/holosoma/processed2"
# OUTPUT_DIR="/mnt/Exp_ziqian/projects/holosoma/retargeted2"
# MOTION_LIST="/mnt/Exp_HDD/projects/spider_n/spider/test.txt"
# SMPLX_MODEL_DIR="/mnt/Exp_ziqian/projects/phuma/PHUMA/asset/human_model"
# SMPLX_DATA_DIR="/mnt/Exp_HDD/ori_data"

PROCESSED_DATA_DIR="${1:?Need PROCESSED_DATA_DIR}"
OUTPUT_DIR="${2:?Need OUTPUT_DIR}"
MOTION_LIST="${3:?Need MOTION_LIST}"
SMPLX_MODEL_DIR="${4:?Need SMPLX_MODEL_DIR}"
SMPLX_DATA_DIR="${5:?Need SMPLX_DATA_DIR}"

python src/holosoma_retargeting/holosoma_retargeting/data_utils/human_body_prior/prep_amass_smplx_for_rt.py \
    --amass-root-folder "$SMPLX_DATA_DIR" \
    --output-folder "$PROCESSED_DATA_DIR" \
    --model-root-folder "$SMPLX_MODEL_DIR" \
    --motion-list "$MOTION_LIST"

python src/holosoma_retargeting/holosoma_retargeting/examples/retarget.py \
    --processed-data-dir "$PROCESSED_DATA_DIR" \
    --output-path "$OUTPUT_DIR" \
    --motion-list "$MOTION_LIST"