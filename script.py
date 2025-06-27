import os

# Accès à la variable globale
global_var = os.environ.get("GLOBAL_VAR")

# Accès à la variable locale
local_var = os.environ.get("LOCAL_VAR")

# Affichage
print(f"Global variable from env: {global_var}")
print(f"Local variable from env: {local_var}")