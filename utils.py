import torchvision.transforms as transforms
import PIL

def file_to_tensor(filename):
    # TODO docstring
    img_raw = PIL.Image.open(filename)
    width, height = img_raw.size
    
    # The original image must be square
    assert (width == height), \
    'The height and width of the input image must be equal.'
    
    preprocess_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    
    img = preprocess_transform(img_raw)
    # shape of return value is (3, 224, 224)
    return img

