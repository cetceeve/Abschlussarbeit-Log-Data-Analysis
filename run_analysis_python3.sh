echo 'starting analysis'
mkdir -p out/
python3 analysis_per_user.py
python3 analysis_alt_tct.py
python3 analysis_usage_time.py
python3 analysis_interaction_on_elements.py
echo 'finished'
