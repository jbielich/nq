import argparse
import os

from command import initcommand
from command import loadcommand
from db import nqdb
# https://docs.python.org/2/library/argparse.html#module-argparse


def init_args():
    parser = argparse.ArgumentParser(description='Nmap Querying Utility', version="0.1a")
    parser.add_argument("-i", "--init", action='store_true',
                        help="Initialize a database. NOTE: This will erase any existing database!")
    parser.add_argument("--load", nargs=1,
                        help="load the specified nmap xml output file into database",
                        metavar="FILENAME")

    return parser

if __name__ == '__main__':
    # TODO: make this configurable via config file
    db_location = os.path.join(os.environ["HOME"], "nq.db")
    dbm = nqdb.DatabaseManager(db_location)

    parser = init_args()

    try:
        args = parser.parse_args()
        print args
    except IOError, msg:
        parser.error(str(msg))

    # Initialize Database
    if args.init:
        initcommand.execute(dbm)

    if args.load:
        print args.load[0]
        loadcommand.execute(dbm, args.load[0])
