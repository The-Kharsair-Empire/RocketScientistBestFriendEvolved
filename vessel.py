import json


class VesselSequenceDescription:

    @staticmethod
    def parse_vessel(description: list):
        return description

    @staticmethod
    def parse_vessel_from_file(file_path: str):
        if not file_path.endswith('.json'):
            print("you should provide json description of the vessel")
            return

        file = open(file_path)
        data = json.load(file)
        return VesselSequenceDescription.parse_vessel(data)

    @staticmethod
    def parse_vessel_from_json_str(obj: str):
        return VesselSequenceDescription.parse_vessel(json.loads(obj))

    # @classmethod
    # def create_vessel(cls, ):

    def __init__(self, vessel_name, vessel_description):
        self.parse_vessel(vessel_description)
        # self.data_streams = {}


class VesselDataStream:

    def __init__(self, conn, vessel):
        self.conn = conn
        self.vessel = vessel
        self.name = vessel.name
        self.data_streams = {}

    def add_stream(self, attr_name: str):  # todo: designing parameter list
        pass

    def add_resources_to_stream(self, sequence_description: VesselSequenceDescription):
        # todo: add all stage resource to stream
        pass
