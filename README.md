# img-classification-adversarial-examples
A repository containing examples of adversarial machine learning for image classification in PyTorch.

TODO maybe change file main.ipynb to examples.ipynb and utils.py to main.py (only show examples in Jupyter notebook and have entire code in .py script file)

Adversarial machine learning is .... The goal is to construct an image which a human can classify correctly, but which a neural network classifies wrongly.

An adversarial example is ...

For more information about adversarial machine learning, see the following links:
- https://en.wikipedia.org/wiki/Adversarial_machine_learning
- Chapter 7.13 of _Deep Learning_ by Ian Goodfellow, Yoshua Bengio and Aaron Courville (available to read online [here](https://www.deeplearningbook.org/))

The neural networks used in the code are pretrained models available in the `torchvision` package (https://pytorch.org/docs/stable/torchvision/models.html).

## Image Sources

The original images were taken from [Unsplash](https://unsplash.com/).

Original images:
- `anne-nygard-CYBgMHYgES4-unsplash.jpg` (1920 x 1281), Photo by [Anne Nygård](https://unsplash.com/@polarmermaid), taken from https://unsplash.com/photos/CYBgMHYgES4

The images used in the code were derived by me from the original images.

Images used in code:
- `golden_retriever.jpg` (1280 x 1280) was created by cropping `anne-nygard-CYBgMHYgES4-unsplash.jpg`.

## Setup instructions
### Cloning the repository

To clone the repository using HTTPS, type the following command into a terminal:
```
git clone https://github.com/a-rimpapa/img-classification-adversarial-examples.git
```

... Alternative links for cloning or downloading the repository are at the top right of the page.

### Installing packages

* pip: Run `pip ... requirements.txt`
* conda: Run `conda ... environment.yml`

### Running the code

To run `main.ipynb`, start a Jupyter notebook server on your computer and open the notebook. This can be done for example by running `jupyter notebook` in the command line. ... (TODO other ways), or by using an IDE which automatically starts the notebook server.

Alternatively, 
