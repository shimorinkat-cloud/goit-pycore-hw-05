import sys
from pathlib import Path


def parse_log_line(line: str) -> dict | None:
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None
    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level.upper(),
        "message": message,
    }


def load_logs(file_path: str) -> list[dict]:
    path = Path(file_path)
    if not path.exists() or not path.is_file():
        raise FileNotFoundError

    with path.open("r", encoding="utf-8") as f:
        return list(filter(None, map(parse_log_line, f)))


def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    level = level.upper()
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for log in logs:
        lvl = log["level"]
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts


def display_log_counts(counts: dict[str, int]) -> None:
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    order = ["INFO", "DEBUG", "ERROR", "WARNING"]
    for level in order:
        if level in counts:
            print(f"{level:<15} | {counts[level]}")



def main():
    if len(sys.argv) < 2:
        print("Usage: python task_3.py <logfile_path> [level]")
        return

    file_path = sys.argv[1]
    level_arg = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        if level_arg:
            filtered = filter_logs_by_level(logs, level_arg)
            print(f"\nДеталі логів для рівня '{level_arg.upper()}':")
            for log in filtered:
                print(f"{log['date']} {log['time']} - {log['message']}")

    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception:
        print("Сталася помилка.")


if __name__ == "__main__":
    main()
