import argparse
import os
from dotenv import load_dotenv
from src.spotify_etl import SpotifyETL


def load_environment() -> None:
    if os.path.exists("config/config.env"):
        load_dotenv(dotenv_path="config/config.env")
    else:
        raise FileNotFoundError("\"config/config.env\" not found")


def load_arg():
    # Initialize arg parser
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--option", help="help")
    args = arg_parser.parse_args()
    run_option = args.option
    return run_option


def main() -> None:
    load_environment()
    run_option = load_arg()

    etl = SpotifyETL()
    if run_option == 'daily_history_push':
        etl.daily_etl()

    elif run_option == 'weekly_report':
        etl.weekly_etl()
        

if __name__ == "__main__":
    main()

