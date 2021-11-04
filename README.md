////venv///////////////////////////////////////
<<start>>
wsl
source venv_wsl/bin/activate
cd app
python main.py
<<stop>>
CTRT + C
deactivate
exit

////docker-compose////////////////////////////
<<start>>
docker-compose up
<<stop>>
CTRT + C
docker-compose down