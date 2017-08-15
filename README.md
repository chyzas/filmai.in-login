"# filmai.in-login" 

```git clone https://github.com/chyzas/filmai.in-login.git```

Užpildyti ```settings.py``` su prisijungimo prie filmai.in duomenimis.

Gauti emaila jei nepavyko prisijungti supildyti ```email```

Geriausia leisti cron job'ą kiekviena dieną:


```* */12 * * * python /home/pi/filmai.in-login/login.py```
