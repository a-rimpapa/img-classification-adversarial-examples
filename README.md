# img-classification-adversarial-examples
A repository containing examples of adversarial machine learning for image classification in PyTorch.

TODO maybe rename utils.py to main.py

Adversarial machine learning is .... (TODO general definition) The goal is to construct an image which a human can classify correctly, but which a neural network classifies wrongly, sometimes called an adversarial example. Here, adversarial examples are constructed by taking an image A and adding a (small) noise image N to it to produce a resulting image A', although there are many more ways to construct adversarial examples. The noise image is a variable parameter, and the parameters of the network remain unchanged throughout the training process. The objective function which is minimized is taken to be the loss between the network's prediction given A' as input and a specified target. This aims to make the neural network misclassify the image A' as the class associated with this specific target, given enough training epochs.

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

To clone the repository using HTTPS, execute the following command:
```
git clone https://github.com/a-rimpapa/img-classification-adversarial-examples.git
```

Alternative links for cloning or downloading the repository are at the top right of the page.

### Installing packages

* pip: Run `pip ... requirements.txt`
* conda: Run `conda ... environment.yml`

### Running the code

To run `examples.ipynb`, start a Jupyter notebook server on your computer and open the notebook. This can be done for example by running `jupyter notebook` in the command line. ... (TODO other ways), or by using an IDE which automatically starts the notebook server.

Alternatively, 
