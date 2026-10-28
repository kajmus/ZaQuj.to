#file for building project
# to run type in powershell:         python .\build.py
"""
if server got stuck on widnows:
Get-NetTCPConnection -LocalPort 8000 -State Listen |
    Select-Object LocalAddress, LocalPort, OwningProcess

check that id:
Get-CimInstance Win32_Process -Filter "ProcessId = 12345" |
    Select-Object ProcessId, ParentProcessId, Name, CommandLine
then paste the id in and kill it:
Stop-Process -Id 12345 -Force
"""
import os
import platform


#config
#set to True what you want to build all else to False
FIRST_SETUP = False
BUILD_FRONTEND = False

RUN_DEVELOPMENT = True
RUN_PRODUCTION = False

if (platform.system() == "Windows"):
    if (FIRST_SETUP):
        os.system("cd backend && pip install -r requirements.txt")
        os.system("cd frontend && npm install")
        # os.system("cd frontend && npm run build")
        print("First setup completed. You can now run the project.")
        exit(0)

    if (RUN_DEVELOPMENT):
        # os.system("cd backend && python -m uvicorn main:app --reload")
        # os.system("cd frontend && npm run dev")
        os.system(
        'start powershell -NoExit -Command "cd backend; python -m uvicorn main:app --reload"'
        )

        os.system(
        'start powershell -NoExit -Command "cd frontend; npm.cmd run dev"'
        )
        print("Started dev enviroment")


if (platform.system() == "Linux"):
    pass

