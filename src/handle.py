from env_centralizer import DotEnvCentralizer

def handle():
    base_dir = "/home/lucas/dev"

    centralizer = DotEnvCentralizer(base_dir)
    centralizer.save_env_files()


if __name__ == '__main__':
    handle()