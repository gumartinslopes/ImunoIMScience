import argparse
import cv2
import os

# Default directory names if not specified
DEFAULT__MARKER_DIR = 'markers'
DEFAULT__SKELETON_DIR = 'skeletons'

def skeletonize(input_dir, save_skeletons, output_dir):
      # tuple list(skeleton_img, filename)
      skeletons = []
      for i, filename in enumerate(os.listdir(input_dir)):
        img = cv2.imread(input_dir+"/"+filename, cv2.IMREAD_GRAYSCALE)
        ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        skeleton = cv2.ximgproc.thinning(img, None, cv2.ximgproc.THINNING_ZHANGSUEN)
        skeletons.append((skeleton, filename))
      save_skeleton_list(skeletons, save_skeletons, output_dir)
        
      return skeletons

def save_skeleton_list(skeletons, save_skeletons, output_dir):
  if save_skeletons:
    output_dir = output_dir if output_dir!= None else DEFAULT__SKELETON_DIR 
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    for skeleton in skeletons:
        output_filename = skeleton[1] + '_skeleton.png'
        cv2.imwrite('./' + output_dir + "/" + output_filename, skeleton[0])

def setup_arguments(parser):
   parser.add_argument('--input_dir', help='Path to the folder where the input images are located.')
   parser.add_argument('--output_dir', help='Path to the folder where the output markers will be located.')
   parser.add_argument('--save_skeletons', help='Type y to save the skeletons of the image', default = 'N')
   parser.add_argument('--skeleton_dir', help='Path to the folder where the output skeletons will be located.')

def arguments_validated(args):
  save_skeletons_confirmation = (args.save_skeletons.lower() == 'y' or args.save_skeletons.lower =='yes')
  if(args.input_dir == None):
      print('Argument Invalid, the input folder path must not be empty!')
      return False
  return True

# def check_directory(input_dir, output_dir):
#     if os.path.isdir(input_dir):
#       print('Ja existe uma pasta de input com esse nome!')
#     else:
#       print('Pasta de input nao encontrada')

#     if os.path.isdir(output_dir):
#       print('Ja existe uma pasta de input com esse nome!')
#     else:
#       print('Criando pasta de output...')
#       os.mkdir(output_dir)

def make_markers(input_dir, output_dir, save_skeletons, skeleton_dir):
  skels = skeletonize(input_dir, save_skeletons, skeleton_dir)
  print(skels)
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Code for generating the iDISF markers given images.')
  setup_arguments(parser)
  args = parser.parse_args()

  if(arguments_validated(args)):
    input_dir = args.input_dir
    output_dir = args.output_dir
    save_skeletons = args.save_skeletons.lower() == 'y'
    skeleton_dir = args.skeleton_dir
    make_markers(input_dir, output_dir,save_skeletons, skeleton_dir)
    # skels = skeletonize(input_dir, output_dir)
  else:
     print('Vacilou menor')