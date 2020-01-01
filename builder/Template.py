import os

from jinja2 import Environment, PackageLoader, select_autoescape
from utils.DataHelper import get_yml_data


class Template:

    def __init__(self, template_type, target_path, klog_path=None):
        self.stream_data = {}
        self.template_type = template_type  # Template Type
        self.target_path = target_path  # Build Target Path
        self.dump_path = target_path + '/klog/{}.html'.format(template_type)  # Template Dump Path
        self.klog_path = klog_path  # KLOG YML Directory Path

        self.init_stream_data()  # Template Data + Me Data

        # Init JinJa Environment
        self.env = Environment(
            loader=PackageLoader('builder', '/templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def build_template(self):
        self.env\
            .get_template('{}.html'.format(self.template_type))\
            .stream(self.stream_data)\
            .dump(self.dump_path)

    def init_stream_data(self):
        yml_path = self.klog_path + '/{}.yml'.format(self.template_type)
        me_path = self.klog_path + '/me.yml'

        if os.path.exists(yml_path):
            self.stream_data.update(get_yml_data(yml_path))

        self.stream_data.update(get_yml_data(me_path))

    def update_stream_data(self, data):
        self.stream_data.update(data)

    def update_dump_path(self, path):
        self.dump_path = self.target_path + path

