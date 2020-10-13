import matplotlib.pyplot as plt
import torch.nn as nn
import torchvision.transforms as transforms
import PIL

def file_to_tensor(filepath):
    """Converts a JPEG image into a 3 x 224 x 224 tensor.
    
    Takes a file path pointing to a JPEG image file as input, resizes the image
    to 224 x 224 and returns a 3 x 224 x 224 tensor. The image is assumed to 
    be square (width == height), if it is not, a ValueError is raised.

    Args:
        filepath: A string containing the path to the JPEG image file.

    Returns:
        A torch.Tensor (shape 3 x 224 x 224) containing the resized image.
    """
    img_raw = PIL.Image.open(filepath)
    width, height = img_raw.size
    
    if (width != height):
        raise ValueError(f'The width ({width}) and height ({height}) of the ' + \
                          'input image must be equal.')
    
    img_dim = 224
    preprocess_transform = transforms.Compose([
        transforms.Resize((img_dim, img_dim)),
        transforms.ToTensor()
    ])
    
    img = preprocess_transform(img_raw)
    return img

def transform_to_input(img):
    """Transforms a tensor to be able to pass it as input to a pretrained model.
    
    Normalizes the input image tensor so that the resulting tensor can be passed 
    as input to one of the pretrained models in torchvision.models, as described
    here: https://pytorch.org/docs/stable/torchvision/models.html. An additional
    dimension of size 1 is also inserted at position 0, to ensure that the tensor 
    has the correct shape.

    Args:
        img: A torch.Tensor (shape 3 x 224 x 224) containing a 224 x 224 image.

    Returns:
        A torch.Tensor (shape 1 x 3 x 224 x 224) containing the normalized image.
    """
    normalize_transform = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                               std=[0.229, 0.224, 0.225])
    
    img_normalized = normalize_transform(img)
    img_normalized = img_normalized.unsqueeze(0)
    return img_normalized

# TODO comments, docstring
def visualize(img_tensor):
    img_numpy = img_tensor.numpy().transpose((1, 2, 0))
    
    fig, ax = plt.subplots()
    ax.imshow(img_numpy)
    plt.show()

# TODO rename
class Net(nn.Module):
    # TODO class docstring
    
    # TODO argument for parameter initialization
    def __init__(self, pretrained_model):
        super(Net, self).__init__()
        
    # TODO
    # TODO can forward take no arguments? probably not,
    # then just disregard argument x and have original image as instance variable
    def forward(self, x):
        return x
        


# TODO: somewhere (maybe in predict method?), check whether tensor is proper
# shape to be input of model (3, 224, 224)