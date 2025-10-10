# The command line handler (currently the entry point of the application)
import argparse
from adjust_brightness import adjust_brightness_contrast
from input_loader import load_images_from_directory
from output_saver import save_output_images
from sharpen import sharpen_image
from reduce_noise import reduce_noise

# Instantiating the command line argument parser
parser = argparse.ArgumentParser(description="Batch image enhancer.")

# Defining the image enhancement arguments (true for apply)
parser.add_argument("-denoise", "--reduce_noise", 
                   action="store_true", 
                   help="Reduce the image noise by applying Gaussian Blur.")
parser.add_argument("-adjustBC", "--fix_brightness_contrast", 
                   action="store_true",
                   help="Make an adjustment to the brightness and contrast.")
parser.add_argument("-sharpen", "--sharpen_image", 
                   action="store_true",
                   help="Sharpen the image using a high-pass filter.")

# Defining the main positional arguments (source dir, destination dir)
parser.add_argument("SourceDirectory",
                    type=str, 
                    help="The source directory containing the input images.")
parser.add_argument("OutputDirectory", 
                    type=str,
                    help="The output directory to save the enhanced images into.")

# Parsing the arguments
args = parser.parse_args()

# Defining the dictionary of the input images
myImgs_dict = load_images_from_directory(args.SourceDirectory)

# Processing... Enhancing...
for filename, image_data in myImgs_dict.items():
    if args.sharpen_image:
        myImgs_dict[filename] = sharpen_image(image_data)
    if args.fix_brightness_contrast:
        myImgs_dict[filename] = adjust_brightness_contrast(image_data)
    if args.reduce_noise:
        myImgs_dict[filename] = reduce_noise(image_data)

# Saving the enhanced images
if(args.sharpen_image or args.fix_brightness_contrast
   or args.reduce_noise):
    save_output_images(myImgs_dict, args.OutputDirectory)