import argparse
import subprocess
import torch

parser = argparse.ArgumentParser(description='Process an input image and save it to an output file.')
parser.add_argument('-s', '--source', type=str, help='Input image file path', required=True)
parser.add_argument('-t', '--target', type=str, help='Output image file path', required=True)

args = parser.parse_args()

input_file = args.source
output_file = args.target

# Run the anonymization script
subprocess.run(["python", "anonymize.py", "-s", input_file, "-t", output_file])

torch.cuda.empty_cache()

# Run the counting script
subprocess.run(["python", "P2PNET_ROOT/run_test.py", "--weight_path", "./P2PNET_ROOT/weights/SHTechA.pth", "--output_dir", "./logs/", '--input_img', f"{output_file}"])
