

PROCESSED_DATA_DIR="/mnt/Exp_ziqian/projects/holosoma/processed2"
OUTPUT_DIR="/mnt/Exp_ziqian/projects/holosoma/retargeted2"
MOTION_LIST="/mnt/Exp_HDD/projects/spider_n/spider/test.txt"
SMPLX_MODEL_DIR="/mnt/Exp_ziqian/projects/phuma/PHUMA/asset/human_model"
SMPLX_DATA_DIR="/mnt/Exp_HDD/ori_data"

python src/holosoma_retargeting/holosoma_retargeting/data_utils/human_body_prior/prep_amass_smplx_for_rt.py \
    --amass-root-folder "$SMPLX_DATA_DIR" \
    --output-folder "$PROCESSED_DATA_DIR" \
    --model-root-folder "$SMPLX_MODEL_DIR" \
    --motion-list "$MOTION_LIST"

python src/holosoma_retargeting/holosoma_retargeting/examples/retarget.py \
    --processed-data-dir "$PROCESSED_DATA_DIR" \
    --output-path "$OUTPUT_DIR" \
    --motion-list "$MOTION_LIST"