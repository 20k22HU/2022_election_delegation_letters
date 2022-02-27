# merging user data and template into html files

import json
from jinja2 import Template


def read_users(file_str='../input/user_testdata.json'):
    """reads the user json dump file and returns as json variable"""
    with open(file_str, 'r', encoding='utf-8') as f:
        oevks = json.load(f)
    return oevks


def read_letter_template(file_str='../input/megbizolevel_teszt.html'):
    """reads the mail template file and returns it as text variable"""
    with open(file_str, 'r', encoding='utf-8') as f:
        template = Template(f.read())
    return template


def generate_documents(user_json_obj, jinja_template):
    """generating all documents using the template and the user db"""
    path = "../output/"
    for oevk in user_json_obj:
        for tevk in oevk['tevks']:
            filename = f"OEVK{oevk['id']}_TEVK{tevk['id']}" \
                       f"_szszb_megbizo_{oevk['name']}_{tevk['name']}" \
                       f"_hitelesitett.html"
            result = jinja_template.render(tevk = tevk)
            with open(path+filename, 'w', encoding='utf-8') as f:
                f.write(result)


generate_documents(
    read_users(),
    read_letter_template()
)