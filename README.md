# test_automation

## Sklep testowy

Obecnie testujemy instancję sklepu dostępną w sieci Hackerspace Trójmiasto pod adresem http://192.168.1.226/

## Instalacja podstawowa

1. Instalacja [PyCharm](https://www.jetbrains.com/pycharm/download/) 
2. Instalacja Pythona 3 
   - dla Windowsa: [python.org](https://www.python.org/downloads/windows/)
   - dla Linuxa: `apt-get install python3-pip`

3. W PyCharm dodaj nowego env (dolny prawy róg -> Add interpreter)
4. Aktywacja venva - Jeśli nie masz aktywnego venva to musisz go aktywować
    - dla Windowsa:  
      - Gdy używasz PowerShell  wpisz komende `venv\Scripts\activate.ps1`
      - Gdy używasz cmd wpisz komendę  `venv\Scripts\activate.bat`
    - dla Linuxa i MacOS wpisz `source venv/bin/activate`
5. Instalacja zależności. W Terminalu PyCharm wykonaj: `pip install -r requirement.txt` 
6. Uruchomienie naszego testu automatycznego w konsoli przez pytest: `pytest main.py`

Istnieją dwie możliwości uruchamiania testów: lokalna oraz z użyciem Selenium Grid.

Sposoby ich konfiguracji są opisane poniżej.

### Lokalny WebDriver

Zainstalować wybrany WebDriver:

* Chrome
https://chromedriver.chromium.org/getting-started
* Firefox
https://github.com/mozilla/geckodriver/releases
* Edge
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Upewnić się że wybrany driver jest odnajdowalny w PATH, np. poprzez wpisanie:
```console
geckodriver
```

### Selenium Grid

1. Zainstalować Dockera: https://docs.docker.com/engine/install/
2. Zainstalować docker-compose: https://docs.docker.com/compose/install/
3. Uruchomić Selenium Grid: `docker-compose -f selenium-grid.yaml up -d`

Na koniec pracy zatrzymać Selenium Grid: `docker-compose -f selenium-grid.yaml down`
