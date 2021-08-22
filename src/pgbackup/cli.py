from argparse import Action, ArgumentParser

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = ArgumentParser(
        description="""
        Backup PostgreSQL databases locally or to AWS S3
        """
    )

    parser.add_argument("url", help="URL of the database to backup")
    parser.add_argument("--driver", "-d", help="how & where to store backup", nargs=2, metavar=("DRIVER", "DESTINATION"), action=DriverAction, required=True)

    return parser


def main():
    import time
    import boto3
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    destination = args.destination
    url = args.url

    dump = pgdump.dump(url)

    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H-%M", time.localtime())
        file_name = pgdump.dump_file_name(url, timestamp)

        print(f"Backing database up to {destination} in S3 as {file_name}")
        storage.s3(client, dump.stdout, destination, file_name)
    else:
        outfile = open(destination, 'wb')

        print(f"Backing database up locally to {outfile.name}")
        storage.local(dump.stdout, outfile)

