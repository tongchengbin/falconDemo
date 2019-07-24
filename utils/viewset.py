import json
class BaseViewSet():
    '''基础视图'''
    auth=True

    def json_to_str(self, body_dict):
        return json.dumps(body_dict)

    def JsonResponse(self, data):
        return self.json_to_str(body_dict=data)