import os
import shutil
import webbrowser

from Template import Template
from utils.DataHelper import get_yml_data
from utils.DataHelper import init_target_directory, convert_all_md_to_html


class Builder:
    def __init__(self, klog_path):
        self.KLOG_PAHT = klog_path
        cur_path = os.path.dirname(__file__)
        par_path = os.path.abspath(os.path.join(cur_path, '../'))
        self.ROOT_DIR = cur_path
        self.TARGET_PATH = os.path.abspath(os.path.join(par_path, 'target'))

    # TODO: Make Type Add After
    def make(self):
        self.build_all_template()

    def build_all_template(self):
        index_path = self.ROOT_DIR + '/templates/index.html'
        target_common_path = self.TARGET_PATH + '/klog/common/'
        template_common_path = self.ROOT_DIR + '/templates/common'

        init_target_directory(self.TARGET_PATH)  # Init Setup Target Directory
        shutil.copytree(template_common_path, target_common_path)  # Copy Common Directory
        shutil.copyfile(index_path, self.TARGET_PATH + '/klog/index.html')  # Copy Index html
        shutil.copytree(self.KLOG_PAHT + '/img', target_common_path + '/img')  # Copy Image Directory

        # Build Template From YML
        for template_type in ['about', 'works', 'articles']:
            self.build_from_yml(template_type)

        # Build Template From Markdown
        for template_type in ['work', 'article']:
            self.build_from_md(template_type)

    def build_from_yml(self, template_type):
        # Build Template
        about = Template(template_type, self.TARGET_PATH, self.KLOG_PAHT)
        about.build_template()

    def build_from_md(self, template_type):
        # Convert All Works Md File to HTML
        html_list = convert_all_md_to_html(
            self.KLOG_PAHT + '/{}s'.format(template_type),
            self.ROOT_DIR + '/templates'
        )

        # Build Template
        for index, value in html_list.items():
            work = Template(template_type, self.TARGET_PATH, self.KLOG_PAHT)
            work.update_stream_data({'md_path': 'tmp/' + index + '.html'})
            work.update_dump_path('/klog/{}s/{}.html'.format(template_type, index))
            work.build_template()

        shutil.rmtree(self.ROOT_DIR + '/templates/tmp')


if __name__ == '__main__':
    builder = Builder('/Users/kimjimin/Dev/Codes/Klog-Builder/docs/default_klog')
    builder.make()
