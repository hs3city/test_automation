# test_automation

1. Instalacja [PyCharm](https://www.jetbrains.com/pycharm/download/) 
2. Instalacja Pythona 3 
   - dla Windowsa: [python.org](https://www.python.org/downloads/windows/)
   - dla Linuxa: `Apt-get install python3-pip`

3. W PyCharm dodaj nowego env (dolny prawy róg -> Add interpreter)
4. Aktywacja venva - Jeśli nie masz aktywnego venva to musisz go aktywować
    - dla Windowsa:  
      - Gdy używasz PowerShell  wpisz komende `venv\Scripts\activate.ps1`
      - Gdy używasz cmd wpisz komendę  `venv\Scripts\activate.bat`
    - dla Linuxa i MacOS wpisz `source venv/bin/activate`

5. Instalacja zależności. W Terminalu PyCharm wykonaj: `pip install -r requirement.txt` 
6. Uruchomienie naszego testu automatycznego w konsoli: `pytest main.py`

