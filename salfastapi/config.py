import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="salfastapi",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="salfastapi_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from salfastapi.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export salfastapi_KEY=value
export salfastapi_KEY="@int 42"
export salfastapi_KEY="@jinja {{ this.db.uri }}"
export salfastapi_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
salfastapi_ENV=production salfastapi run
```

Read more on https://dynaconf.com
"""
