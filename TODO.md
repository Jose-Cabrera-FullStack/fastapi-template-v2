1.- Automatizar la validación de las migraciones, en caso de tener una nueva se debe correr el script de Alembic. En caso de que ya se aplique la migración, no se debe ejecutar nuevamente.

https://www.miguelg.com/2020/04/comprobar-multiple-heads-alembic-migrations.html?utm_source=chatgpt.com

Correr tests:
``` python
from unittest import TestCase

from alembic.script import ScriptDirectory
from flask_migrate import Config


class TestAlembicMigrations(TestCase):
    def test_migration_tree(self):
        config = Config()
        config.set_main_option("script_location", "app:migrations")
        script = ScriptDirectory.from_config(config)

        current_head = script.get_current_head()

        self.assertIsNotNone(current_head)
```

2.- Gestión de errores: Maneja los errores de manera segura para no revelar información sensible.

3.- Registro y monitoreo: Implementa un sistema de registro y monitoreo para detectar y responder a incidentes de seguridad.
    - Grafana: Utiliza Grafana para monitorear métricas y alertas.
    - Prometheus: Utiliza Prometheus para recopilar métricas y monitorear servicios.

4.- Medidas de seguridad para prevenir ataques comunes
    - CSRF (Cross-Site Request Forgery): Implementa tokens CSRF para proteger contra ataques CSRF.
    - XSS (Cross-Site Scripting): Sanitiza todas las entradas del usuario para prevenir XSS.
    - Rate Limiting: Implementa limitación de tasa para prevenir ataques de fuerza bruta.

5.- Seguridad básica en APIs
    - JWT (JSON Web Tokens): Implementa JWT para la autenticación de usuarios.
    - OAuth2: Utiliza OAuth2 para la autorización de acceso a recursos.
    - HTTPS: Asegúrate de que todas las comunicaciones se realicen a través de HTTPS.

6.- Actualizar la versión de Python a la última estable.

    - Migrar de requests a httpx.