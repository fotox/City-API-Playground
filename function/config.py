import os


def config_test() -> dict:
    """
    Load test config setup
    :return: config setup
    """
    return {
        'TESTING': True,
        'DEBUG': True,
        'PORT': 1337,
        'NAME': 'test',
        'SQLALCHEMY_DATABASE_URI': (f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
                                    f"{os.getenv('PGHOST')}:{os.getenv('PGPORT')}/{os.getenv('PGDATABASE')}"),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }


def config_dev() -> dict:
    """
    Load development config setup
    :return: config setup
    """
    return {
        'TESTING': False,
        'DEBUG': True,
        'PORT': 1337,
        'NAME': 'dev',
        'SQLALCHEMY_DATABASE_URI': (f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
                                    f"{os.getenv('PGHOST')}:{os.getenv('PGPORT')}/{os.getenv('PGDATABASE')}"),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }


def config_prod() -> dict:
    """
    Load productive config setup
    :return: config setup
    """
    return {
        'TESTING': False,
        'DEBUG': False,
        'PORT': 1337,
        'NAME': 'prod',
        'SQLALCHEMY_DATABASE_URI': (f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
                                    f"{os.getenv('PGHOST')}:{os.getenv('PGPORT')}/{os.getenv('PGDATABASE')}"),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }


def set_config(config_type: str) -> dict:
    if config_type == "dev":
        return config_dev()
    if config_type == "prod":
        return config_prod()
    if config_type == "test":
        return config_test()
