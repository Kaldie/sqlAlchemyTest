import os
import yaml
import logging.config


def setup_logging( default_path='Logging/config.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if not os.path.exists(path):
        raise ValueError("Could not resolve the logging config")
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

setup_logging()

