import subprocess
import sys
from website import create_app

app = create_app()

def run_microservice():
    try:
        subprocess.Popen(['go', 'run', 'main.go'], cwd='microservice')
    except Exception as e:
        print(f"Ошибка при запуске микросервиса: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_microservice()
    app.run(debug=True)
    
