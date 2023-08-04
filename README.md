# Chittis: Brain Tumor Detection

This is a web application for brain tumor detection using a pre-trained deep learning model (ResNet-50). The application allows users to upload an image of a brain scan, and it will predict whether a brain tumor is present or not.

## How to run the app

1. Clone the repository
2. Move to the `Chittis-Brain-Tumor-Detection` folder
3. Create a virtual environment using `virtualenv 'envirnoment name'`.
4. Activate the virtual environment. For Windows, use: `. \Scripts\activate`, and for Linux/Mac, use: `source /envirnoment name/bin/activate`
5. Install the required packages by running the command: `pip install -r requirements.txt`
6. If you encounter an error related to torch or torchvision libraries, install them using the following commands:

For Windows CPU (torch library):
   - With Conda: `conda install pytorch torchvision cpuonly -c pytorch`
   - With pip: `pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html`

7. Download the model file from [here](https://drive.google.com/file/d/1QcQEhmPjDg86NfgYSEb-t_c0EO8NOXhJ/view?usp=drive_link) and add it to the `models` directory in order to run the project.
8. Run the app using: `flask run`

For production deployment:
1. Configure a production WSGI server (e.g., Gunicorn, uWSGI, or mod_wsgi) to run the app. Example for Gunicorn: `gunicorn wsgi:app`
2. The app will be accessible at `http://localhost:8000` (assuming Gunicorn is running on port 8000).

## How the app works

- The main page displays a welcome message and navigation links to other pages.
- The "Brain Tumor Detection" page allows users to upload an image and get the prediction result for the brain tumor detection.
- The "All About Brain Tumors" page provides information about brain tumors and their types.
- The "Find Nearby Hospitals" page allows users to search for nearby hospitals to get medical assistance.

Please note that this app is for educational and demonstrational purposes only, and the prediction results may not be accurate for real medical diagnosis. Always consult a medical professional for accurate diagnosis and treatment.
