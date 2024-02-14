# PythonV2_keep_alive
This project contains a Function App in Python Programming model V2. Two triggers (http/timer) the timer runs every 4 minutes and post a name in the Http trigger.6

The goal: Use it as an example to avoid the Azure Function Apps go idle when running on Consumption plans.
How? This Function will runs every 4 minutes posting a parameter name in the http trigger function, avoiding the Function's cold starts. 


Check the <a href="//learn.microsoft.com/en-us/azure/azure-functions/functions-scale#timeout." target="_blank">Function app timeout duration.</a>
<br>
And the cold start <a href="https://azure.microsoft.com/en-us/blog/understanding-serverless-cold-start/" target="_blank">Understanding serverless cold start.</a>
