from cornice import Service
from financial_system.api import API_V1_PATH


hello = Service(name="test service", path=API_V1_PATH + "/test", description="view of test")


@hello.get()
def get_test_view(request):
    return {"Hello": "World"}
