import datetime
import functools


def log_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            now = datetime.datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")

            with open("exceptions.log", "a", encoding="utf-8") as log_file:
                log_file.write(f"[{date_time}] {type(e).__name__}\n")

            raise

    return wrapper
