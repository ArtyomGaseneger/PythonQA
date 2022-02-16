from datetime import datetime
from subprocess import run


def max_update(max_dict: dict, current_dict: dict):
    if current_dict["value"] > max_dict["value"]:
        max_dict.update(current_dict)
    return max_dict


stdout = run(["ps", "aux"], capture_output=True).stdout
output = stdout.decode("utf-8").splitlines()
users = {}
total_mem = 0
max_mem = {"value": -1, "process": ""}
total_cpu = 0
max_cpu = {"value": -1, "process": ""}
for line in output[1:]:
    # line format: USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
    line_list = line.split()
    user = line_list[0]
    users[user] = users[user] + 1 if user in users.keys() else 1
    process = " ".join(line_list[10:])[:20]
    mem = float(line_list[3])
    total_mem += mem
    max_mem = max_update(max_mem, {"value": mem, "process": process})
    cpu = float(line_list[2])
    total_cpu += cpu
    max_cpu = max_update(max_cpu, {"value": cpu, "process": process})
result = "ОТЧЁТ О СОСТОЯНИИ СИСТЕМЫ\n"
result += f"Пользователи: {', '.join(list(users.keys()))}\n"
result += f"Процессов всего: {len(output) - 1}\n"
result += "Процессов пользователей:\n"
for item in users.items():
    result += f"{item[0]} - {item[1]}\n"
result += f"Памяти всего используется: {round(total_mem, 1)}%\n"
result += f"Памяти больше всех использует: {max_mem['process']} - {max_mem['value']}%\n"
result += f"CPU всего используется: {round(total_cpu, 1)}%\n"
result += f"CPU больше всех использует: {max_cpu['process']} - {max_cpu['value']}%\n"
filename = f"{datetime.now().strftime('%d%m%Y_%H%M')}_parse.txt"
with open(file=filename, mode="w", encoding="utf-8") as file:
    file.write(result)
print(result)
print(f"Отчёт сохранён в файл {filename}")
