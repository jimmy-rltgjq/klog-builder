import os
import sys

from Builder import Builder
from utils.DataHelper import check_klog_require_files, check_folder


class Cli:
    def __init__(self):
        self.klog_path = sys.argv[1]
        self.builder = Builder(self.klog_path)

    def execute(self):
        # Print Signature Logo
        print("""
 __  __     __         ______     ______   
/\ \/ /    /\ \       /\  __ \   /\  ___\  
\ \  _"-.  \ \ \____  \ \ \/\ \  \ \ \__ \ 
 \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\
 
  \/_/\/_/   \/_____/   \/_____/   \/_____/
  
Klog Builder Start
--------------------------------------------
""")

        if not check_folder(self.klog_path) & check_klog_require_files(self.klog_path):
            exit(1)

        self.builder.make()


if __name__ == '__main__':
    cli = Cli()
    cli.execute()
