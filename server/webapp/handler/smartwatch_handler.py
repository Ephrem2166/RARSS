from tornado.web import RequestHandler
from tornado.escape import json_decode, json_encode
from webapp.service.sensory_data_service import SensoryDataService
from data_preprocessor import data_sampler

sensory_data_service = SensoryDataService()
class SmartwatchHandler(RequestHandler):
    def post(self):
        print(self.request.body)
        d = json_decode(self.request.body)

        activity_type = d['activityType']
        sensory_data = d['sensoryData']

        sensory_data_service.handle_smartwatch_sensory_data(activity_type, sensory_data)
        data_sampler.sample_data_by_frequency() # Data processing is only done when both Smartphone and Smartwatch data is stored
        self.write(json_encode({'result': True}))