 
# 1. Setup virtual environment
cd Demo_SARCMedIQ
sudo pip3 install virtualenv

# 2. Make a directory
mkdir .venv

# 3. Create virtual environment
virtualenv ./.venv/

# 4. Activate virtual environment
source .venv/bin/activate

# 5. Install requirements
pip3 install -r requirements.txt
 
# 6. Make migrations
python3 manage.py makemigrations
python3 manage.py migrate

# 7. Run the server
python3 manage.py runserver 0:8000

python3 manage.py startapp Patient