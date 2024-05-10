# Python 3.11.5
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start project
python main.py
# Hot reload
gradio main.py --demo-name=my_demo