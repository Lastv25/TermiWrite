import argparse

from app import TermiWriteApp

parser = argparse.ArgumentParser(description="Folder for the app to run on")
parser.add_argument("path", help="path for the run")
args = parser.parse_args()

if __name__ == "__main__":
    app = TermiWriteApp(args.path)
    app.run()
