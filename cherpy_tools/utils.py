import csv
from loguru import logger


def dict_to_csv(my_dict, columns, filename, **kwargs):
    mode = kwargs.get("filemode", 'w')
    logger.debug(f"writing to file {filename}")
    with open(filename, mode, newline='') as out_file:
        w = csv.DictWriter(out_file, columns)
        w.writeheader()
        for d in my_dict:
            w.writerow(d)


def create_temp_file(value_pairs, file_name):
    columns = value_pairs[::2]
    values = value_pairs[1::2]

    with open(file_name, 'w') as outf:
        outf.write(",".join(columns) + "\n")
        outf.write(",".join(values) + "\n")
