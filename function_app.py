import azure.functions as func
import logging
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
@app.timer_trigger(schedule="0 */4 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def TimerTriggerFunction(myTimer: func.TimerRequest) -> None:
    
    URL = "<fn-name>.azurewebsites.net/api/http_trigger?name=FME-trigger"

    r = requests.post(url=URL)
    logging.info('FMELogs - '+r.text)
    
