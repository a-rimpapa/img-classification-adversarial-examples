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
        A torch.Tensor of shape 3 x 224 x 224 containing the resized image.

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

