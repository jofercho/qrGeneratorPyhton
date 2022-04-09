from asyncio.windows_events import NULL
import qrcode
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-c", "--content", dest="content", help="qr content")

args = parser.parse_args();
if args.content is not None:
    img = qrcode.make(args.content);
    img.save("safira.png");
