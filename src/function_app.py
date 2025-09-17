import azure.functions as func
import logging
import time
import requests
import json

app = func.FunctionApp()

@app.function_name("first_http_function")
@app.route(route="first_http_function", auth_level=func.AuthLevel.ANONYMOUS)
def first_http_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function (first) processed a request.')
    
    # Call the second function
    base_url = f"{req.url.split('/api/')[0]}/api"
    second_function_url = f"{base_url}/second_http_function"
    
    response = requests.get(second_function_url)
    second_function_result = response.text
    
    result = {
        "message": "Hello from the first function!",
        "second_function_response": second_function_result
    }
    
    return func.HttpResponse(
        json.dumps(result),
        status_code=200,
        mimetype="application/json"
    )


@app.function_name("second_http_function")
@app.route(route="second_http_function", auth_level=func.AuthLevel.ANONYMOUS)
@app.service_bus_queue_output(arg_name="outputsbmsg", queue_name="%ServiceBusQueueName%",
                              connection="ServiceBusConnection")
def second_http_function(req: func.HttpRequest, outputsbmsg: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function (second) processed a request.')

    message = "This is the second function responding."
    
    # Send a message to the Service Bus queue
    queue_message = "Message from second HTTP function to trigger ServiceBus queue processing"
    outputsbmsg.set(queue_message)
    logging.info('Sent message to ServiceBus queue: %s', queue_message)
    
    return func.HttpResponse(
        message,
        status_code=200
    )


@app.service_bus_queue_trigger(arg_name="azservicebus", queue_name="%ServiceBusQueueName%",
                               connection="ServiceBusConnection") 
def servicebus_queue_trigger(azservicebus: func.ServiceBusMessage):
    logging.info('Python ServiceBus Queue trigger start processing a message: %s',
                azservicebus.get_body().decode('utf-8'))
    time.sleep(5)
    logging.info('Python ServiceBus Queue trigger end processing a message')