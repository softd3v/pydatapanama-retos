import os
import subprocess
import collections
import json

# Puntos por cada acción
POINTS_CREATE_CHALLENGE = 40
POINTS_SUBMIT_SOLUTION = 30
POINTS_UPDATE_CHALLENGE = 10

# Archivo donde se guarda el ranking
RANKING_FILE = "RANKING.md"
ranking = collections.defaultdict(int)

# Obtener cambios en Git (archivos nuevos y modificados)
new_files = subprocess.check_output(
    "git log --diff-filter=A --name-only --pretty=''",
    shell=True
).decode().split("\n")

modified_files = subprocess.check_output(
    "git log --diff-filter=M --name-only --pretty=''",
    shell=True
).decode().split("\n")

# Obtener cambios desde GitHub Actions (si está disponible)
event_file = os.getenv('GITHUB_EVENT_PATH', '')
if event_file and os.path.exists(event_file):
    with open(event_file, 'r') as f:
        event = json.load(f)
        new_files.extend(event.get('pull_request', {}).get('added_files', []))
        modified_files.extend(event.get('pull_request', {}).get('changed_files', []))

# Normalizar los nombres de archivo (eliminar espacios vacíos)
new_files = [file.strip() for file in new_files if file.strip()]
modified_files = [file.strip() for file in modified_files if file.strip()]

# Leer el ranking actual si existe
current_ranking = {}
if os.path.exists(RANKING_FILE):
    with open(RANKING_FILE, "r") as f:
        for line in f.readlines():
            if "|" in line and "-" not in line:
                parts = line.split("|")
                user = parts[1].strip()
                points = parts[2].strip()
                if user.isalnum():
                    current_ranking[user] = int(points)

# Asignar puntos a los usuarios
for file in new_files:
    parts = file.split("/")
    if len(parts) > 2 and "retos" in parts[0]:
        challenge_name = parts[1]
        if challenge_name.startswith("reto-"):
            user = challenge_name.split("-")[-1]
            ranking[user] += POINTS_CREATE_CHALLENGE
        elif "submissions" in parts:
            user = parts[-1].replace(".ipynb", "").split("-")[-1]
            ranking[user] += POINTS_SUBMIT_SOLUTION

for file in modified_files:
    parts = file.split("/")
    if len(parts) > 2 and "retos" in parts[0]:
        challenge_name = parts[1]
        if challenge_name.startswith("reto-"):
            user = challenge_name.split("-")[-1]
            ranking[user] += POINTS_UPDATE_CHALLENGE

# Sumar los nuevos puntajes a los existentes
for user, points in current_ranking.items():
    ranking[user] += points  # Acumulamos en lugar de sobrescribir

# Ordenar y escribir el nuevo ranking
ranking_sorted = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

with open(RANKING_FILE, "w") as f:
    f.write("# 🏆 PyData Panama Contributors Ranking\n\n")
    f.write("| User | Points |\n")
    f.write("|---------|--------|\n")
    for user, points in ranking_sorted:
        f.write(f"| {user} | {points} |\n")
    f.write("\n🚀 **Keep contributing to climb up the ranking!**\n")

print("✅ Ranking successfully updated.")