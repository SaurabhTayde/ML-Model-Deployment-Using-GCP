# ML-Model-Deployment-Using-GCP

Built very simple ML model with a simplified dataset. (In this repository, more focus was on deploying the model on GCP, so simplified dataset is taken and basic ML model was built on it)

'Store purchase data' consists of different customers with their age, salary and whether they have purchased from the store or not.
Based on this data we will build a machine learning classification model, which will predict whether a
new customer with a certain age and salary would buy or not.
Following steps are covered in this repository:

1. Two binary or serialized files for our classifier and standard scalar objects are created. (In code 'ml_pipeline.py')

2. Saved the model and standard scalar in binary format using Python Pickle library. ('classifier.pickle' and 'sc.pickle')

3. Deserialized and used this pickle object in another python environment on the local and on the cloud ('classifier_rest_service_GCP.py')

4. Exposed Machine Learning Model to REST API. Sent request over http and get a response back ('classifier_rest_service.py')

5. Used Flask framework to build REST API. Sent data in JSON format and got the response back in JSN format

6. Accessed ML code through client and got the prediction

7. Created GCP Cloud account and created a VM Instance on GCP.

8. Required permissions are provided, so that model can be accessed using the IP address and VM instace.

9. On the instance that was created, required Python libraries were installed. Python Codes and pickle files are imported and kept on this VM instance. Python classifier code is compiled and output URL is copied. ((All of this done in 'SSH In Browser')

10. This URL is used in 'classifier_rest_service_GCP.py' code where JSON input is given and we get the desied output by compiling the Client Code.

11. In this way, deployed this model on Google Cloud so that anybody who has access to the IP address of the VM can access the model.
