# -*- coding: utf-8 -*-
import argparse
import requests
import sys, os

CONFIG_FILE = os.path.expanduser('~/.mailme/config')


def mailme(args):
    data = {"from": args["from"],
            "to": args["to"],
            "subject": args["subject"],
            "text": args["message"]}
    return requests.post(args["mailgun_api_endpoint"],
                        auth=("api", args["mailgun_api_key"]),
                        data=data)


def create_parser():
    parser = argparse.ArgumentParser(description='send quick email from yourself to yourself (or anyone), using mailgun')

    parser.add_argument('message', metavar='MESSAGE', nargs='?', default=sys.stdin, help='the message to send')
    parser.add_argument('-c','--config', help='specify a config file', action=ParseConfig)

    parser.add_argument('-s','--subject', help='the subject of the email', default="mailme.py email")
    parser.add_argument('-f','--from', help='the email the message is to be sent from', default="mailgun.py@example.com")
    parser.add_argument('-t','--to', help='the email the message is to be sent to', action='append')
    parser.add_argument('--mailgun_api_key', help='mailgun secret api key')
    parser.add_argument('--mailgun_api_endpoint', help='mailgun api endpoint')

    return parser


def parse_config(config_file):
    defaults = dict()
    with open(config_file) as config:
        for line in config:
            if line[0] == "#": # then the line is a comment
                pass
            else:
                var, value = line.split("=")
                defaults[var.strip()] = value.strip()
    return defaults


class ParseConfig(argparse.Action):
    def __call__(self, parser, namespace, config_file, option_string=None):
        config_file = os.path.expanduser(config_file)
        defaults = parse_config(config_file)
        parser.set_defaults(**defaults)


def command_line_runner():
    parser = create_parser()
    defaults = parse_config(CONFIG_FILE)
    parser.set_defaults(**defaults)
    args = vars(parser.parse_args())

    print("Sending email to {}...".format(args["to"]))
    mailme(args)
    print("...done.")


if __name__ == '__main__':
    command_line_runner()
