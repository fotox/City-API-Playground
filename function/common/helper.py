from log_module.log_app import viki_log

logger = viki_log("city_api")


def check_format_of_dataset(dataset: dict) -> str:
    """
    Check if all attribute in create city dataset set and valid. If not return an error message for error handler.
    :param dataset: dataset what if set in body by post request with type json
    :return: Succeed or error message
    """
    message: str = "Dataset is valid"
    if 'name' not in dataset or not isinstance(dataset['name'], str) or dataset['name'] == "":
        message = f"name must set and type must be a str and not empty."
    elif 'population' not in dataset or not isinstance(dataset['population'], int) or int(dataset['population']) <= 0:
        message = f"population must set and type must be a int bigger than 0."
    elif 'beauty' not in dataset or not isinstance(dataset['beauty'], str):
        message = f"beauty must set and type must be a int or str."
    elif 'geo_location_latitude' not in dataset or not isinstance(dataset['geo_location_latitude'], float):
        message = f"geo_location_latitude must set and type must be a float."
    elif 'geo_location_longitude' not in dataset or not isinstance(dataset['geo_location_longitude'], float):
        message = f"geo_location_longitude must set and type must be a float."
    elif 'allied_cities' not in dataset or not isinstance(dataset['allied_cities'], list):
        message = f"allied_cities must be an empty list or filled with city_id."
    else:
        return message

    logger.error(f"{check_format_of_dataset} send: {message}")
    return message
