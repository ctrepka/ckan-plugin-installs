#!/usr/bin/python
from ntpath import join
import os
import sys
import getopt
# end
PLUGINS_LIST = (
    "stats", "text_view", "image_view",
    "recline_view", "datastore", "twdh_theme",
    "twdh_schema", "spatial_metadata", "spatial_query",
    "scheming_datasets", "officedocs_view", "pages",
    "showcase", "contact", "harvest", "ckan_harvester",
)
# default list
"""
envvars image_view text_view recline_view datastore datapusher
"""
CKAN_INI = "/srv/app/production.ini"
PLUGINS_DIR = "/srv/app/src/ckan/ckanext" #"./ckanext"

# install twdh_theme
def install_twdh_theme(github_token=''):
    PLUGIN_NAME = "ckanext-twdh_theme"

    install_cmds = """
    git clone https://{GHT}@github.com/dathere/ckanext-twdh_theme.git {PD}/{PN} && \
    cd {PD}/{PN} && \
    pip install -e . && \
    pip install -r requirements.txt
    """.format(
        PD=PLUGINS_DIR,
        PN=PLUGIN_NAME,
        GHT=github_token
    )

    print('running cmd: {c}'.format(c=install_cmds))
    os.system(install_cmds)

# install twdh_schema
def install_twdh_schema(github_token=''):
    PLUGIN_NAME = "ckanext-twdh_schema"

    install_cmds = """
    git clone https://{GHT}@github.com/dathere/ckanext-twdh_schema.git {PD}/{PN} && \
    cd {PD}/{PN} && \
    pip install -e . && \
    pip install -r requirements.txt
    """.format(
        PD=PLUGINS_DIR,
        PN=PLUGIN_NAME,
        GHT=github_token
    )

    print('running cmd: {c}'.format(c=install_cmds))
    os.system(install_cmds)

# install both spatial_metadata and
# install spatial_query
def install_ckanext_spatial(github_token=''):
    PLUGIN_NAME = "ckanext-spatial"

    install_cmds = """
    pip install -e "git+https://{GHT}@github.com/ckan/ckanext-spatial.git#egg=ckanext-spatial" && \

    """.format(
        GHT=github_token
    )

    print('running cmd: {c}'.format(c=install_cmds))
    os.system(install_cmds)

# install scheming_datasets
def install_ckanext_scheming(github_token=''):
    PLUGIN_NAME = "ckanext-scheming"

    install_cmds = """
    pip install -e 'git+https://{GHT}@github.com/ckan/ckanext-scheming.git#egg=ckanext-scheming'
    """.format(
        GHT=github_token
    )

    print('running cmd: {c}'.format(c=install_cmds))
    os.system(install_cmds)

# install officedocs_view
def install_ckanext_officedocs(github_token=''):
    PLUGIN_NAME = "ckanext-officedocs"

    install_cmds = """
    git clone https://{GHT}@github.com/dathere/ckanext-officedocs {PD}/{PN} && \
    python setup.py install
    """.format(
        PD=PLUGINS_DIR,
        PN=PLUGIN_NAME,
        GHT=github_token
    )

    print('running cmd: {c}'.format(c=install_cmds))
    os.system(install_cmds)

# install pages
def install_pages(github_token=''):
    PLUGIN_NAME = "ckanext-pages"

    install_cmds = """
    pip install -e 'git+https://{GHT}@github.com/ckan/ckanext-pages.git#egg=ckanext-pages'
    """.format(
        GHT=github_token
    )

    print('running cmd: {c}'.format(c=install_cmds))
    os.system(install_cmds)
# install showcase
def install_ckanext_showcase():
    PLUGIN_NAME = "ckanext-showcase"

    install_cmds = """
    pip install ckanext-showcase
    """

    print('running cmd: {c}'.format(c=install_cmds))
    os.system(install_cmds)

# install contact
def install_ckanext_contact(github_token=''):
    PLUGIN_NAME = "ckanext-contact"

    install_cmds = """
    git clone https://{GHT}@github.com/dathere/ckanext-contact {PD}/{PN} && \
    python setup.py install
    """.format(
        PD=PLUGINS_DIR,
        PN=PLUGIN_NAME,
        GHT=github_token
    )

    print('running cmd: {c}'.format(c=install_cmds))
    os.system(install_cmds)

# install ckanext-harvest
def install_ckanext_harvest(github_token=''):
    PLUGIN_NAME = "ckanext-harvest"

    install_cmds = """
    pip install -e git+https://{GHT}@github.com/ckan/ckanext-harvest.git#egg=ckanext-harvest#egg=ckanext-harvest
    """.format(
        GHT=github_token
    )

    print('running cmd: {c}'.format(c=install_cmds))
    os.system(install_cmds)


def config_ckan_plugins_ini():
    ckan_config_plugins_cmd = """
    ckan config-tool /srv/app/production.ini ckan.plugins='{plugins}'
    """.format(plugins=(", ").join(PLUGINS_LIST))

    os.system(ckan_config_plugins_cmd)

def main(argv):
    gh_token = ''
    try:
        opts, args = getopt.getopt(argv, "g:", ["gh-token=", ])
    except getopt.GetoptError:
        print('installs.py -g <github-token>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('installs.py -g <github-token>')
            sys.exit()
        elif opt == '-g' or opt == '--gh-token':
            gh_token = arg

    print("using github token: {g}".format(g=gh_token))

    install_twdh_theme(gh_token)
    install_ckanext_contact(gh_token)
    install_ckanext_harvest(gh_token)
    install_ckanext_officedocs(gh_token)
    install_ckanext_scheming(gh_token)
    install_ckanext_showcase()
    install_pages(gh_token)
    install_twdh_schema(gh_token)
    install_ckanext_spatial(gh_token)

    config_ckan_plugins_ini()

if __name__ == "__main__":
    main(sys.argv[1:])
