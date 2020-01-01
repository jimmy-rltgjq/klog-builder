HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def get_convert_warring_msg(msg):
    return '{}{}{}'.format(WARNING, msg, ENDC)


def get_convert_fail_msg(msg):
    return '{}{}{}{}'.format(FAIL, '[ERROR] ', msg, ENDC)
