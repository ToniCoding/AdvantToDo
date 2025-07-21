from json import load as jload

class JSONReader:
    def __init__(self, json_path: str):
        self.json_data = self._read_json_file(json_path)

    def _read_json_file(self, json_conf_file: str) -> dict:
        with open(json_conf_file, 'r') as json_conf:
            data = jload(json_conf)
        return data

    def get_task_configuration(self) -> list:
        task_config = [""] * int(self.json_data["app_config"]["internal_management"]["amount_task_configurations"])

        task_config[0] = self.json_data["app_config"]["task_restrictions"]["name_max_length"]
        task_config[1] = self.json_data["app_config"]["task_restrictions"]["description_max_length"]

        return task_config

    def get_software_info(self) -> list:
        software_config = [""] * int(self.json_data["app_config"]["internal_management"]["amount_software_info"])

        software_config[0] = self.json_data["software_info"]["name"]
        software_config[1] = self.json_data["software_info"]["version"]
        software_config[2] = self.json_data["software_info"]["release_date"]
        software_config[3] = self.json_data["software_info"]["author"]
        software_config[4] = self.json_data["software_info"]["description"]

        return software_config
