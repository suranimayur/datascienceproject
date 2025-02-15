import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
from box import Box, ConfigBox


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read yaml file and returns a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other error occurs.

    Returns:
        ConfigBox: Content of the YAML file.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("yaml file is empty")
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_dictionaries(path_to_directories: list, verbose=True):
    """Create directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths.
        verbose (bool, optional): Whether to log directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}.")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save data as a JSON file.

    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to be saved.
    """
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    logger.info(f"JSON file saved at: {path}.")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as a ConfigBox.
    """
    with open(path, 'r') as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}.")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save data as a binary file.

    Args:
        data (Any): Data to be saved.
        path (Path): Path to save the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}.")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load data from a binary file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Data loaded from the file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded successfully from: {path}.")
    return data
