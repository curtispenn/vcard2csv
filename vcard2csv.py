#!/usr/bin/env python
import vobject
import glob
import csv
import argparse
import os
import sys
import logging
import collections

column_order = [
    'Name',
    'Full name',
    'Cell phone',
    'Work phone',
    'Home phone',
    'Email',
    'Note',
]

def get_phone_numbers(vCard):
    cell = home = work = None
    for tel in vCard.tel_list:
        tel_type = tel.singletonparams if vCard.version.value == '2.1' else tel.params.get('TYPE', [])
        
        if 'CELL' in tel_type:
            cell = str(tel.value).strip()
        elif 'WORK' in tel_type:
            work = str(tel.value).strip()
        elif 'HOME' in tel_type:
            home = str(tel.value).strip()
        else:
            logging.warning("Warning: Unrecognized phone number category in `{}'".format(vCard))
            tel.prettyPrint()
    
    return cell, home, work

def get_info_list(vCard, vcard_filepath):
    vcard = collections.OrderedDict()
    for column in column_order:
        vcard[column] = None

    name = cell = work = home = email = note = None
    vCard.validate()

    for key, val in vCard.contents.items():
        if key == 'fn':
            vcard['Full name'] = vCard.fn.value
        elif key == 'n':
            name = str(vCard.n.valueRepr()).replace('  ', ' ').strip()
            vcard['Name'] = name
        elif key == 'tel':
            cell, home, work = get_phone_numbers(vCard)
            vcard['Cell phone'] = cell
            vcard['Home phone'] = home
            vcard['Work phone'] = work
        elif key == 'email':
            vcard['Email'] = str(vCard.email.value).strip()
        elif key == 'note':
            vcard['Note'] = str(vCard.note.value)

    if name is None:
        logging.warning("No name for vCard in file `{}'".format(vcard_filepath))
    if all(phone is None for phone in [cell, work, home]):
        logging.warning("No telephone numbers for file `{}' with name `{}'".format(vcard_filepath, name))

    return vcard

def get_vcards(vcard_filepath):
    with open(vcard_filepath) as fp:
        all_text = fp.read()
    for vCard in vobject.readComponents(all_text):
        yield vCard

def readable_directory(path):
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f'Not an existing directory: {path}')
    if not os.access(path, os.R_OK):
        raise argparse.ArgumentTypeError(f'Not a readable directory: {path}')
    return path

def writable_file(path):
    if os.path.exists(path):
        if not os.access(path, os.W_OK):
            raise argparse.ArgumentTypeError(f'Not a writable file: {path}')
    else:
        with open(path, 'w') as fp:
            pass
    return path

def main():
    parser = argparse.ArgumentParser(
        description='Convert vCard (.vcf) files to a single TSV file.'
    )
    parser.add_argument(
        'read_dir',
        type=readable_directory,
        help='Directory to read vCard files from.'
    )
    parser.add_argument(
        'tsv_file',
        type=writable_file,
        help='Output TSV file',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        help='More verbose logging',
        dest="loglevel",
        default=logging.WARNING,
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        '-d',
        '--debug',
        help='Enable debugging logs',
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
    )
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    vcard_pattern = os.path.join(args.read_dir, "*.vcf")
    vcard_paths = sorted(glob.glob(vcard_pattern))
    if not vcard_paths:
        logging.error("No files ending with `.vcf` in directory `{}'".format(args.read_dir))
        sys.exit(2)

    with open(args.tsv_file, 'w', encoding="utf-8", newline='') as tsv_fp:
        writer = csv.writer(tsv_fp, delimiter='\t')
        writer.writerow(column_order)

        for vcard_path in vcard_paths:
            for vcard in get_vcards(vcard_path):
                vcard_info = get_info_list(vcard, vcard_path)
                writer.writerow(list(vcard_info.values()))

if __name__ == "__main__":
    main()
