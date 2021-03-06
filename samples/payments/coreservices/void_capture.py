from CyberSource import *
import capture_payment
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()


def void_a_capture():
    try:
        api_capture_response=capture_payment.capture_a_payment()
        id = api_capture_response.id
        request = VoidCaptureRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code ="test_capture_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        void_obj = VoidApi(details_dict1)
        return_data, status, body =void_obj.void_capture(message_body, id)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    void_a_capture()
