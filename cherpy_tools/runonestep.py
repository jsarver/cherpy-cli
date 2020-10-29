import yaml
import os
from zeep import Client
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('runit.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


def create_client(url, user, passwd):
    client = Client(url)
    logger.debug(client.service.Login(user, passwd))
    logger.info("logging in")
    return client


def get_env_value(env="RUNIT_SETTINGS"):
    """
    Takes env var and returns value
    :param env:
    :return:
    """

    logger.debug("getting config for env {}".format(env))
    cfg = os.environ.get(env)
    return cfg


def config_from_file(file_name):
    """
    loads config from file
    :param file_name:
    :return:
    """
    cfg = yaml.load(open(file_name))
    return cfg


def client_from_env(env="RUNIT_SETTINGS"):
    cfg_path = get_env_value(env)
    cfg = config_from_file(cfg_path)
    logger.debug("Creating client with url {} for user: {} ".format(cfg.get('url'), cfg.get('user')))
    client = create_client(cfg['url'], cfg['user'], cfg['passwd'])
    return client


def client_from_file(file_name):
    cfg = config_from_file(file_name)
    client = create_client(cfg['url'], cfg['user'], cfg['passwd'])
    return client


def run_one_step(client, object_name_or_id, recid=None, scope="Global", scope_owner="(none)", onestep_name_or_id=None,
                 prompts=None):
    # ""Customer Update","","Core","(none)","Stand alone Dept Job Code Update","(none)""
    # setting values to empty string if none were supplied

    logger.debug(
        f"running onestep for object: {object_name_or_id}, recid: {recid}, scope: {scope}, scope_owner: {scope_owner}, "
        f"onestep: {onestep_name_or_id}, prompts: {prompts}")
    recid = "" if not recid else recid
    onestep_name_or_id = "" if not onestep_name_or_id else onestep_name_or_id
    prompts = "" if not prompts else prompts
    response = client.service.RunOneStep(object_name_or_id, recid, scope, scope_owner, onestep_name_or_id, prompts)
    return response
