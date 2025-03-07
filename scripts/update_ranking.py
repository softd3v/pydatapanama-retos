import os
import subprocess
import collections
import json

# Puntos por cada acción
POINTS_CREATE_CHALLENGE = 40
POINTS_SUBMIT_SOLUTION = 30
POINTS_UPDATE_CHALLENGE = 10

# Archivos donde se guarda el ranking y los retos procesados
RANKING_FILE = "RANKING.md"
PROCESSED_FILE = "processed_challenges.json"
ranking = collections.defaultdict(int)

# Cargar retos ya procesados
if os.path.exists(PROCESSED_FILE):
    with open(PROCESSED_FILE, "r") as f:
        processed_challenges = set(json.load(f))
else:
    processed_challenges = set()

# Obtener cambios en Git (archivos nuevos y modificados)
def get_git_changes(diff_filter):
    try:
        output = subprocess.check_output(
            f"git log --diff-filter={diff_filter} --name-only --pretty=''", shell=True
        ).decode().split("\n")
        return [file.strip() for file in output if file.strip()]
    except subprocess.CalledProcessError:
        return []

new_files = set(get_git_changes("A"))
modified_files = set(get_git_changes("M"))

# Verificar si GitHub Actions proporciona datos adicionales
event_file = os.getenv("GITHUB_EVENT_PATH", "")
if event_file and os.path.exists(event_file):
    with open(event_file, "r") as f:
        event = json.load(f)
        new_files.update(event.get("pull_request", {}).get("added_files", []))
        modified_files.update(event.get("pull_request", {}).get("changed_files", []))

# Depuración: Imprimir archivos detectados
print(f"📝 DEBUG: New files detected: {new_files}")
print(f"🛠️  DEBUG: Modified files detected: {modified_files}")

# Leer el ranking actual si existe
current_ranking = {}
if os.path.exists(RANKING_FILE):
    with open(RANKING_FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "|" in line and not line.startswith("| User"):  # Evita la fila de encabezado
                parts = line.split("|")
                user = parts[1].strip()
                points = parts[2].strip()
                if points.isdigit():
                    current_ranking[user] = int(points)

# Procesar archivos nuevos (solo retos que no han sido procesados antes)
for file in new_files:
    parts = file.split("/")
    
    # Detectar retos nuevos (evitar el template)
    if len(parts) > 1 and "retos" in parts[0] and "reto-" in parts[1]:
        challenge_name = parts[1]
        user = challenge_name.split("-")[-1]

        if "template" not in challenge_name and challenge_name not in processed_challenges:
            print(f"✅ DEBUG: New challenge detected '{challenge_name}' by user '{user}'")
            ranking[user] += POINTS_CREATE_CHALLENGE
            processed_challenges.add(challenge_name)  # Guardar en el set
        else:
            print(f"🚫 DEBUG: Ignoring template challenge '{challenge_name}'")

    # Detectar soluciones nuevas
    elif "submissions" in parts and file.endswith(".ipynb"):
        user = parts[-1].replace(".ipynb", "").split("-")[-1]
        print(f"✅ DEBUG: New solution submitted by '{user}'")
        ranking[user] += POINTS_SUBMIT_SOLUTION

# Procesar archivos modificados
for file in modified_files:
    parts = file.split("/")
    
    # Detectar mejoras en retos existentes (evitar el template)
    if len(parts) > 1 and "retos" in parts[0] and "reto-" in parts[1]:
        challenge_name = parts[1]
        user = challenge_name.split("-")[-1]

        if "template" not in challenge_name and challenge_name not in processed_challenges:
            print(f"🔄 DEBUG: Challenge '{challenge_name}' modified by '{user}'")
            ranking[user] += POINTS_UPDATE_CHALLENGE
            processed_challenges.add(challenge_name)  # Guardar en el set
        else:
            print(f"🚫 DEBUG: Ignoring template update '{challenge_name}'")

# Guardar la lista de retos procesados
with open(PROCESSED_FILE, "w") as f:
    json.dump(list(processed_challenges), f)

# Sumar los nuevos puntajes a los existentes
for user, points in current_ranking.items():
    ranking[user] += points

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