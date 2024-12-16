import os
import shutil


class DotEnvCentralizer:
    def __init__(self, base_path):
        self.base_path = base_path


    def save_env_files(self):
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file == ".env":
                    env_path = os.path.join(root, file)
                    service_name = os.path.basename(root)
                    new_env_name = f"env-{service_name}"
                    new_env_path = os.path.join(self.base_path, new_env_name)
                    shutil.copy(env_path, new_env_path)
                    print(f"File '{env_path}' saved as '{new_env_path}'")