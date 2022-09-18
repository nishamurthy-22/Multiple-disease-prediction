# Multiple-disease-prediction
We, Team ***Break-A-Leg***, participated in the Weal Club at PESU Hackathon Healthack. The problem statement we chose to tackle was ***"Analysis, Diagnosis and Enryption of Blood Work Using Machine Learning and Block Chain"***. Why choose this problem statement, according to the statistics the society is moving towards home based medical testing systems. As a normal person the first step we would take, after receiving the medical test report is to approach the doctor to diagnose your blood report, this would involve some consultation charges. This is where our solution will come. 

We have designed a module that takes in the blood report and reads all the information using the ***Optical Character Recognition***. Our model is built to diagnose three main diseases namely i) Diabeties ii) Heart Disease iii) Chronic Kidney Disease. As we all know these three diseases required three different set of values to predict whether the patient has acquired the disease or not. Our model is trained in such a way that, for each disease it takes only the values that are required for prediction. All the prediction models are built on various ***Machine Learning and Deep Learning models***. The calculations say that we have an ***overall 92% accuracy*** in predictng the diseases based on the inputs received from the blood report. The additional feature we have added is that while people use our solution, we store and use their data and add it back to our dataset allowing us to increase our accuracy. Now arises a question, what about the personal details that are present on the blood report

We have used ***Block Chain*** concept to keep all the personal information of our users safe. This Block Chain has been built on ***Ethrium*** and is successfully deployed on ***Polygon***. In this part of the solution, we pass all the personal infromation like the Name, Contact Information, City to the Block Chain which will hold the encrypted data. All these data has been encrypted on a high level, with high security. We have ensured that the key generated for each blood report data will be available only for that specific patient and their family doctor. This final preoduct has been hosted on web using ***Streamlit***.

This total product has been successfully deployed on the web. Do use the link to test our product: https://nishamurthy-22-multiple-disease-prediction-test-0ldo4u.streamlitapp.com/ . To test the product, please download and use the "Blood_report.pdf" file given in this repository.

## Thank You
### -Team Break-A-Leg
