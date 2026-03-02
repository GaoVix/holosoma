# python src/holosoma_retargeting/holosoma_retargeting/data_utils/human_body_prior/prep_amass_smplx_for_rt.py \
#     --amass-root-folder "/mnt/projects/dataset/amass" \
#     --output-folder "/mnt/projects/holosoma/processed" \
#     --model-root-folder "/mnt/projects/holosoma/" \
#     --motion-list "lists/f3.txt"

# python src/holosoma_retargeting/holosoma_retargeting/data_utils/human_body_prior/prep_amass_smplx_for_rt.py \
#     --amass-root-folder "/mnt/projects/dataset/amass" \
#     --output-folder "/mnt/projects/holosoma/processed" \
#     --model-root-folder "/mnt/projects/holosoma/" \
#     --motion-list "lists/f2.txt"


# python src/holosoma_retargeting/holosoma_retargeting/data_utils/human_body_prior/prep_amass_smplx_for_rt.py \
#     --amass-root-folder "/mnt/projects/dataset/amass" \
#     --output-folder "/mnt/projects/holosoma/processed" \
#     --model-root-folder "/mnt/projects/holosoma/" \
#     --motion-list "lists/f1.txt"

# python src/holosoma_retargeting/holosoma_retargeting/data_utils/human_body_prior/prep_amass_smplx_for_rt.py \
#     --amass-root-folder "/mnt/projects/dataset/amass" \
#     --output-folder "/mnt/projects/holosoma/processed" \
#     --model-root-folder "/mnt/projects/holosoma/" \
#     --motion-list "lists/f0.txt"


python src/holosoma_retargeting/holosoma_retargeting/data_utils/human_body_prior/prep_amass_smplx_for_rt.py \
    --amass-root-folder "/mnt/projects/dataset/amass" \
    --output-folder "/mnt/projects/holosoma/processed" \
    --model-root-folder "/mnt/projects/holosoma/" \
    --motion-list "lists/supp2.txt"


# python src/holosoma_retargeting/holosoma_retargeting/examples/retarget.py \
#     --processed-data-dir "/mnt/projects/holosoma/processed" \
#     --output-path "/mnt/projects/holosoma/retargeted" \
#     --motion-list "lists/f3.txt" \
#     --time-file "/mnt/projects/holosoma/retargeted/holosoma_f3.csv"

# python src/holosoma_retargeting/holosoma_retargeting/examples/retarget.py \
#     --processed-data-dir "/mnt/projects/holosoma/processed" \
#     --output-path "/mnt/projects/holosoma/retargeted" \
#     --motion-list "lists/f2.txt" \
#     --time-file "/mnt/projects/holosoma/retargeted/holosoma_f2.csv"

# python src/holosoma_retargeting/holosoma_retargeting/examples/retarget.py \
#     --processed-data-dir "/mnt/projects/holosoma/processed" \
#     --output-path "/mnt/projects/holosoma/retargeted" \
#     --motion-list "lists/f1.txt" \
#     --time-file "/mnt/projects/holosoma/retargeted/holosoma_f1.csv"

# python src/holosoma_retargeting/holosoma_retargeting/examples/retarget.py \
#     --processed-data-dir "/mnt/projects/holosoma/processed" \
#     --output-path "/mnt/projects/holosoma/retargeted" \
#     --motion-list "lists/f0.txt" \
#     --time-file "/mnt/projects/holosoma/retargeted/holosoma_f0.csv"

python src/holosoma_retargeting/holosoma_retargeting/examples/retarget.py \
    --processed-data-dir "/mnt/projects/holosoma/processed" \
    --output-path "/mnt/projects/holosoma/retargeted" \
    --motion-list "lists/supp2.txt" \
    --time-file "/mnt/projects/holosoma/retargeted/holosoma_supp2.csv"