import logging


def pytest_configure(config):
    # Set the global log level to DEBUG
    logging.basicConfig(level=logging.DEBUG)
