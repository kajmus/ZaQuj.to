Poniżej kroki dla Windowsa (PowerShell).

1. Utwórz venv w folderze backend


cd backend
python -m venv venv

Powstanie folder backend\venv.

2. Aktywuj go
.\venv\Scripts\Activate.ps1

Jeśli PowerShell zgłosi błąd o polityce wykonywania skryptów, wykonaj raz:


Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Po aktywacji na początku linii zobaczysz (venv).

3. Zainstaluj zależności


pip install --upgrade pip
pip install fastapi "uvicorn[standard]"

albo, jeśli masz już requirements.txt:


pip install -r requirements.txt

Żeby wygenerować requirements.txt z aktualnie zainstalowanych paczek:


pip freeze > requirements.txt

4. Uruchom serwer


python -m uvicorn app.main:app --reload

5. Wyjście z venv


deactivate

=====================================================================================================================================================
Linux


1. Doinstaluj obsługę venv (tylko Debian/Ubuntu, raz)


sudo apt update
sudo apt install python3 python3-venv python3-pip

2. Utwórz i aktywuj venv


cd backend
python3 -m venv venv
source venv/bin/activate

Na początku linii pojawi się (venv).

3. Zainstaluj zależności


pip install --upgrade pip
pip install -r requirements.txt

4. Uruchom serwer


python -m uvicorn app.main:app --reload

5. Wyjście z venv

deactivate