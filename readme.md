# Lista de ventas globales

## Instalación
1. Ejecutar
```
pip install -r requirements,txt
``` 
2. Crear '-config.py'
Renombrar '_config_template.py' a '_config.py' e informar sus claves

3. Renombrar '.env' (solo para desarrollo)
Renombrar '.env_template' a '.env' e informar las claves:
-FLASK_APP=run.py
-FLASK_ENV=cualquiera de 'development' o 'production'

4. Crear BBDD
Ejecutar 'migrations.sql' con 'sqlite3' en el fichero elegido como BBDD