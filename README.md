# locustio installation wiht virtualenv

python3 -m venv {project_dir}/venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
locust -f locustfile.py
