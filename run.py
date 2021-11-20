import argparse
import os
from dotenv import load_dotenv
from src.api_manager import APIManager


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
    run_option = load_arg

    api_manager = APIManager()

    if run_option == 'daily_history_push':
        api_manager.get_recently_played_df()

    elif run_option == 'weekly_report':
        # Weekly report
        pass    






if __name__ == "__main__":
    main()