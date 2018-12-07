import pytest


pytest_plugins = ['common_fixtures']

# def pytest_logger_config(logger_config):
    # logger_config.add_loggers(['public_api'], stdout_level='info')
    # logger_config.set_log_option_default('public_api')

# def pytest_logger_logdirlink(config):
    # return os.path.join(os.path.dirname(__file__), 'logs')
