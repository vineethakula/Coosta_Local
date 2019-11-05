from os import environ

if "COOSTA_ENVIRON" in environ.keys():
    if environ["COOSTA_ENVIRON"] == "PROD":
        from .production import *
    if environ["COOSTA_ENVIRON"] == "QA":
        from .QA import *
    if environ["COOSTA_ENVIRON"] == "dev":
        from .dev import *
    if environ["COOSTA_ENVIRON"] == "JENKINS":
        from .jenkins import *
else:
    try:
        from .local import *
    except:
        pass
