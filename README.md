# 1. Installation
Initially, create a virtual environment. I have used virtualenv:
`python -m venv .env`

Activate the virtual environment:
`source .env/bin/activate`

Firstly install torch and torchvision:
`pip install torch torchvision`

Secondly, install DeepPrivacy and the necessary libraries by running:
`pip install git+https://github.com/hukkelas/DeepPrivacy/`

Lastly, install the other necessary libraries for the crowd counting to work. 
`pip install -r requirements.txt`

# 2. Usage
`python main.py -s [INPUT IMAGE PATH] -t [OUTPUT IMAGE PATH]`

Working with .jpg and .jpeg images is reccomeneded as it saves much more needed memory when loading the images. Too large images might result in Insufficient memory error. 