echo 'starting analysis'
mkdir -p out/
python analysis_per_user.py
python analysis_alt_tct.py
python analysis_usage_time.py
python analysis_interaction_on_elements.py
echo 'finished'
